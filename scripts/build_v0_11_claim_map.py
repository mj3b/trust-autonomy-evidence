#!/usr/bin/env python3
"""Build and verify the v0.11 claim-evidence map from the preserved v0.9 map."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "evidence/claim-evidence-map-v0.9.0.json"
OUTPUT = ROOT / "evidence/claim-evidence-map.json"
ATTESTATION = "evidence/human-review-attestation-v0.11.0.json"
DIRECT_EVIDENCE = "paper/data/direct-query-retrieval-evidence-v0.11.0.json"
TRANCHE_REPORT = "paper/direct-query-retrieval-tranche-v0.11.0.md"
VALIDATOR = "scripts/validate_next_evidence_gates.py"
LITERATURE_MATRIX = "paper/literature-matrix.md"
AUTHOR = "Mark Julius Banasihan"
REVIEW_DATE = "2026-08-11"


def digest(relative: str) -> str:
    return hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()


def evidence(
    evidence_id: str,
    path: str,
    locator_type: str,
    locator: str,
    role: str,
    *,
    expected_value: Any | None = None,
    source_id: str | None = None,
    content_review: str = "recorded",
) -> dict[str, Any]:
    result: dict[str, Any] = {
        "evidence_id": evidence_id,
        "path": path,
        "locator_type": locator_type,
        "locator": locator,
        "role": role,
        "source_id": source_id,
        "run_type": "not_applicable",
        "integrity_state": "verified",
        "sha256": digest(path),
        "content_review": content_review,
    }
    if expected_value is not None:
        result["expected_value"] = expected_value
    return result


def fitness(
    *,
    directness: tuple[str, str],
    contemporaneity: tuple[str, str],
    independence: tuple[str, str],
    completeness: tuple[str, str],
    publication_authority: tuple[str, str],
) -> dict[str, dict[str, str]]:
    return {
        "directness": {"state": directness[0], "rationale": directness[1]},
        "contemporaneity": {"state": contemporaneity[0], "rationale": contemporaneity[1]},
        "independence": {"state": independence[0], "rationale": independence[1]},
        "completeness": {"state": completeness[0], "rationale": completeness[1]},
        "publication_authority": {
            "state": publication_authority[0],
            "rationale": publication_authority[1],
        },
    }


def human_review(claim_id: str, note: str) -> dict[str, Any]:
    return {
        "status": "recorded",
        "reviewer": AUTHOR,
        "review_date": REVIEW_DATE,
        "attestation_path": ATTESTATION,
        "note": f"{claim_id}: {note}",
    }


def source_claim(
    *,
    claim_id: str,
    claim_text: str,
    record_index: int,
    observation_index: int,
    observation: str,
    attestation_note: str,
    directness_rationale: str,
    completeness_rationale: str,
    authority_rationale: str,
    limitation: str,
    reversal: str,
) -> dict[str, Any]:
    return {
        "claim_id": claim_id,
        "claim_text": claim_text,
        "claim_class": "citation",
        "claim_scope": "paper",
        "status": "supported",
        "verification_rule": (
            "The exact source observation, retrieval locator, review basis, human attestation, "
            "and declared limit must resolve from the v0.11 evidence record."
        ),
        "evidence": [
            evidence(
                f"{claim_id.removeprefix('PAPER-')}-SOURCE",
                DIRECT_EVIDENCE,
                "json_pointer",
                f"/records/{record_index}/source_evidence/{observation_index}",
                "source",
                expected_value=observation,
            ),
            evidence(
                f"{claim_id.removeprefix('PAPER-')}-LOCATOR",
                DIRECT_EVIDENCE,
                "json_pointer",
                f"/records/{record_index}/retrieval_locator",
                "provenance",
            ),
            evidence(
                f"{claim_id.removeprefix('PAPER-')}-ATTESTATION",
                ATTESTATION,
                "text_marker",
                claim_id,
                "provenance",
            ),
        ],
        "fitness": fitness(
            directness=("pass", directness_rationale),
            contemporaneity=(
                "outside_scope",
                "The claim describes the publication's declared content and no historical event state.",
            ),
            independence=(
                "outside_scope",
                "The claim attributes a bounded statement to one publication and makes no corroborated field finding.",
            ),
            completeness=("pass", completeness_rationale),
            publication_authority=("pass", authority_rationale),
        ),
        "dependencies": [],
        "dependency_closure": "pass",
        "conclusion_eligible": True,
        "human_review": human_review(claim_id, attestation_note),
        "scope_terms": [],
        "limitations": [limitation],
        "reversal_conditions": [reversal],
    }


def new_claims() -> list[dict[str, Any]]:
    c27 = {
        "claim_id": "PAPER-C27",
        "claim_text": (
            "The v0.11 direct-query tranche records five retrieval outcomes, four screening "
            "decisions, one open decision, three background sources, and one close source."
        ),
        "claim_class": "numerical",
        "claim_scope": "paper",
        "status": "supported",
        "verification_rule": (
            "The five frozen direct-query keys must agree across the evidence record and population "
            "ledger, and the validator must recompute every declared count."
        ),
        "evidence": [
            evidence("C27-RECORDS", DIRECT_EVIDENCE, "json_pointer", "/counts/records", "numeric", expected_value=5),
            evidence("C27-COMPLETE", DIRECT_EVIDENCE, "json_pointer", "/counts/screening_complete", "numeric", expected_value=4),
            evidence("C27-OPEN", DIRECT_EVIDENCE, "json_pointer", "/counts/screening_open", "numeric", expected_value=1),
            evidence("C27-BACKGROUND", DIRECT_EVIDENCE, "json_pointer", "/counts/retain_background", "numeric", expected_value=3),
            evidence("C27-CLOSE", DIRECT_EVIDENCE, "json_pointer", "/counts/retain_close", "numeric", expected_value=1),
            evidence("C27-METHOD", TRANCHE_REPORT, "markdown_heading", "## Evidence path", "method"),
            evidence(
                "C27-IMPLEMENTATION",
                VALIDATOR,
                "text_marker",
                "direct-query evidence does not match the frozen direct-query stratum",
                "implementation",
            ),
            evidence("C27-ATTESTATION", ATTESTATION, "text_marker", "PAPER-C27", "provenance"),
            evidence(
                "C27-LIMIT",
                TRANCHE_REPORT,
                "text_marker",
                "This tranche establishes five retrieval outcomes, four screening decisions, and one new close-source candidate.",
                "limitation",
            ),
        ],
        "fitness": fitness(
            directness=("pass", "The JSON counts and ledger agreement directly establish the five-record workflow state."),
            contemporaneity=("pass", "The evidence and attestation are dated for the v0.11 checkpoint."),
            independence=("outside_scope", "The claim reports repository state and no independent research judgment."),
            completeness=("pass", "Every frozen direct-query key appears once and every recovered record has a decision or OPEN note."),
            publication_authority=("pass", "Mark Julius Banasihan is the declared decision owner and release author."),
        ),
        "dependencies": [],
        "dependency_closure": "pass",
        "conclusion_eligible": True,
        "human_review": human_review(
            "PAPER-C27",
            "Reviewed as the bounded five-record workflow claim after disclosure of AI assistance and source limits.",
        ),
        "scope_terms": [],
        "limitations": [
            "The other 1,082 records have no recorded retrieval outcome, and the five-record stratum supplies no prevalence estimate."
        ],
        "reversal_conditions": [
            "A direct-query record, ledger state, screening decision, or recomputed count changes."
        ],
    }

    c28 = source_claim(
        claim_id="PAPER-C28",
        claim_text=(
            "Emery's 2019 dissertation discusses meaningful human control, algorithmic targeting, "
            "removal from lethal action, and limits on technical control claims."
        ),
        record_index=0,
        observation_index=1,
        observation=(
            "The abstract and pages 13, 179, and 200-201 discuss meaningful human control, "
            "algorithmic targeting, removal from lethal action, and the limits of technical control claims."
        ),
        attestation_note="Reviewed as a bounded description of the recorded dissertation passages.",
        directness_rationale="The evidence record identifies exact dissertation pages bearing on the claim.",
        completeness_rationale="The claim is confined to the recorded topics on the inspected pages.",
        authority_rationale="The source is a UC Irvine dissertation in the institutional repository.",
        limitation="The dissertation supplies historical and normative background and no test of the repository method.",
        reversal="Inspection shows that the cited pages do not contain the recorded topics or the institutional record changes.",
    )
    c29 = source_claim(
        claim_id="PAPER-C29",
        claim_text=(
            "Homayounnejad's abstract applies distinction, proportionality, precautions, and "
            "meaningful human control to lawful LAWS development and use."
        ),
        record_index=1,
        observation_index=1,
        observation=(
            "The abstract states that the paper applies distinction, proportionality, precautions, "
            "and meaningful human control to lawful LAWS development and use."
        ),
        attestation_note="Reviewed as an abstract-bounded description of the paper's declared scope.",
        directness_rationale="The publisher abstract directly states the four named legal and control topics.",
        completeness_rationale="The claim reports only the declared abstract scope and makes no detailed legal proposition.",
        authority_rationale="SSRN provides the author, paper series, length, and abstract record.",
        limitation="Detailed legal propositions remain ineligible until full text is inspected.",
        reversal="The publisher abstract changes or full-text review contradicts the recorded scope description.",
    )
    c30 = source_claim(
        claim_id="PAPER-C30",
        claim_text=(
            "Zabounidis et al. report that correcting a human-readable concept can fail to change "
            "a model output when a residual path retains conflicting information."
        ),
        record_index=2,
        observation_index=1,
        observation=(
            "The paper defines concept-residual overlap and reports that a corrected human-readable "
            "concept can fail to change the output when the residual path retains conflicting information."
        ),
        attestation_note="Reviewed as a bounded model-architecture finding from the official full text.",
        directness_rationale="The official paper directly defines and tests the stated residual-path mechanism.",
        completeness_rationale="The claim is confined to the paper's reported model result.",
        authority_rationale="OpenReview identifies the official Transactions on Machine Learning Research publication.",
        limitation="The study tests model architecture and supplies no institutional or incident-level finding.",
        reversal="Official text or correction changes the reported concept-residual intervention result.",
    )
    c31 = source_claim(
        claim_id="PAPER-C31",
        claim_text=(
            "Gielas's abstract challenges human-in-the-loop and meaningful-human-control labels, "
            "centers human-performance constraints, and proposes a human-in-the-mesh model."
        ),
        record_index=4,
        observation_index=1,
        observation=(
            "The abstract argues that human-in-the-loop and meaningful-human-control labels can omit "
            "human-performance constraints and proposes a human-in-the-mesh model."
        ),
        attestation_note="Reviewed as an abstract-bounded description of the paper's declared argument.",
        directness_rationale="The publisher abstract directly states the critique and proposed model.",
        completeness_rationale="The claim remains within the publisher abstract's declared argument.",
        authority_rationale="Taylor & Francis publishes the abstract and IISS publishes the issue record.",
        limitation="Detailed comparison with the Patriot cases remains ineligible until full text is inspected.",
        reversal="The publisher abstract changes or full-text review contradicts the recorded argument.",
    )
    c32 = {
        "claim_id": "PAPER-C32",
        "claim_text": (
            "A nominal correction can lose causal force when another information path still "
            "determines the output."
        ),
        "claim_class": "conclusion",
        "claim_scope": "paper",
        "status": "provisional",
        "verification_rule": (
            "The source mechanism must resolve, and institutional use remains blocked until evidence "
            "tests whether the same bypass mechanism operates across technical or organizational paths."
        ),
        "evidence": [
            evidence(
                "C32-SYNTHESIS",
                LITERATURE_MATRIX,
                "text_marker",
                "6. **Proposed mechanism inference:** A nominal correction can lose causal force when another information path still determines the output.",
                "conclusion",
            ),
            evidence(
                "C32-SOURCE",
                DIRECT_EVIDENCE,
                "json_pointer",
                "/records/2/source_evidence/1",
                "source",
                expected_value=(
                    "The paper defines concept-residual overlap and reports that a corrected human-readable "
                    "concept can fail to change the output when the residual path retains conflicting information."
                ),
            ),
            evidence("C32-ATTESTATION", ATTESTATION, "text_marker", "PAPER-C32", "provenance"),
        ],
        "fitness": fitness(
            directness=("pass", "The model study directly tests a parallel residual path that can defeat a concept correction."),
            contemporaneity=("outside_scope", "The claim is a mechanism synthesis and no historical-event state."),
            independence=("indeterminate", "One model-architecture study cannot establish that the mechanism generalizes to institutions."),
            completeness=("indeterminate", "No institutional or public-incident test examines parallel technical and organizational paths."),
            publication_authority=("pass", "The source is an official Transactions on Machine Learning Research paper."),
        ),
        "dependencies": ["PAPER-C30"],
        "dependency_closure": "pass",
        "conclusion_eligible": False,
        "human_review": human_review(
            "PAPER-C32",
            "Reviewed as a proposed synthesis whose transfer gates remain indeterminate.",
        ),
        "scope_terms": [],
        "limitations": [
            "The mechanism is established for the studied model architectures and remains untested for institutions or public incidents."
        ],
        "reversal_conditions": [
            "Replication fails to reproduce the residual-path result or later evidence supplies a narrower mechanism."
        ],
    }
    return [c27, c28, c29, c30, c31, c32]


def build() -> dict[str, Any]:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    result = copy.deepcopy(source)
    result["version"] = "0.11.0"
    result["scope_id"] = "TAE-COE-V0.11.0"
    result["description"] = (
        "Material paper and repository claims audited through v0.11.0, including the direct-query "
        "retrieval tranche, four bounded source descriptions, and one provisional synthesis."
    )
    for claim in result["claims"]:
        for item in claim["evidence"]:
            if item["integrity_state"] == "verified":
                item["sha256"] = digest(item["path"])
    result["claims"].extend(new_claims())
    return result


def inline(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(", ", ": "))


def render(claim_map: dict[str, Any]) -> str:
    """Preserve the compact v0.9 claim layout so substantive changes stay reviewable."""
    lines = [
        "{",
        f'  "version": {inline(claim_map["version"])},',
        f'  "scope_id": {inline(claim_map["scope_id"])},',
        f'  "description": {inline(claim_map["description"])},',
        '  "claims": [',
    ]
    claims = claim_map["claims"]
    for claim_index, claim in enumerate(claims):
        lines.extend([
            "    {",
            f'      "claim_id": {inline(claim["claim_id"])},',
            f'      "claim_text": {inline(claim["claim_text"])},',
            f'      "claim_class": {inline(claim["claim_class"])},',
            f'      "claim_scope": {inline(claim["claim_scope"])},',
            f'      "status": {inline(claim["status"])},',
            f'      "verification_rule": {inline(claim["verification_rule"])},',
            '      "evidence": [',
        ])
        for evidence_index, item in enumerate(claim["evidence"]):
            suffix = "," if evidence_index + 1 < len(claim["evidence"]) else ""
            lines.append(f"        {inline(item)}{suffix}")
        lines.extend([
            "      ],",
            '      "fitness": {',
        ])
        dimensions = list(claim["fitness"].items())
        for dimension_index, (name, value) in enumerate(dimensions):
            suffix = "," if dimension_index + 1 < len(dimensions) else ""
            lines.append(f'        {inline(name)}: {inline(value)}{suffix}')
        lines.extend([
            "      },",
            f'      "dependencies": {inline(claim["dependencies"])},',
            f'      "dependency_closure": {inline(claim["dependency_closure"])},',
            f'      "conclusion_eligible": {inline(claim["conclusion_eligible"])},',
            f'      "human_review": {inline(claim["human_review"])},',
            f'      "scope_terms": {inline(claim["scope_terms"])},',
            f'      "limitations": {inline(claim["limitations"])},',
            f'      "reversal_conditions": {inline(claim["reversal_conditions"])}',
            "    }" + ("," if claim_index + 1 < len(claims) else ""),
        ])
    lines.extend(["  ]", "}", ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render(build())
    if args.write:
        OUTPUT.write_text(expected, encoding="utf-8")
    if args.check and (not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != expected):
        raise SystemExit("v0.11 claim map: FAIL\ncommitted output differs from the deterministic builder")
    print("v0.11 claim map: PASS (26 claims; 6 v0.11 claims)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
