#!/usr/bin/env python3
"""Validate the frozen v0.7.0 search, screening, and metadata artifacts."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SEARCH_PATH = ROOT / "paper/data/formal-search-v0.7.0.json"
SCREENING_PATH = ROOT / "paper/data/formal-screening-proposals-v0.7.0.json"
METADATA_PATH = ROOT / "paper/data/formal-metadata-verification-v0.7.0.json"
SCREENING_REPORT = ROOT / "paper/formal-search-screening-v0.7.0.md"
CHAIN_REPORT = ROOT / "paper/formal-citation-chain-v0.7.0.md"
AUTHOR_QUEUE = ROOT / "paper/data/author-screening-queue-v0.7.0.csv"
PROTOCOL = "paper/formal-literature-search-protocol-v0.7.0.md"
CUTOFF = "2026-08-09"
QUERY_IDS = {f"F{number:02d}" for number in range(1, 9)}
CHAIN_SEEDS = {
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
DECISIONS = {
    "exclude-outside-cutoff",
    "exclude-single-component",
    "exclude-topic",
    "inaccessible",
    "retain-background",
    "retain-close",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def norm(value: str | None) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", (value or "").lower())).strip()


def record_key(record: dict[str, Any]) -> str:
    external = record.get("externalIds") or {}
    doi = str(external.get("DOI") or "").lower()
    if doi:
        return f"doi:{doi}"
    return f"title:{norm(record.get('title'))}|year:{record.get('year') or ''}"


def after_cutoff(record: dict[str, Any]) -> bool:
    publication_date = record.get("publicationDate")
    if publication_date:
        try:
            return date.fromisoformat(publication_date) > date.fromisoformat(CUTOFF)
        except ValueError:
            pass
    year = record.get("year")
    return bool(year and int(year) > date.fromisoformat(CUTOFF).year)


def main() -> None:
    search = load(SEARCH_PATH)
    screening = load(SCREENING_PATH)
    metadata = load(METADATA_PATH)
    failures: list[str] = []

    for name, payload in (("search", search), ("screening", screening), ("metadata", metadata)):
        if payload.get("schema_version") != "1.0":
            failures.append(f"{name} schema version mismatch")
        if payload.get("protocol") != PROTOCOL:
            failures.append(f"{name} protocol link mismatch")
    if search.get("publication_cutoff") != CUTOFF or screening.get("publication_cutoff") != CUTOFF:
        failures.append("publication cutoff mismatch")

    runs = search.get("search_runs", {})
    if set(runs) != QUERY_IDS:
        failures.append(f"search query identifiers mismatch: {sorted(runs)}")
    pooled_count = 0
    for query_id, run in runs.items():
        records = run.get("records", [])
        if run.get("record_count") != len(records):
            failures.append(f"{query_id} record count mismatch")
        if sum(item.get("returned", 0) for item in run.get("requests", [])) != len(records):
            failures.append(f"{query_id} request count mismatch")
        pooled_count += len(records)

    chains = search.get("citation_chains", {})
    if {key: value.get("seed") for key, value in chains.items()} != CHAIN_SEEDS:
        failures.append("citation-chain seeds differ from the frozen set")
    for chain_id, chain in chains.items():
        references = chain.get("references", [])
        citations = chain.get("citations", [])
        if chain.get("reference_count") != len(references):
            failures.append(f"{chain_id} reference count mismatch")
        if chain.get("citation_count") != len(citations):
            failures.append(f"{chain_id} citation count mismatch")
        if sum(item.get("returned", 0) for item in chain.get("reference_requests", [])) != len(references):
            failures.append(f"{chain_id} reference request count mismatch")
        if sum(item.get("returned", 0) for item in chain.get("citation_requests", [])) != len(citations):
            failures.append(f"{chain_id} citation request count mismatch")
        pooled_count += len(references) + len(citations)
    if search.get("pooled_record_count") != pooled_count:
        failures.append("pooled record count mismatch")

    deduplicated = search.get("deduplicated_records", [])
    deduplicated_keys = [record_key(record) for record in deduplicated]
    records_by_key = {record_key(record): record for record in deduplicated}
    if search.get("deduplicated_record_count") != len(deduplicated):
        failures.append("deduplicated record count mismatch")
    if len(deduplicated_keys) != len(set(deduplicated_keys)):
        failures.append("deduplicated record set contains duplicate keys")

    if screening.get("decision_status") != "ai-assisted preliminary":
        failures.append("screening status must remain preliminary")
    if screening.get("author_confirmation_required") is not True:
        failures.append("screening must require author confirmation")
    decisions = screening.get("decisions", [])
    if screening.get("record_count") != len(decisions) or len(decisions) != len(deduplicated):
        failures.append("screening record count mismatch")
    decision_keys = [item.get("record_key") for item in decisions]
    if set(decision_keys) != set(deduplicated_keys) or len(decision_keys) != len(set(decision_keys)):
        failures.append("screening records do not map one-to-one to the deduplicated set")
    for item in decisions:
        if item.get("proposed_decision") not in DECISIONS:
            failures.append(f"unknown screening proposal: {item.get('proposed_decision')}")
        if item.get("decision_status") != "ai-assisted preliminary":
            failures.append(f"screening record is not preliminary: {item.get('record_key')}")
        if item.get("author_confirmation_required") is not True:
            failures.append(f"screening record lacks author gate: {item.get('record_key')}")
        source_record = records_by_key.get(str(item.get("record_key")), {})
        if item.get("proposed_decision") == "exclude-outside-cutoff" and not after_cutoff(source_record):
            failures.append(f"cutoff exclusion lacks a post-cutoff year: {item.get('record_key')}")
    actual_counts = dict(sorted(Counter(item.get("proposed_decision") for item in decisions).items()))
    if screening.get("counts") != actual_counts:
        failures.append("screening proposal counts mismatch")

    with AUTHOR_QUEUE.open(encoding="utf-8", newline="") as handle:
        queue = list(csv.DictReader(handle))
    expected_queue_keys = {
        item["record_key"]
        for item in decisions
        if item.get("proposed_decision") in {"retain-close", "exclude-single-component"}
    }
    if {item.get("record_key") for item in queue} != expected_queue_keys:
        failures.append("author-screening queue differs from the close and attention sets")
    if any(item.get("author_decision") or item.get("author_notes") for item in queue):
        failures.append("author-screening queue contains an unverified author decision")

    retained_dois = {
        item["doi"]
        for item in decisions
        if str(item.get("proposed_decision", "")).startswith("retain-") and item.get("doi")
    }
    if set(metadata.get("crossref", {})) != retained_dois:
        failures.append("Crossref verification set differs from retained DOI set")
    if set(metadata.get("openalex", {})) != set(CHAIN_SEEDS):
        failures.append("OpenAlex verification set differs from citation-chain seeds")
    for index_name in ("crossref", "openalex"):
        for identifier, item in metadata.get(index_name, {}).items():
            if item.get("status") not in {"resolved", "unresolved"}:
                failures.append(f"invalid {index_name} status for {identifier}")

    screening_text = SCREENING_REPORT.read_text(encoding="utf-8")
    if "author confirmation required" not in screening_text.lower():
        failures.append("screening report omits the author-confirmation gate")
    if "does not claim that the author read 2,431 full texts" not in screening_text:
        failures.append("screening report omits the full-text-reading boundary")
    chain_text = CHAIN_REPORT.read_text(encoding="utf-8")
    if "Semantic Scholar" not in chain_text or "OpenAlex" not in chain_text:
        failures.append("citation-chain report omits its index boundaries")

    if failures:
        raise SystemExit("formal-search validation: FAIL\n" + "\n".join(failures))
    print(
        "formal-search validation: PASS "
        f"({len(runs)} queries; {len(chains)} chains; {len(deduplicated):,} records; "
        f"{len(queue)} frozen author-queue records)"
    )


if __name__ == "__main__":
    main()
