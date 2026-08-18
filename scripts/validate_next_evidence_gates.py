#!/usr/bin/env python3
"""Initialize and validate the v0.10 literature evidence gates."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUTHOR_QUEUE = ROOT / "paper/data/author-screening-queue-v0.7.0.csv"
AUTHOR_DECISIONS = ROOT / "paper/data/author-screening-decisions-v0.9.0.csv"
FORMAL_PROPOSALS = ROOT / "paper/data/formal-screening-proposals-v0.7.0.json"
FULL_TEXT_LEDGER = ROOT / "paper/data/close-source-full-text-gate-v0.10.0.csv"
RETRIEVAL_LEDGER = ROOT / "paper/data/inaccessible-record-retrieval-v0.10.0.csv"
RISK_SAMPLE = ROOT / "paper/data/inaccessible-risk-sample-v0.11.0.csv"
RISK_SAMPLE_SUMMARY = ROOT / "paper/data/inaccessible-risk-sample-v0.11.0.json"
DIRECT_QUERY_EVIDENCE = ROOT / "paper/data/direct-query-retrieval-evidence-v0.11.0.json"
DIRECT_QUERY_RESOLUTION = ROOT / "paper/data/direct-query-resolution-v0.14.0.json"
FORWARD_CITATION_EVIDENCE = ROOT / "paper/data/forward-citation-retrieval-evidence-v0.12.0.json"
FORWARD_CITATION_QUEUE = ROOT / "paper/data/forward-citation-author-review-queue-v0.12.0.csv"
FORWARD_CITATION_DECISIONS = ROOT / "paper/data/forward-citation-author-screening-decisions-v0.13.0.csv"
FORWARD_CITATION_SCREENING = ROOT / "paper/data/forward-citation-author-screening-v0.13.0.json"
FORWARD_CITATION_ATTESTATION = ROOT / "evidence/human-review-attestation-v0.13.0.json"
FORWARD_PROPOSITION_REVIEW = ROOT / "paper/data/forward-citation-proposition-review-v0.14.0.json"
HUMAN_REVIEW_ATTESTATION = ROOT / "evidence/human-review-attestation-v0.11.0.json"
INTERFACE_LEDGER = ROOT / "paper/data/authenticated-interface-searches-v0.10.0.csv"
SUMMARY = ROOT / "paper/data/next-evidence-gates-v0.10.0.json"
REPORT = ROOT / "paper/next-evidence-gates-v0.10.0.md"

AUTHOR = "Mark Julius Banasihan"
EXPECTED_CLOSE = 27
EXPECTED_INACCESSIBLE = 1087
EXPECTED_RISK_SAMPLE = 284
EXPECTED_RISK_STRATA = {
    "forward-citation": 102,
    "backward-reference": 177,
    "direct-query": 5,
}
EXPECTED_FORWARD_CITATIONS = 102
TERMINAL_FULL_TEXT_STATES = {
    "verified",
    "abstract-only-not-used",
    "excluded-after-full-text",
    "inaccessible",
}
ALLOWED_FULL_TEXT_STATES = TERMINAL_FULL_TEXT_STATES | {"open"}
ALLOWED_RETRIEVAL_OUTCOMES = {
    "abstract-recovered",
    "full-text-recovered",
    "metadata-only",
    "duplicate",
    "outside-cutoff",
    "unavailable",
}
RECOVERED_CONTENT_OUTCOMES = {"abstract-recovered", "full-text-recovered"}
ALLOWED_SCREENING_DECISIONS = {
    "retain-close",
    "retain-background",
    "exclude-single-component",
    "exclude-topic",
    "exclude-record-type",
    "inaccessible",
}
REQUIRED_INTERFACES = {
    "scopus-or-web-of-science",
    "acm-digital-library",
    "ieee-xplore",
    "philpapers",
    "heinonline-or-hollis",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def initialize_ledgers() -> None:
    queue = {row["record_key"]: row for row in read_csv(AUTHOR_QUEUE)}
    decisions = read_csv(AUTHOR_DECISIONS)
    close = [row for row in decisions if row["author_decision"] == "retain-close"]
    if len(close) != EXPECTED_CLOSE:
        raise SystemExit(f"expected {EXPECTED_CLOSE} close sources; found {len(close)}")

    full_text_rows: list[dict[str, str]] = []
    for decision in close:
        source = queue[decision["record_key"]]
        full_text = "full_text" in decision["review_basis"]
        full_text_rows.append(
            {
                "record_key": decision["record_key"],
                "title": source["title"],
                "source_locator": decision["source_locator"],
                "screening_review_basis": decision["review_basis"],
                "verification_state": "verified" if full_text else "open",
                "full_text_locator": decision["source_locator"] if full_text else "",
                "verification_notes": (
                    "Full text was recorded as inspected during v0.9 author screening; "
                    "support remains proposition-specific."
                    if full_text
                    else ""
                ),
                "reviewer": decision["decision_owner"] if full_text else "",
                "review_date": decision["decision_date"] if full_text else "",
                "ai_assistance": decision["ai_assistance"] if full_text else "",
                "full_text_gate_pass": "true" if full_text else "false",
            }
        )
    write_csv(
        FULL_TEXT_LEDGER,
        [
            "record_key",
            "title",
            "source_locator",
            "screening_review_basis",
            "verification_state",
            "full_text_locator",
            "verification_notes",
            "reviewer",
            "review_date",
            "ai_assistance",
            "full_text_gate_pass",
        ],
        full_text_rows,
    )

    if not RETRIEVAL_LEDGER.exists():
        write_csv(
            RETRIEVAL_LEDGER,
            [
                "record_key",
                "retrieval_outcome",
                "retrieval_locator",
                "retrieval_date",
                "screening_decision",
                "author_notes",
                "decision_owner",
                "ai_assistance",
            ],
            [],
        )

    if not INTERFACE_LEDGER.exists():
        rows = [
            {
                "surface": surface,
                "status": "open",
                "access_condition": "",
                "query_record": "paper/formal-literature-search-protocol-v0.7.0.md#frozen-query-families",
                "search_date": "",
                "displayed_results": "",
                "deduplicated_records": "",
                "author_decisions_complete": "",
                "notes": "",
            }
            for surface in sorted(REQUIRED_INTERFACES)
        ]
        write_csv(
            INTERFACE_LEDGER,
            [
                "surface",
                "status",
                "access_condition",
                "query_record",
                "search_date",
                "displayed_results",
                "deduplicated_records",
                "author_decisions_complete",
                "notes",
            ],
            rows,
        )


def inspect() -> tuple[list[str], dict[str, object]]:
    errors: list[str] = []
    decisions = read_csv(AUTHOR_DECISIONS)
    close_keys = {
        row["record_key"] for row in decisions if row["author_decision"] == "retain-close"
    }
    full_text = read_csv(FULL_TEXT_LEDGER)
    ledger_keys = [row["record_key"] for row in full_text]

    if len(close_keys) != EXPECTED_CLOSE:
        errors.append(f"author ledger contains {len(close_keys)} close sources; expected {EXPECTED_CLOSE}")
    if len(ledger_keys) != len(set(ledger_keys)):
        errors.append("full-text ledger contains duplicate record keys")
    if set(ledger_keys) != close_keys:
        missing = sorted(close_keys - set(ledger_keys))
        extra = sorted(set(ledger_keys) - close_keys)
        errors.append(f"full-text ledger key mismatch; missing={missing}; extra={extra}")

    for row in full_text:
        state = row["verification_state"]
        if state not in ALLOWED_FULL_TEXT_STATES:
            errors.append(f'{row["record_key"]}: invalid verification state {state!r}')
        if state == "verified":
            required = (
                "full_text_locator",
                "verification_notes",
                "reviewer",
                "review_date",
                "ai_assistance",
            )
            blank = [field for field in required if not row[field].strip()]
            if blank:
                errors.append(f'{row["record_key"]}: verified row lacks {blank}')
            if row["reviewer"].strip() != AUTHOR:
                errors.append(f'{row["record_key"]}: reviewer must be {AUTHOR}')
            if row["full_text_gate_pass"].lower() != "true":
                errors.append(f'{row["record_key"]}: verified row must pass the full-text gate')
        elif row["full_text_gate_pass"].lower() == "true":
            errors.append(f'{row["record_key"]}: non-verified source cannot pass the full-text gate')

    proposal = json.loads(FORMAL_PROPOSALS.read_text(encoding="utf-8"))
    inaccessible_keys = {
        row["record_key"]
        for row in proposal["decisions"]
        if row["proposed_decision"] == "inaccessible"
    }
    if len(inaccessible_keys) != EXPECTED_INACCESSIBLE:
        errors.append(
            f"frozen proposal set contains {len(inaccessible_keys)} inaccessible records; "
            f"expected {EXPECTED_INACCESSIBLE}"
        )
    retrieval = read_csv(RETRIEVAL_LEDGER)
    retrieval_keys = [row["record_key"] for row in retrieval]
    if len(retrieval_keys) != len(set(retrieval_keys)):
        errors.append("inaccessible-record ledger contains duplicate record keys")
    unknown = sorted(set(retrieval_keys) - inaccessible_keys)
    if unknown:
        errors.append(f"inaccessible-record ledger contains unknown keys: {unknown}")
    for row in retrieval:
        if row["retrieval_outcome"] not in ALLOWED_RETRIEVAL_OUTCOMES:
            errors.append(
                f'{row["record_key"]}: invalid retrieval outcome {row["retrieval_outcome"]!r}'
            )
        required = ("retrieval_locator", "retrieval_date", "decision_owner", "ai_assistance")
        blank = [field for field in required if not row[field].strip()]
        if blank:
            errors.append(f'{row["record_key"]}: retrieval row lacks {blank}')
        if row["decision_owner"].strip() != AUTHOR:
            errors.append(f'{row["record_key"]}: decision owner must be {AUTHOR}')
        screening_decision = row["screening_decision"].strip()
        if screening_decision and screening_decision not in ALLOWED_SCREENING_DECISIONS:
            errors.append(
                f'{row["record_key"]}: invalid screening decision {screening_decision!r}'
            )
        if (
            row["retrieval_outcome"] in RECOVERED_CONTENT_OUTCOMES
            and not screening_decision
            and not row["author_notes"].startswith("OPEN:")
        ):
            errors.append(
                f'{row["record_key"]}: recovered content without a screening decision '
                "must preserve an OPEN note"
            )

    risk_sample = read_csv(RISK_SAMPLE)
    risk_keys = [row["record_key"] for row in risk_sample]
    if len(risk_keys) != EXPECTED_RISK_SAMPLE:
        errors.append(
            f"risk sample contains {len(risk_keys)} records; expected {EXPECTED_RISK_SAMPLE}"
        )
    if len(risk_keys) != len(set(risk_keys)):
        errors.append("risk sample contains duplicate record keys")
    unknown_risk_keys = sorted(set(risk_keys) - inaccessible_keys)
    if unknown_risk_keys:
        errors.append(f"risk sample contains unknown keys: {unknown_risk_keys}")
    risk_strata = Counter(row["primary_stratum"] for row in risk_sample)
    if dict(risk_strata) != EXPECTED_RISK_STRATA:
        errors.append(
            f"risk sample stratum allocation mismatch: {dict(risk_strata)}"
        )
    if any(row["selection_status"] != "selected-before-retrieval" for row in risk_sample):
        errors.append("risk sample contains an invalid selection status")
    risk_summary = json.loads(RISK_SAMPLE_SUMMARY.read_text(encoding="utf-8"))
    if risk_summary.get("status") != "FROZEN_BEFORE_RETRIEVAL":
        errors.append("risk sample summary status mismatch")
    if risk_summary.get("population_size") != EXPECTED_INACCESSIBLE:
        errors.append("risk sample summary population mismatch")
    if risk_summary.get("selected_records") != EXPECTED_RISK_SAMPLE:
        errors.append("risk sample summary selection count mismatch")

    direct_query_keys = {
        row["record_key"] for row in risk_sample if row["primary_stratum"] == "direct-query"
    }
    direct_query_evidence = json.loads(DIRECT_QUERY_EVIDENCE.read_text(encoding="utf-8"))
    direct_query_resolution = json.loads(DIRECT_QUERY_RESOLUTION.read_text(encoding="utf-8"))
    if (
        direct_query_resolution.get("status") != "DIRECT_QUERY_SCREENING_CLOSED"
        or direct_query_resolution.get("decision") != "retain-close"
        or direct_query_resolution.get("claim_permission")
        != "none-until-readable-proposition-review"
    ):
        errors.append("v0.14 direct-query resolution metadata mismatch")
    evidence_records = direct_query_evidence.get("records", [])
    evidence_keys = [row.get("record_key", "") for row in evidence_records]
    if direct_query_evidence.get("status") != "PARTIAL_SCREENING":
        errors.append("direct-query evidence status mismatch")
    if len(evidence_keys) != len(set(evidence_keys)):
        errors.append("direct-query evidence contains duplicate record keys")
    if set(evidence_keys) != direct_query_keys:
        errors.append("direct-query evidence does not match the frozen direct-query stratum")
    evidence_outcomes = Counter(row.get("retrieval_outcome", "") for row in evidence_records)
    evidence_decisions = Counter(
        row.get("screening_decision")
        for row in evidence_records
        if row.get("screening_decision")
    )
    expected_evidence_counts = {
        "records": len(evidence_records),
        "full_text_recovered": evidence_outcomes["full-text-recovered"],
        "abstract_recovered": evidence_outcomes["abstract-recovered"],
        "screening_complete": sum(evidence_decisions.values()),
        "screening_open": len(evidence_records) - sum(evidence_decisions.values()),
        "retain_close": evidence_decisions["retain-close"],
        "retain_background": evidence_decisions["retain-background"],
    }
    if direct_query_evidence.get("counts") != expected_evidence_counts:
        errors.append("direct-query evidence counts do not match its records")
    retrieval_by_key = {row["record_key"]: row for row in retrieval}
    for evidence_row in evidence_records:
        key = evidence_row.get("record_key", "")
        evidence_required = (
            "sample_id",
            "title",
            "retrieval_outcome",
            "retrieval_locator",
            "review_basis",
            "screening_rationale",
            "limits",
            "decision_owner",
            "ai_assistance",
        )
        evidence_blank = [field for field in evidence_required if not evidence_row.get(field)]
        if evidence_blank:
            errors.append(f"{key}: direct-query evidence lacks {evidence_blank}")
        if not evidence_row.get("routes_checked"):
            errors.append(f"{key}: direct-query evidence lacks checked routes")
        if not evidence_row.get("source_evidence"):
            errors.append(f"{key}: direct-query evidence lacks source observations")
        ledger_row = retrieval_by_key.get(key)
        if ledger_row is None:
            errors.append(f"{key}: direct-query evidence lacks a retrieval-ledger row")
            continue
        expected_decision = evidence_row.get("screening_decision") or ""
        if key == direct_query_resolution.get("record_key"):
            expected_decision = direct_query_resolution.get("decision", "")
        for field, expected in (
            ("retrieval_outcome", evidence_row.get("retrieval_outcome", "")),
            ("retrieval_locator", evidence_row.get("retrieval_locator", "")),
            ("screening_decision", expected_decision),
            ("decision_owner", evidence_row.get("decision_owner", "")),
        ):
            if ledger_row[field] != expected:
                errors.append(f"{key}: direct-query evidence disagrees with ledger field {field}")

    forward_keys = {
        row["record_key"] for row in risk_sample if row["primary_stratum"] == "forward-citation"
    }
    forward_evidence = json.loads(FORWARD_CITATION_EVIDENCE.read_text(encoding="utf-8"))
    forward_records = forward_evidence.get("records", [])
    forward_evidence_keys = [row.get("record_key", "") for row in forward_records]
    if forward_evidence.get("status") != "RETRIEVAL_COMPLETE_SCREENING_OPEN":
        errors.append("forward-citation evidence status mismatch")
    if len(forward_evidence_keys) != len(set(forward_evidence_keys)):
        errors.append("forward-citation evidence contains duplicate record keys")
    if len(forward_evidence_keys) != EXPECTED_FORWARD_CITATIONS:
        errors.append(
            f"forward-citation evidence contains {len(forward_evidence_keys)} records; "
            f"expected {EXPECTED_FORWARD_CITATIONS}"
        )
    if set(forward_evidence_keys) != forward_keys:
        errors.append("forward-citation evidence does not match the frozen forward stratum")
    forward_outcomes = Counter(row.get("retrieval_outcome", "") for row in forward_records)
    forward_screening_required = sum(
        row.get("retrieval_outcome") in RECOVERED_CONTENT_OUTCOMES
        for row in forward_records
    )
    forward_snapshot_screening_complete = sum(
        bool(row.get("screening_decision")) for row in forward_records
    )
    expected_forward_counts = {
        "selected": len(forward_records),
        "retrieval_complete": len(forward_records),
        "screening_required": forward_screening_required,
        "screening_complete": forward_snapshot_screening_complete,
        "screening_open": forward_screening_required - forward_snapshot_screening_complete,
        "outcomes": dict(sorted(forward_outcomes.items())),
    }
    if forward_evidence.get("counts") != expected_forward_counts:
        errors.append("forward-citation evidence counts do not match its records")
    for evidence_row in forward_records:
        key = evidence_row.get("record_key", "")
        required = (
            "sample_id", "title", "retrieval_outcome", "retrieval_locator",
            "retrieval_date", "routes_checked", "source_evidence", "review_basis",
            "screening_rationale", "decision_owner", "ai_assistance", "claim_limit",
        )
        blank = [field for field in required if not evidence_row.get(field)]
        if blank:
            errors.append(f"{key}: forward-citation evidence lacks {blank}")
        ledger_row = retrieval_by_key.get(key)
        if ledger_row is None:
            errors.append(f"{key}: forward-citation evidence lacks a retrieval-ledger row")
            continue
        for field, expected in (
            ("retrieval_outcome", evidence_row.get("retrieval_outcome", "")),
            ("retrieval_locator", evidence_row.get("retrieval_locator", "")),
            ("retrieval_date", evidence_row.get("retrieval_date", "")),
            ("decision_owner", evidence_row.get("decision_owner", "")),
        ):
            if ledger_row[field] != expected:
                errors.append(f"{key}: forward-citation evidence disagrees with ledger field {field}")

    forward_queue = read_csv(FORWARD_CITATION_QUEUE)
    queue_keys = [row["record_key"] for row in forward_queue]
    recovered_forward_keys = {
        row.get("record_key", "")
        for row in forward_records
        if row.get("retrieval_outcome") in RECOVERED_CONTENT_OUTCOMES
    }
    if len(queue_keys) != len(set(queue_keys)):
        errors.append("forward-citation author queue contains duplicate record keys")
    if set(queue_keys) != recovered_forward_keys:
        errors.append("forward-citation author queue does not match recovered source content")
    for row in forward_queue:
        if row["decision_owner"] != AUTHOR:
            errors.append(f'{row["record_key"]}: forward queue decision owner must be {AUTHOR}')
        if row["decision_status"] not in {"pending-author-review", "author-reviewed"}:
            errors.append(f'{row["record_key"]}: invalid forward queue decision status')
        if row["decision_status"] == "pending-author-review":
            if row["author_decision"] or row["author_rationale"]:
                errors.append(f'{row["record_key"]}: pending forward queue row contains a decision')
            if row["claim_permission"] != "none-until-decision":
                errors.append(f'{row["record_key"]}: pending forward queue row grants claim permission')

    forward_decisions = read_csv(FORWARD_CITATION_DECISIONS)
    decision_keys = [row["record_key"] for row in forward_decisions]
    if decision_keys != queue_keys:
        errors.append("v0.13 forward decisions do not preserve the frozen queue order")
    forward_decision_counts = Counter(row["author_decision"] for row in forward_decisions)
    forward_screening_complete = len(forward_decisions)
    if forward_screening_complete != forward_screening_required:
        errors.append(
            f"v0.13 forward screening contains {forward_screening_complete} decisions; "
            f"expected {forward_screening_required}"
        )
    for decision_row in forward_decisions:
        key = decision_row["record_key"]
        ledger_row = retrieval_by_key.get(key)
        if ledger_row is None:
            errors.append(f"{key}: v0.13 decision lacks a retrieval-ledger row")
            continue
        if ledger_row["screening_decision"] != decision_row["author_decision"]:
            errors.append(f"{key}: v0.13 decision disagrees with population ledger")
        if decision_row["claim_permission"] not in {
            "none-until-proposition-review", "none-excluded"
        }:
            errors.append(f"{key}: v0.13 decision contains an invalid claim-permission state")

    forward_screening_summary = json.loads(
        FORWARD_CITATION_SCREENING.read_text(encoding="utf-8")
    )
    if forward_screening_summary.get("status") != "FORWARD_CITATION_AUTHOR_SCREENING_CLOSED":
        errors.append("v0.13 forward-screening summary status mismatch")
    if forward_screening_summary.get("counts", {}).get("decisions") != dict(
        sorted(forward_decision_counts.items())
    ):
        errors.append("v0.13 forward-screening summary counts mismatch")
    forward_attestation = json.loads(
        FORWARD_CITATION_ATTESTATION.read_text(encoding="utf-8")
    )
    if (
        forward_attestation.get("decision_owner") != AUTHOR
        or forward_attestation.get("scope", {}).get("screening_decisions_complete")
        != forward_screening_complete
    ):
        errors.append("v0.13 forward-screening attestation mismatch")

    proposition_review = json.loads(
        FORWARD_PROPOSITION_REVIEW.read_text(encoding="utf-8")
    )
    proposition_counts = proposition_review.get("counts", {})
    if (
        proposition_review.get("status") != "PROPOSITION_REVIEW_CLOSED"
        or proposition_counts.get("retained_close_sources") != 13
        or proposition_counts.get("reviewed") != 13
        or proposition_counts.get("open") != 0
        or proposition_counts.get("manuscript_use") != 5
        or proposition_counts.get("background_only") != 2
        or proposition_counts.get("quarantined") != 6
        or proposition_counts.get("proposition_permissions") != 5
    ):
        errors.append("v0.14 forward proposition-review summary mismatch")

    attestation = json.loads(HUMAN_REVIEW_ATTESTATION.read_text(encoding="utf-8"))
    if attestation.get("version") != "0.11.0" or attestation.get("reviewer") != AUTHOR:
        errors.append("human-review attestation metadata mismatch")
    evidence_by_sample = {row.get("sample_id", ""): row for row in evidence_records}
    decision_attestations = attestation.get("screening_decisions", [])
    attested_samples = [row.get("sample_id", "") for row in decision_attestations]
    if len(attested_samples) != len(set(attested_samples)):
        errors.append("human-review attestation contains duplicate sample identifiers")
    if set(attested_samples) != set(evidence_by_sample):
        errors.append(
            "human-review attestation does not match the five-record direct-query evidence"
        )
    for row in decision_attestations:
        sample_id = row.get("sample_id", "")
        source = evidence_by_sample.get(sample_id, {})
        if row.get("decision") != source.get("screening_decision"):
            errors.append(f"{sample_id}: attested decision disagrees with direct-query evidence")
        expected_support = "recorded" if source.get("screening_decision") else "open"
        if row.get("support_review") != expected_support:
            errors.append(f"{sample_id}: attested support-review state mismatch")
        if not row.get("scope"):
            errors.append(f"{sample_id}: attestation lacks a scope statement")
    claim_attestations = attestation.get("claim_attestations", [])
    expected_claims = {f"PAPER-C{number}" for number in range(27, 33)}
    attested_claims = {row.get("claim_id", "") for row in claim_attestations}
    if attested_claims != expected_claims:
        errors.append("human-review attestation does not cover PAPER-C27 through PAPER-C32")
    if any(row.get("support_review") != "recorded" for row in claim_attestations):
        errors.append("human-review attestation contains an unrecorded v0.11 claim review")
    if not attestation.get("limits"):
        errors.append("human-review attestation lacks declared limits")

    interfaces = read_csv(INTERFACE_LEDGER)
    interface_names = [row["surface"] for row in interfaces]
    if len(interface_names) != len(set(interface_names)):
        errors.append("authenticated-interface ledger contains duplicate surfaces")
    if set(interface_names) != REQUIRED_INTERFACES:
        errors.append("authenticated-interface ledger does not match the five declared surfaces")
    for row in interfaces:
        if row["status"] not in {"open", "complete", "access-failure"}:
            errors.append(f'{row["surface"]}: invalid interface status {row["status"]!r}')
        if row["status"] != "open":
            required = ("access_condition", "search_date", "notes")
            blank = [field for field in required if not row[field].strip()]
            if blank:
                errors.append(f'{row["surface"]}: completed interface row lacks {blank}')

    states = Counter(row["verification_state"] for row in full_text)
    terminal = sum(states[state] for state in TERMINAL_FULL_TEXT_STATES)
    verified = states["verified"]
    open_full_text = states["open"]
    retrieved = len(retrieval)
    retrieval_outcomes = Counter(row["retrieval_outcome"] for row in retrieval)
    recovered_rows = [
        row for row in retrieval if row["retrieval_outcome"] in RECOVERED_CONTENT_OUTCOMES
    ]
    screening_decisions = Counter(
        row["screening_decision"] for row in recovered_rows if row["screening_decision"]
    )
    screening_required = len(recovered_rows)
    screening_complete = sum(screening_decisions.values())
    sampled_retrieved = len(set(risk_keys) & set(retrieval_keys))
    sampled_rows = [row for row in retrieval if row["record_key"] in set(risk_keys)]
    sampled_screening_required = sum(
        row["retrieval_outcome"] in RECOVERED_CONTENT_OUTCOMES for row in sampled_rows
    )
    sampled_screening_complete = sum(
        row["retrieval_outcome"] in RECOVERED_CONTENT_OUTCOMES
        and bool(row["screening_decision"])
        for row in sampled_rows
    )
    direct_query_rows = [row for row in retrieval if row["record_key"] in direct_query_keys]
    direct_query_screening_complete = sum(bool(row["screening_decision"]) for row in direct_query_rows)
    interface_counts = Counter(row["status"] for row in interfaces)
    coverage_status = "CLOSED" if retrieved == EXPECTED_INACCESSIBLE else "OPEN"
    interface_status = (
        "CLOSED"
        if interface_counts["complete"] == len(REQUIRED_INTERFACES)
        else "OPEN"
    )
    full_text_status = "CLOSED" if terminal == EXPECTED_CLOSE else "OPEN"

    summary: dict[str, object] = {
        "version": "0.10.0",
        "status": "INVALID" if errors else "OPEN",
        "decision_owner": AUTHOR,
        "source_release": "v0.9.0",
        "gates": {
            "close_source_full_text": {
                "status": full_text_status,
                "records": EXPECTED_CLOSE,
                "terminal": terminal,
                "verified": verified,
                "abstract_only_not_used": states["abstract-only-not-used"],
                "excluded_after_full_text": states["excluded-after-full-text"],
                "inaccessible": states["inaccessible"],
                "open": open_full_text,
                "terminal_without_verification": terminal - verified,
                "claim_rule": "Only verified full text may support a proposition that exceeds the abstract.",
            },
            "inaccessible_record_retrieval": {
                "status": coverage_status,
                "records": EXPECTED_INACCESSIBLE,
                "retrieval_rows_complete": retrieved,
                "retrieval_rows_open": EXPECTED_INACCESSIBLE - retrieved,
                "retrieval_outcomes": dict(sorted(retrieval_outcomes.items())),
                "recovered_content_requiring_screening": screening_required,
                "screening_decisions_complete": screening_complete,
                "screening_decisions_open": screening_required - screening_complete,
                "screening_decisions": dict(sorted(screening_decisions.items())),
                "recovered_close_sources": screening_decisions["retain-close"],
                "residual_risk_sample": {
                    "status": "FROZEN_BEFORE_RETRIEVAL",
                    "selected": EXPECTED_RISK_SAMPLE,
                    "sampled_retrieval_complete": sampled_retrieved,
                    "sampled_retrieval_open": EXPECTED_RISK_SAMPLE - sampled_retrieved,
                    "sampled_screening_required": sampled_screening_required,
                    "sampled_screening_complete": sampled_screening_complete,
                    "sampled_screening_open": (
                        sampled_screening_required - sampled_screening_complete
                    ),
                    "strata": EXPECTED_RISK_STRATA,
                    "sample_record": "paper/data/inaccessible-risk-sample-v0.11.0.csv",
                },
                "direct_query_tranche": {
                    "status": "SCREENING_CLOSED_WITH_SOURCE_LIMIT",
                    "selected": len(direct_query_keys),
                    "retrieval_complete": len(direct_query_rows),
                    "screening_complete": direct_query_screening_complete,
                    "screening_open": len(direct_query_rows) - direct_query_screening_complete,
                    "evidence_record": "paper/data/direct-query-retrieval-evidence-v0.11.0.json",
                    "resolution_overlay": "paper/data/direct-query-resolution-v0.14.0.json",
                    "proposition_permissions": 0,
                },
                "forward_citation_tranche": {
                    "status": "PROPOSITION_REVIEW_CLOSED",
                    "selected": len(forward_records),
                    "retrieval_complete": len(forward_records),
                    "screening_required": forward_screening_required,
                    "screening_complete": forward_screening_complete,
                    "screening_open": forward_screening_required - forward_screening_complete,
                    "screening_decisions": dict(sorted(forward_decision_counts.items())),
                    "retrieval_outcomes": dict(sorted(forward_outcomes.items())),
                    "evidence_record": "paper/data/forward-citation-retrieval-evidence-v0.12.0.json",
                    "author_queue": "paper/data/forward-citation-author-review-queue-v0.12.0.csv",
                    "decision_ledger": "paper/data/forward-citation-author-screening-decisions-v0.13.0.csv",
                    "proposition_review": "paper/data/forward-citation-proposition-review-v0.14.0.json",
                    "proposition_review_counts": proposition_counts,
                },
                "claim_rule": "A completed risk sample estimates residual risk and does not establish exhaustive coverage.",
            },
            "authenticated_interfaces": {
                "status": interface_status,
                "required_surfaces": len(REQUIRED_INTERFACES),
                "complete": interface_counts["complete"],
                "access_failures": interface_counts["access-failure"],
                "open": interface_counts["open"],
                "claim_rule": "An access failure remains a coverage limit and cannot close the originality exception.",
            },
            "independent_assessment": {
                "status": "OPEN",
                "next_cycle": False,
                "claim_rule": "Internal reproducibility work cannot establish independent reliability or field validity.",
            },
        },
        "validation_errors": errors,
    }
    return errors, summary


def report_text(summary: dict[str, object]) -> str:
    gates = summary["gates"]
    full_text = gates["close_source_full_text"]
    inaccessible = gates["inaccessible_record_retrieval"]
    risk_sample = inaccessible["residual_risk_sample"]
    direct_query = inaccessible["direct_query_tranche"]
    forward_citation = inaccessible["forward_citation_tranche"]
    interfaces = gates["authenticated_interfaces"]
    return f"""# Next Evidence Gates, v0.10.0

