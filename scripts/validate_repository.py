#!/usr/bin/env python3
"""Validate the public research repository without external dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.1.0"

REQUIRED_FILES = (
    "README.md",
    "RESEARCH_STATUS.md",
    "CLAIMS.md",
    "LIMITATIONS.md",
    "SOURCES.md",
    "CITATION.cff",
    "CHANGELOG.md",
    "LICENSE",
    "research/trust-autonomy-and-evidence.md",
    "evidence/trust-evidence-register.md",
    "protocols/independent-review-protocol.md",
    "protocols/practical-human-control-test.md",
    "cases/README.md",
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


def main() -> int:
    failures: list[str] = []
    validate_required_files(failures)
    validate_internal_links(failures)
    validate_versions(failures)
    validate_claim_ids(failures)
    validate_public_boundary(failures)

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print(f"repository validation: FAIL ({len(failures)} error(s))")
        return 1

    print("repository validation: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
