#!/usr/bin/env python3
"""Verify retained DOI metadata and compare citation-seed index coverage."""

from __future__ import annotations

import argparse
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


USER_AGENT = "trust-autonomy-evidence/0.7.0 (mailto:mark.julius.banasihan@users.noreply.github.com)"


def fetch(url: str, retries: int = 5) -> dict[str, Any]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return json.load(response)
        except (urllib.error.HTTPError, urllib.error.URLError) as exc:
            if isinstance(exc, urllib.error.HTTPError) and exc.code not in {429, 500, 502, 503, 504}:
                raise
            if attempt == retries - 1:
                raise
            time.sleep(min(2 ** attempt, 20))
    raise RuntimeError("request retries exhausted")


def compact_crossref(message: dict[str, Any]) -> dict[str, Any]:
    return {
        "doi": message.get("DOI"),
        "title": (message.get("title") or [None])[0],
        "author": message.get("author") or [],
        "container_title": (message.get("container-title") or [None])[0],
        "type": message.get("type"),
        "published": message.get("published") or message.get("published-print") or message.get("published-online"),
        "url": message.get("URL"),
    }


def compact_openalex(work: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": work.get("id"),
        "doi": work.get("doi"),
        "title": work.get("title"),
        "publication_year": work.get("publication_year"),
        "cited_by_count": work.get("cited_by_count"),
        "referenced_works_count": len(work.get("referenced_works") or []),
        "type": work.get("type"),
        "primary_location": work.get("primary_location"),
    }


def request_result(url: str, transform) -> dict[str, Any]:
    try:
        return {"status": "resolved", "record": transform(fetch(url))}
    except urllib.error.HTTPError as exc:
        return {"status": "unresolved", "http_status": exc.code, "reason": str(exc)}
    except urllib.error.URLError as exc:
        return {"status": "unresolved", "reason": str(exc)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--search", type=Path, default=Path("paper/data/formal-search-v0.7.0.json"))
    parser.add_argument("--screening", type=Path, default=Path("paper/data/formal-screening-proposals-v0.7.0.json"))
    parser.add_argument("--output", type=Path, default=Path("paper/data/formal-metadata-verification-v0.7.0.json"))
    parser.add_argument("--delay", type=float, default=0.2)
    args = parser.parse_args()

    search = json.loads(args.search.read_text(encoding="utf-8"))
    screening = json.loads(args.screening.read_text(encoding="utf-8"))
    retained_dois = sorted({item["doi"] for item in screening["decisions"] if item["proposed_decision"].startswith("retain-") and item.get("doi")})

    crossref: dict[str, Any] = {}
    for doi in retained_dois:
        url = f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='')}"
        result = request_result(url, lambda payload: compact_crossref(payload["message"]))
        result["request_url"] = url
        crossref[doi] = result
        time.sleep(args.delay)

    openalex: dict[str, Any] = {}
    for literature_id, chain in search["citation_chains"].items():
        seed = chain["seed"]
        prefix, identifier = seed.split(":", 1)
        work_id = f"https://doi.org/{identifier}" if prefix.upper() == "DOI" else f"https://arxiv.org/abs/{identifier}"
        url = f"https://api.openalex.org/works/{urllib.parse.quote(work_id, safe='')}"
        result = request_result(url, compact_openalex)
        result["seed"] = seed
        result["request_url"] = url
        openalex[literature_id] = result
        time.sleep(args.delay)

    output = {
        "schema_version": "1.0",
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "protocol": "paper/formal-literature-search-protocol-v0.7.0.md",
        "crossref_purpose": "bibliographic verification for DOI-bearing retained proposals",
        "openalex_purpose": "citation-index coverage comparison for frozen chain seeds",
        "crossref": crossref,
        "openalex": openalex,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "crossref_resolved": sum(item["status"] == "resolved" for item in crossref.values()),
        "crossref_total": len(crossref),
        "openalex_resolved": sum(item["status"] == "resolved" for item in openalex.values()),
        "openalex_total": len(openalex),
        "output": str(args.output),
    }, indent=2))


if __name__ == "__main__":
    main()