**Status:** `{summary['status']}`  
**Decision owner:** {summary['decision_owner']}  
**Source release:** `{summary['source_release']}`

## Decision

The next research cycle addresses support and search coverage before the manuscript makes a stronger contribution claim. The case question and the three frozen topics remain unchanged.

## Gate state

| Gate | Population | Complete | Open | Current state |
|---|---:|---:|---:|---|
| Close-source full-text verification | {full_text['records']} | {full_text['terminal']} terminal | {full_text['open']} | `{full_text['status']}` |
| Inaccessible-record retrieval | {inaccessible['records']} | {inaccessible['retrieval_rows_complete']} | {inaccessible['retrieval_rows_open']} | `{inaccessible['status']}` |
| Authenticated and disciplinary interfaces | {interfaces['required_surfaces']} | {interfaces['complete']} | {interfaces['open']} | `{interfaces['status']}` |
| Independent assessment | 1 study | 0 | 1 | `OPEN`, outside this cycle |

## Residual-risk sample

The sample is frozen before retrieval with {risk_sample['selected']} selected records: {risk_sample['strata']['forward-citation']} forward citations, {risk_sample['strata']['backward-reference']} backward references, and {risk_sample['strata']['direct-query']} direct-query records. Retrieval outcomes are recorded for {risk_sample['sampled_retrieval_complete']} of {risk_sample['selected']} sampled records. Recovered content requires screening for {risk_sample['sampled_screening_required']} records; {risk_sample['sampled_screening_complete']} decisions are recorded and {risk_sample['sampled_screening_open']} {'remains' if risk_sample['sampled_screening_open'] == 1 else 'remain'} open. Frozen membership establishes selection lineage. The current partial result supplies no prevalence, exhaustive-coverage, or originality finding.

