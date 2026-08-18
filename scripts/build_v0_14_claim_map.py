#!/usr/bin/env python3
"""Build and verify the v0.14 claim map from the v0.13 builder."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from build_v0_13_claim_map import build as build_v0_13
from build_v0_11_claim_map import evidence, fitness, render


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = "evidence/claim-evidence-map.json"
SUMMARY = "paper/data/forward-citation-proposition-review-v0.14.0.json"
LEDGER = "paper/data/forward-citation-proposition-review-v0.14.0.csv"
REPORT = "paper/forward-citation-proposition-review-v0.14.0.md"
PROTOCOL = "paper/forward-citation-proposition-review-protocol-v0.14.0.md"
VALIDATOR = "scripts/validate_forward_citation_proposition_review_v0_14_0.py"
DIRECT_RESOLUTION = "paper/data/direct-query-resolution-v0.14.0.json"
ATTESTATION = "evidence/human-review-attestation-v0.14.0.json"
MANUSCRIPT = "paper/manuscript.md"
AUTHOR = "Mark Julius Banasihan"
REVIEW_DATE = "2026-08-13"


def human_review(claim_id: str, note: str) -> dict[str, Any]:
    return {
        "status": "recorded",
        "reviewer": AUTHOR,
        "review_date": REVIEW_DATE,
        "attestation_path": ATTESTATION,
        "note": f"{claim_id}: {note}",
    }


def proposition_review_completion() -> dict[str, Any]:
    return {
        "claim_id": "PAPER-C35",
        "claim_text": (
            "All 13 forward-citation sources classified close in v0.13 received one terminal "
            "proposition-review decision in v0.14, with zero open decisions."
        ),
        "claim_class": "numerical",
        "claim_scope": "paper",
        "status": "supported",
        "verification_rule": (
            "The review ledger must preserve the frozen 13-source membership and order, contain "
            "one terminal decision per source, resolve required fields, and recompute zero open decisions."
        ),
        "evidence": [
            evidence("C35-RETAINED", SUMMARY, "json_pointer", "/counts/retained_close_sources", "numeric", expected_value=13),
            evidence("C35-REVIEWED", SUMMARY, "json_pointer", "/counts/reviewed", "numeric", expected_value=13),
            evidence("C35-OPEN", SUMMARY, "json_pointer", "/counts/open", "numeric", expected_value=0),
            evidence("C35-LEDGER", LEDGER, "file", "", "provenance"),
            evidence("C35-METHOD", PROTOCOL, "markdown_heading", "## Completion conditions", "method"),
            evidence(
                "C35-IMPLEMENTATION",
                VALIDATOR,
                "text_marker",
                "proposition-review ledger does not preserve frozen close-source membership and order",
                "implementation",
            ),
            evidence("C35-ATTESTATION", ATTESTATION, "text_marker", "PAPER-C35", "provenance"),
        ],
        "fitness": fitness(
            directness=("pass", "The frozen input, ordered ledger, and recomputed summary directly establish completion."),
            contemporaneity=("pass", "The protocol, decisions, summary, and attestation share the v0.14 review date."),
            independence=("outside_scope", "The claim reports an author-owned workflow state and no independent scientific judgment."),
            completeness=("pass", "Every frozen close-source identifier appears once with all required fields."),
            publication_authority=("pass", "The repository records its own workflow and names the accountable author."),
        ),
        "dependencies": ["PAPER-C34"],
        "dependency_closure": "pass",
        "conclusion_eligible": True,
        "human_review": human_review("PAPER-C35", "Reviewed as the bounded 13-of-13 proposition-review completion claim."),
        "scope_terms": [
            {"term": "all", "justification": "All refers only to the 13 sources classified retain-close in the frozen v0.13 forward-citation ledger."}
        ],
        "limitations": [
            "Completion establishes a recorded decision for each source and supplies no independent agreement or source-truth finding."
        ],
        "reversal_conditions": [
            "Frozen membership, order, required fields, a terminal decision, or recomputed counts change."
        ],
    }


def permission_composition() -> dict[str, Any]:
    return {
        "claim_id": "PAPER-C36",
        "claim_text": (
            "The v0.14 review permits five bounded manuscript propositions, retains two sources "
            "as background-only, and quarantines six sources."
        ),
        "claim_class": "numerical",
        "claim_scope": "paper",
        "status": "supported",
        "verification_rule": (
            "Decision counts, permission states, required fitness dimensions, passage locators, "
            "bibliography keys, and manuscript citations must agree across the ledger and validator."
        ),
        "evidence": [
            evidence("C36-MANUSCRIPT", SUMMARY, "json_pointer", "/counts/manuscript_use", "numeric", expected_value=5),
            evidence("C36-BACKGROUND", SUMMARY, "json_pointer", "/counts/background_only", "numeric", expected_value=2),
            evidence("C36-QUARANTINED", SUMMARY, "json_pointer", "/counts/quarantined", "numeric", expected_value=6),
            evidence("C36-PERMISSIONS", SUMMARY, "json_pointer", "/counts/proposition_permissions", "numeric", expected_value=5),
            evidence("C36-REPORT", REPORT, "markdown_heading", "## Manuscript-use propositions", "method"),
            evidence(
                "C36-IMPLEMENTATION",
                VALIDATOR,
                "text_marker",
                "manuscript-use row has a failed or indeterminate required fitness state",
                "implementation",
            ),
            evidence("C36-ATTESTATION", ATTESTATION, "text_marker", "PAPER-C36", "provenance"),
        ],
        "fitness": fitness(
            directness=("pass", "The decision summary and row-level validator directly establish the three classes and permissions."),
            contemporaneity=("pass", "The decision artifacts share the v0.14 review date."),
            independence=("outside_scope", "The claim reports review composition and no independent support judgment."),
            completeness=("pass", "Each permitted row has a bounded proposition, stable locator, passage locator, fitness states, limitation, and reversal condition."),
            publication_authority=("pass", "The responsible author is identified for each decision and in the attestation."),
        ),
        "dependencies": ["PAPER-C35"],
        "dependency_closure": "pass",
        "conclusion_eligible": True,
        "human_review": human_review("PAPER-C36", "Reviewed as the bounded permission composition for the 13-source gate."),
        "scope_terms": [],
        "limitations": [
            "Permission applies only to the five recorded propositions and does not validate a source beyond its inspected passages."
        ],
        "reversal_conditions": [
            "A source decision, permission, fitness state, passage locator, bibliography key, or manuscript citation changes."
        ],
    }


def direct_query_closure() -> dict[str, Any]:
    return {
        "claim_id": "PAPER-C37",
        "claim_text": (
            "The v0.14 overlay closes the fifth direct-query screening decision as retain-close "
            "and grants it zero proposition permission."
        ),
        "claim_class": "documentary_classification",
        "claim_scope": "paper",
        "status": "supported",
        "verification_rule": (
            "The overlay must identify RS-DQ-004, preserve the v0.11 snapshot, record retain-close, "
            "show zero open screening decisions, and keep claim permission closed."
        ),
        "evidence": [
            evidence("C37-STATUS", DIRECT_RESOLUTION, "json_pointer", "/status", "provenance", expected_value="DIRECT_QUERY_SCREENING_CLOSED"),
            evidence("C37-DECISION", DIRECT_RESOLUTION, "json_pointer", "/decision", "provenance", expected_value="retain-close"),
            evidence("C37-OPEN", DIRECT_RESOLUTION, "json_pointer", "/resulting_counts/screening_open", "numeric", expected_value=0),
            evidence(
                "C37-PERMISSION",
                DIRECT_RESOLUTION,
                "json_pointer",
                "/claim_permission",
                "limitation",
                expected_value="none-until-readable-proposition-review",
            ),
            evidence(
                "C37-IMPLEMENTATION",
                VALIDATOR,
                "text_marker",
                "direct-query resolution must close screening without proposition permission",
                "implementation",
            ),
            evidence("C37-ATTESTATION", ATTESTATION, "text_marker", "PAPER-C37", "provenance"),
        ],
        "fitness": fitness(
            directness=("pass", "The overlay directly records the terminal screening decision and closed permission state."),
            contemporaneity=("pass", "The overlay and authorization are dated for v0.14."),
            independence=("outside_scope", "The claim concerns screening state and no independent source-content judgment."),
            completeness=("pass", "The title-based decision and every unresolved source-content limit remain visible."),
            publication_authority=("pass", "The repository author owns the screening decision; the publisher route is preserved without content attribution."),
        ),
        "dependencies": [],
        "dependency_closure": "pass",
        "conclusion_eligible": True,
        "human_review": human_review("PAPER-C37", "Reviewed as a conservative relevance classification with zero proposition permission."),
        "scope_terms": [],
        "limitations": [
            "Unreadable text and unresolved author identity block every substantive source claim."
        ],
        "reversal_conditions": [
            "Readable exact text resolves the author identity or changes the screening relevance decision."
        ],
    }


def bounded_source_synthesis() -> dict[str, Any]:
    return {
        "claim_id": "PAPER-C38",
        "claim_text": (
            "Within five proposition-reviewed sources, perceived safety can diverge from reasons-tracking, "
            "feedback mode and latency can limit observed intervention effect, and reconstruction output can "
            "depend on analytic method and source completeness."
        ),
        "claim_class": "conclusion",
        "claim_scope": "paper",
        "status": "supported",
        "verification_rule": (
            "Each component must resolve to its permitted ledger proposition, stable passage locator, "
            "manuscript citation, recorded fitness decision, and v0.14 attestation."
        ),
        "evidence": [
            evidence(
                "C38-PERCEPTION",
                LEDGER,
                "csv_cell",
                "sample_id=RS-FC-042|permitted_proposition",
                "source",
                expected_value=(
                    "In a secondary analysis of 99 Tesla-user interviews, perceived safety sometimes "
                    "coexisted with failures to track driver reasons, while takeover readiness and prior "
                    "reliable experience shaped perception."
                ),
            ),
            evidence(
                "C38-FEEDBACK",
                LEDGER,
                "csv_cell",
                "sample_id=RS-FC-052|permitted_proposition",
                "source",
                expected_value=(
                    "In a 28-participant sandbox study, direct manipulation had a higher task-completion "
                    "rate than text guidance, 83.3 percent versus 61.9 percent, while delayed or ineffective "
                    "feedback made intervention effects harder for participants to assess."
                ),
            ),
            evidence(
                "C38-METHOD",
                LEDGER,
                "csv_cell",
                "sample_id=RS-FC-096|permitted_proposition",
                "source",
                expected_value=(
                    "Three analyst teams applied HFACS, AcciMap, and STAMP to the same official report; "
                    "the methods produced different factor sets, and the authors state that missing report "
                    "detail can hide material factors."
                ),
            ),
            evidence(
                "C38-MANUSCRIPT",
                MANUSCRIPT,
                "text_marker",
                "perceived control and formal feedback access can remain separate from demonstrated intervention effect",
                "conclusion",
            ),
            evidence("C38-ATTESTATION", ATTESTATION, "text_marker", "PAPER-C38", "provenance"),
        ],
        "fitness": fitness(
            directness=("pass", "Each component restates one proposition-reviewed source finding at the same or narrower scope."),
            contemporaneity=("outside_scope", "The synthesis concerns present publications and reconstruction method, not a new historical event state."),
            independence=("outside_scope", "The claim reports distinct source-specific mechanisms and makes no prevalence or replication claim."),
            completeness=("pass", "The synthesis includes the recorded sample, setting, method, and source limits needed for its bounded scope."),
            publication_authority=("pass", "Each component resolves to an identified publication and exact review locator."),
        ),
        "dependencies": ["PAPER-C36"],
        "dependency_closure": "pass",
        "conclusion_eligible": True,
        "human_review": human_review("PAPER-C38", "Reviewed as a bounded synthesis of three source-specific mechanisms, with transfer claims excluded."),
        "scope_terms": [],
        "limitations": [
            "The sources differ in domain and method and establish no common effect size, prevalence, causal validation, or institutional transfer."
        ],
        "reversal_conditions": [
            "A permitted proposition, passage locator, source limitation, or manuscript wording changes."
        ],
    }


def build() -> dict[str, Any]:
    result = build_v0_13()
    result["version"] = "0.14.0"
    result["scope_id"] = "TAE-COE-V0.14.0"
    result["description"] = (
        "Material paper and repository claims audited through v0.14.0, including the closed "
        "13-source proposition-review gate, five bounded manuscript permissions, and the closed "
        "direct-query screening overlay."
    )
    result["claims"].extend([
        proposition_review_completion(),
        permission_composition(),
        direct_query_closure(),
        bounded_source_synthesis(),
    ])
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
        raise SystemExit("v0.14 claim map: FAIL\ncommitted output differs from the deterministic builder")
    print(
        "v0.14 claim map: PASS "
        "(32 claims; proposition review and direct-query screening closed within declared scope)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
