#!/usr/bin/env python3
"""Validate the current sentence-level literature-support register."""

from __future__ import annotations

import json
import re
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "paper/literature-support-audit-v0.9.0.json"
SCHEMA = ROOT / "schemas/literature-support-audit.schema.json"
MANUSCRIPT = ROOT / "paper/manuscript.md"
BIBLIOGRAPHY = ROOT / "paper/references.bib"


def main() -> None:
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(audit)

    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    bibliography = BIBLIOGRAPHY.read_text(encoding="utf-8")
    keys = set(re.findall(r"@[A-Za-z]+\{([^,]+),", bibliography))
    failures: list[str] = []

    for entry in audit["entries"]:
        if manuscript.count(entry["locator"]) != 1:
            failures.append(f'{entry["claim_id"]}: locator must occur exactly once')
        missing = sorted(set(entry["citation_keys"]) - keys)
        if missing:
            failures.append(f'{entry["claim_id"]}: missing citation keys {missing}')
        if entry["support_state"] != "pass":
            failures.append(f'{entry["claim_id"]}: support state is {entry["support_state"]}')

    if re.search(r"\bnovel\b", manuscript, flags=re.IGNORECASE):
        failures.append("manuscript contains prohibited novelty wording")
    if "Authenticated Scopus or Web of Science" not in manuscript:
        failures.append("manuscript does not disclose the authenticated-database limit")

    if failures:
        raise SystemExit("literature-support validation: FAIL\n" + "\n".join(failures))
    print(f'literature-support validation: PASS ({len(audit["entries"])} propositions)')


if __name__ == "__main__":
    main()