## Direct-query tranche

The five-record direct-query stratum has {direct_query['retrieval_complete']} retrieval outcomes and {direct_query['screening_complete']} bounded screening decisions, with no screening decision open. The v0.14 overlay classifies RS-DQ-004 as close from its title and workflow relevance. Its unreadable text layer and unresolved author-name mismatch grant zero proposition permission. The [tranche report](direct-query-retrieval-tranche-v0.11.0.md), [historical evidence record](data/direct-query-retrieval-evidence-v0.11.0.json), and [resolution overlay](data/direct-query-resolution-v0.14.0.json) preserve the route, basis, decision, and limit.

## Forward-citation tranche

All {forward_citation['selected']} records in the frozen forward-citation stratum have a retrieval outcome. The pass recovered full text for {forward_citation['retrieval_outcomes'].get('full-text-recovered', 0)} records and abstracts for {forward_citation['retrieval_outcomes'].get('abstract-recovered', 0)} records. It recorded {forward_citation['retrieval_outcomes'].get('metadata-only', 0)} metadata-only outcomes, {forward_citation['retrieval_outcomes'].get('unavailable', 0)} unavailable outcomes, and {forward_citation['retrieval_outcomes'].get('duplicate', 0)} duplicates. All {forward_citation['screening_required']} recovered-content records have an author-authorized, AI-assisted screening decision: {forward_citation['screening_decisions'].get('retain-close', 0)} close, {forward_citation['screening_decisions'].get('retain-background', 0)} background, {forward_citation['screening_decisions'].get('exclude-single-component', 0)} single-component exclusions, and {forward_citation['screening_decisions'].get('exclude-topic', 0)} topic exclusions. All {forward_citation['proposition_review_counts']['retained_close_sources']} close sources then received proposition review. Five receive one locator-bounded manuscript permission each, two remain background-only, and six remain quarantined.

