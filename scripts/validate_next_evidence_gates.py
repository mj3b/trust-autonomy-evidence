#!/usr/bin/env python3
"""Initialize and validate the v0.10 literature evidence gates."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUTHOR_QUEUE = ROOT / "paper/data/author-screening-queue-v0.7.0.csv"
AUTHOR_DECISIONS = ROOT / "paper/data/author-screening-decisions-v0.9.0.csv"
FORMAL_PROPOSALS = ROOT / "paper/data/formal-screening-proposals-v0.7.0.json"
FULL_TEXT_LEDGER = ROOT / "paper/data/close-source-full-text-gate-v0.10.0.csv"
RETRIEVAL_LEDGER = ROOT / "paper/data/inaccessible-record-retrieval-v0.10.0.csv"
RISK_SAMPLE = ROOT / "paper/data/inaccessible-risk-sample-v0.11.0.csv"
RISK_SAMPLE_SUMMARY = ROOT / "paper/data/inaccessible-risk-sample-v0.11.0.json"
INTERFACE_LEDGER = ROOT / "paper/data/authenticated-interface-searches-v0.10.0.csv"
SUMMARY = ROOT / "paper/data/next-evidence-gates-v0.10.0.json"
REPORT = ROOT / "paper/next-evidence-gates-v0.10.0.md"

AUTHOR = "Mark Julius Banasihan"
EXPECTED_CLOSE = 27
EXPECTED_INACCESSIBLE = 1087
EXPECTED_RISK_SAMPLE = 284
EXPECTED_RISK_STRATA = {
    "forward-citation": 102,
    "backward-reference": 177,
    "direct-query": 5,
}
TERMINAL_FULL_TEXT_STATES = {
    "verified",
    "abstract-only-not-used",
    "excluded-after-full-text",
    "inaccessible",
}
ALLOWED_FULL_TEXT_STATES = TERMINAL_FULL_TEXT_STATES | {"open"}
ALLOWED_RETRIEVAL_OUTCOMES = {
    "abstract-recovered",
    "full-text-recovered",
    "metadata-only",
    "duplicate",
    "outside-cutoff",
    "unavailable",
}
REQUIRED_INTERFACES = {
    "scopus-or-web-of-science",
    "acm-digital-library",
    "ieee-xplore",
    "philpapers",
    "heinonline-or-hollis",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def initialize_ledgers() -> None:
    queue = {row["record_key"]: row for row in read_csv(AUTHOR_QUEUE)}
    decisions = read_csv(AUTHOR_DECISIONS)
    close = [row for row in decisions if row["author_decision"] == "retain-close"]
    if len(close) != EXPECTED_CLOSE:
        raise SystemExit(f"expected {EXPECTED_CLOSE} close sources; found {len(close)}")

    full_text_rows: list[dict[str, str]] = []
    for decision in close:
        source = queue[decision["record_key"]]
        full_text = "full_text" in decision["review_basis"]
        full_text_rows.append(
            {
                "record_key": decision["record_key"],
                "title": source["title"],
                "source_locator": decision["source_locator"],
                "screening_review_basis": decision["review_basis"],
                "verification_state": "verified" if full_text else "open",
                "full_text_locator": decision["source_locator"] if full_text else "",
                "verification_notes": (
                    "Full text was recorded as inspected during v0.9 author screening; "
                    "support remains proposition-specific."
                    if full_text
                    else ""
                ),
                "reviewer": decision["decision_owner"] if full_text else "",
                "review_date": decision["decision_date"] if full_text else "",
                "ai_assistance": decision["ai_assistance"] if full_text else "",
                "full_text_gate_pass": "true" if full_text else "false",
            }
        )
    write_csv(
        FULL_TEXT_LEDGER,
        [
            "record_key",
            "title",
            "source_locator",
            "screening_review_basis",
            "verification_state",
            "full_text_locator",
            "verification_notes",
            "reviewer",
            "review_date",
            "ai_assistance",
            "full_text_gate_pass",
        ],
        full_text_rows,
    )

    if not RETRIEVAL_LEDGER.exists():
        write_csv(
            RETRIEVAL_LEDGER,
            [
                "record_key",
                "retrieval_outcome",
                "retrieval_locator",
                "retrieval_date",
                "screening_decision",
                "author_notes",
                "decision_owner",
                "ai_assistance",
            ],
            [],
        )

    if not INTERFACE_LEDGER.exists():
        rows = [
            {
                "surface": surface,
                "status": "open",
                "access_condition": "",
                "query_record": "paper/formal-literature-search-protocol-v0.7.0.md#frozen-query-families",
                "search_date": "",
                "displayed_results": "",
                "deduplicated_records": "",
                "author_decisions_complete": "",
                "notes": "",
            }
            for surface in sorted(REQUIRED_INTERFACES)
        ]
        write_csv(
            INTERFACE_LEDGER,
            [
                "surface",
                "status",
                "access_condition",
                "query_record",
                "search_date",
                "displayed_results",
                "deduplicated_records",
                "author_decisions_complete",
                "notes",
            ],
            rows,
        )


def inspect() -> tuple[list[str], dict[str, object]]:
    errors: list[str] = []
    decisions = read_csv(AUTHOR_DECISIONS)
    close_keys = {
        row["record_key"] for row in decisions if row["author_decision"] == "retain-close"
    }
    full_text = read_csv(FULL_TEXT_LEDGER)
    ledger_keys = [row["record_key"] for row in full_text]

    if len(close_keys) != EXPECTED_CLOSE:
        errors.append(f"author ledger contains {len(close_keys)} close sources; expected {EXPECTED_CLOSE}")
    if len(ledger_keys) != len(set(ledger_keys)):
        errors.append("full-text ledger contains duplicate record keys")
    if set(ledger_keys) != close_keys:
        missing = sorted(close_keys - set(ledger_keys))
        extra = sorted(set(ledger_keys) - close_keys)
        errors.append(f"full-text ledger key mismatch; missing={missing}; extra={extra}")

    for row in full_text:
        state = row["verification_state"]
        if state not in ALLOWED_FULL_TEXT_STATES:
            errors.append(f'{row["record_key"]}: invalid verification state {state!r}')
        if state == "verified":
            required = (
                "full_text_locator",
                "verification_notes",
                "reviewer",
                "review_date",
                "ai_assistance",
            )
            blank = [field for field in required if not row[field].strip()]
            if blank:
                errors.append(f'{row["record_key"]}: verified row lacks {blank}')
            if row["reviewer"].strip() != AUTHOR:
                errors.append(f'{row["record_key"]}: reviewer must be {AUTHOR}')
            if row["full_text_gate_pass"].lower() != "true":
                errors.append(f'{row["record_key"]}: verified row must pass the full-text gate')
        elif row["full_text_gate_pass"].lower() == "true":
            errors.append(f'{row["record_key"]}: non-verified source cannot pass the full-text gate')

    proposal = json.loads(FORMAL_PROPOSALS.read_text(encoding="utf-8"))
    inaccessible_keys = {
        row["record_key"]
        for row in proposal["decisions"]
        if row["proposed_decision"] == "inaccessible"
    }
    if len(inaccessible_keys) != EXPECTED_INACCESSIBLE:
        errors.append(
            f"frozen proposal set contains {len(inaccessible_keys)} inaccessible records; "
            f"expected {EXPECTED_INACCESSIBLE}"
        )
    retrieval = read_csv(RETRIEVAL_LEDGER)
    retrieval_keys = [row["record_key"] for row in retrieval]
    if len(retrieval_keys) != len(set(retrieval_keys)):
        errors.append("inaccessible-record ledger contains duplicate record keys")
    unknown = sorted(set(retrieval_keys) - inaccessible_keys)
    if unknown:
        errors.append(f"inaccessible-record ledger contains unknown keys: {unknown}")
    for row in retrieval:
        if row["retrieval_outcome"] not in ALLOWED_RETRIEVAL_OUTCOMES:
            errors.append(
                f'{row["record_key"]}: invalid retrieval outcome {row["retrieval_outcome"]!r}'
            )
        required = ("retrieval_locator", "retrieval_date", "decision_owner", "ai_assistance")
        blank = [field for field in required if not row[field].strip()]
        if blank:
            errors.append(f'{row["record_key"]}: retrieval row lacks {blank}')
        if row["decision_owner"].strip() != AUTHOR:
            errors.append(f'{row["record_key"]}: decision owner must be {AUTHOR}')

    risk_sample = read_csv(RISK_SAMPLE)
    risk_keys = [row["record_key"] for row in risk_sample]
    if len(risk_keys) != EXPECTED_RISK_SAMPLE:
        errors.append(
            f"risk sample contains {len(risk_keys)} records; expected {EXPECTED_RISK_SAMPLE}"
        )
    if len(risk_keys) != len(set(risk_keys)):
        errors.append("risk sample contains duplicate record keys")
    unknown_risk_keys = sorted(set(risk_keys) - inaccessible_keys)
    if unknown_risk_keys:
        errors.append(f"risk sample contains unknown keys: {unknown_risk_keys}")
    risk_strata = Counter(row["primary_stratum"] for row in risk_sample)
    if dict(risk_strata) != EXPECTED_RISK_STRATA:
        errors.append(
            f"risk sample stratum allocation mismatch: {dict(risk_strata)}"
        )
    if any(row["selection_status"] != "selected-before-retrieval" for row in risk_sample):
        errors.append("risk sample contains an invalid selection status")
    risk_summary = json.loads(RISK_SAMPLE_SUMMARY.read_text(encoding="utf-8"))
    if risk_summary.get("status") != "FROZEN_BEFORE_RETRIEVAL":
        errors.append("risk sample summary status mismatch")
    if risk_summary.get("population_size") != EXPECTED_INACCESSIBLE:
        errors.append("risk sample summary population mismatch")
    if risk_summary.get("selected_records") != EXPECTED_RISK_SAMPLE:
        errors.append("risk sample summary selection count mismatch")

    interfaces = read_csv(INTERFACE_LEDGER)
    interface_names = [row["surface"] for row in interfaces]
    if len(interface_names) != len(set(interface_names)):
        errors.append("authenticated-interface ledger contains duplicate surfaces")
    if set(interface_names) != REQUIRED_INTERFACES:
        errors.append("authenticated-interface ledger does not match the five declared surfaces")
    for row in interfaces:
        if row["status"] not in {"open", "complete", "access-failure"}:
            errors.append(f'{row["surface"]}: invalid interface status {row["status"]!r}')
        if row["status"] != "open":
            required = ("access_condition", "search_date", "notes")
            blank = [field for field in required if not row[field].strip()]
            if blank:
                errors.append(f'{row["surface"]}: completed interface row lacks {blank}')

    states = Counter(row["verification_state"] for row in full_text)
    terminal = sum(states[state] for state in TERMINAL_FULL_TEXT_STATES)
    verified = states["verified"]
    open_full_text = states["open"]
    retrieved = len(retrieval)
    sampled_retrieved = len(set(risk_keys) & set(retrieval_keys))
    interface_counts = Counter(row["status"] for row in interfaces)
    coverage_status = "CLOSED" if retrieved == EXPECTED_INACCESSIBLE else "OPEN"
    interface_status = (
        "CLOSED"
        if interface_counts["complete"] == len(REQUIRED_INTERFACES)
        else "OPEN"
    )
    full_text_status = "CLOSED" if terminal == EXPECTED_CLOSE else "OPEN"

    summary: dict[str, object] = {
        "version": "0.10.0",
        "status": "INVALID" if errors else "OPEN",
        "decision_owner": AUTHOR,
        "source_release": "v0.9.0",
        "gates": {
            "close_source_full_text": {
                "status": full_text_status,
                "records": EXPECTED_CLOSE,
                "terminal": terminal,
                "verified": verified,
                "abstract_only_not_used": states["abstract-only-not-used"],
                "excluded_after_full_text": states["excluded-after-full-text"],
                "inaccessible": states["inaccessible"],
                "open": open_full_text,
                "terminal_without_verification": terminal - verified,
                "claim_rule": "Only verified full text may support a proposition that exceeds the abstract.",
            },
            "inaccessible_record_retrieval": {
                "status": coverage_status,
                "records": EXPECTED_INACCESSIBLE,
                "retrieval_rows_complete": retrieved,
                "retrieval_rows_open": EXPECTED_INACCESSIBLE - retrieved,
                "residual_risk_sample": {
                    "status": "FROZEN_BEFORE_RETRIEVAL",
                    "selected": EXPECTED_RISK_SAMPLE,
                    "sampled_retrieval_complete": sampled_retrieved,
                    "sampled_retrieval_open": EXPECTED_RISK_SAMPLE - sampled_retrieved,
                    "strata": EXPECTED_RISK_STRATA,
                    "sample_record": "paper/data/inaccessible-risk-sample-v0.11.0.csv",
                },
                "claim_rule": "A completed risk sample estimates residual risk and does not establish exhaustive coverage.",
            },
            "authenticated_interfaces": {
                "status": interface_status,
                "required_surfaces": len(REQUIRED_INTERFACES),
                "complete": interface_counts["complete"],
                "access_failures": interface_counts["access-failure"],
                "open": interface_counts["open"],
                "claim_rule": "An access failure remains a coverage limit and cannot close the originality exception.",
            },
            "independent_assessment": {
                "status": "OPEN",
                "next_cycle": False,
                "claim_rule": "Internal reproducibility work cannot establish independent reliability or field validity.",
            },
        },
        "validation_errors": errors,
    }
    return errors, summary


def report_text(summary: dict[str, object]) -> str:
    gates = summary["gates"]
    full_text = gates["close_source_full_text"]
    inaccessible = gates["inaccessible_record_retrieval"]
    risk_sample = inaccessible["residual_risk_sample"]
    interfaces = gates["authenticated_interfaces"]
    return f"""# Next Evidence Gates, v0.10.0

