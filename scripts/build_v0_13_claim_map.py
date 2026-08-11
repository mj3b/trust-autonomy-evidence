#!/usr/bin/env python3
"""Build and verify the v0.13 claim map from the v0.12 builder."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from build_v0_12_claim_map import build as build_v0_12
from build_v0_11_claim_map import evidence, fitness, render


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = "evidence/claim-evidence-map.json"
FORWARD_EVIDENCE = "paper/data/forward-citation-retrieval-evidence-v0.12.0.json"
FORWARD_DECISIONS = "paper/data/forward-citation-author-screening-decisions-v0.13.0.csv"
FORWARD_SUMMARY = "paper/data/forward-citation-author-screening-v0.13.0.json"
FORWARD_REPORT = "paper/forward-citation-author-screening-v0.13.0.md"
FORWARD_PROTOCOL = "paper/forward-citation-author-screening-protocol-v0.13.0.md"
FORWARD_VALIDATOR = "scripts/validate_forward_citation_author_screening_v0_13_0.py"
ATTESTATION = "evidence/human-review-attestation-v0.13.0.json"
AUTHOR = "Mark Julius Banasihan"
REVIEW_DATE = "2026-08-11"


def human_review(claim_id: str, note: str) -> dict[str, Any]:
    return {
        "status": "recorded",
        "reviewer": AUTHOR,
        "review_date": REVIEW_DATE,
        "attestation_path": ATTESTATION,
        "note": f"{claim_id}: {note}",
    }


def retrieval_claim() -> dict[str, Any]:
    return {
        "claim_id": "PAPER-C33",
        "claim_text": (
            "The frozen forward-citation tranche records 102 retrieval outcomes: 34 full-text "
            "recoveries, 37 abstract recoveries, 26 metadata-only outcomes, 3 duplicates, and "
            "2 unavailable records."
        ),
        "claim_class": "numerical",
        "claim_scope": "paper",
        "status": "supported",
        "verification_rule": (
            "The 102 frozen forward-citation keys and five retrieval classes must resolve from "
            "the v0.12 evidence record, and completed source screening must preserve the frozen queue."
        ),
        "evidence": [
            evidence("C33-SELECTED", FORWARD_EVIDENCE, "json_pointer", "/counts/selected", "numeric", expected_value=102),
            evidence("C33-FULL", FORWARD_EVIDENCE, "json_pointer", "/counts/outcomes/full-text-recovered", "numeric", expected_value=34),
            evidence("C33-ABSTRACT", FORWARD_EVIDENCE, "json_pointer", "/counts/outcomes/abstract-recovered", "numeric", expected_value=37),
            evidence("C33-METADATA", FORWARD_EVIDENCE, "json_pointer", "/counts/outcomes/metadata-only", "numeric", expected_value=26),
            evidence("C33-DUPLICATE", FORWARD_EVIDENCE, "json_pointer", "/counts/outcomes/duplicate", "numeric", expected_value=3),
            evidence("C33-UNAVAILABLE", FORWARD_EVIDENCE, "json_pointer", "/counts/outcomes/unavailable", "numeric", expected_value=2),
            evidence(
                "C33-REVIEW",
                ATTESTATION,
                "text_marker",
                "authorized AI-assisted inspection and screening of the frozen 71-record forward-citation queue",
                "provenance",
            ),
        ],
        "fitness": fitness(
            directness=("pass", "The frozen evidence record directly exposes membership and recomputed retrieval counts."),
            contemporaneity=("pass", "The retrieval record and screening attestation are dated for the v0.12 and v0.13 checkpoints."),
            independence=("outside_scope", "The claim reports repository workflow state and no independent scientific judgment."),
            completeness=("pass", "Every frozen forward-citation key appears once and every recovered-content key entered the screening queue."),
            publication_authority=("pass", "The repository records its own retrieval workflow and names the decision owner."),
        ),
        "dependencies": [],
        "dependency_closure": "pass",
        "conclusion_eligible": True,
        "human_review": human_review(
            "PAPER-C33",
            "Reviewed as the bounded 102-record retrieval state after the recovered-content queue received decisions.",
        ),
        "scope_terms": [],
        "limitations": [
            "Retrieval outcomes identify access states and do not establish source truth, relevance, exhaustive coverage, or prevalence."
        ],
        "reversal_conditions": [
            "A frozen key, retrieval outcome, queue membership, or recomputed count changes."
        ],
    }


def screening_claim() -> dict[str, Any]:
    return {
        "claim_id": "PAPER-C34",
        "claim_text": (
            "All 71 recovered forward-citation records have a screening decision: 13 close, "
            "22 background, 11 single-component exclusions, and 25 topic exclusions; none has "
            "permission to support a manuscript proposition."
        ),
        "claim_class": "numerical",
        "claim_scope": "paper",
        "status": "supported",
        "verification_rule": (
            "The frozen queue hash, ordered ledger membership, required decision fields, population-ledger "
            "agreement, recomputed class totals, author attestation, and zero-permission rule must all pass."
        ),
        "evidence": [
            evidence("C34-QUEUE", FORWARD_SUMMARY, "json_pointer", "/counts/queue_records", "numeric", expected_value=71),
            evidence("C34-COMPLETE", FORWARD_SUMMARY, "json_pointer", "/counts/decisions_complete", "numeric", expected_value=71),
            evidence("C34-OPEN", FORWARD_SUMMARY, "json_pointer", "/counts/decisions_open", "numeric", expected_value=0),
            evidence("C34-CLOSE", FORWARD_SUMMARY, "json_pointer", "/counts/decisions/retain-close", "numeric", expected_value=13),
            evidence("C34-BACKGROUND", FORWARD_SUMMARY, "json_pointer", "/counts/decisions/retain-background", "numeric", expected_value=22),
            evidence("C34-SINGLE", FORWARD_SUMMARY, "json_pointer", "/counts/decisions/exclude-single-component", "numeric", expected_value=11),
            evidence("C34-TOPIC", FORWARD_SUMMARY, "json_pointer", "/counts/decisions/exclude-topic", "numeric", expected_value=25),
            evidence("C34-PERMISSION", FORWARD_SUMMARY, "json_pointer", "/counts/claim_permission_granted", "numeric", expected_value=0),
            evidence("C34-LEDGER", FORWARD_DECISIONS, "file", "", "provenance"),
            evidence("C34-METHOD", FORWARD_PROTOCOL, "markdown_heading", "## Completion conditions", "method"),
            evidence(
                "C34-IMPLEMENTATION",
                FORWARD_VALIDATOR,
                "text_marker",
                "decision ledger does not preserve frozen queue order and membership",
                "implementation",
            ),
            evidence("C34-REPORT", FORWARD_REPORT, "markdown_heading", "## Decision control", "method"),
            evidence(
                "C34-ATTESTATION",
                ATTESTATION,
                "text_marker",
                "AUTHOR_AUTHORIZED_AI_ASSISTED_SCREENING_COMPLETE",
                "provenance",
            ),
        ],
        "fitness": fitness(
            directness=("pass", "The decision summary, ordered ledger, and validator directly establish the screening counts and permission states."),
            contemporaneity=("pass", "The protocol, decisions, and attestation share the v0.13 decision date."),
            independence=("outside_scope", "The claim reports an author-owned workflow state and makes no independent reliability claim."),
            completeness=("pass", "All 71 frozen queue records have the required decision, rationale, basis, locator, owner, date, disclosure, and permission state."),
            publication_authority=("pass", "Mark Julius Banasihan is the declared decision owner and repository author."),
        ),
        "dependencies": ["PAPER-C33"],
        "dependency_closure": "pass",
        "conclusion_eligible": True,
        "human_review": human_review(
            "PAPER-C34",
            "Reviewed as the bounded author-authorized, AI-assisted screening composition and zero-permission result.",
        ),
        "scope_terms": [],
        "limitations": [
            "Screening determines corpus membership only; retained sources require proposition-level review with stable locators.",
            "The screening pass supplies no independent agreement, exhaustive-coverage, originality, prevalence, field-validity, or institutional-effect result.",
        ],
        "reversal_conditions": [
            "A queue hash, record membership, decision, rationale, permission state, attestation, or recomputed count changes."
        ],
    }


def build() -> dict[str, Any]:
    result = build_v0_12()
    result["version"] = "0.13.0"
    result["scope_id"] = "TAE-COE-V0.13.0"
    result["description"] = (
        "Material paper and repository claims audited through v0.13.0, including the "
        "closed 71-record forward-citation screening gate and its proposition-review boundary."
    )
    result["claims"] = [
        claim for claim in result["claims"] if claim["claim_id"] != "PAPER-C33"
    ]
    result["claims"].extend([retrieval_claim(), screening_claim()])
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render(build())
    output = ROOT / OUTPUT_PATH
    if args.write:
        output.write_text(expected, encoding="utf-8")
    if args.check and (not output.is_file() or output.read_text(encoding="utf-8") != expected):
        raise SystemExit("v0.13 claim map: FAIL\ncommitted output differs from the deterministic builder")
    print("v0.13 claim map: PASS (28 claims; PAPER-C33 and PAPER-C34 eligible within workflow scope)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
