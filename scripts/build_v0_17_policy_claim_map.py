#!/usr/bin/env python3
"""Build the v0.17.0 policy-crosswalk claim map."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from build_v0_11_claim_map import evidence, fitness, render


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "evidence/policy-claim-evidence-map-v0.17.0.json"
SOURCE_REVIEW = "paper/data/policy-and-standards-source-review-v0.17.0.json"
CROSSWALK = "paper/policy-and-standards-crosswalk-v0.17.0.md"
PROTOCOL = "protocols/regulatory-sandbox-validation-protocol-v0.17.0.md"
VALIDATOR = "scripts/validate_policy_crosswalk_v0_17_0.py"
LATEX = "paper/preprints/main.tex"
ATTESTATION = "evidence/human-review-attestation-v0.17.0.json"


def recorded_review(claim_id: str, note: str) -> dict[str, Any]:
    return {
        "status": "recorded",
        "reviewer": "Mark Julius Banasihan",
        "review_date": "2026-09-05",
        "attestation_path": ATTESTATION,
        "note": f"{claim_id}: {note}",
    }


def source_fitness(completeness: str) -> dict[str, Any]:
    return fitness(
        directness=("pass", "The claim resolves to a named proposition and locator in the targeted official-source review."),
        contemporaneity=("pass", "The review date and instrument state are recorded as 5 September 2026."),
        independence=("pass", "The proposition is taken from the issuing authority's official public source."),
        completeness=("pass", completeness),
        publication_authority=("pass", "The cited page or enacted text is published by the issuing public authority."),
    )


def build() -> dict[str, Any]:
    claims = [
        {
            "claim_id": "PAPER-C47",
            "claim_text": "The v0.17.0 targeted policy review contains eight official-source records and preserves a use limit for each record.",
            "claim_class": "numerical",
            "claim_scope": "repository",
            "status": "supported",
            "verification_rule": "The source-count field must equal eight, every record must contain a permitted-use statement and limit, and the bounded author review must resolve to the v0.17.0 attestation.",
            "evidence": [
                evidence("C47-COUNT", SOURCE_REVIEW, "json_pointer", "/source_count", "numeric", expected_value=8),
                evidence("C47-LIMIT", SOURCE_REVIEW, "json_pointer", "/global_limits/0", "limitation"),
                evidence("C47-ATTESTATION", ATTESTATION, "text_marker", "APPROVE_BOUNDED_MANUSCRIPT_INCLUSION", "provenance"),
            ],
            "fitness": source_fitness("All eight selected records are represented; the selection is targeted and does not claim legal completeness."),
            "dependencies": [],
            "dependency_closure": "pass",
            "conclusion_eligible": True,
            "human_review": recorded_review("PAPER-C47", "Approved the eight-record ledger for the bounded use stated in the attestation."),
            "scope_terms": [{"term": "all", "justification": "All refers to the eight records selected for this targeted crosswalk."}],
            "limitations": ["The count describes the repository ledger and supplies no claim about the completeness of legal research."],
            "reversal_conditions": ["The source ledger contains a different number of records or a record lacks its use boundary."],
        },
        {
            "claim_id": "PAPER-C48",
            "claim_text": "The reviewed text of EU AI Act Article 14 addresses understanding, automation-bias awareness, interpretation, override, reversal, intervention, and stopping for human oversight of high-risk AI systems.",
            "claim_class": "citation",
            "claim_scope": "paper",
            "status": "supported",
            "verification_rule": "The official Article 14 locator, bounded proposition, crosswalk mapping, and legal-sufficiency limit must resolve without a compliance claim.",
            "evidence": [
                evidence("C48-SOURCE", SOURCE_REVIEW, "json_pointer", "/records/0/observed_proposition", "source", source_id="POL-EU-AIA-14"),
                evidence("C48-CROSSWALK", CROSSWALK, "text_marker", "EU AI Act, Article 14", "conclusion"),
                evidence("C48-LATEX", LATEX, "text_marker", "Governance instruments can require human oversight", "conclusion"),
                evidence("C48-LIMIT", SOURCE_REVIEW, "json_pointer", "/records/0/limits", "limitation", source_id="POL-EU-AIA-14"),
                evidence("C48-ATTESTATION", ATTESTATION, "text_marker", "PAPER-C48", "provenance"),
            ],
            "fitness": source_fitness("The claim is limited to the cited Article 14 oversight capabilities."),
            "dependencies": ["PAPER-C47"],
            "dependency_closure": "pass",
            "conclusion_eligible": True,
            "human_review": recorded_review("PAPER-C48", "Approved the bounded Article 14 proposition and manuscript mapping."),
            "scope_terms": [],
            "limitations": ["The claim supplies no legal interpretation or finding that the method satisfies Article 14."],
            "reversal_conditions": ["The official text changes or the cited capabilities do not appear at the recorded locator."],
        },
        {
            "claim_id": "PAPER-C49",
            "claim_text": "EU AI Act Article 57 supplies a plausible prospective setting for testing the six-stage method under a protocol fixed before observed outcomes.",
            "claim_class": "methodological",
            "claim_scope": "method",
            "status": "supported",
            "verification_rule": "The Article 57 source proposition, proposed protocol, six-stage method, and validator must agree on the bounded sandbox use and its untested status.",
            "evidence": [
                evidence("C49-SOURCE", SOURCE_REVIEW, "json_pointer", "/records/1/observed_proposition", "source", source_id="POL-EU-AIA-57"),
                evidence("C49-METHOD", PROTOCOL, "text_marker", "Can a preregistered six-stage evidence protocol", "method"),
                evidence("C49-LATEX", LATEX, "text_marker", "Regulatory sandboxes as the next empirical setting", "conclusion"),
                evidence("C49-IMPLEMENTATION", VALIDATOR, "text_marker", "EXPECTED_STAGES", "implementation"),
                evidence("C49-LIMIT", SOURCE_REVIEW, "json_pointer", "/records/1/limits", "limitation", source_id="POL-EU-AIA-57"),
                evidence("C49-ATTESTATION", ATTESTATION, "text_marker", "PAPER-C49", "provenance"),
            ],
            "fitness": source_fitness("The legal proposition and the author's proposed research use are separated and both boundaries are recorded."),
            "dependencies": ["PAPER-C47", "PAPER-C48"],
            "dependency_closure": "pass",
            "conclusion_eligible": True,
            "human_review": recorded_review("PAPER-C49", "Approved the sandbox design as a proposed validation setting with no field-validation claim."),
            "scope_terms": [],
            "limitations": [
                "No sandbox authority or independent assessor has accepted or applied the protocol.",
                "Participant or protected operational data require the applicable ethics determination and data authority before collection.",
            ],
            "reversal_conditions": ["Article 57 no longer supports the recorded setting or the prospective protocol changes its six required stages."],
        },
        {
            "claim_id": "PAPER-C50",
            "claim_text": "The reviewed NIST AI RMF outcomes and ISO/IEC 42001 public overview support a bounded organization-to-event comparison without a compliance or certification finding.",
            "claim_class": "citation",
            "claim_scope": "paper",
            "status": "supported",
            "verification_rule": "The NIST and ISO propositions, locators, public-source limits, and crosswalk mappings must resolve; certification and legal-sufficiency language must remain excluded.",
            "evidence": [
                evidence("C50-NIST", SOURCE_REVIEW, "json_pointer", "/records/2/observed_proposition", "source", source_id="POL-NIST-AI-RMF-CORE"),
                evidence("C50-ISO", SOURCE_REVIEW, "json_pointer", "/records/3/observed_proposition", "source", source_id="POL-ISO-IEC-42001"),
                evidence("C50-CROSSWALK", CROSSWALK, "text_marker", "A possible evidence layer connecting management controls", "conclusion"),
                evidence("C50-LATEX", LATEX, "text_marker", "NIST AI RMF outcomes GOVERN 2.1", "conclusion"),
                evidence("C50-LIMIT", SOURCE_REVIEW, "json_pointer", "/records/3/limits", "limitation", source_id="POL-ISO-IEC-42001"),
                evidence("C50-ATTESTATION", ATTESTATION, "text_marker", "PAPER-C50", "provenance"),
            ],
            "fitness": source_fitness("NIST use is limited to three cited outcomes; ISO use is limited to the official public overview."),
            "dependencies": ["PAPER-C47"],
            "dependency_closure": "pass",
            "conclusion_eligible": True,
            "human_review": recorded_review("PAPER-C50", "Approved the NIST and ISO comparison within the recorded public-source limits."),
            "scope_terms": [],
            "limitations": ["The full licensed ISO standard was not reviewed, and the NIST AI RMF is voluntary and under revision."],
            "reversal_conditions": ["The cited NIST outcomes or ISO public overview change materially, or the manuscript asserts conformity or compliance."],
        },
        {
            "claim_id": "PAPER-C51",
            "claim_text": "The reviewed New York City, California, Colorado, and Illinois materials are reserved as applied-policy sites and do not change the historical case results.",
            "claim_class": "documentary_classification",
            "claim_scope": "repository",
            "status": "supported",
            "verification_rule": "All four official-source records must resolve, Chicago must remain within the Illinois entry absent a selected municipal source, and the crosswalk must prohibit transfer into the historical results.",
            "evidence": [
                evidence("C51-NYC", SOURCE_REVIEW, "json_pointer", "/records/4/observed_proposition", "source", source_id="POL-NYC-LL144"),
                evidence("C51-CA", SOURCE_REVIEW, "json_pointer", "/records/5/observed_proposition", "source", source_id="POL-CA-ADMT"),
                evidence("C51-CO", SOURCE_REVIEW, "json_pointer", "/records/6/observed_proposition", "source", source_id="POL-CO-ADMT"),
                evidence("C51-IL", SOURCE_REVIEW, "json_pointer", "/records/7/observed_proposition", "source", source_id="POL-IL-HB3773"),
                evidence("C51-BOUNDARY", CROSSWALK, "text_marker", "They do not change the historical case results", "limitation"),
                evidence("C51-LATEX", LATEX, "text_marker", "United States application boundaries", "conclusion"),
                evidence("C51-ATTESTATION", ATTESTATION, "text_marker", "PAPER-C51", "provenance"),
            ],
            "fitness": source_fitness("The claim covers only the four named applied-policy entries and preserves each source-specific limit."),
            "dependencies": ["PAPER-C47"],
            "dependency_closure": "pass",
            "conclusion_eligible": True,
            "human_review": recorded_review("PAPER-C51", "Approved the four possible application sites while preserving later jurisdiction-specific review."),
            "scope_terms": [{"term": "all", "justification": "All refers to the four selected United States applied-policy records."}],
            "limitations": ["The entry supplies no legal advice, compliance finding, municipal Chicago conclusion, or event-level assessment."],
            "reversal_conditions": ["A cited instrument changes, a separate Chicago instrument is selected, or a jurisdiction enters a case-level analysis."],
        },
    ]
    return {
        "version": "0.17.0",
        "scope_id": "TAE-COE-V0.17.0",
        "description": "Five bounded claims governing the targeted policy crosswalk, prospective regulatory-sandbox protocol, and v0.17.0 manuscript section. The accountable author's inclusion decision is recorded; legal compliance and field-validation claims remain excluded.",
        "claims": claims,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render(build())
    if args.write:
        OUTPUT.write_text(expected, encoding="utf-8")
    if args.check and (not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != expected):
        raise SystemExit("v0.17 policy claim map: FAIL\ncommitted output differs from the deterministic builder")
    print("v0.17 policy claim map: PASS (5 bounded claims; author inclusion recorded)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