**Status:** `{summary['status']}`  
**Decision owner:** {summary['decision_owner']}  
**Source release:** `{summary['source_release']}`

## Decision

The next research cycle addresses support and search coverage before the manuscript makes a stronger contribution claim. The case question and the three frozen topics remain unchanged.

## Gate state

| Gate | Population | Complete | Open | Current state |
|---|---:|---:|---:|---|
| Close-source full-text verification | {full_text['records']} | {full_text['terminal']} terminal | {full_text['open']} | `{full_text['status']}` |
| Inaccessible-record retrieval | {inaccessible['records']} | {inaccessible['retrieval_rows_complete']} | {inaccessible['retrieval_rows_open']} | `{inaccessible['status']}` |
| Authenticated and disciplinary interfaces | {interfaces['required_surfaces']} | {interfaces['complete']} | {interfaces['open']} | `{interfaces['status']}` |
| Independent assessment | 1 study | 0 | 1 | `OPEN`, outside this cycle |

## Residual-risk sample

The sample is frozen before retrieval with {risk_sample['selected']} selected records: {risk_sample['strata']['forward-citation']} forward citations, {risk_sample['strata']['backward-reference']} backward references, and {risk_sample['strata']['direct-query']} direct-query records. Retrieval is complete for {risk_sample['sampled_retrieval_complete']} of {risk_sample['selected']} sampled records. Frozen membership establishes selection lineage. It supplies no retrieval, prevalence, exhaustive-coverage, or originality result.