## Claim controls

1. A title-and-abstract review can support a bounded description of a source's declared purpose, model, or result.
2. A proposition that exceeds the abstract requires a verified full-text locator and proposition-specific support check.
3. A risk sample of inaccessible records can estimate residual coverage risk. It cannot establish exhaustive retrieval.
4. An authenticated-interface access failure remains visible and leaves the originality exception open.
5. Internal validation can test reproducibility and corruption detection. It cannot establish independent reliability or field validity.

## Current finding

The 89-decision author gate resolved the original screening queue. The retained-close full-text gate is closed with {full_text['verified']} verified sources, {full_text['abstract_only_not_used']} abstract-only sources quarantined from stronger use, {full_text['excluded_after_full_text']} exclusions after full-text review, and {full_text['inaccessible']} inaccessible sources. Gate 2 has recorded {inaccessible['retrieval_rows_complete']} retrieval outcomes and leaves {inaccessible['retrieval_rows_open']} records unresolved. Its recovered content has {inaccessible['screening_decisions_complete']} decisions and {inaccessible['screening_decisions_open']} open decisions. Proposition permission remains a separate, stricter gate: five forward-citation propositions pass, while RS-DQ-004 retains zero permission.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--initialize", action="store_true", help="create the three v0.10 ledgers")
    parser.add_argument("--write-report", action="store_true", help="write the generated JSON and Markdown summaries")
    parser.add_argument("--check", action="store_true", help="verify committed ledgers and summaries")
    args = parser.parse_args()

    if args.initialize:
        initialize_ledgers()
    required = (
        FULL_TEXT_LEDGER,
        RETRIEVAL_LEDGER,
        RISK_SAMPLE,
        RISK_SAMPLE_SUMMARY,
        DIRECT_QUERY_EVIDENCE,
        DIRECT_QUERY_RESOLUTION,
        FORWARD_CITATION_EVIDENCE,
        FORWARD_CITATION_QUEUE,
        FORWARD_CITATION_DECISIONS,
        FORWARD_CITATION_SCREENING,
        FORWARD_CITATION_ATTESTATION,
        FORWARD_PROPOSITION_REVIEW,
        HUMAN_REVIEW_ATTESTATION,
        INTERFACE_LEDGER,
    )
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    if missing:
        raise SystemExit("next evidence gates: FAIL\nmissing ledgers: " + ", ".join(missing))

    errors, summary = inspect()
    expected_summary = json.dumps(summary, indent=2) + "\n"
    expected_report = report_text(summary)
    if args.write_report:
        SUMMARY.write_text(expected_summary, encoding="utf-8")
        REPORT.write_text(expected_report, encoding="utf-8")
    if args.check:
        if not SUMMARY.is_file() or SUMMARY.read_text(encoding="utf-8") != expected_summary:
            errors.append("next-evidence-gate JSON summary is missing or stale")
        if not REPORT.is_file() or REPORT.read_text(encoding="utf-8") != expected_report:
            errors.append("next-evidence-gate Markdown report is missing or stale")
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        print(f"next evidence gates: INVALID ({len(errors)} error(s))")
        return 1

    gate_data = summary["gates"]
    full_text = gate_data["close_source_full_text"]
    inaccessible = gate_data["inaccessible_record_retrieval"]
    print(
        "next evidence gates: OPEN "
        f"({full_text['verified']}/{full_text['records']} close sources full-text verified; "
        f"{inaccessible['retrieval_rows_complete']}/{inaccessible['records']} inaccessible records resolved)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
