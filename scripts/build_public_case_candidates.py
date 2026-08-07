#!/usr/bin/env python3
"""Build the frozen public-case candidate search output.

The script reads the AI Incident Database weekly archive without extracting it and
reads OECD AIM exports from their Open XML workbook representation. It writes
metadata and report citations, never full article text.
"""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import io
import json
import re
import tarfile
import zipfile
from datetime import date
from pathlib import Path
from xml.etree import ElementTree


VERSION = "0.3.0"
EVIDENCE_CUTOFF = date.fromisoformat("2026-08-06")
TERMS = (
    "agent",
    "autonomous",
    "assistant",
    "copilot",
    "chatbot",
    "tool use",
    "computer use",
    "browser",
    "operator",
    "automated decision",
    "automated action",
    "human review",
    "human oversight",
    "override",
    "intervention",
    "appeal",
    "rollback",
    "incident response",
)
TOKEN_PATTERNS = {
    term: re.compile(r"(?<!\w)" + re.escape(term.casefold()) + r"(?!\w)")
    for term in TERMS
}
AIID_INCIDENTS = "mongodump_full_snapshot/incidents.csv"
AIID_REPORTS = "mongodump_full_snapshot/reports.csv"
SHEET_NS = {"x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_date(value: str) -> date | None:
    if not value:
        return None
    try:
        return date.fromisoformat(value[:10])
    except ValueError:
        return None


def matched_terms(text: str) -> list[str]:
    folded = text.casefold()
    return [term for term, pattern in TOKEN_PATTERNS.items() if pattern.search(folded)]


def read_csv_member(archive: tarfile.TarFile, name: str) -> list[dict[str, str]]:
    raw = archive.extractfile(name)
    if raw is None:
        raise ValueError(f"archive member is missing: {name}")
    with io.TextIOWrapper(raw, encoding="utf-8-sig", newline="") as text:
        return list(csv.DictReader(text))


def build_aiid_candidates(path: Path) -> tuple[dict[str, int], list[dict[str, object]]]:
    with tarfile.open(path, "r:bz2") as archive:
        reports = read_csv_member(archive, AIID_REPORTS)
        incidents = read_csv_member(archive, AIID_INCIDENTS)

    reports_by_number = {
        int(row["report_number"]): row
        for row in reports
        if row.get("report_number", "").isdigit()
    }
    candidates: list[dict[str, object]] = []
    included_report_count = 0
    excluded_undated_report_count = 0
    excluded_post_cutoff_report_count = 0

    for incident in incidents:
        event_date = parse_date(incident["date"])
        if event_date is None or event_date > EVIDENCE_CUTOFF:
            continue

        report_numbers = ast.literal_eval(incident["reports"])
        eligible_reports: list[dict[str, str]] = []
        for report_number in report_numbers:
            report = reports_by_number.get(report_number)
            if report is None:
                continue
            publication_date = parse_date(report["date_published"])
            if publication_date is None:
                excluded_undated_report_count += 1
                continue
            if publication_date > EVIDENCE_CUTOFF:
                excluded_post_cutoff_report_count += 1
                continue
            eligible_reports.append(report)

        searchable = "\n".join(
            [incident["title"], incident["description"]]
            + [
                "\n".join((row["title"], row["description"], row["text"]))
                for row in eligible_reports
            ]
        )
        terms = matched_terms(searchable)
        if not terms:
            continue

        included_report_count += len(eligible_reports)
        candidates.append(
            {
                "candidate_id": f"AIID-{incident['incident_id']}",
                "collection": "AI Incident Database",
                "collection_id": int(incident["incident_id"]),
                "event_date": incident["date"],
                "title": incident["title"],
                "summary": incident["description"],
                "matched_terms": terms,
                "eligible_report_count": len(eligible_reports),
                "reports": [
                    {
                        "report_number": int(row["report_number"]),
                        "title": row["title"],
                        "publisher_domain": row["source_domain"],
                        "publication_date": row["date_published"][:10],
                        "url": row["url"],
                    }
                    for row in eligible_reports
                ],
            }
        )

    counts = {
        "incident_records": len(incidents),
        "report_records": len(reports),
        "candidate_records": len(candidates),
        "eligible_report_references_in_candidates": included_report_count,
        "undated_report_references_excluded": excluded_undated_report_count,
        "post_cutoff_report_references_excluded": excluded_post_cutoff_report_count,
    }
    return counts, candidates


def cell_value(cell: ElementTree.Element) -> str:
    return "".join(node.text or "" for node in cell.findall(".//x:t", SHEET_NS))


def read_oecd_export(path: Path) -> list[dict[str, str]]:
    with zipfile.ZipFile(path) as workbook:
        root = ElementTree.fromstring(workbook.read("xl/worksheets/sheet1.xml"))

    rows: list[list[str]] = []
    for row in root.findall(".//x:sheetData/x:row", SHEET_NS):
        values = [cell_value(cell) for cell in row.findall("x:c", SHEET_NS)]
        rows.append(values)
    if not rows:
        return []

    headers = rows[0]
    return [dict(zip(headers, row, strict=False)) for row in rows[1:]]


def build_oecd_candidates(paths: list[Path]) -> tuple[dict[str, int], list[dict[str, object]]]:
    exported: dict[str, dict[str, str]] = {}
    for path in paths:
        for row in read_oecd_export(path):
            exported[row["id"]] = row

    candidates: list[dict[str, object]] = []
    for row in exported.values():
        event_date = parse_date(row.get("date", ""))
        if event_date is None or event_date > EVIDENCE_CUTOFF:
            continue
        visible_terms = matched_terms("\n".join((row.get("title", ""), row.get("summary", ""))))
        candidates.append(
            {
                "candidate_id": f"OECD-{row['id']}",
                "collection": "OECD AI Incidents and Hazards Monitor",
                "collection_id": row["id"],
                "event_date": row["date"],
                "title": row["title"],
                "summary": row["summary"],
                "matched_terms_visible_in_export": visible_terms,
                "query_match": "provider search across the frozen OR vocabulary",
                "concepts": row.get("concepts", ""),
                "companies": row.get("companies", ""),
                "country": row.get("country", ""),
            }
        )

    return {"exported_unique_records": len(exported), "candidate_records": len(candidates)}, candidates


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--aiid-archive", type=Path, required=True)
    parser.add_argument("--oecd-export", type=Path, action="append", default=[])
    parser.add_argument("--retrieval-date", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    aiid_counts, aiid_candidates = build_aiid_candidates(args.aiid_archive)
    oecd_counts, oecd_candidates = build_oecd_candidates(args.oecd_export)
    candidates = aiid_candidates + oecd_candidates
    candidates.sort(key=lambda row: (row["event_date"], row["candidate_id"]))

    result = {
        "version": VERSION,
        "retrieval_date": args.retrieval_date,
        "evidence_cutoff": EVIDENCE_CUTOFF.isoformat(),
        "matching_rule": "Unicode casefold with whole-token or whole-phrase boundaries",
        "fixed_search_vocabulary": list(TERMS),
        "inputs": {
            "aiid": {
                "file": args.aiid_archive.name,
                "sha256": sha256(args.aiid_archive),
                "counts": aiid_counts,
            },
            "oecd": [
                {"file": path.name, "sha256": sha256(path)} for path in args.oecd_export
            ],
            "oecd_counts": oecd_counts,
        },
        "limitations": [
            "AIID report text is used for matching but is omitted from this output to avoid redistributing articles.",
            "AIID reports without a usable publication date are excluded from report-text matching.",
            "The OECD interface exports only the visible result page. The included workbook is the 100-row page produced by the frozen OR query.",
            "OECD article text is absent from the workbook, so visible-term matches can be fewer than provider-query matches.",
        ],
        "candidate_count": len(candidates),
        "candidates": candidates,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {len(candidates)} candidates to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
