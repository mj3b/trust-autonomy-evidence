#!/usr/bin/env python3
"""Validate the author-decision gate that separates preliminary and final search flow."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "paper" / "data" / "author-screening-queue-v0.7.0.csv"
DECISIONS = ROOT / "paper" / "data" / "author-screening-decisions-v0.8.0.csv"
REPORT = ROOT / "paper" / "author-screening-completion-gate.md"
SUMMARY = ROOT / "paper" / "data" / "author-screening-gate-v0.8.0.json"
EXPECTED_ROWS = 89
ALLOWED_DECISIONS = {
    "retain-close",
    "retain-background",
    "exclude-topic",
    "exclude-single-component",
    "exclude-outside-cutoff",
    "inaccessible",
}


def read_rows() -> list[dict[str, str]]:
    with QUEUE.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    with DECISIONS.open(encoding="utf-8", newline="") as handle:
        decision_rows = list(csv.DictReader(handle))
    indexed = {row["record_key"]: row for row in decision_rows}
    for row in rows:
        decision = indexed.get(row["record_key"], {})
        row["author_decision"] = decision.get("author_decision", "").strip()
        row["author_notes"] = decision.get("author_notes", "").strip()
    rows.append({"_decision_ledger_rows": str(len(decision_rows)), "_decision_ledger_keys": "\n".join(indexed)})
    return rows


def inspect(rows: list[dict[str, str]]) -> tuple[list[str], int, int, Counter[str], Counter[str]]:
    errors: list[str] = []
    metadata = rows[-1]
    rows = rows[:-1]
    if len(rows) != EXPECTED_ROWS:
        errors.append(f"queue contains {len(rows)} rows; expected {EXPECTED_ROWS}")
    keys = [row.get("record_key", "").strip() for row in rows]
    if any(not key for key in keys):
        errors.append("queue contains a blank record key")
    if len(keys) != len(set(keys)):
        errors.append("queue contains duplicate record keys")
    ledger_keys = [key for key in metadata.get("_decision_ledger_keys", "").split("\n") if key]
    if int(metadata.get("_decision_ledger_rows", "0")) != len(ledger_keys):
        errors.append("decision ledger contains duplicate record keys")
    unknown = sorted(set(ledger_keys) - set(keys))
    if unknown:
        errors.append(f"decision ledger contains unknown record keys: {', '.join(unknown)}")
    invalid = sorted(
        {
            row.get("author_decision", "").strip()
            for row in rows
            if row.get("author_decision", "").strip()
            and row.get("author_decision", "").strip() not in ALLOWED_DECISIONS
        }
    )
    if invalid:
        errors.append(f"queue contains invalid author decisions: {', '.join(invalid)}")
    departures_without_notes = [
        row["record_key"]
        for row in rows
        if row.get("author_decision", "").strip()
        and row.get("author_decision", "").strip() != row.get("proposed_decision", "").strip()
        and not row.get("author_notes", "").strip()
    ]
    if departures_without_notes:
        errors.append(
            "author decisions that depart from proposals require notes: "
            + ", ".join(departures_without_notes)
        )
    proposed = Counter(row.get("proposed_decision", "").strip() for row in rows)
    author = Counter(row.get("author_decision", "").strip() for row in rows if row.get("author_decision", "").strip())
    completed = sum(author.values())
    open_count = len(rows) - completed
    return errors, completed, open_count, proposed, author


def report_text(rows: list[dict[str, str]]) -> str:
    errors, completed, open_count, proposed, author = inspect(rows)
    rows = rows[:-1]
    status = "INVALID" if errors else ("CLOSED" if open_count == 0 else "OPEN")
    close_complete = sum(
        bool(row.get("author_decision", "").strip())
        for row in rows
        if row.get("proposed_decision") == "retain-close"
    )
    attention_complete = sum(
        bool(row.get("author_decision", "").strip())
        for row in rows
        if row.get("proposed_decision") == "exclude-single-component"
    )
    lines = [
        "# Author Screening Completion Gate",
        "",
        f"**Status:** {status}",
        "",
        "Mark Julius Banasihan is the recorded decision owner. AI-assisted proposals remain proposals until the v0.8 decision ledger records his decision. The final search-flow figure is eligible only after every queued record has a valid author decision.",
        "",
        "## Current state",
        "",
        "| Queue component | Records | Author decisions complete | Decisions open |",
        "|---|---:|---:|---:|",
        f"| Proposed retain-close | {proposed.get('retain-close', 0)} | {close_complete} | {proposed.get('retain-close', 0) - close_complete} |",
        f"| Proposed attention | {proposed.get('exclude-single-component', 0)} | {attention_complete} | {proposed.get('exclude-single-component', 0) - attention_complete} |",
        f"| Total author gate | {len(rows)} | {completed} | {open_count} |",
        "",
        "## Completion conditions",
        "",
        "1. The v0.8 decision ledger contains one permitted `author_decision` value for every v0.7 queue record.",
        "2. Decisions that depart from the proposal contain a short `author_notes` rationale.",
        "3. Retained close sources receive full-text verification before they support a substantive manuscript claim.",
        "4. The search table and Figure 5 are rebuilt from the author decisions.",
        "5. The manuscript replaces preliminary-screening language with final-screening language only after this gate closes.",
        "",
        "## Permitted decisions",
        "",
        "`retain-close`, `retain-background`, `exclude-topic`, `exclude-single-component`, `exclude-outside-cutoff`, or `inaccessible`.",
        "",
        "## Current boundary",
        "",
        f"The gate is {status.lower()}. Figure 5 remains a preliminary search-flow figure. The repository can report retrieval and proposal counts; it cannot report final screening counts while {open_count} author decisions remain open.",
    ]
    if author:
        lines.extend(["", "## Recorded author decisions", ""])
        lines.extend(f"- `{decision}`: {count}" for decision, count in sorted(author.items()))
    if errors:
        lines.extend(["", "## Validation errors", ""])
        lines.extend(f"- {error}" for error in errors)
    return "\n".join(lines) + "\n"


def summary_text(rows: list[dict[str, str]]) -> str:
    errors, completed, open_count, proposed, author = inspect(rows)
    queue_length = len(rows) - 1
    status = "INVALID" if errors else ("CLOSED" if open_count == 0 else "OPEN")
    summary = {
        "version": "0.8.0",
        "status": status,
        "records": queue_length,
        "author_decisions_complete": completed,
        "author_decisions_open": open_count,
        "proposed_counts": dict(sorted(proposed.items())),
        "author_counts": dict(sorted(author.items())),
        "final_search_flow_eligible": status == "CLOSED",
        "validation_errors": errors,
    }
    return json.dumps(summary, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-report", action="store_true", help="write the Markdown gate report")
    parser.add_argument("--check", action="store_true", help="verify the queue and committed report")
    parser.add_argument("--require-complete", action="store_true", help="fail while any author decision is open")
    args = parser.parse_args()

    rows = read_rows()
    errors, completed, open_count, _, _ = inspect(rows)
    queue_length = len(rows) - 1
    expected_report = report_text(rows)
    expected_summary = summary_text(rows)
    if args.write_report:
        REPORT.write_text(expected_report, encoding="utf-8")
        SUMMARY.write_text(expected_summary, encoding="utf-8")
    if args.check:
        if not REPORT.is_file() or REPORT.read_text(encoding="utf-8") != expected_report:
            errors.append("author-screening gate report is missing or stale")
        if not SUMMARY.is_file() or SUMMARY.read_text(encoding="utf-8") != expected_summary:
            errors.append("author-screening gate summary is missing or stale")
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        print(f"author screening gate: INVALID ({len(errors)} error(s))")
        return 1
    if args.require_complete and open_count:
        print(f"author screening gate: OPEN ({completed}/{queue_length} complete; {open_count} open)")
        return 1
    state = "CLOSED" if open_count == 0 else "OPEN"
    print(f"author screening gate: {state} ({completed}/{queue_length} complete; {open_count} open)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
