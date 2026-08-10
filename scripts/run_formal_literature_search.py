#!/usr/bin/env python3
"""Retrieve the frozen v0.7.0 literature queries and citation chains."""

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


SEMANTIC_BASE = "https://api.semanticscholar.org/graph/v1"
USER_AGENT = "trust-autonomy-evidence/0.7.0 (https://github.com/mj3b/trust-autonomy-evidence)"
FIELDS = (
    "paperId,corpusId,externalIds,url,title,abstract,venue,year,publicationDate,"
    "authors,citationCount,referenceCount,publicationTypes,openAccessPdf"
)
SEARCH_QUERIES = {
    "F01": '"meaningful human control" AND (evidence OR assessment OR operationalization OR assurance)',
    "F02": '"effective human oversight" AND (evidence OR performance OR audit OR evaluation OR compliance)',
    "F03": '("human oversight" OR "human control") AND ("incident reconstruction" OR "accident reconstruction")',
    "F04": '("formal authority" OR "human authority") AND ("practical control" OR override OR intervention OR contestability) AND (automation OR "artificial intelligence" OR autonomous)',
    "F05": '("AI incident" OR "algorithmic incident") AND (reconstruction OR provenance OR "chain of custody" OR "missing evidence")',
    "F06": '("assurance case" OR "assurance audit") AND ("human control" OR "human oversight")',
    "F07": '("claim evidence" OR "chain of evidence") AND ("human control" OR "human oversight")',
    "F08": '(indeterminate OR missingness) AND ("human oversight" OR "meaningful human control")',
}
SEEDS = {
    "L01": "DOI:10.3389/frobt.2018.00015",
    "L02": "DOI:10.1007/s43681-022-00167-3",
    "L04": "DOI:10.1007/s11948-025-00554-z",
    "L06": "DOI:10.1007/s43681-026-01147-7",
    "L10": "DOI:10.1016/j.clsr.2022.105681",
    "L12": "DOI:10.1609/aies.v8i1.36596",
    "L14": "DOI:10.1007/s43681-022-00178-0",
    "L15": "DOI:10.1016/j.ress.2025.111311",
    "L16": "DOI:10.1016/S0022-4375(02)00032-4",
    "L17": "DOI:10.1111/risa.13850",
    "L24": "ARXIV:2605.26340",
    "L25": "DOI:10.1007/s11023-024-09701-0",
    "L26": "DOI:10.1007/978-3-032-07132-3_11",
    "L27": "DOI:10.1145/3630106.3658957",
    "L28": "ARXIV:2605.16278",
}


def fetch_json(url: str, retries: int = 6) -> dict[str, Any]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            if exc.code not in {429, 500, 502, 503, 504} or attempt == retries - 1:
                raise
        except urllib.error.URLError:
            if attempt == retries - 1:
                raise
        time.sleep(min(2 ** attempt, 30))
    raise RuntimeError("request retries exhausted")


def api_url(path: str, params: dict[str, Any]) -> str:
    return f"{SEMANTIC_BASE}{path}?{urllib.parse.urlencode(params)}"


def search_all(query: str, request_delay: float) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    records: list[dict[str, Any]] = []
    requests: list[dict[str, Any]] = []
    token: str | None = None
    while True:
        params: dict[str, Any] = {"query": query, "fields": FIELDS, "sort": "publicationDate:asc"}
        if token:
            params["token"] = token
        url = api_url("/paper/search/bulk", params)
        payload = fetch_json(url)
        page = payload.get("data", [])
        records.extend(page)
        requests.append({"url": url, "returned": len(page), "estimated_total": payload.get("total")})
        token = payload.get("token")
        if not token:
            break
        time.sleep(request_delay)
    return records, requests


def chain_all(seed: str, relation: str, request_delay: float) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    records: list[dict[str, Any]] = []
    requests: list[dict[str, Any]] = []
    offset = 0
    while True:
        params = {"offset": offset, "limit": 100, "fields": FIELDS}
        url = api_url(f"/paper/{urllib.parse.quote(seed, safe='')}/{relation}", params)
        payload = fetch_json(url)
        page = payload.get("data", [])
        normalized = []
        for item in page:
            paper = item.get("citedPaper") or item.get("citingPaper") or item
            if paper:
                normalized.append(paper)
        records.extend(normalized)
        requests.append({"url": url, "returned": len(normalized)})
        next_offset = payload.get("next")
        if next_offset is None or not page:
            break
        offset = int(next_offset)
        time.sleep(request_delay)
    return records, requests


def normalize_title(value: str | None) -> str:
    return " ".join("".join(ch.lower() if ch.isalnum() else " " for ch in value or "").split())


def record_key(record: dict[str, Any]) -> str:
    external = record.get("externalIds") or {}
    doi = external.get("DOI")
    if doi:
        return f"doi:{doi.lower()}"
    return f"title:{normalize_title(record.get('title'))}|year:{record.get('year') or ''}"


def deduplicate(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: dict[str, dict[str, Any]] = {}
    for record in records:
        key = record_key(record)
        if key not in seen:
            seen[key] = record
    return list(seen.values())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("paper/data/formal-search-v0.7.0.json"))
    parser.add_argument("--delay", type=float, default=1.1)
    args = parser.parse_args()

    search_runs: dict[str, Any] = {}
    pooled: list[dict[str, Any]] = []
    for query_id, query in SEARCH_QUERIES.items():
        records, requests = search_all(query, args.delay)
        search_runs[query_id] = {"query": query, "record_count": len(records), "requests": requests, "records": records}
        pooled.extend(records)
        time.sleep(args.delay)

    chains: dict[str, Any] = {}
    for literature_id, seed in SEEDS.items():
        references, reference_requests = chain_all(seed, "references", args.delay)
        time.sleep(args.delay)
        citations, citation_requests = chain_all(seed, "citations", args.delay)
        chains[literature_id] = {
            "seed": seed,
            "reference_count": len(references),
            "citation_count": len(citations),
            "reference_requests": reference_requests,
            "citation_requests": citation_requests,
            "references": references,
            "citations": citations,
        }
        pooled.extend(references)
        pooled.extend(citations)
        time.sleep(args.delay)

    output = {
        "schema_version": "1.0",
        "protocol": "paper/formal-literature-search-protocol-v0.7.0.md",
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "publication_cutoff": "2026-08-09",
        "source": "Semantic Scholar Academic Graph API",
        "search_runs": search_runs,
        "citation_chains": chains,
        "pooled_record_count": len(pooled),
        "deduplicated_record_count": len(deduplicate(pooled)),
        "deduplicated_records": deduplicate(pooled),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(args.output),
        "search_records": sum(item["record_count"] for item in search_runs.values()),
        "chain_records": sum(item["reference_count"] + item["citation_count"] for item in chains.values()),
        "deduplicated_records": output["deduplicated_record_count"],
    }, indent=2))


if __name__ == "__main__":
    main()
