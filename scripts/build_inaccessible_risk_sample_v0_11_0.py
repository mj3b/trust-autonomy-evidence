#!/usr/bin/env python3
"""Build and verify the v0.11.0 inaccessible-record risk sample."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "paper/data/formal-screening-proposals-v0.7.0.json"
RETRIEVAL_LEDGER = ROOT / "paper/data/inaccessible-record-retrieval-v0.10.0.csv"
CSV_OUTPUT = ROOT / "paper/data/inaccessible-risk-sample-v0.11.0.csv"
JSON_OUTPUT = ROOT / "paper/data/inaccessible-risk-sample-v0.11.0.json"
REPORT_OUTPUT = ROOT / "paper/inaccessible-risk-sample-v0.11.0.md"

VERSION = "0.11.0"
PROTOCOL = "protocols/search-coverage-and-full-text-protocol-v0.10.0.md"
AUTHOR = "Mark Julius Banasihan"
SELECTION_DATE = "2026-08-11"
SEED = "TAE-v0.10-risk-sample"
EXPECTED_POPULATION = 1087
TARGET_SAMPLE = 284
RETRIEVAL_ROWS_AT_FREEZE = 0
STRATA = (
    ("forward-citation", "citation:", "FC"),
    ("backward-reference", "reference:", "BR"),
    ("direct-query", "query:", "DQ"),
)
FIELDS = (
    "sample_id",
    "record_key",
    "title",
    "year",
    "venue",
    "primary_stratum",
    "stratum_population",
    "stratum_allocation",
    "stratum_rank",
    "selection_digest",
    "origins",
    "selection_status",
)


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def primary_stratum(origins: list[str]) -> str:
    for stratum, prefix, _ in STRATA:
        if any(origin.startswith(prefix) for origin in origins):
            return stratum
    raise ValueError(f"record has no declared origin stratum: {origins}")


def apportion(counts: Counter[str], target: int) -> dict[str, int]:
    population = sum(counts.values())
    allocations = {
        stratum: (target * counts[stratum]) // population for stratum, _, _ in STRATA
    }
    remaining = target - sum(allocations.values())
    order = sorted(
        (stratum for stratum, _, _ in STRATA),
        key=lambda stratum: (
            -((target * counts[stratum]) % population),
            next(index for index, item in enumerate(STRATA) if item[0] == stratum),
        ),
    )
    for stratum in order[:remaining]:
        allocations[stratum] += 1
    return allocations


def inaccessible_records() -> list[dict[str, object]]:
    payload = json.loads(SOURCE.read_text(encoding="utf-8"))
    records = [
        row for row in payload["decisions"] if row["proposed_decision"] == "inaccessible"
    ]
    keys = [str(row["record_key"]) for row in records]
    if len(records) != EXPECTED_POPULATION:
        raise ValueError(
            f"expected {EXPECTED_POPULATION} inaccessible records; found {len(records)}"
        )
    if len(keys) != len(set(keys)):
        raise ValueError("inaccessible population contains duplicate record keys")
    return records


def selection_rows() -> tuple[list[dict[str, str]], Counter[str], dict[str, int]]:
    records = inaccessible_records()
    grouped: dict[str, list[dict[str, object]]] = {
        stratum: [] for stratum, _, _ in STRATA
    }
    for record in records:
        origins = [str(origin) for origin in record.get("origins", [])]
        grouped[primary_stratum(origins)].append(record)

    counts = Counter({stratum: len(rows) for stratum, rows in grouped.items()})
    allocations = apportion(counts, TARGET_SAMPLE)
    output: list[dict[str, str]] = []
    for stratum, _, abbreviation in STRATA:
        ordered = sorted(
            grouped[stratum],
            key=lambda row: (
                sha256_bytes(f"{SEED}|{row['record_key']}".encode("utf-8")),
                str(row["record_key"]),
            ),
        )
        for rank, record in enumerate(ordered[: allocations[stratum]], start=1):
            record_key = str(record["record_key"])
            output.append(
                {
                    "sample_id": f"RS-{abbreviation}-{rank:03d}",
                    "record_key": record_key,
                    "title": str(record.get("title") or ""),
                    "year": str(record.get("year") or ""),
                    "venue": str(record.get("venue") or ""),
                    "primary_stratum": stratum,
                    "stratum_population": str(counts[stratum]),
                    "stratum_allocation": str(allocations[stratum]),
                    "stratum_rank": str(rank),
                    "selection_digest": sha256_bytes(
                        f"{SEED}|{record_key}".encode("utf-8")
                    ),
                    "origins": ";".join(str(origin) for origin in record.get("origins", [])),
                    "selection_status": "selected-before-retrieval",
                }
            )
    return output, counts, allocations


def csv_text(rows: list[dict[str, str]]) -> str:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def summary_data(
    rows: list[dict[str, str]], counts: Counter[str], allocations: dict[str, int], csv_payload: str
) -> dict[str, object]:
    return {
        "version": VERSION,
        "status": "FROZEN_BEFORE_RETRIEVAL",
        "protocol": PROTOCOL,
        "selection_date": SELECTION_DATE,
        "decision_owner": AUTHOR,
        "human_responsibility": (
            "Authorized the sampling checkpoint and remains responsible for retrieval, screening, "
            "interpretation, and manuscript claims."
        ),
        "ai_assistance": (
            "Codex drafted the builder and records, computed the deterministic selection, and ran "
            "consistency checks under author authorization."
        ),
        "software_record": "scripts/build_inaccessible_risk_sample_v0_11_0.py",
        "population_source": str(SOURCE.relative_to(ROOT)),
        "population_source_sha256": sha256_file(SOURCE),
        "seed": SEED,
        "digest_rule": "SHA-256 of TAE-v0.10-risk-sample|record_key",
        "primary_stratum_order": [stratum for stratum, _, _ in STRATA],
        "allocation_method": (
            "Hamilton largest-remainder apportionment; equal remainders follow the declared "
            "primary-stratum order"
        ),
        "population_size": EXPECTED_POPULATION,
        "unresolved_at_freeze": EXPECTED_POPULATION,
        "retrieval_rows_at_freeze": RETRIEVAL_ROWS_AT_FREEZE,
        "target_sample_size": TARGET_SAMPLE,
        "selected_records": len(rows),
        "strata": [
            {
                "stratum": stratum,
                "population": counts[stratum],
                "allocation": allocations[stratum],
            }
            for stratum, _, _ in STRATA
        ],
        "sample_csv": str(CSV_OUTPUT.relative_to(ROOT)),
        "sample_csv_sha256": sha256_bytes(csv_payload.encode("utf-8")),
        "claim_boundary": (
            "Selection fixes which records receive residual-risk inspection. It supplies no retrieval, "
            "screening, prevalence, exhaustive-coverage, or originality result."
        ),
    }


def report_text(summary: dict[str, object]) -> str:
    strata = summary["strata"]
    rows = "\n".join(
        f"| {row['stratum']} | {row['population']:,} | {row['allocation']:,} |"
        for row in strata
    )
    return f"""# Inaccessible-Record Residual-Risk Sample, v0.11.0

