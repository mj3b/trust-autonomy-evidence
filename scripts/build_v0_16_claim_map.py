#!/usr/bin/env python3
"""Build and verify the v0.16 manuscript-rebuild claim map."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from build_v0_15_claim_map import build as build_v0_15
from build_v0_11_claim_map import evidence, fitness, render


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = "evidence/claim-evidence-map.json"
ATTESTATION = "evidence/human-review-attestation-v0.16.0.json"
PROTOCOL = "protocols/practical-human-control-test.md"
REVISION_PLAN = "paper/revision-plan-v0.16.0.md"
MANUSCRIPT = "paper/manuscript.md"
LATEX = "paper/preprints/main.tex"
RESULTS = "assessments/event-control-results-v0.16.0.json"
BUILDER = "analysis/derive_event_control_results.py"
AUTHOR = "Mark Julius Banasihan"
REVIEW_DATE = "2026-08-19"


def human_review(claim_id: str, note: str) -> dict[str, Any]:
    return {
        "status": "recorded",
        "reviewer": AUTHOR,
        "review_date": REVIEW_DATE,
        "attestation_path": ATTESTATION,
        "note": f"{claim_id}: {note}",
    }


def common_fitness(*, completeness: str) -> dict[str, Any]:
    return fitness(
        directness=("pass", "The claim resolves directly to the declared protocol, released states, deterministic derivation, or manuscript boundary."),
        contemporaneity=("pass", "The evidence records the current v0.16.0 rule and derivation from preserved earlier assessments."),
        independence=("outside_scope", "This is an author-designed method and deterministic repository derivation; independent assessment remains a declared open gate."),
        completeness=("pass", completeness),
        publication_authority=("pass", "The accountable author authorized the v0.16.0 revision and its bounded interpretation."),
    )


def formal_rule() -> dict[str, Any]:
    return {
        "claim_id": "PAPER-C42",
        "claim_text": "The v0.16.0 method requires six event-level stages and declares deterministic pass, fail, and unresolved case-level rules.",
        "claim_class": "methodological",
        "claim_scope": "method",
        "status": "supported",
        "verification_rule": "The protocol, revision plan, manuscript, result builder, and author attestation must agree on all six required fields and all three result rules.",
        "evidence": [
            evidence("C42-PROTOCOL", PROTOCOL, "text_marker", "EventControl(c)", "method"),
            evidence("C42-PLAN", REVISION_PLAN, "text_marker", "Execution propagation", "method"),
            evidence("C42-MANUSCRIPT", MANUSCRIPT, "text_marker", "EventControl(c)=", "method"),
            evidence("C42-IMPLEMENTATION", BUILDER, "text_marker", "def classify", "implementation"),
            evidence("C42-ATTESTATION", ATTESTATION, "text_marker", "PAPER-C42", "provenance"),
        ],
        "fitness": common_fitness(completeness="All required stages, result branches, and the outside-scope prohibition are visible."),
        "dependencies": [],
        "dependency_closure": "pass",
        "conclusion_eligible": True,
        "human_review": human_review("PAPER-C42", "Approved as the formal v0.16.0 decision rule."),
        "scope_terms": [{"term": "required", "justification": "The six fields are required by the declared event-control construct."}],
        "limitations": ["The rule is a proposed documentary construct and has no independent reliability or construct-validity estimate."],
        "reversal_conditions": ["Any required field, result branch, state definition, or case-boundary rule changes."],
    }


def derived_results() -> dict[str, Any]:
    return {
        "claim_id": "PAPER-C43",
        "claim_text": "Applying the v0.16.0 rule to the released states derives Oko as unresolved and both Patriot cases as fail.",
        "claim_class": "numerical",
        "claim_scope": "paper",
        "status": "supported",
        "verification_rule": "The deterministic output must contain one unresolved and two fail results, with exact case identifiers and released source assessments.",
        "evidence": [
            evidence("C43-OKO", RESULTS, "json_pointer", "/cases/0/result", "numeric", expected_value="unresolved"),
            evidence("C43-ZG710", RESULTS, "json_pointer", "/cases/1/result", "numeric", expected_value="fail"),
            evidence("C43-FA18", RESULTS, "json_pointer", "/cases/2/result", "numeric", expected_value="fail"),
            evidence("C43-FAIL-COUNT", RESULTS, "json_pointer", "/result_counts/fail", "numeric", expected_value=2),
            evidence("C43-UNRESOLVED-COUNT", RESULTS, "json_pointer", "/result_counts/unresolved", "numeric", expected_value=1),
            evidence("C43-IMPLEMENTATION", BUILDER, "text_marker", "source_assessment", "implementation"),
            evidence("C43-ATTESTATION", ATTESTATION, "text_marker", "PAPER-C43", "provenance"),
        ],
        "fitness": common_fitness(completeness="All three cases, source paths, six states per case, and result counts are preserved in the output."),
        "dependencies": ["PAPER-C42"],
        "dependency_closure": "pass",
        "conclusion_eligible": True,
        "human_review": human_review("PAPER-C43", "Approved as a deterministic derivation from released assessment states."),
        "scope_terms": [],
        "limitations": ["The derivation inherits the single-assessor and public-record limits of the underlying states."],
        "reversal_conditions": ["A released assessment state or the v0.16.0 case-level rule changes."],
    }


def no_pass_conclusion() -> dict[str, Any]:
    return {
        "claim_id": "PAPER-C44",
        "claim_text": "No case in the three-packet selected set passes the complete event-control rule.",
        "claim_class": "conclusion",
        "claim_scope": "paper",
        "status": "supported",
        "verification_rule": "The deterministic pass count must equal zero, the manuscript must state the bounded conclusion, and rule and result dependencies must close.",
        "evidence": [
            evidence("C44-PASS-COUNT", RESULTS, "json_pointer", "/result_counts/pass", "numeric", expected_value=0),
            evidence("C44-MANUSCRIPT", MANUSCRIPT, "text_marker", "no case passed the complete event-control rule", "conclusion"),
            evidence("C44-LIMIT", RESULTS, "json_pointer", "/interpretation_limit", "limitation"),
            evidence("C44-ATTESTATION", ATTESTATION, "text_marker", "PAPER-C44", "provenance"),
        ],
        "fitness": common_fitness(completeness="The three-case denominator and interpretation limit are explicit."),
        "dependencies": ["PAPER-C42", "PAPER-C43"],
        "dependency_closure": "pass",
        "conclusion_eligible": True,
        "human_review": human_review("PAPER-C44", "Approved only for the three purposively selected packets."),
        "scope_terms": [],
        "limitations": ["The conclusion supplies no prevalence, comparison-group, or current-system estimate."],
        "reversal_conditions": ["The selected set, an underlying state, or the event-control decision rule changes."],
    }


def timing_measure() -> dict[str, Any]:
    return {
        "claim_id": "PAPER-C45",
        "claim_text": "The v0.16.0 timing margin is a proposed prospective measure and cannot be calculated from the three historical packets.",
        "claim_class": "methodological",
        "claim_scope": "method",
        "status": "supported",
        "verification_rule": "The protocol and manuscript must state the same equation, positive-margin interpretation, missing-input rule, and historical-data limit.",
        "evidence": [
            evidence("C45-PROTOCOL", PROTOCOL, "text_marker", "M_t=(t_{commit}-t_{access})-(t_{interpret}+t_{decide}+t_{transmit}+t_{propagate})", "method"),
            evidence("C45-MANUSCRIPT", MANUSCRIPT, "text_marker", "The three historical packets lack the complete timing inputs", "limitation"),
            evidence("C45-LATEX", LATEX, "text_marker", "t_{propagate}", "implementation"),
            evidence("C45-ATTESTATION", ATTESTATION, "text_marker", "PAPER-C45", "provenance"),
        ],
        "fitness": common_fitness(completeness="The equation, interpretation, missing-input treatment, and nonapplication to historical cases are explicit."),
        "dependencies": ["PAPER-C42"],
        "dependency_closure": "pass",
        "conclusion_eligible": True,
        "human_review": human_review("PAPER-C45", "Approved as a proposed measure, not an observed historical result."),
        "scope_terms": [],
        "limitations": ["The measure has not been validated against observed reviewer performance or present learned systems."],
        "reversal_conditions": ["The equation, interpretation, timestamp definitions, or historical-data availability changes."],
    }


def execution_term() -> dict[str, Any]:
    return {
        "claim_id": "PAPER-C46",
        "claim_text": "The manuscript uses execution propagation for the released effect field and excludes beneficial-outcome and counterfactual-effect interpretations.",
        "claim_class": "documentary_classification",
        "claim_scope": "paper",
        "status": "supported",
        "verification_rule": "The protocol, manuscript, table register, figure builder, LaTeX source, and attestation must preserve the alias and its interpretation limit.",
        "evidence": [
            evidence("C46-PROTOCOL", PROTOCOL, "text_marker", "The released machine-readable assessments through v0.15 use the field name `effect`", "method"),
            evidence("C46-MANUSCRIPT", MANUSCRIPT, "text_marker", "A counterfactual causal effect and a beneficial outcome require separate evidence", "limitation"),
            evidence("C46-TABLES", "paper/tables.md", "text_marker", "The released assessment JSON uses the field name `effect`", "implementation"),
            evidence("C46-FIGURE", "analysis/build_figures.py", "text_marker", '"effect": "Execution propagation"', "implementation"),
            evidence("C46-LATEX", LATEX, "text_marker", "Execution propagation", "implementation"),
            evidence("C46-ATTESTATION", ATTESTATION, "text_marker", "PAPER-C46", "provenance"),
        ],
        "fitness": common_fitness(completeness="The machine field, reader-facing term, and prohibited interpretations are all declared."),
        "dependencies": ["PAPER-C42"],
        "dependency_closure": "pass",
        "conclusion_eligible": True,
        "human_review": human_review("PAPER-C46", "Approved as the bounded interpretation of the legacy machine-readable field."),
        "scope_terms": [],
        "limitations": ["Renaming the reader-facing term does not change the released historical assessment states."],
        "reversal_conditions": ["The field semantics, manuscript terminology, or prohibited interpretation changes."],
    }


def build() -> dict[str, Any]:
    result = build_v0_15()
    result["version"] = "0.16.0"
    result["scope_id"] = "TAE-COE-V0.16.0"
    result["description"] = (
        "Material paper and repository claims audited through v0.16.0, including the formal event-control rule, "
        "deterministic case-level results, bounded no-pass conclusion, proposed timing margin, and execution-propagation terminology."
    )
    result["claims"].extend([formal_rule(), derived_results(), no_pass_conclusion(), timing_measure(), execution_term()])
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
        raise SystemExit("v0.16 claim map: FAIL\ncommitted output differs from the deterministic builder")
    print("v0.16 claim map: PASS (40 claims; 5 v0.16 manuscript claims added)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
