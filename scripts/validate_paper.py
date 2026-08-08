#!/usr/bin/env python3
"""Validate the unreleased practical human control paper workspace."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUTHOR = "Mark Julius Banasihan"
ORCID = "0009-0001-8121-2878"
QUESTION = (
    "How can a frozen, evidence-traceable assessment procedure represent formal "
    "human authority, practical human control, and unresolved evidence in a bounded "
    "public incident record?"
)
VERSION_DOI = "10.5281/zenodo.21844706"
PAPER_FILES = (
    "paper/README.md",
    "paper/paper-charter.md",
    "paper/manuscript.md",
    "paper/literature-matrix.md",
    "paper/literature-search-log.md",
    "paper/novelty-audit.md",
    "paper/references.bib",
    "paper/claim-evidence-register.md",
    "paper/submission-notes.md",
    "paper/review-record-pr11.md",
)


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def validate_files(failures: list[str]) -> None:
    for relative in PAPER_FILES:
        path = ROOT / relative
        if not path.is_file():
            fail(f"missing paper file: {relative}", failures)
        elif path.stat().st_size == 0:
            fail(f"empty paper file: {relative}", failures)


def validate_identity(failures: list[str]) -> None:
    required_author_files = (
        "paper/manuscript.md",
        "paper/paper-charter.md",
        "paper/submission-notes.md",
    )
    for relative in required_author_files:
        text = (ROOT / relative).read_text(encoding="utf-8")
        if AUTHOR not in text:
            fail(f"full author name missing from {relative}", failures)
    manuscript = (ROOT / "paper/manuscript.md").read_text(encoding="utf-8")
    if ORCID not in manuscript:
        fail("ORCID missing from paper/manuscript.md", failures)
    combined = "\n".join(
        (ROOT / relative).read_text(encoding="utf-8")
        for relative in PAPER_FILES
        if relative.endswith(".md")
    )
    if re.search(r"\bMark Banasihan\b", combined):
        fail("ambiguous author name found in paper workspace", failures)


def validate_question(failures: list[str]) -> None:
    for relative in (
        "paper/README.md",
        "paper/paper-charter.md",
        "paper/manuscript.md",
    ):
        text = (ROOT / relative).read_text(encoding="utf-8")
        if QUESTION not in text:
            fail(f"paper question mismatch in {relative}", failures)


def validate_bibliography(failures: list[str]) -> None:
    text = (ROOT / "paper/references.bib").read_text(encoding="utf-8")
    entries = re.findall(r"^@\w+\{([^,]+),", text, flags=re.MULTILINE)
    if len(entries) < 23:
        fail(f"paper bibliography has {len(entries)} entries; expected at least 23", failures)
    if len(entries) != len(set(entries)):
        fail("duplicate BibTeX keys in paper/references.bib", failures)
    doi_fields = re.findall(r"^\s+doi\s*=", text, flags=re.MULTILINE | re.IGNORECASE)
    if len(doi_fields) < 20:
        fail(f"paper bibliography has {len(doi_fields)} DOI fields; expected at least 20", failures)
    if "\\\\&" in text:
        fail("doubled backslash before ampersand in paper/references.bib", failures)


def validate_boundaries(failures: list[str]) -> None:
    review = (ROOT / "paper/review-record-pr11.md").read_text(encoding="utf-8")
    register = (ROOT / "paper/claim-evidence-register.md").read_text(encoding="utf-8")
    manuscript = (ROOT / "paper/manuscript.md").read_text(encoding="utf-8")
    for relative, text in (
        ("paper/review-record-pr11.md", review),
        ("paper/claim-evidence-register.md", register),
        ("paper/manuscript.md", manuscript),
    ):
        if "PAPER-BLOCKER-01" not in text:
            fail(f"open paper blocker missing from {relative}", failures)
    citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    if VERSION_DOI not in citation:
        fail("CITATION.cff does not contain the v0.4.0 version DOI", failures)
    if VERSION_DOI not in manuscript:
        fail("v0.4.0 version DOI missing from paper/manuscript.md", failures)


def main() -> int:
    failures: list[str] = []
    validate_files(failures)
    if not failures:
        validate_identity(failures)
        validate_question(failures)
        validate_bibliography(failures)
        validate_boundaries(failures)
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print(f"paper validation: FAIL ({len(failures)} error(s))")
        return 1
    print("paper validation: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