**Status:** `FROZEN_BEFORE_RETRIEVAL`  
**Decision owner:** {summary['decision_owner']}  
**Selection date:** {summary['selection_date']}  
**Controlling protocol:** [`{PROTOCOL}`](../{PROTOCOL})

**Assistance disclosure:** Codex drafted the builder and records, computed the deterministic selection, and ran consistency checks under author authorization. Mark Julius Banasihan remains responsible for retrieval, screening, interpretation, and manuscript claims.

## Decision

Sample membership can become outcome-dependent when it is chosen after retrieval begins. This checkpoint fixes the 284 selected records while all 1,087 records remain unresolved. Later retrieval outcomes cannot change membership.

## Population and allocation

The source population is the 1,087 records classified as `inaccessible` in [`formal-screening-proposals-v0.7.0.json`](data/formal-screening-proposals-v0.7.0.json). Each record receives one primary stratum using the frozen order: forward citation, backward reference, then direct query.

| Primary stratum | Population | Selected |
|---|---:|---:|
{rows}
| **Total** | **{summary['population_size']:,}** | **{summary['selected_records']:,}** |

The allocation uses Hamilton largest-remainder apportionment. Integer ties follow the declared stratum order. This rounding rule was recorded before any sampled retrieval outcome.

## Reproduction rule

Within each stratum, records are ordered by the SHA-256 digest of `{SEED}|record_key`. The lowest digests enter the sample until the stratum allocation is met. [`inaccessible-risk-sample-v0.11.0.csv`](data/inaccessible-risk-sample-v0.11.0.csv) records the digest, rank, origin set, and source metadata for every selected record.

The executable builder checks the 1,087-record population, primary-stratum assignment, proportional allocation, digest order, selected keys, and exact CSV and JSON bytes.

## Evidence boundary

This checkpoint establishes deterministic sample membership and selection lineage. It supplies no retrieval, screening, prevalence, exhaustive-coverage, or originality result. Sampled records still require the lawful retrieval procedure and author decision recorded in [`inaccessible-record-retrieval-v0.10.0.csv`](data/inaccessible-record-retrieval-v0.10.0.csv).
"""


def expected_outputs() -> tuple[str, str, str]:
    rows, counts, allocations = selection_rows()
    csv_payload = csv_text(rows)
    summary = summary_data(rows, counts, allocations, csv_payload)
    json_payload = json.dumps(summary, indent=2, ensure_ascii=False) + "\n"
    return csv_payload, json_payload, report_text(summary)


def retrieval_row_count() -> int:
    with RETRIEVAL_LEDGER.open(newline="", encoding="utf-8") as handle:
        return sum(1 for _ in csv.DictReader(handle))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write the frozen sample artifacts")
    parser.add_argument("--check", action="store_true", help="verify the committed sample artifacts")
    args = parser.parse_args()

    csv_payload, json_payload, report_payload = expected_outputs()
    if args.write:
        if retrieval_row_count() != RETRIEVAL_ROWS_AT_FREEZE:
            raise SystemExit(
                "risk sample: REFUSED\nselection must be frozen before retrieval rows are recorded"
            )
        CSV_OUTPUT.write_text(csv_payload, encoding="utf-8")
        JSON_OUTPUT.write_text(json_payload, encoding="utf-8")
        REPORT_OUTPUT.write_text(report_payload, encoding="utf-8")

    errors: list[str] = []
    if args.check:
        for path, expected in (
            (CSV_OUTPUT, csv_payload),
            (JSON_OUTPUT, json_payload),
            (REPORT_OUTPUT, report_payload),
        ):
            if not path.is_file():
                errors.append(f"missing sample artifact: {path.relative_to(ROOT)}")
            elif path.read_text(encoding="utf-8") != expected:
                errors.append(f"stale sample artifact: {path.relative_to(ROOT)}")
    if errors:
        raise SystemExit("risk sample: FAIL\n" + "\n".join(errors))
    print(f"risk sample: PASS ({EXPECTED_POPULATION} population; {TARGET_SAMPLE} selected)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
