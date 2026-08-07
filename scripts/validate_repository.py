#!/usr/bin/env python3
"""Validate the public research repository and solo-validation artifacts."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.2.0"

REQUIRED_FILES = (
    "README.md",
    "RESEARCH_STATUS.md",
    "CLAIMS.md",
    "LIMITATIONS.md",
    "SOURCES.md",
    "CITATION.cff",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "LICENSE",
    "requirements-dev.txt",
    "research/trust-autonomy-and-evidence.md",
    "evidence/trust-evidence-register.md",
    "protocols/independent-review-protocol.md",
    "protocols/practical-human-control-test.md",
    "protocols/solo-validation-protocol.md",
    "protocols/public-case-reconstruction-protocol.md",
    "cases/README.md",
    "cases/public-case-selection-register.md",
    "schemas/autonomy-profile.schema.json",
    "schemas/solo-case.schema.json",
    "schemas/trust-evidence-assessment.schema.json",
    "schemas/practical-control-assessment.schema.json",
    "schemas/mutation-suite.schema.json",
    "fixtures/synthetic/cases.json",
    "fixtures/mutations/mutations.json",
    "oracles/solo-validation-v0.2.0.json",
    "oracles/manifest.json",
    "analysis/assessment.py",
    "analysis/run_solo_validation.py",
    "assessments/generated-results.json",
    "reports/solo-validation-v0.2.0.md",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/case-proposal.yml",
    ".github/ISSUE_TEMPLATE/construct-ambiguity.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    "mappings/governed-decision-intelligence.md",
    "mappings/human-influence-telemetry.md",
    "mappings/cdfi-framework.md",
    "mappings/cdcf-governance.md",
)

PRIVATE_TERMS = (
    "Research Scholar " + "candidacy",
    "application " + "strategy",
    "what Mark " + "can claim",
)

MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
CLAIM_ID = re.compile(r"\bTAE-C\d{2}\b")


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def validate_required_files(failures: list[str]) -> None:
    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.is_file():
            fail(f"missing required file: {relative}", failures)
        elif path.stat().st_size == 0:
            fail(f"empty required file: {relative}", failures)


def validate_internal_links(failures: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(text):
            clean_target = target.split("#", 1)[0]
            if not clean_target or clean_target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / clean_target).resolve()
            if not resolved.exists():
                relative_source = path.relative_to(ROOT)
                fail(f"broken local link in {relative_source}: {target}", failures)


def validate_versions(failures: list[str]) -> None:
    required_markers = {
        "README.md": f"Version: {VERSION}",
        "RESEARCH_STATUS.md": f"**Version:** {VERSION}",
        "CITATION.cff": f"version: {VERSION}",
        "CHANGELOG.md": f"## {VERSION}",
    }
    for relative, marker in required_markers.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        if marker not in text:
            fail(f"version marker missing from {relative}: {marker}", failures)


def validate_claim_ids(failures: list[str]) -> None:
    text = (ROOT / "CLAIMS.md").read_text(encoding="utf-8")
    identifiers = CLAIM_ID.findall(text)
    duplicates = sorted({identifier for identifier in identifiers if identifiers.count(identifier) > 1})
    if duplicates:
        fail(f"duplicate claim identifiers: {', '.join(duplicates)}", failures)
    if not identifiers:
        fail("no claim identifiers found", failures)


def validate_public_boundary(failures: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix not in {".md", ".cff", ".yml", ".yaml"}:
            continue
        text = path.read_text(encoding="utf-8")
        for term in PRIVATE_TERMS:
            if term.lower() in text.lower():
                relative = path.relative_to(ROOT)
                fail(f"private term found in {relative}: {term}", failures)


def validate_solo_suite(failures: list[str]) -> str:
    result = subprocess.run(
        [sys.executable, "analysis/run_solo_validation.py", "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        detail = (result.stdout + result.stderr).strip()
        fail(f"solo-validation suite failed: {detail}", failures)
        return ""
    return result.stdout.strip()


def main() -> int:
    failures: list[str] = []
    validate_required_files(failures)
    validate_internal_links(failures)
    validate_versions(failures)
    validate_claim_ids(failures)
    validate_public_boundary(failures)
    solo_result = validate_solo_suite(failures)

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print(f"repository validation: FAIL ({len(failures)} error(s))")
        return 1

    if solo_result:
        print(solo_result)
    print("repository validation: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
