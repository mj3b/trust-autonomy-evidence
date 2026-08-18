#!/usr/bin/env python3
"""Build and verify the v0.15 venue-revision claim map."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from build_v0_14_claim_map import build as build_v0_14
from build_v0_11_claim_map import evidence, fitness, render


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = "evidence/claim-evidence-map.json"
METADATA = "paper/preprints/metadata.yaml"
MANUSCRIPT = "paper/manuscript.md"
PACKAGE_README = "paper/preprints/README.md"
ATTESTATION = "evidence/human-review-attestation-v0.15.0.json"
AUTHOR = "Mark Julius Banasihan"
REVIEW_DATE = "2026-08-18"


def human_review(claim_id: str, note: str) -> dict[str, Any]:
    return {
        "status": "recorded",
        "reviewer": AUTHOR,
        "review_date": REVIEW_DATE,
        "attestation_path": ATTESTATION,
        "note": f"{claim_id}: {note}",
    }


def prior_version_trace() -> dict[str, Any]:
    return {
        "claim_id": "PAPER-C39",
        "claim_text": (
            "The v0.15 venue package identifies the Zenodo v0.14.0 preprint through the issued "
            "version DOI 10.5281/zenodo.21926005."
        ),
        "claim_class": "documentary_classification",
        "claim_scope": "paper",
        "status": "supported",
        "verification_rule": (
            "The prior platform, version, DOI, manuscript relationship statement, and package note "
            "must resolve to the same frozen record."
        ),
        "evidence": [
            evidence("C39-METADATA", METADATA, "text_marker", 'doi: "10.5281/zenodo.21926005"', "provenance"),
            evidence("C39-MANUSCRIPT", MANUSCRIPT, "text_marker", "The v0.14.0 preprint was archived on Zenodo", "method"),
            evidence("C39-PACKAGE", PACKAGE_README, "text_marker", "The package identifies the Zenodo v0.14.0 preprint", "implementation"),
            evidence("C39-ATTESTATION", ATTESTATION, "text_marker", "PAPER-C39", "provenance"),
        ],
        "fitness": fitness(
            directness=("pass", "The three package records identify the same version DOI directly."),
            contemporaneity=("pass", "The records were created for the v0.15 venue revision."),
            independence=("outside_scope", "The claim records repository provenance and makes no independent research judgment."),
            completeness=("pass", "Platform, prior version, DOI, and present-version relationship are visible."),
            publication_authority=("pass", "Zenodo issued the DOI and the author approved the repository version relationship."),
        ),
        "dependencies": [],
        "dependency_closure": "pass",
        "conclusion_eligible": True,
        "human_review": human_review("PAPER-C39", "Approved as the public relationship between the frozen Zenodo v0.14.0 record and this venue candidate."),
        "scope_terms": [],
        "limitations": [
            "The relationship statement does not establish that Preprints.org will accept a manuscript previously archived elsewhere."
        ],
        "reversal_conditions": [
            "The Zenodo record, version DOI, manuscript relationship statement, or package metadata changes."
        ],
    }


def author_identity_trace() -> dict[str, Any]:
    return {
        "claim_id": "PAPER-C40",
        "claim_text": (
            "The v0.15 venue metadata identifies Mark Julius Banasihan, ORCID 0009-0001-8121-2878, "
            "as an independent researcher with Node & Norm, with a specific Harvard University student-status note "
            "and two author-approved correspondence addresses."
        ),
        "claim_class": "documentary_classification",
        "claim_scope": "paper",
        "status": "supported",
        "verification_rule": (
            "The full author name, ORCID, Node & Norm affiliation, student status, independence disclaimer, "
            "two correspondence addresses, and author attestation must resolve in the venue package."
        ),
        "evidence": [
            evidence("C40-AUTHOR", METADATA, "text_marker", 'name: "Mark Julius Banasihan"', "provenance"),
            evidence("C40-ORCID", METADATA, "text_marker", 'orcid: "0009-0001-8121-2878"', "provenance"),
            evidence("C40-AFFILIATION", METADATA, "text_marker", 'affiliation: "Independent Researcher, Node & Norm, United States"', "provenance"),
            evidence("C40-CORRESPONDENCE", METADATA, "text_marker", 'corresponding_email: "mab7898@g.harvard.edu"', "provenance"),
            evidence("C40-ALTERNATE", METADATA, "text_marker", 'alternate_email: "markjuliusbanasihan@gmail.com"', "provenance"),
            evidence("C40-STUDENT", METADATA, "text_marker", 'student_status: "ALB candidate in Extension Studies, Harvard University"', "provenance"),
            evidence("C40-INDEPENDENCE", METADATA, "text_marker", "It was not sponsored, supervised, or endorsed by Harvard University", "limitation"),
            evidence("C40-ATTESTATION", ATTESTATION, "text_marker", "PAPER-C40", "provenance"),
        ],
        "fitness": fitness(
            directness=("pass", "The venue metadata records each identity, affiliation, status, contact, and independence field directly."),
            contemporaneity=("pass", "The author confirmed the Node & Norm affiliation and both correspondence addresses on 2026-08-18."),
            independence=("outside_scope", "The claim records author-controlled identity metadata."),
            completeness=("pass", "The package includes full name, ORCID, independent affiliation, student status, two addresses, and the independence disclaimer."),
            publication_authority=("pass", "The author controls the identity declaration and authenticated to Preprints.org through ORCID."),
        ),
        "dependencies": [],
        "dependency_closure": "pass",
        "conclusion_eligible": True,
        "human_review": human_review("PAPER-C40", "Confirmed Node & Norm as the independent research affiliation and authorized both correspondence addresses."),
        "scope_terms": [],
        "limitations": [
            "Node & Norm is not represented as an LLC before incorporation; the Harvard University statement identifies student status only."
        ],
        "reversal_conditions": [
            "The author name, ORCID, affiliation, student status, correspondence addresses, disclaimer, or author direction changes."
        ],
    }


def submission_readiness_gate() -> dict[str, Any]:
    return {
        "claim_id": "PAPER-C41",
        "claim_text": "The v0.15 Preprints.org package is ready for final submission.",
        "claim_class": "conclusion",
        "claim_scope": "paper",
        "status": "provisional",
        "verification_rule": (
            "The conflict declaration, compiled-PDF inspection, prior-version disclosure, repository "
            "validation, integrity audit, and exact submitted-file hashes must all close."
        ),
        "evidence": [
            evidence("C41-STATE", METADATA, "text_marker", 'submission_state: "DRAFT_DO_NOT_SUBMIT"', "limitation", content_review="pending"),
            evidence("C41-CONFLICT", METADATA, "text_marker", 'conflicts_of_interest: "AUTHOR_CONFIRMATION_REQUIRED"', "limitation", content_review="pending"),
            evidence("C41-GATES", PACKAGE_README, "markdown_heading", "## Submission gates", "method", content_review="pending"),
        ],
        "fitness": fitness(
            directness=("pass", "The package exposes each remaining submission gate."),
            contemporaneity=("pass", "The gates describe the current v0.15 submission state."),
            independence=("outside_scope", "Platform screening and peer review remain external to repository readiness."),
            completeness=("indeterminate", "Conflict confirmation, compiled-PDF inspection, and final submitted-file hashes remain open."),
            publication_authority=("pass", "The author controls the declarations and final submission decision."),
        ),
        "dependencies": ["PAPER-C39", "PAPER-C40"],
        "dependency_closure": "pass",
        "conclusion_eligible": False,
        "human_review": {
            "status": "pending",
            "reviewer": AUTHOR,
            "review_date": None,
            "attestation_path": ATTESTATION,
            "note": "Identity and prior-version metadata are approved; final submission gates remain open.",
        },
        "scope_terms": [],
        "limitations": [
            "The package has not been compiled as v0.15.0, visually inspected, uploaded to Preprints.org, or submitted."
        ],
        "reversal_conditions": [
            "Any declaration, compiled artifact, validation result, archive member, or submission field changes."
        ],
    }


def build() -> dict[str, Any]:
    result = build_v0_14()
    result["version"] = "0.15.0"
    result["scope_id"] = "TAE-COE-V0.15.0"
    result["description"] = (
        "Material paper and repository claims audited through v0.15.0, including prior-version "
        "provenance, venue identity metadata, and an explicit final-submission gate."
    )
    result["claims"].extend([prior_version_trace(), author_identity_trace(), submission_readiness_gate()])
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
        raise SystemExit("v0.15 claim map: FAIL\ncommitted output differs from the deterministic builder")
    print("v0.15 claim map: PASS (35 claims; final submission gate remains open)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
