#!/usr/bin/env python3
"""Build the v0.9.0 author-screening ledger from the frozen v0.7 queue."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "paper/data/author-screening-queue-v0.7.0.csv"
OUTPUT = ROOT / "paper/data/author-screening-decisions-v0.9.0.csv"
EXPECTED_QUEUE_SHA256 = "e889a2fd5e9dbefc2b052069706baca3bdd9cc0a1711aaef4348e7b9d3d07180"
AUTHOR = "Mark Julius Banasihan"
DECISION_DATE = "2026-08-10"
ASSISTANCE = "AI-assisted title-and-abstract screening under author authorization; the author retains decision accountability"


CLOSE_NOTES = {
    1: "Operationalizes a chain of control and traceability for meaningful human control across four automated-driving examples.",
    6: "Joins tracking, tracing, an evaluation cascade, and engineering use cases for meaningful human control.",
    7: "Applies a GSN assurance case to human control across manual, supervised, and autonomous recovery cases.",
    14: "Combines workflow audit, forensic reconstruction, decision-state logging, and override documentation in AI-enabled cybersecurity.",
    21: "Specifies authorization boundaries, escalation, auditability, and a validation plan for delegated LLM action.",
    27: "Joins human control, audit, provenance, and control-plane governance in one proposed assurance architecture.",
    32: "Applies action-level oversight tiers to AI Incident Database records and reports independent-annotation agreement.",
    38: "Translates human-oversight duties into audit criteria for a real embodied-AI deployment.",
    40: "Joins post-incident evidence mapping, traceable policy review, and human oversight in one executable workflow proposal.",
    45: "Defines comprehension, authorization, intervention, contestation, restoration, and responsibility as a weakest-link control chain.",
    47: "Maps audit evidence into binding assurance constraints and applies the method retrospectively to the Cruise incident.",
    48: "Publishes a runnable protocol that maps a decision chain, traces owners and artifacts, and tests rollback and review gates.",
    55: "Embeds authority, delegation boundaries, escalation, override, and audit interfaces in the runtime control plane.",
    63: "Defines a versioned assurance case linking claims, assumptions, evidence, control points, and a trace of practical human override.",
    72: "Defines non-delegable human decision points and reproducible per-step audit artifacts for AI-assisted expert work.",
    78: "Quantifies causal responsibility and shows that allocated human functions can coexist with low causal responsibility.",
    79: "Connects intervention rights to information, practical exercise, and lifecycle contestability.",
    80: "Joins technical, sociotechnical, and governance control layers in an operational oversight framework.",
    81: "Treats overseer competence and incentives as institutional design constraints on effective control.",
    82: "Proposes counterargument prompts as a concrete mechanism for resisting automation complacency.",
    83: "Defines effective oversight through causal power, epistemic access, self-control, and fitting intentions.",
    84: "Synthesizes conceptual, technical, legal, and organizational conditions for human oversight.",
    85: "Models stable and adaptive feedback loops through which human learning supports continuing control.",
    86: "Links typed claims to evidence, deterministic validation, and provenance before entry into an official record.",
    87: "Separates constitutive participation from corrective intervention through a causal runtime taxonomy.",
    88: "Reports four forms of contemporary agent-oversight work from interviews with 17 experienced developers.",
    89: "Joins selective human review, escalation, durable records, and measured audit completeness in a synthetic decision pathway.",
}


BACKGROUND_NOTES = {
    3: "Supplies autonomous-transport risk, meaningful-control, certification, and incident-learning context without the tested reconstruction path.",
    4: "Argues that military-AI normal accidents can defeat meaningful-control assurances without supplying a case-evidence procedure.",
    12: "Proposes measurable meaningful-control indicators for firefighting teams without versioned public incident packets.",
    15: "Supplies evidence about bias-audit standardization and access limits without a practical-control chain.",
    16: "Identifies nominal-oversight loopholes and contestability duties in South African automated-decision law.",
    22: "Synthesizes explanation and interface conditions that support human reasoning without reconstructing control in incidents.",
    24: "Proposes safety controls and meaningful oversight for autonomous weapons without the paper's evidence adjudication method.",
    26: "Identifies interface conditions for supervisory control and calibrated trust without a public-evidence procedure.",
    29: "Specifies role-dependent information and intervention constraints in drilling automation.",
    30: "Identifies evidence, human-interaction, operational-domain, and systems-assurance gaps in UK Defence guidance.",
    31: "Provides a testbed and pilot measures for variable autonomy, workload, trust, authority, and situation awareness.",
    33: "Connects explainability, traceability, override authority, auditability, and contestation in tax administration.",
    37: "Proposes interpretive checkpoints, attention pacing, escalation, override, and decision traceability.",
    42: "Proposes effective oversight, documentation, monitoring, and impact assessment for automated child-welfare decisions.",
    43: "Examines human control and evidentiary reliability in nuclear-disarmament verification through doctrinal analysis.",
    44: "Defines five normative conditions for meaningful human control in AI-assisted medicine.",
    46: "Empirically separates formal board responsibility from measured oversight capacity in a 26-person pilot.",
    49: "Connects automated social services to human review, reasons, appeal, and record access.",
    53: "Uses contemporary military cases to examine time compression, opacity, and narrowed human validation windows.",
    54: "Proposes prospective escalation, intervention controls, and review evidence for generated interfaces.",
    58: "Shows how operators receive multiple evidence views and decide whether an automated maritime alert warrants action.",
    60: "Documents how operational, psychological, and social conditions shape supervisory capacity in current semi-autonomous driving.",
    62: "Examines meaningful human engagement and responsibility in contemporary AI-assisted warfare.",
    65: "Provides a claim-evidence and provenance method for scientific extraction without assessing human practical control.",
    66: "Reports large-scale structured physician review and observed variation in rejection rates across specialties.",
    69: "Uses 44 public-authority requests to connect AI adoption with recordkeeping, guidance, training, and hybrid review.",
    70: "Supplies human-factors mechanisms and a recent aviation case without an AI-control evidence adjudication method.",
    71: "Defines epistemic, control, temporal, organizational, and information-environment integrity, including fictional oversight.",
    73: "Empirically traces how oversight bodies obtain, interpret, and act on information under structural access limits.",
    75: "Defines human capacities for end-setting, reason-giving, contestation, revision, and shared responsibility.",
    76: "Provides a five-gate, auditable automation-decision protocol and a process-level human-anchor condition.",
    77: "Connects high-velocity operation to cognitive saturation and continuous oversight architecture.",
}


TOPIC_INDICES = {
    2, 11, 17, 18, 19, 20, 23, 25, 28, 35,
    36, 39, 41, 51, 52, 57, 59, 64, 68, 74,
}

SINGLE_COMPONENT_INDICES = {5, 8, 9, 10, 13, 34, 50, 56, 61, 67}

FULL_TEXT_BASIS = {
    32: "official_full_text",
    48: "official_full_text",
    63: "publisher_full_text",
    80: "open_full_text",
    81: "open_full_text",
    83: "official_full_text",
    84: "official_report_full_text",
    85: "open_full_text",
}


def decision_for(index: int) -> tuple[str, str]:
    if index in CLOSE_NOTES:
        return "retain-close", CLOSE_NOTES[index]
    if index in BACKGROUND_NOTES:
        return "retain-background", BACKGROUND_NOTES[index]
    if index in TOPIC_INDICES:
        return (
            "exclude-topic",
            "Title and abstract concern another application or evaluation task and do not assess practical human control or the tested research-method combination.",
        )
    if index in SINGLE_COMPONENT_INDICES:
        return (
            "exclude-single-component",
            "Title and abstract address one relevant control or evidence component without the tested selection, packet, adjudication, and correction path.",
        )
    raise ValueError(f"no decision registered for queue row {index}")


def source_locator(row: dict[str, str]) -> str:
    doi = row.get("doi", "").strip()
    if doi:
        return f"https://doi.org/{doi}"
    arxiv = row.get("arxiv", "").strip()
    if arxiv:
        return f"https://arxiv.org/abs/{arxiv}"
    return "metadata record in paper/data/formal-search-v0.7.0.json"


def main() -> None:
    digest = hashlib.sha256(QUEUE.read_bytes()).hexdigest()
    if digest != EXPECTED_QUEUE_SHA256:
        raise SystemExit(f"frozen queue hash changed: {digest}")

    with QUEUE.open(encoding="utf-8", newline="") as handle:
        queue = list(csv.DictReader(handle))
    if len(queue) != 89:
        raise SystemExit(f"expected 89 queue rows; found {len(queue)}")

    fieldnames = [
        "record_key",
        "proposed_decision",
        "author_decision",
        "author_notes",
        "review_basis",
        "source_locator",
        "decision_owner",
        "decision_date",
        "ai_assistance",
    ]
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for index, row in enumerate(queue, start=1):
            decision, notes = decision_for(index)
            writer.writerow(
                {
                    "record_key": row["record_key"],
                    "proposed_decision": row["proposed_decision"],
                    "author_decision": decision,
                    "author_notes": notes,
                    "review_basis": FULL_TEXT_BASIS.get(index, "title_and_abstract"),
                    "source_locator": source_locator(row),
                    "decision_owner": AUTHOR,
                    "decision_date": DECISION_DATE,
                    "ai_assistance": ASSISTANCE,
                }
            )

    print(f"wrote {len(queue)} decisions to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