## Claim controls

1. A title-and-abstract review can support a bounded description of a source's declared purpose, model, or result.
2. A proposition that exceeds the abstract requires a verified full-text locator and proposition-specific support check.
3. A risk sample of inaccessible records can estimate residual coverage risk. It cannot establish exhaustive retrieval.
4. An authenticated-interface access failure remains visible and leaves the originality exception open.
5. Internal validation can test reproducibility and corruption detection. It cannot establish independent reliability or field validity.

## Current finding

The 89-decision author gate resolved screening accountability. The retained-close full-text gate is now closed with {full_text['verified']} verified sources, {full_text['abstract_only_not_used']} abstract-only sources quarantined from stronger use, {full_text['excluded_after_full_text']} exclusions after full-text review, and {full_text['inaccessible']} inaccessible sources. Search retrieval created a separate unresolved set of {inaccessible['records']} records without abstracts. These evidence problems remain separate and require separate ledgers.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--initialize", action="store_true", help="create the three v0.10 ledgers")
    parser.add_argument("--write-report", action="store_true", help="write the generated JSON and Markdown summaries")
    parser.add_argument("--check", action="store_true", help="verify committed ledgers and summaries")
    args = parser.parse_args()

    if args.initialize:
        initialize_ledgers()
    required = (
        FULL_TEXT_LEDGER,
        RETRIEVAL_LEDGER,
        RISK_SAMPLE,
        RISK_SAMPLE_SUMMARY,
        INTERFACE_LEDGER,
    )
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    if missing:
        raise SystemExit("next evidence gates: FAIL\nmissing ledgers: " + ", ".join(missing))

    errors, summary = inspect()
    expected_summary = json.dumps(summary, indent=2) + "\n"
    expected_report = report_text(summary)
    if args.write_report:
        SUMMARY.write_text(expected_summary, encoding="utf-8")
        REPORT.write_text(expected_report, encoding="utf-8")
    if args.check:
        if not SUMMARY.is_file() or SUMMARY.read_text(encoding="utf-8") != expected_summary:
            errors.append("next-evidence-gate JSON summary is missing or stale")
        if not REPORT.is_file() or REPORT.read_text(encoding="utf-8") != expected_report:
            errors.append("next-evidence-gate Markdown report is missing or stale")
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        print(f"next evidence gates: INVALID ({len(errors)} error(s))")
        return 1

    gate_data = summary["gates"]
    full_text = gate_data["close_source_full_text"]
    inaccessible = gate_data["inaccessible_record_retrieval"]
    print(
        "next evidence gates: OPEN "
        f"({full_text['verified']}/{full_text['records']} close sources full-text verified; "
        f"{inaccessible['retrieval_rows_complete']}/{inaccessible['records']} inaccessible records resolved)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
