#!/usr/bin/env python3
"""Build the v0.13.0 forward-citation author-screening evidence set."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "paper/data/forward-citation-author-review-queue-v0.12.0.csv"
DECISIONS = ROOT / "paper/data/forward-citation-author-screening-decisions-v0.13.0.csv"
SUMMARY = ROOT / "paper/data/forward-citation-author-screening-v0.13.0.json"
REPORT = ROOT / "paper/forward-citation-author-screening-v0.13.0.md"
ATTESTATION = ROOT / "evidence/human-review-attestation-v0.13.0.json"
POPULATION_LEDGER = ROOT / "paper/data/inaccessible-record-retrieval-v0.10.0.csv"

EXPECTED_QUEUE_SHA256 = "6626338915c50da8e58e1487d3ef5f523a89421f0b21ae7f16f42b71140817e9"
AUTHOR = "Mark Julius Banasihan"
DECISION_DATE = "2026-08-11"
ASSISTANCE = (
    "AI-assisted source-content inspection and screening under author authorization; "
    "Mark Julius Banasihan retains decision accountability."
)


# Decisions are bounded to corpus membership. They do not grant proposition support.
# Each note names the source mechanism that controls the screening decision.
DECISION_DATA: dict[str, tuple[str, str, str]] = {
    "RS-FC-002": (
        "exclude-single-component",
        "The guide organizes data-justice duties across a policy lifecycle, but it does not assess practical human control, incident reconstruction, or claim-level evidence adjudication.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-004": (
        "retain-background",
        "The correction and linked original article map responsibility-gap positions for lethal autonomous weapons; the record informs responsibility attribution but supplies no practical-control evidence test.",
        "correction_notice_and_original_article",
    ),
    "RS-FC-005": (
        "retain-close",
        "The paper applies AcciMap, Cognitive Work Analysis, and STAMP to a bounded road-rail crash, directly supplying a comparative public-incident reconstruction method.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-008": (
        "retain-background",
        "The study examines consequences of assigning legal responsibility to the wrong actor in automated-vehicle use, informing the paper's distinction between named responsibility and demonstrated control.",
        "title_and_abstract",
    ),
    "RS-FC-009": (
        "exclude-topic",
        "The article develops a healthcare-improvement evaluation scale and does not assess human control over automation, incident evidence, or the paper's reconstruction procedure.",
        "title_and_abstract",
    ),
    "RS-FC-010": (
        "exclude-topic",
        "The paper studies emergent agent communities for educational partnership rather than human authority, intervention effectiveness, or incident evidence.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-011": (
        "exclude-topic",
        "The value-sensitive design study concerns a mental-health quality-of-life instrument and supplies no automation-control or incident-reconstruction mechanism.",
        "title_and_abstract",
    ),
    "RS-FC-012": (
        "retain-background",
        "The proposed Ultimate AI Accountability Owner assigns final institutional responsibility across the AI lifecycle, providing a formal-authority comparison without testing whether that owner can intervene effectively.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-014": (
        "retain-background",
        "The embedded health-AI study shifts lifecycle analysis toward decision-shaping events and value conflicts, offering a governance-process mechanism without a practical-control chain.",
        "title_and_abstract",
    ),
    "RS-FC-015": (
        "exclude-topic",
        "The article distinguishes robots from AI as moral categories and does not test oversight capacity, incident evidence, or reconstruction decisions.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-017": (
        "retain-background",
        "The aviation dissertation links communication, comprehension, silence, and situation awareness under time pressure, supplying mechanisms for the information and comprehension stages of practical control.",
        "title_and_abstract",
    ),
    "RS-FC-018": (
        "exclude-topic",
        "The study concerns AI curriculum design for media education and supplies no human-control or incident-evidence mechanism.",
        "title_and_abstract",
    ),
    "RS-FC-020": (
        "retain-close",
        "The article develops a core-task accident-analysis method and applies case-by-case, comparative, and synthesis stages to official maritime investigations, directly addressing incident reconstruction.",
        "title_and_abstract",
    ),
    "RS-FC-021": (
        "exclude-single-component",
        "The survey describes judges' views of AI-assisted adjudication, but it does not establish an intervention chain or a source-adjudication method.",
        "title_and_abstract",
    ),
    "RS-FC-022": (
        "exclude-single-component",
        "The reinforcement-learning framework models complex human-AI interaction without testing formal authority, practical intervention, or public-incident evidence.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-023": (
        "exclude-topic",
        "The article critiques the concept of the human across AI and environmental ethics and does not assess practical control or incident reconstruction.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-024": (
        "exclude-topic",
        "The article maps broad ethical issues in AI and work without a specific control, evidence, or incident-analysis mechanism for this paper.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-026": (
        "retain-background",
        "The thesis studies how display content, format, and form affect detection and response under unreliable automation, informing information access, comprehension, and opportunity to intervene.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-027": (
        "exclude-topic",
        "The article proposes an ontology of AI fairness rather than evaluating human control, incident reconstruction, or evidence traceability.",
        "title_and_abstract",
    ),
    "RS-FC-029": (
        "retain-background",
        "The assessment addresses organizational safety culture, a condition that can shape reporting and challenge behavior, without supplying the paper's incident-control procedure.",
        "title_and_abstract",
    ),
    "RS-FC-031": (
        "retain-background",
        "The government-agency design study reports user needs for understandable explanations, workflow-specific information, and preserved human judgment, informing comprehension and control conditions.",
        "title_and_abstract",
    ),
    "RS-FC-034": (
        "exclude-single-component",
        "The chapter applies resilience concepts to human-robot interaction but does not reconstruct practical control or adjudicate public evidence.",
        "title_and_abstract",
    ),
    "RS-FC-035": (
        "exclude-topic",
        "The IT-design paper concerns meaning innovation, transparency, and sustainability without a practical-control or incident-evidence assessment.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-036": (
        "retain-close",
        "The paper applies and evaluates a systems accident-analysis framework in a bounded safety domain, directly informing the reconstruction method and system-level causal scope.",
        "title_and_abstract",
    ),
    "RS-FC-037": (
        "retain-background",
        "The review describes incident-reporting, event handling, root-cause analysis, feedback, and shared learning systems, supplying an institutional evidence-preservation comparison.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-038": (
        "exclude-topic",
        "The article reframes deception in human-centered AI and does not assess intervention capacity or public-incident evidence.",
        "title_and_abstract",
    ),
    "RS-FC-039": (
        "exclude-topic",
        "The preprint concerns combining big data and AI for decision support rather than human-control evidence or incident reconstruction.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-040": (
        "exclude-single-component",
        "The study examines perceptions of machine moral judgments, which informs attribution attitudes but does not test actual authority or intervention effects.",
        "title_and_abstract",
    ),
    "RS-FC-042": (
        "retain-close",
        "The study compares meaningful-human-control tracking conditions with Tesla users' reported safety and trust, directly testing a practical-control concept against user evidence.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-043": (
        "exclude-topic",
        "The article offers broad cyberspace-governance recommendations without a specific practical-control chain or incident-evidence procedure.",
        "title_and_abstract",
    ),
    "RS-FC-046": (
        "exclude-topic",
        "The article concerns optimization and human meaning in a post-AI society, not operational human control or incident reconstruction.",
        "title_and_abstract",
    ),
    "RS-FC-047": (
        "retain-close",
        "The article distinguishes control gaps within distributed healthcare AI responsibility, directly addressing when multiple accountable actors do not amount to effective control.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-048": (
        "exclude-single-component",
        "The transportation study links safety culture to passenger injury prevention but does not assess automation intervention or evidence adjudication.",
        "title_and_abstract",
    ),
    "RS-FC-049": (
        "exclude-single-component",
        "The construction study examines firm size, injury risk, and reporting behavior; reporting is relevant to missingness, but the source does not test the paper's control mechanism.",
        "title_and_abstract",
    ),
    "RS-FC-050": (
        "retain-background",
        "The review considers autonomy, surgeon roles, and responsibility in robotic surgery, providing a high-stakes domain comparison without a control-chain assessment.",
        "title_and_abstract",
    ),
    "RS-FC-051": (
        "retain-close",
        "The framework treats users as principals who delegate agency and maps incidents to competencies, autonomy, and meaningful control, directly addressing whether oversight roles are exercisable.",
        "title_and_abstract",
    ),
    "RS-FC-052": (
        "retain-close",
        "The study compares direct manipulation and text guidance for intervening in autonomous task execution, directly examining practical oversight modalities and error correction.",
        "title_and_abstract",
    ),
    "RS-FC-053": (
        "exclude-topic",
        "The article provides a multilevel analysis of digital vulnerability without a bounded human-control or incident-evidence procedure.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-054": (
        "retain-background",
        "The trustworthy-AI survey supplies a taxonomy of strategic decisions and governance concerns but does not test practical human control or case reconstruction.",
        "title_and_abstract",
    ),
    "RS-FC-055": (
        "exclude-topic",
        "The surgical-robotics reference entry concerns the clinical technology and does not supply a control or evidence-assessment mechanism.",
        "title_and_abstract",
    ),
    "RS-FC-057": (
        "retain-background",
        "The chapter organizes ethical perspectives on automated vehicles, including responsibility and control questions, without the paper's evidence-state procedure.",
        "title_and_abstract",
    ),
    "RS-FC-058": (
        "exclude-topic",
        "The dissertation evaluates child-protection reform and does not address automated control or incident reconstruction.",
        "title_and_abstract",
    ),
    "RS-FC-059": (
        "exclude-topic",
        "The occupational-safety psychology work concerns workplace risk prevention without an automation-control or public-evidence mechanism.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-060": (
        "retain-close",
        "The paper formalizes dynamic allocation and reallocation of morally significant tasks in human-agent teams, directly addressing how control can move between actors.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-061": (
        "retain-close",
        "The paper models transitions of human control across automation levels and identifies out-of-the-loop and behavioral-adaptation risks, directly addressing practical control over time.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-063": (
        "retain-background",
        "The empirical design study lets nontechnical users shape early machine-learning design, informing upstream user control without testing runtime intervention or incident evidence.",
        "title_and_abstract",
    ),
    "RS-FC-064": (
        "retain-background",
        "The article analyzes dignity, conflict, and responsibility arguments about autonomous weapons, informing responsibility boundaries without a practical-control test.",
        "title_and_abstract",
    ),
    "RS-FC-065": (
        "exclude-topic",
        "The dissertation studies driver attitudes and aberrant road behavior and does not assess human control over automation or incident evidence.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-069": (
        "retain-background",
        "The case study applies structured absolute-probability judgment to human reliability, offering an assessor-method comparison without a practical-control chain.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-070": (
        "retain-close",
        "The article uses principal-agent theory and agency law to analyze delegated authority, information asymmetry, monitoring, and enforcement limits for AI agents, directly addressing practical governance control.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-071": (
        "exclude-topic",
        "The traffic study predicts accidents from driver celeration behavior and supplies no automation-control or evidence-adjudication procedure.",
        "title_and_abstract",
    ),
    "RS-FC-072": (
        "retain-background",
        "The nursing case study examines how conceptions of human error shape incident reporting, informing evidence availability and blame-sensitive reporting behavior.",
        "title_and_abstract",
    ),
    "RS-FC-073": (
        "retain-background",
        "The review maps driver-distraction methods and mechanisms, supplying human-factors context for attention and opportunity without a practical-control assessment.",
        "title_and_abstract",
    ),
    "RS-FC-075": (
        "exclude-topic",
        "The article evaluates child-protection partnerships through a systems approach and does not address automated control or incident evidence.",
        "title_and_abstract",
    ),
    "RS-FC-077": (
        "retain-background",
        "The chapter examines AI control and unintended consequences through meta-values, supplying normative control context without an operational evidence chain.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-078": (
        "exclude-single-component",
        "The study measures preference under trust conflict and algorithm aversion; perceived preference does not establish actual intervention capacity or effect.",
        "title_and_abstract",
    ),
    "RS-FC-079": (
        "exclude-topic",
        "The article develops a causation account for construction rework and does not assess human control over automation or source traceability.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-080": (
        "retain-close",
        "The article connects responsible algorithmic-decision design to ethical judgment and meaningful human control, directly addressing conditions for human agency in automated decisions.",
        "title_and_abstract",
    ),
    "RS-FC-083": (
        "exclude-single-component",
        "The dissertation develops driver-distraction theory around capacity and workload but does not assess formal authority, intervention effect, or incident evidence.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-085": (
        "exclude-single-component",
        "The article supplies a general risk-assessment method without the paper's human-control stages, public-case selection, or evidence-state rules.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-087": (
        "exclude-topic",
        "The study examines employee safety and quality decisions in grain elevators and does not assess automated control or incident reconstruction.",
        "title_and_abstract",
    ),
    "RS-FC-088": (
        "exclude-topic",
        "The legal article examines Italian judgments after adoption of the EU AI Act and supplies no practical-control or incident-evidence assessment.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-091": (
        "retain-background",
        "The human-AI interaction paper maps design challenges for human-centered AI, supplying interface and collaboration context without a reconstructed control chain.",
        "title_and_abstract",
    ),
    "RS-FC-092": (
        "exclude-single-component",
        "The bridge-design thesis treats accidental-hazard risk controls but does not assess human authority over automation or public-incident evidence.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-094": (
        "retain-background",
        "The thesis characterizes critical incidents in dynamic positioning, offering an operational human-system incident comparison without the paper's evidence-state procedure.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-096": (
        "retain-close",
        "The article applies HFACS, AcciMap, and STAMP to the same bounded port disaster, directly supporting comparison of incident-reconstruction methods and system boundaries.",
        "title_and_abstract",
    ),
    "RS-FC-097": (
        "retain-close",
        "The article transfers air-crash investigation principles to AI-safety governance and directly addresses institutional investigation, incident learning, and evidence after AI failures.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-098": (
        "exclude-topic",
        "The article examines intentionality in AI-mediated art and design rather than operational human control or incident evidence.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-099": (
        "exclude-topic",
        "The preprint concerns large-scale knowledge discovery from big data and AI, not human intervention or incident reconstruction.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-100": (
        "retain-background",
        "The paper examines unmanned-aircraft cyber operations and associated human-system risks, providing a domain comparison without a practical-control evidence chain.",
        "title_abstract_and_full_text_route",
    ),
    "RS-FC-101": (
        "retain-background",
        "The report reviews and explores human factors in led-outdoor accidents, informing incident-analysis scope without the paper's formal-authority distinction or claim-level provenance.",
        "title_abstract_and_full_text_route",
    ),
}


def read_queue() -> list[dict[str, str]]:
    with QUEUE.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def claim_permission(decision: str) -> str:
    if decision.startswith("retain-"):
        return "none-until-proposition-review"
    if decision.startswith("exclude-"):
        return "none-excluded"
    return "none-unresolved"


def write_csv(rows: list[dict[str, str]]) -> None:
    fields = [
        "sample_id",
        "record_key",
        "title",
        "year",
        "author_decision",
        "author_rationale",
        "review_basis_used",
        "source_locator",
        "decision_owner",
        "decision_date",
        "ai_assistance",
        "decision_status",
        "claim_permission",
    ]
    with DECISIONS.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def update_population_ledger(rows: list[dict[str, str]]) -> None:
    with POPULATION_LEDGER.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fields = list(reader.fieldnames or [])
        population = list(reader)
    if not fields:
        fields = [
            "record_key", "retrieval_outcome", "retrieval_locator", "retrieval_date",
            "screening_decision", "author_notes", "decision_owner", "ai_assistance",
        ]
    decisions_by_key = {row["record_key"]: row for row in rows}
    matched: set[str] = set()
    for population_row in population:
        decision = decisions_by_key.get(population_row["record_key"])
        if decision is None:
            continue
        population_row["screening_decision"] = decision["author_decision"]
        population_row["author_notes"] = decision["author_rationale"]
        population_row["decision_owner"] = decision["decision_owner"]
        population_row["ai_assistance"] = decision["ai_assistance"]
        matched.add(population_row["record_key"])
    missing = sorted(set(decisions_by_key) - matched)
    if missing:
        raise SystemExit(f"population ledger lacks forward-citation records: {missing}")
    with POPULATION_LEDGER.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(population)


def main() -> int:
    digest = hashlib.sha256(QUEUE.read_bytes()).hexdigest()
    if digest != EXPECTED_QUEUE_SHA256:
        raise SystemExit(f"frozen queue hash changed: {digest}")

    queue = read_queue()
    if len(queue) != 71:
        raise SystemExit(f"expected 71 queue rows; found {len(queue)}")
    queue_ids = {row["sample_id"] for row in queue}
    if queue_ids != set(DECISION_DATA):
        raise SystemExit(
            "decision map mismatch: "
            f"missing={sorted(queue_ids - set(DECISION_DATA))}; "
            f"extra={sorted(set(DECISION_DATA) - queue_ids)}"
        )

    rows: list[dict[str, str]] = []
    for source in queue:
        decision, rationale, basis = DECISION_DATA[source["sample_id"]]
        rows.append(
            {
                "sample_id": source["sample_id"],
                "record_key": source["record_key"],
                "title": source["title"],
                "year": source["year"],
                "author_decision": decision,
                "author_rationale": rationale,
                "review_basis_used": basis,
                "source_locator": source["source_locator"],
                "decision_owner": AUTHOR,
                "decision_date": DECISION_DATE,
                "ai_assistance": ASSISTANCE,
                "decision_status": "author-authorized-ai-assisted-screening-complete",
                "claim_permission": claim_permission(decision),
            }
        )
    write_csv(rows)
    update_population_ledger(rows)

    counts = Counter(row["author_decision"] for row in rows)
    retained = sum(counts[key] for key in ("retain-close", "retain-background"))
    summary = {
        "version": "0.13.0",
        "status": "FORWARD_CITATION_AUTHOR_SCREENING_CLOSED",
        "frozen_input": str(QUEUE.relative_to(ROOT)),
        "frozen_input_sha256": digest,
        "decision_owner": AUTHOR,
        "decision_date": DECISION_DATE,
        "assistance_disclosure": ASSISTANCE,
        "counts": {
            "queue_records": len(rows),
            "decisions_complete": len(rows),
            "decisions_open": 0,
            "retained_for_source_review": retained,
            "excluded": len(rows) - retained,
            "decisions": dict(sorted(counts.items())),
            "claim_permission_granted": 0,
        },
        "claim_rule": (
            "Screening determines corpus membership only. Retained sources require proposition-level "
            "review with a stable locator before they may support a manuscript claim."
        ),
        "limits": [
            "AI assistance was used under author authorization; this record does not represent independent screening or inter-assessor agreement.",
            "The 71-record queue is the recovered-content subset of a frozen 102-record forward-citation risk sample.",
            "The result does not establish exhaustive coverage, originality, prevalence, reliability, field validity, or institutional effects.",
            "A retained screening decision does not establish that a source supports any manuscript proposition.",
        ],
    }
    SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    table_rows = "\n".join(
        f"| `{decision}` | {count} |" for decision, count in sorted(counts.items())
    )
    REPORT.write_text(
        "# Forward-Citation Author Screening, v0.13.0\n\n"
        "**Status:** `CLOSED`  \n"
        f"**Decision owner:** {AUTHOR}  \n"
        f"**Decision date:** {DECISION_DATE}\n\n"
        "## Result\n\n"
        "All 71 recovered-content records in the frozen forward-citation queue now have an author-authorized, AI-assisted screening decision. Screening determines which sources proceed to close or background review. It grants no manuscript claim permission.\n\n"
        "| Decision | Records |\n"
        "|---|---:|\n"
        f"{table_rows}\n\n"
        f"The pass retains {retained} records for a separate source review and excludes {len(rows) - retained} records while preserving their rationales. Retained records remain in `none-until-proposition-review`.\n\n"
        "## Decision control\n\n"
        "The input hash was checked before decisions were written. Records were processed in ascending sample order under the frozen v0.13 protocol. Every ledger row contains a decision, mechanism-specific rationale, inspected basis, locator, owner, date, assistance disclosure, and claim-permission state.\n\n"
        "## Interpretation boundary\n\n"
        "This gate closes corpus membership for the 71 recovered records. It does not show that the retained sources support any proposition, that excluded records are irrelevant to all research questions, or that the full inaccessible population has the same composition. Independent reliability and field validity remain open.\n",
        encoding="utf-8",
    )

    attestation = {
        "version": "0.13.0",
        "decision_owner": AUTHOR,
        "date": DECISION_DATE,
        "status": "AUTHOR_AUTHORIZED_AI_ASSISTED_SCREENING_COMPLETE",
        "statement": (
            "Mark Julius Banasihan authorized AI-assisted inspection and screening of the frozen 71-record "
            "forward-citation queue and retains accountability for the recorded corpus decisions."
        ),
        "scope": {
            "frozen_queue_records": len(rows),
            "screening_decisions_complete": len(rows),
            "screening_decisions_open": 0,
            "retained_for_proposition_review": retained,
            "manuscript_claim_permissions_granted": 0,
        },
        "ai_assistance": ASSISTANCE,
        "limits": summary["limits"],
    }
    ATTESTATION.write_text(json.dumps(attestation, indent=2) + "\n", encoding="utf-8")
    print(
        f"forward-citation author screening: {len(rows)}/{len(rows)} complete; "
        f"retained={retained}; excluded={len(rows) - retained}; counts={dict(sorted(counts.items()))}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
