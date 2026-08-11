#!/usr/bin/env python3
"""Validate the frozen v0.13 forward-citation author-screening gate."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "paper/data/forward-citation-author-review-queue-v0.12.0.csv"
DECISIONS = ROOT / "paper/data/forward-citation-author-screening-decisions-v0.13.0.csv"
SUMMARY = ROOT / "paper/data/forward-citation-author-screening-v0.13.0.json"
REPORT = ROOT / "paper/forward-citation-author-screening-v0.13.0.md"
ATTESTATION = ROOT / "evidence/human-review-attestation-v0.13.0.json"
POPULATION_LEDGER = ROOT / "paper/data/inaccessible-record-retrieval-v0.10.0.csv"
BUILDER = ROOT / "scripts/build_forward_citation_author_screening_v0_13_0.py"

EXPECTED_QUEUE_SHA256 = "6626338915c50da8e58e1487d3ef5f523a89421f0b21ae7f16f42b71140817e9"
EXPECTED_COUNTS = {
    "exclude-single-component": 11,
    "exclude-topic": 25,
    "retain-background": 22,
    "retain-close": 13,
}
ALLOWED_DECISIONS = set(EXPECTED_COUNTS)
AUTHOR = "Mark Julius Banasihan"
STATUS = "author-authorized-ai-assisted-screening-complete"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def expected_permission(decision: str) -> str:
    if decision.startswith("retain-"):
        return "none-until-proposition-review"
    return "none-excluded"


def main() -> int:
    errors: list[str] = []
    required = (QUEUE, DECISIONS, SUMMARY, REPORT, ATTESTATION, POPULATION_LEDGER, BUILDER)
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    if missing:
        raise SystemExit("forward-citation author screening: FAIL\nmissing: " + ", ".join(missing))

    digest = hashlib.sha256(QUEUE.read_bytes()).hexdigest()
    if digest != EXPECTED_QUEUE_SHA256:
        errors.append(f"frozen queue hash changed: {digest}")

    queue = read_csv(QUEUE)
    decisions = read_csv(DECISIONS)
    queue_keys = [row["record_key"] for row in queue]
    decision_keys = [row["record_key"] for row in decisions]
    sample_ids = [row["sample_id"] for row in decisions]
    if len(queue) != 71 or len(decisions) != 71:
        errors.append(f"expected 71 queue and decision rows; found {len(queue)} and {len(decisions)}")
    if len(decision_keys) != len(set(decision_keys)):
        errors.append("decision ledger contains duplicate record keys")
    if len(sample_ids) != len(set(sample_ids)):
        errors.append("decision ledger contains duplicate sample identifiers")
    if decision_keys != queue_keys:
        errors.append("decision ledger does not preserve frozen queue order and membership")

    queue_by_key = {row["record_key"]: row for row in queue}
    counts = Counter(row["author_decision"] for row in decisions)
    if dict(sorted(counts.items())) != EXPECTED_COUNTS:
        errors.append(f"decision counts changed: {dict(sorted(counts.items()))}")
    for row in decisions:
        key = row["record_key"]
        source = queue_by_key.get(key, {})
        if row["author_decision"] not in ALLOWED_DECISIONS:
            errors.append(f"{key}: invalid decision {row['author_decision']!r}")
        required_fields = (
            "sample_id", "title", "author_rationale", "review_basis_used", "source_locator",
            "decision_owner", "decision_date", "ai_assistance", "decision_status", "claim_permission",
        )
        blank = [field for field in required_fields if not row.get(field, "").strip()]
        if blank:
            errors.append(f"{key}: required fields are blank: {blank}")
        for field in ("sample_id", "title", "year", "source_locator"):
            if row.get(field, "") != source.get(field if field != "source_locator" else "source_locator", ""):
                errors.append(f"{key}: decision ledger disagrees with queue field {field}")
        if row["decision_owner"] != AUTHOR:
            errors.append(f"{key}: decision owner must be {AUTHOR}")
        if row["decision_status"] != STATUS:
            errors.append(f"{key}: invalid decision status")
        permission = expected_permission(row["author_decision"])
        if row["claim_permission"] != permission:
            errors.append(f"{key}: claim permission must be {permission}")
        if len(row["author_rationale"].split()) < 12:
            errors.append(f"{key}: rationale is too short to name a controlling mechanism")
        if "AI-assisted" not in row["ai_assistance"] or AUTHOR not in row["ai_assistance"]:
            errors.append(f"{key}: assistance disclosure is incomplete")

    correction = next((row for row in decisions if row["sample_id"] == "RS-FC-004"), {})
    if "original article" not in correction.get("author_rationale", ""):
        errors.append("RS-FC-004: correction-to-original version reconciliation is missing")

    population = {row["record_key"]: row for row in read_csv(POPULATION_LEDGER)}
    for row in decisions:
        key = row["record_key"]
        ledger_row = population.get(key)
        if ledger_row is None:
            errors.append(f"{key}: population ledger row is missing")
            continue
        for field, expected in (
            ("screening_decision", row["author_decision"]),
            ("author_notes", row["author_rationale"]),
            ("decision_owner", row["decision_owner"]),
            ("ai_assistance", row["ai_assistance"]),
        ):
            if ledger_row[field] != expected:
                errors.append(f"{key}: population ledger disagrees on {field}")

    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    summary_counts = summary.get("counts", {})
    if summary.get("status") != "FORWARD_CITATION_AUTHOR_SCREENING_CLOSED":
        errors.append("summary status is not closed")
    if summary.get("frozen_input_sha256") != digest:
        errors.append("summary frozen-input hash mismatch")
    if summary_counts.get("queue_records") != 71 or summary_counts.get("decisions_complete") != 71:
        errors.append("summary completion counts mismatch")
    if summary_counts.get("decisions_open") != 0 or summary_counts.get("claim_permission_granted") != 0:
        errors.append("summary opens a completed decision or grants claim permission")
    if summary_counts.get("decisions") != EXPECTED_COUNTS:
        errors.append("summary decision counts mismatch")
    if summary_counts.get("retained_for_source_review") != 35 or summary_counts.get("excluded") != 36:
        errors.append("summary retained or excluded totals mismatch")

    report = REPORT.read_text(encoding="utf-8")
    for marker in (
        "**Status:** `CLOSED`",
        "All 71 recovered-content records",
        "retains 35 records",
        "excludes 36 records",
        "It grants no manuscript claim permission",
    ):
        if marker not in report:
            errors.append(f"screening report lacks marker: {marker}")

    attestation = json.loads(ATTESTATION.read_text(encoding="utf-8"))
    if attestation.get("version") != "0.13.0" or attestation.get("decision_owner") != AUTHOR:
        errors.append("v0.13 attestation metadata mismatch")
    if attestation.get("status") != "AUTHOR_AUTHORIZED_AI_ASSISTED_SCREENING_COMPLETE":
        errors.append("v0.13 attestation status mismatch")
    scope = attestation.get("scope", {})
    if scope.get("screening_decisions_complete") != 71 or scope.get("manuscript_claim_permissions_granted") != 0:
        errors.append("v0.13 attestation scope mismatch")
    if not attestation.get("limits"):
        errors.append("v0.13 attestation lacks limits")

    process = subprocess.run(
        [sys.executable, str(BUILDER.relative_to(ROOT))],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if process.returncode != 0:
        errors.append("deterministic builder failed: " + (process.stdout + process.stderr).strip())

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        print(f"forward-citation author screening: INVALID ({len(errors)} error(s))")
        return 1
    print(
        "forward-citation author screening: CLOSED "
        "(71/71 decisions; 13 close; 22 background; 36 exclusions; 0 claim permissions)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
