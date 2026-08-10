#!/usr/bin/env python3
"""Create preliminary, auditable screening proposals for the v0.7.0 search.

The output is a machine aid. Mark Julius Banasihan remains responsible for
confirming every retained source and every exclusion used in a contribution
claim.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any


CUTOFF = date.fromisoformat("2026-08-09")

# These records were already admitted to the working literature matrix before
# the formal search. Their presence in the retrieved set is recorded as
# background retention, not as a new screening decision.
EXISTING_DOIS = {
    "10.3389/frobt.2018.00015",
    "10.1007/s43681-022-00167-3",
    "10.3389/fdata.2022.1017677",
    "10.1007/s11948-025-00554-z",
    "10.1007/s43681-024-00489-4",
    "10.1007/s43681-026-01147-7",
    "10.1016/0005-1098(83)90046-8",
    "10.1518/hfes.46.1.50_30392",
    "10.1177/0018720816681350",
    "10.1016/j.clsr.2022.105681",
    "10.1093/jopart/muac007",
    "10.1609/aies.v8i1.36596",
    "10.1609/aaai.v39i28.35163",
    "10.1007/s43681-022-00178-0",
    "10.1016/j.ress.2025.111311",
    "10.1016/s0022-4375(02)00032-4",
    "10.1111/risa.13850",
    "10.1609/aaai.v40i44.41139",
    "10.1145/3774905.3795469",
    "10.1609/aaai.v35i17.17817",
    "10.1007/s11023-024-09701-0",
    "10.1007/978-3-032-07132-3_11",
    "10.1145/3630106.3658957",
}
EXISTING_ARXIV = {"2605.26340", "2605.16278", "2606.03777"}

# Close records were checked against an official publisher, proceedings, or
# institutional source after retrieval. The stated reasons remain bounded to
# the source's declared construct or method.
CLOSE_RECORDS = {
    "10.1007/s11023-020-09532-9": "joins technical, sociotechnical, and governance control layers",
    "10.1145/3322640.3326699": "connects human intervention to information and contestability",
    "10.1109/tase.2020.2965466": "quantifies causal responsibility under human-automation function allocation",
    "10.1017/s0963180122000718": "tests a design intervention intended to support effective oversight",
    "10.1007/s00146-025-02401-y": "treats human learning as a condition for stable and adaptive control",
    "10.4230/dagrep.15.6.189": "synthesizes epistemic access, causal power, intention, and organizational conditions",
    "10.1145/3630106.3659051": "defines effective oversight through causal power, epistemic access, self-control, and fitting intentions",
    "10.1145/3805689.3812402": "reports developer oversight work, constraints, and heuristics for software agents",
    "10.48550/arxiv.2603.19213": "separates constitutive and corrective runtime involvement",
    "10.1007/s00146-023-01777-z": "develops institutional design principles around the fallibility of overseers",
    "10.3390/info17070694": "joins selective human review with structured case-level audit records",
    "10.1109/facct71761.2026.00009": "formalizes evidence-linked claims and machine-checkable argument validation",
}

CONTROL_TERMS = {
    "human oversight",
    "human control",
    "meaningful human control",
    "effective oversight",
    "practical control",
    "human intervention",
    "human authority",
    "contestability",
}
EVIDENCE_TERMS = {
    "incident",
    "reconstruction",
    "evidence",
    "provenance",
    "audit",
    "assurance",
    "traceability",
    "traceable",
    "recordkeeping",
    "missingness",
    "indeterminate",
    "chain of custody",
}


def norm(value: str | None) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", (value or "").lower())).strip()


def doi_of(record: dict[str, Any]) -> str:
    return str((record.get("externalIds") or {}).get("DOI") or "").lower()


def arxiv_of(record: dict[str, Any]) -> str:
    return str((record.get("externalIds") or {}).get("ArXiv") or "").lower()


def record_key(record: dict[str, Any]) -> str:
    doi = doi_of(record)
    if doi:
        return f"doi:{doi}"
    return f"title:{norm(record.get('title'))}|year:{record.get('year') or ''}"


def build_origins(payload: dict[str, Any]) -> dict[str, set[str]]:
    origins: dict[str, set[str]] = defaultdict(set)
    for query_id, run in payload["search_runs"].items():
        for record in run["records"]:
            origins[record_key(record)].add(f"query:{query_id}")
    for seed_id, chain in payload["citation_chains"].items():
        for record in chain["references"]:
            origins[record_key(record)].add(f"reference:{seed_id}")
        for record in chain["citations"]:
            origins[record_key(record)].add(f"citation:{seed_id}")
    return origins


def after_cutoff(record: dict[str, Any]) -> bool:
    publication_date = record.get("publicationDate")
    if publication_date:
        try:
            return date.fromisoformat(publication_date) > CUTOFF
        except ValueError:
            pass
    return bool(record.get("year") and int(record["year"]) > CUTOFF.year)


def term_hits(text: str, terms: set[str]) -> list[str]:
    normalized = norm(text)
    return sorted(term for term in terms if norm(term) in normalized)


def propose(record: dict[str, Any]) -> tuple[str, str]:
    doi = doi_of(record)
    arxiv = arxiv_of(record)
    if after_cutoff(record):
        return "exclude-outside-cutoff", "indexed publication date falls after 9 August 2026"
    if doi in CLOSE_RECORDS:
        return "retain-close", CLOSE_RECORDS[doi]
    if doi in EXISTING_DOIS or arxiv in EXISTING_ARXIV:
        return "retain-background", "already admitted to the pre-search literature matrix"

    title = record.get("title") or ""
    abstract = record.get("abstract") or ""
    if not abstract.strip():
        return "inaccessible", "metadata lacks an abstract; substantive relevance is unresolved"

    text = f"{title} {abstract}"
    control = term_hits(text, CONTROL_TERMS)
    evidence = term_hits(text, EVIDENCE_TERMS)
    if control and evidence:
        return (
            "exclude-single-component",
            f"term overlap requires author check; control={control[:3]}, evidence={evidence[:3]}",
        )
    return "exclude-topic", "title and abstract do not join a human-control construct to an evidence procedure"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path("paper/data/formal-search-v0.7.0.json"))
    parser.add_argument("--json-output", type=Path, default=Path("paper/data/formal-screening-proposals-v0.7.0.json"))
    parser.add_argument("--report-output", type=Path, default=Path("paper/formal-search-screening-v0.7.0.md"))
    parser.add_argument("--queue-output", type=Path, default=Path("paper/data/author-screening-queue-v0.7.0.csv"))
    args = parser.parse_args()

    payload = json.loads(args.input.read_text(encoding="utf-8"))
    origins = build_origins(payload)
    decisions = []
    for record in payload["deduplicated_records"]:
        decision, reason = propose(record)
        decisions.append(
            {
                "record_key": record_key(record),
                "paper_id": record.get("paperId"),
                "doi": doi_of(record) or None,
                "arxiv": arxiv_of(record) or None,
                "title": record.get("title"),
                "year": record.get("year"),
                "venue": record.get("venue"),
                "origins": sorted(origins.get(record_key(record), set())),
                "proposed_decision": decision,
                "proposal_reason": reason,
                "decision_status": "ai-assisted preliminary",
                "author_confirmation_required": True,
            }
        )

    counts = Counter(item["proposed_decision"] for item in decisions)
    output = {
        "schema_version": "1.0",
        "protocol": "paper/formal-literature-search-protocol-v0.7.0.md",
        "source_record": str(args.input),
        "publication_cutoff": CUTOFF.isoformat(),
        "decision_status": "ai-assisted preliminary",
        "author_confirmation_required": True,
        "record_count": len(decisions),
        "counts": dict(sorted(counts.items())),
        "decisions": decisions,
    }
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    retained = [item for item in decisions if item["proposed_decision"].startswith("retain-")]
    lines = [
        "# Formal Search Screening Proposals, v0.7.0",
        "",
        "**Author and decision owner:** Mark Julius Banasihan",
        "",
        "**Status:** AI-assisted preliminary proposals; author confirmation required",
        "",
        f"**Retrieved records:** {len(decisions):,} deduplicated records",
        "",
        f"**Publication cutoff:** {CUTOFF.isoformat()}",
        "",
        "## Interpretation rule",
        "",
        "This file records triage proposals. It does not claim that the author read 2,431 full texts or approved every exclusion. A retained source may enter a manuscript claim only after its cited proposition is checked against an abstract, full text, publisher record, proceedings record, or institutional copy. Exclusion proposals remain reversible.",
        "",
        "## Proposal counts",
        "",
        "| Proposed decision | Records |",
        "|---|---:|",
    ]
    lines.extend(f"| `{key}` | {counts[key]:,} |" for key in sorted(counts))
    lines.extend([
        "",
        "## Proposed retained set",
        "",
        "| Decision | Source | Year | Retrieval origin | Reason |",
        "|---|---|---:|---|---|",
    ])
    for item in sorted(retained, key=lambda x: (x["proposed_decision"], x["year"] or 0, x["title"] or "")):
        locator = f"https://doi.org/{item['doi']}" if item["doi"] else f"https://arxiv.org/abs/{item['arxiv']}" if item["arxiv"] else ""
        source = f"[{item['title']}]({locator})" if locator else item["title"]
        origins_text = ", ".join(item["origins"]) or "deduplicated pool"
        reason = str(item["proposal_reason"]).replace("|", "/")
        lines.append(f"| `{item['proposed_decision']}` | {source} | {item['year'] or ''} | {origins_text} | {reason} |")
    lines.extend([
        "",
        "## Decision gate",
        "",
        "The machine proposals can prioritize close records and expose records that lack abstracts. They cannot close the contribution decision. Mark Julius Banasihan must confirm the retained close set, inspect any exclusion that could change the paper's contribution boundary, and approve the final wording in the manuscript and novelty audit.",
        "",
        "The [author-screening queue](data/author-screening-queue-v0.7.0.csv) isolates the 12 close-source proposals and 77 attention records. Its author-decision fields remain blank until Mark Julius Banasihan completes that review.",
        "",
    ])
    args.report_output.write_text("\n".join(lines), encoding="utf-8")

    author_queue = [
        item
        for item in decisions
        if item["proposed_decision"] in {"retain-close", "exclude-single-component"}
    ]
    args.queue_output.parent.mkdir(parents=True, exist_ok=True)
    with args.queue_output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=(
                "record_key",
                "proposed_decision",
                "author_decision",
                "author_notes",
                "title",
                "year",
                "doi",
                "arxiv",
                "venue",
                "origins",
                "proposal_reason",
            ),
            lineterminator="\n",
        )
        writer.writeheader()
        for item in sorted(author_queue, key=lambda row: (row["proposed_decision"], row["year"] or 0, row["title"] or "")):
            writer.writerow(
                {
                    "record_key": item["record_key"],
                    "proposed_decision": item["proposed_decision"],
                    "author_decision": "",
                    "author_notes": "",
                    "title": item["title"],
                    "year": item["year"],
                    "doi": item["doi"],
                    "arxiv": item["arxiv"],
                    "venue": item["venue"],
                    "origins": "; ".join(item["origins"]),
                    "proposal_reason": item["proposal_reason"],
                }
            )
    print(json.dumps({"records": len(decisions), "counts": dict(sorted(counts.items())), "retained": len(retained)}, indent=2))


if __name__ == "__main__":
    main()
