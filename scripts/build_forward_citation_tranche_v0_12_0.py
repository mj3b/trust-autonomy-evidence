#!/usr/bin/env python3
"""Build the frozen 102-record forward-citation retrieval tranche."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
RISK_SAMPLE = ROOT / "paper/data/inaccessible-risk-sample-v0.11.0.csv"
PROPOSALS = ROOT / "paper/data/formal-screening-proposals-v0.7.0.json"
RETRIEVAL_LEDGER = ROOT / "paper/data/inaccessible-record-retrieval-v0.10.0.csv"
EVIDENCE = ROOT / "paper/data/forward-citation-retrieval-evidence-v0.12.0.json"
AUTHOR_QUEUE = ROOT / "paper/data/forward-citation-author-review-queue-v0.12.0.csv"

AUTHOR = "Mark Julius Banasihan"
RETRIEVAL_DATE = "2026-08-11"
AI_ASSISTANCE = (
    "AI assisted with identifier routing, publisher-page inspection, duplicate detection, "
    "and ledger assembly. No machine summary was used as source evidence."
)


DOI_FULL_TEXT = {
    "RS-FC-002", "RS-FC-004", "RS-FC-010", "RS-FC-015", "RS-FC-023",
    "RS-FC-024", "RS-FC-035", "RS-FC-037", "RS-FC-042", "RS-FC-047",
    "RS-FC-053", "RS-FC-060", "RS-FC-069", "RS-FC-070", "RS-FC-079",
    "RS-FC-088", "RS-FC-097", "RS-FC-098", "RS-FC-100",
}
DOI_METADATA_ONLY = {
    "RS-FC-001", "RS-FC-006", "RS-FC-013", "RS-FC-019", "RS-FC-025",
    "RS-FC-030", "RS-FC-032", "RS-FC-041", "RS-FC-044", "RS-FC-045",
    "RS-FC-056", "RS-FC-066", "RS-FC-067", "RS-FC-068", "RS-FC-074",
    "RS-FC-076", "RS-FC-081", "RS-FC-082", "RS-FC-084", "RS-FC-086",
    "RS-FC-089", "RS-FC-093", "RS-FC-095", "RS-FC-102",
}
DOI_DUPLICATES = {"RS-FC-003"}


TITLE_ROUTES = {
    "RS-FC-005": ("full-text-recovered", "https://pdfs.semanticscholar.org/5964/09d05f32a271dc12204f8ec9ae930eec9648.pdf", "A direct conference-paper PDF was readable."),
    "RS-FC-007": ("metadata-only", "https://scispace.com/papers/an-investigation-of-the-relationship-between-human-and-40snn62po3", "A bibliographic page was found, but no source abstract or full text was verified."),
    "RS-FC-012": ("full-text-recovered", "https://papers.ssrn.com/sol3/Delivery.cfm/5292184.pdf?abstractid=5292184&mirid=1", "The SSRN paper PDF was readable."),
    "RS-FC-016": ("duplicate", "https://link.springer.com/article/10.1007/s43681-023-00297-2", "The title resolves to the published PRAISE article already represented in the formal corpus."),
    "RS-FC-017": ("abstract-recovered", "https://researchdiscovery.drexel.edu/esploro/outputs/doctoral/Aviate-Navigate-Communicate-Silence-Voice-and/991014632338104721", "The university record exposed the dissertation abstract and a full-text link."),
    "RS-FC-022": ("full-text-recovered", "https://alaworkshop2023.github.io/papers/ALA2023_paper_56.pdf", "The workshop-paper PDF was readable."),
    "RS-FC-026": ("full-text-recovered", "https://etheses.bham.ac.uk/id/eprint/9085/7/Morar2019PhD_Redacted.pdf", "The university thesis PDF was readable."),
    "RS-FC-028": ("unavailable", "https://www.semanticscholar.org/paper/93dacf66b966feac3d9293c9050e60a6e9a93b24", "The indexed record did not yield a readable abstract or full text through the checked routes."),
    "RS-FC-031": ("abstract-recovered", "https://umu.diva-portal.org/smash/record.jsf?pid=diva2%3A1890832", "The university record exposed the thesis abstract and a full-text link."),
    "RS-FC-033": ("duplicate", "https://link.springer.com/article/10.1007/s43681-023-00297-2", "The argument-pattern title is another record for the published PRAISE article."),
    "RS-FC-039": ("full-text-recovered", "https://easychair.org/publications/preprint/H8sp/open", "The EasyChair preprint page exposed the paper text."),
    "RS-FC-054": ("abstract-recovered", "https://arxiv.org/abs/2306.00380", "The arXiv record exposed the author abstract and full-text link."),
    "RS-FC-058": ("abstract-recovered", "https://researchonline.lse.ac.uk/134229", "The university record exposed the dissertation abstract and file link."),
    "RS-FC-059": ("full-text-recovered", "https://roderic.uv.es/rest/api/core/bitstreams/b58c4a36-4007-4e74-b7cc-c0be02c3da82/content", "The institutional-repository PDF was readable."),
    "RS-FC-061": ("full-text-recovered", "https://repository.tudelft.nl/file/File_a30c8388-7bbc-45e3-bb15-56a93280d191?preview=1", "The TU Delft conference-paper PDF was readable."),
    "RS-FC-062": ("unavailable", "https://www.semanticscholar.org/paper/b01aaf20ce168b2d650f5a21f087895b9a30ce56", "The malformed title did not yield enough evidence to identify or screen the record."),
    "RS-FC-065": ("full-text-recovered", "https://etheses.whiterose.ac.uk/id/eprint/6765/1/589055.pdf", "The university dissertation PDF was readable."),
    "RS-FC-072": ("abstract-recovered", "https://www.lunduniversity.lu.se/lup/publication/4318225", "The university record exposed a substantive abstract and a PDF link."),
    "RS-FC-077": ("full-text-recovered", "https://pure.tudelft.nl/ws/portalfiles/portal/151937788/2023_ai_control_meta_values.pdf", "The institutional-repository chapter PDF was readable."),
    "RS-FC-083": ("full-text-recovered", "https://jyx.jyu.fi/bitstreams/34f414e4-f3ca-4834-958e-918d158628e7/download", "The university dissertation PDF was readable."),
    "RS-FC-085": ("full-text-recovered", "https://www.researchgate.net/publication/242120689_METHODOLOGICAL_FRAMEWORK_FOR_CONDUCTING_A_RISK_ASSESSMENT_STUDY", "The indexed full-text page exposed the article text."),
    "RS-FC-090": ("metadata-only", "https://dabar.srce.hr/books/pfst%3A2128/show-file/0", "The proceedings table of contents verified the paper title and page, but no paper text was isolated."),
    "RS-FC-091": ("abstract-recovered", "https://www.semanticscholar.org/paper/977bd3b13f3998bab099d84c22a173d6d2d9303b", "The indexed record exposed a substantive author abstract through a secondary route."),
    "RS-FC-092": ("full-text-recovered", "https://lup.lub.lu.se/record/8052270", "The university record exposed the thesis abstract and open manuscript."),
    "RS-FC-094": ("full-text-recovered", "https://www.sintef.no/globalassets/project/hfc/documents/finalmasteroppgave-27.11.pdf", "The thesis PDF was readable."),
    "RS-FC-099": ("full-text-recovered", "https://easychair.org/publications/preprint/njvZ/open", "The EasyChair preprint page exposed the paper text."),
    "RS-FC-101": ("full-text-recovered", "https://outdoorcouncil.asn.au/wp-content/uploads/2016/08/OAI_REPORT_FINAL_VERSION_OCT_15th_2009.pdf", "The research-report PDF was readable."),
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def doi_route(record: dict[str, str]) -> tuple[str, str, str]:
    sample_id = record["sample_id"]
    doi = record["record_key"].removeprefix("doi:")
    locator = f"https://doi.org/{doi}"
    if sample_id in DOI_DUPLICATES:
        return (
            "duplicate",
            "https://arxiv.org/abs/2203.15370",
            "This arXiv record is the preprint of the published PRAISE article already represented in the formal corpus.",
        )
    if sample_id in DOI_FULL_TEXT:
        return (
            "full-text-recovered",
            locator,
            "The DOI route exposed a complete publisher page or a readable full-text file.",
        )
    if sample_id in DOI_METADATA_ONLY:
        if sample_id == "RS-FC-066":
            observation = "The DOI resolved to a different title, so the source could not support the sampled record."
        elif sample_id == "RS-FC-086":
            observation = "The DOI route failed at the legacy publisher host and yielded no readable source content."
        else:
            observation = "The DOI resolved, but the checked publisher route exposed metadata, a purchase page, or an automated access check without readable source content."
        return "metadata-only", locator, observation
    return (
        "abstract-recovered",
        locator,
        "The DOI route exposed a readable publisher abstract. No proposition may exceed that abstract without a separate full-text check.",
    )


def main() -> int:
    risk_rows = [
        row for row in read_csv(RISK_SAMPLE)
        if row["primary_stratum"] == "forward-citation"
    ]
    if len(risk_rows) != 102:
        raise SystemExit(f"expected 102 forward-citation records; found {len(risk_rows)}")

    proposals = json.loads(PROPOSALS.read_text(encoding="utf-8"))
    proposal_by_key = {row["record_key"]: row for row in proposals["decisions"]}
    records: list[dict[str, object]] = []
    ledger_rows: list[dict[str, str]] = []
    queue_rows: list[dict[str, str]] = []

    for row in risk_rows:
        sample_id = row["sample_id"]
        if row["record_key"].startswith("doi:"):
            outcome, locator, observation = doi_route(row)
            checked = [f"https://doi.org/{row['record_key'].removeprefix('doi:')}", "publisher or repository landing page"]
        else:
            if sample_id not in TITLE_ROUTES:
                raise SystemExit(f"missing title route for {sample_id}")
            outcome, locator, observation = TITLE_ROUTES[sample_id]
            paper_id = proposal_by_key[row["record_key"]]["paper_id"]
            checked = [f"https://www.semanticscholar.org/paper/{paper_id}", locator]

        review_basis = {
            "full-text-recovered": "full_text_route",
            "abstract-recovered": "title_and_abstract",
            "metadata-only": "metadata_only",
            "duplicate": "identifier_and_version_match",
            "unavailable": "insufficient_source_content",
        }[outcome]
        author_note = (
            "OPEN: source content recovered; Mark Julius Banasihan must record the screening decision."
            if outcome in {"abstract-recovered", "full-text-recovered"}
            else observation
        )
        evidence_record: dict[str, object] = {
            "sample_id": sample_id,
            "record_key": row["record_key"],
            "title": row["title"],
            "year": row["year"],
            "retrieval_outcome": outcome,
            "retrieval_locator": locator,
            "retrieval_date": RETRIEVAL_DATE,
            "routes_checked": checked,
            "source_evidence": [observation],
            "review_basis": review_basis,
            "screening_decision": None,
            "screening_rationale": author_note,
            "decision_owner": AUTHOR,
            "ai_assistance": AI_ASSISTANCE,
            "claim_limit": (
                "No paper claim until author screening is recorded."
                if outcome in {"abstract-recovered", "full-text-recovered"}
                else "No substantive paper claim from this record."
            ),
        }
        records.append(evidence_record)
        ledger_rows.append(
            {
                "record_key": row["record_key"],
                "retrieval_outcome": outcome,
                "retrieval_locator": locator,
                "retrieval_date": RETRIEVAL_DATE,
                "screening_decision": "",
                "author_notes": author_note,
                "decision_owner": AUTHOR,
                "ai_assistance": AI_ASSISTANCE,
            }
        )
        if outcome in {"abstract-recovered", "full-text-recovered"}:
            queue_rows.append(
                {
                    "sample_id": sample_id,
                    "record_key": row["record_key"],
                    "title": row["title"],
                    "year": row["year"],
                    "retrieval_outcome": outcome,
                    "source_locator": locator,
                    "review_basis_available": review_basis,
                    "author_decision": "",
                    "author_rationale": "",
                    "decision_owner": AUTHOR,
                    "decision_status": "pending-author-review",
                    "claim_permission": "none-until-decision",
                }
            )

    outcomes = Counter(record["retrieval_outcome"] for record in records)
    evidence = {
        "version": "0.12.0",
        "status": "RETRIEVAL_COMPLETE_SCREENING_OPEN",
        "frozen_source": "paper/data/inaccessible-risk-sample-v0.11.0.csv",
        "stratum": "forward-citation",
        "decision_owner": AUTHOR,
        "method_limits": [
            "Publisher access checks and identifier routes do not establish source truth.",
            "Recovered abstracts support screening and bounded source descriptions only.",
            "Recovered full text supports no manuscript claim until author screening and proposition-level support review are recorded.",
            "Metadata-only and unavailable records remain coverage limits, not topic exclusions.",
            "This sampled tranche cannot establish exhaustive coverage, prevalence, originality, reliability, or field validity.",
        ],
        "counts": {
            "selected": len(records),
            "retrieval_complete": len(records),
            "screening_required": len(queue_rows),
            "screening_complete": 0,
            "screening_open": len(queue_rows),
            "outcomes": dict(sorted(outcomes.items())),
        },
        "records": records,
    }
    EVIDENCE.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")

    existing = read_csv(RETRIEVAL_LEDGER)
    forward_keys = {row["record_key"] for row in risk_rows}
    existing = [row for row in existing if row["record_key"] not in forward_keys]
    ledger_fields = [
        "record_key", "retrieval_outcome", "retrieval_locator", "retrieval_date",
        "screening_decision", "author_notes", "decision_owner", "ai_assistance",
    ]
    write_csv(RETRIEVAL_LEDGER, ledger_fields, existing + ledger_rows)
    write_csv(
        AUTHOR_QUEUE,
        [
            "sample_id", "record_key", "title", "year", "retrieval_outcome",
            "source_locator", "review_basis_available", "author_decision",
            "author_rationale", "decision_owner", "decision_status", "claim_permission",
        ],
        queue_rows,
    )
    print(
        "forward-citation tranche: "
        f"{len(records)} retrieval outcomes; {len(queue_rows)} author decisions open; "
        f"outcomes={dict(sorted(outcomes.items()))}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
