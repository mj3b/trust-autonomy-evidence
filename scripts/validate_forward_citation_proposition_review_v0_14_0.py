#!/usr/bin/env python3
"""Validate the frozen v0.14 forward-citation proposition review."""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "paper/data/forward-citation-author-screening-decisions-v0.13.0.csv"
LEDGER = ROOT / "paper/data/forward-citation-proposition-review-v0.14.0.csv"
SUMMARY = ROOT / "paper/data/forward-citation-proposition-review-v0.14.0.json"
REPORT = ROOT / "paper/forward-citation-proposition-review-v0.14.0.md"
PROTOCOL = ROOT / "paper/forward-citation-proposition-review-protocol-v0.14.0.md"
DIRECT_RESOLUTION = ROOT / "paper/data/direct-query-resolution-v0.14.0.json"
BIBLIOGRAPHY = ROOT / "paper/references.bib"
MANUSCRIPT = ROOT / "paper/manuscript.md"
ATTESTATION = ROOT / "evidence/human-review-attestation-v0.14.0.json"

AUTHOR = "Mark Julius Banasihan"
EXPECTED_PERMITTED = {
    "RS-FC-042": "suryana2024tesla",
    "RS-FC-052": "li2025sandbox",
    "RS-FC-060": "vanderwaa2020allocation",
    "RS-FC-070": "kolt2025agents",
    "RS-FC-096": "zhang2018tianjin",
}
ALLOWED_DECISIONS = {"manuscript-use", "background-only", "quarantined"}
FITNESS_STATES = {"pass", "fail", "indeterminate", "outside_scope"}
REQUIRED_FIELDS = (
    "sample_id", "record_key", "verified_citation", "review_basis", "stable_locator",
    "passage_locator", "permitted_proposition", "review_decision", "claim_permission",
    "directness", "contemporaneity", "independence", "completeness",
    "publication_authority", "limitation", "reversal_condition", "decision_owner",
    "decision_date", "ai_assistance",
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    errors: list[str] = []
    inputs = [row for row in read_csv(INPUT) if row["author_decision"] == "retain-close"]
    rows = read_csv(LEDGER)
    input_ids = [row["sample_id"] for row in inputs]
    review_ids = [row["sample_id"] for row in rows]

    if len(rows) != 13:
        errors.append(f"expected 13 proposition-review rows; found {len(rows)}")
    if review_ids != input_ids:
        errors.append("proposition-review ledger does not preserve frozen close-source membership and order")
    if len(review_ids) != len(set(review_ids)):
        errors.append("proposition-review ledger contains duplicate sample identifiers")

    input_by_id = {row["sample_id"]: row for row in inputs}
    for row in rows:
        sample_id = row.get("sample_id", "")
        blanks = [field for field in REQUIRED_FIELDS if not row.get(field, "").strip()]
        if blanks:
            errors.append(f"{sample_id}: blank required fields {blanks}")
        source = input_by_id.get(sample_id)
        if source and row["record_key"] != source["record_key"]:
            errors.append(f"{sample_id}: record key differs from frozen screening ledger")
        if row["review_decision"] not in ALLOWED_DECISIONS:
            errors.append(f"{sample_id}: invalid review decision")
        for field in (
            "directness", "contemporaneity", "independence", "completeness",
            "publication_authority",
        ):
            if row[field] not in FITNESS_STATES:
                errors.append(f"{sample_id}: invalid {field} state")
        if row["decision_owner"] != AUTHOR:
            errors.append(f"{sample_id}: decision owner must be {AUTHOR}")
        if row["decision_date"] != "2026-08-13":
            errors.append(f"{sample_id}: decision date mismatch")

        decision = row["review_decision"]
        permission = row["claim_permission"]
        required_fitness = (
            row["directness"], row["contemporaneity"], row["completeness"],
            row["publication_authority"],
        )
        if decision == "manuscript-use":
            if permission != "proposition-permitted":
                errors.append(f"{sample_id}: manuscript-use row lacks proposition permission")
            if any(state != "pass" for state in required_fitness):
                errors.append(f"{sample_id}: manuscript-use row has a failed or indeterminate required fitness state")
            if row["passage_locator"] == "none" or row["permitted_proposition"] == "No proposition permitted.":
                errors.append(f"{sample_id}: manuscript-use row lacks proposition-level location")
        elif decision == "background-only":
            if permission != "background-only":
                errors.append(f"{sample_id}: background row has invalid permission")
        elif permission != "none":
            errors.append(f"{sample_id}: quarantined row grants claim permission")

    decisions = Counter(row["review_decision"] for row in rows)
    permissions = sum(row["claim_permission"] == "proposition-permitted" for row in rows)
    expected_counts = {
        "retained_close_sources": 13,
        "reviewed": 13,
        "open": 0,
        "manuscript_use": decisions["manuscript-use"],
        "background_only": decisions["background-only"],
        "quarantined": decisions["quarantined"],
        "proposition_permissions": permissions,
    }
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    if summary.get("status") != "PROPOSITION_REVIEW_CLOSED":
        errors.append("proposition-review summary status mismatch")
    if summary.get("counts") != expected_counts:
        errors.append("proposition-review summary counts mismatch")
    if set(summary.get("permitted_sample_ids", [])) != set(EXPECTED_PERMITTED):
        errors.append("permitted-source set mismatch")

    bibliography = BIBLIOGRAPHY.read_text(encoding="utf-8")
    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    bib_keys = set(re.findall(r"^@\w+\{([^,]+),", bibliography, flags=re.MULTILINE))
    manuscript_keys = set(re.findall(r"@([A-Za-z0-9_:.+-]+)", manuscript))
    for sample_id, key in EXPECTED_PERMITTED.items():
        if key not in bib_keys:
            errors.append(f"{sample_id}: bibliography key {key} is missing")
        if key not in manuscript_keys:
            errors.append(f"{sample_id}: permitted proposition is not cited in manuscript")

    resolution = json.loads(DIRECT_RESOLUTION.read_text(encoding="utf-8"))
    if resolution.get("status") != "DIRECT_QUERY_SCREENING_CLOSED":
        errors.append("direct-query resolution status mismatch")
    if resolution.get("decision") != "retain-close" or resolution.get("claim_permission") != "none-until-readable-proposition-review":
        errors.append("direct-query resolution must close screening without proposition permission")
    if resolution.get("resulting_counts", {}).get("screening_open") != 0:
        errors.append("direct-query resolution leaves an open screening decision")

    attestation = json.loads(ATTESTATION.read_text(encoding="utf-8"))
    if attestation.get("reviewer") != AUTHOR or attestation.get("version") != "0.14.0":
        errors.append("v0.14 human-review attestation mismatch")
    attested = {row.get("claim_id") for row in attestation.get("workflow_attestations", [])}
    if attested != {"PAPER-C35", "PAPER-C36", "PAPER-C37", "PAPER-C38"}:
        errors.append("v0.14 attestation does not cover PAPER-C35 through PAPER-C38")

    for path in (REPORT, PROTOCOL):
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            errors.append(f"missing or empty artifact: {path.relative_to(ROOT)}")

    if errors:
        print("v0.14 proposition review: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "v0.14 proposition review: PASS "
        "(13/13 reviewed; 5 manuscript-use; 2 background-only; 6 quarantined; direct query closed)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
