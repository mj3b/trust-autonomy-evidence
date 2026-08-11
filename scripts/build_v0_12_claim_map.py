#!/usr/bin/env python3
"""Build and verify the v0.12 claim map from the v0.11 deterministic builder."""

from __future__ import annotations

import argparse
from typing import Any

from build_v0_11_claim_map import build as build_v0_11
from build_v0_11_claim_map import evidence, fitness, render


OUTPUT_PATH = "evidence/claim-evidence-map.json"
FORWARD_EVIDENCE = "paper/data/forward-citation-retrieval-evidence-v0.12.0.json"
FORWARD_QUEUE = "paper/data/forward-citation-author-review-queue-v0.12.0.csv"
FORWARD_REPORT = "paper/forward-citation-retrieval-tranche-v0.12.0.md"
VALIDATOR = "scripts/validate_next_evidence_gates.py"
BOUNDARY_ATTESTATION = "evidence/human-review-attestation-v0.12.0.json"


def forward_claim() -> dict[str, Any]:
    return {
        "claim_id": "PAPER-C33",
        "claim_text": (
            "The frozen forward-citation tranche records 102 retrieval outcomes: "
            "34 full-text recoveries, 37 abstract recoveries, 26 metadata-only outcomes, "
            "3 duplicates, and 2 unavailable records; 71 author decisions remain open."
        ),
        "claim_class": "numerical",
        "claim_scope": "paper",
        "status": "provisional",
        "verification_rule": (
            "The 102 frozen forward-citation keys must agree across the evidence record, "
            "population ledger, and author queue, and the validator must recompute all counts."
        ),
        "evidence": [
            evidence("C33-SELECTED", FORWARD_EVIDENCE, "json_pointer", "/counts/selected", "numeric", expected_value=102, content_review="pending"),
            evidence("C33-FULL", FORWARD_EVIDENCE, "json_pointer", "/counts/outcomes/full-text-recovered", "numeric", expected_value=34, content_review="pending"),
            evidence("C33-ABSTRACT", FORWARD_EVIDENCE, "json_pointer", "/counts/outcomes/abstract-recovered", "numeric", expected_value=37, content_review="pending"),
            evidence("C33-METADATA", FORWARD_EVIDENCE, "json_pointer", "/counts/outcomes/metadata-only", "numeric", expected_value=26, content_review="pending"),
            evidence("C33-DUPLICATE", FORWARD_EVIDENCE, "json_pointer", "/counts/outcomes/duplicate", "numeric", expected_value=3, content_review="pending"),
            evidence("C33-UNAVAILABLE", FORWARD_EVIDENCE, "json_pointer", "/counts/outcomes/unavailable", "numeric", expected_value=2, content_review="pending"),
            evidence("C33-OPEN", FORWARD_EVIDENCE, "json_pointer", "/counts/screening_open", "numeric", expected_value=71, content_review="pending"),
            evidence("C33-METHOD", FORWARD_REPORT, "markdown_heading", "## Evidence path", "method", content_review="pending"),
            evidence("C33-IMPLEMENTATION", VALIDATOR, "text_marker", "forward-citation evidence does not match the frozen forward stratum", "implementation", content_review="pending"),
            evidence("C33-QUEUE", FORWARD_QUEUE, "file", "", "provenance", content_review="pending"),
            evidence("C33-BOUNDARY", BOUNDARY_ATTESTATION, "text_marker", "No source in the forward-citation tranche has an author screening decision", "limitation", content_review="recorded"),
        ],
        "fitness": fitness(
            directness=("pass", "The evidence record and validator directly expose the frozen membership and recomputed counts."),
            contemporaneity=("pass", "The routes and outcomes are dated for the v0.12 checkpoint."),
            independence=("outside_scope", "The claim reports repository workflow state and no independent research judgment."),
            completeness=("pass", "Every frozen forward-citation key appears once, and every recovered-content key appears in the author queue."),
            publication_authority=("pass", "The repository records its own retrieval workflow and names Mark Julius Banasihan as decision owner."),
        ),
        "dependencies": [],
        "dependency_closure": "pass",
        "conclusion_eligible": False,
        "human_review": {
            "status": "pending",
            "reviewer": "Mark Julius Banasihan",
            "review_date": None,
            "attestation_path": BOUNDARY_ATTESTATION,
            "note": "The workflow boundary is recorded; source routes and retrieval outcomes await author review.",
        },
        "scope_terms": [],
        "limitations": [
            "The 71 recovered-content records have no author screening decision or claim permission.",
            "The tranche cannot establish exhaustive coverage, close-source prevalence, originality, reliability, or field validity.",
        ],
        "reversal_conditions": [
            "A frozen key, retrieval outcome, queue membership, screening decision, or recomputed count changes."
        ],
    }


def build() -> dict[str, Any]:
    result = build_v0_11()
    result["version"] = "0.12.0"
    result["scope_id"] = "TAE-COE-V0.12.0"
    result["description"] = (
        "Material paper and repository claims audited through v0.12.0, including the "
        "forward-citation retrieval workflow with its author-review gate left open."
    )
    result["claims"].append(forward_claim())
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render(build())
    from pathlib import Path
    output = Path(__file__).resolve().parents[1] / OUTPUT_PATH
    if args.write:
        output.write_text(expected, encoding="utf-8")
    if args.check and (not output.is_file() or output.read_text(encoding="utf-8") != expected):
        raise SystemExit("v0.12 claim map: FAIL\ncommitted output differs from the deterministic builder")
    print("v0.12 claim map: PASS (27 claims; PAPER-C33 review pending)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
