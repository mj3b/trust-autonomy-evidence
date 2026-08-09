#!/usr/bin/env python3
"""Validate the v0.6.0 Oko adjudication and its negative controls."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
PRIOR_PATH = ROOT / "cases/TAE-PUB-001-oko-1983/assessment.json"
CURRENT_PATH = ROOT / "assessments/v0.6.0/TAE-PUB-001-oko-1983.json"
LEDGER_PATH = ROOT / "assessments/v0.6.0/oko-change-ledger.json"
MUTATIONS_PATH = ROOT / "fixtures/adjudication-mutations-v0.6.0.json"
EXPECTED_FIELDS = (
    "access",
    "comprehension",
    "authority",
    "feasibility",
    "exercise",
    "effect",
)
EXPECTED_PRIOR_SHA = "27c1da1a0e7596cbfae08ed98024935c70b3a58a7d7870614dde0534f638a353"
EXPECTED_PACKET_SHA = "be0734012f31243a45ba4b3412cf5da7e2ee66880a6702fb9bef565d515a438b"
EXPECTED_PROTOCOL_SHA = "6fef3cc0e69df173496e623c3c721fce57a7ef774dcee57ed7d93cf152f9cb52"


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def schema_errors(data: dict[str, Any], relative_schema: str) -> list[str]:
    schema = read_json(ROOT / relative_schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [error.message for error in validator.iter_errors(data)]


def evaluate(
    ledger: dict[str, Any],
    current: dict[str, Any],
    prior: dict[str, Any],
) -> dict[str, list[str]]:
    findings = {
        "schema": [],
        "artifact_integrity": [],
        "state_rule": [],
        "transition_completeness": [],
        "carry_forward_integrity": [],
        "dependency_closure": [],
    }
    findings["schema"].extend(schema_errors(current, "schemas/public-case-assessment.schema.json"))
    findings["schema"].extend(schema_errors(ledger, "schemas/adjudication-ledger.schema.json"))

    expected_artifacts = (
        (ledger.get("frozen_assessment", {}).get("path"), ledger.get("frozen_assessment", {}).get("sha256"), EXPECTED_PRIOR_SHA),
        (ledger.get("source_packet", {}).get("path"), ledger.get("source_packet", {}).get("sha256"), EXPECTED_PACKET_SHA),
        (ledger.get("adjudication_protocol", {}).get("path"), ledger.get("adjudication_protocol", {}).get("sha256"), EXPECTED_PROTOCOL_SHA),
    )
    for relative, recorded, expected in expected_artifacts:
        if not relative or not (ROOT / relative).is_file():
            findings["artifact_integrity"].append(f"missing adjudication artifact: {relative}")
            continue
        actual = digest(ROOT / relative)
        if recorded != expected or actual != expected:
            findings["artifact_integrity"].append(f"artifact hash mismatch: {relative}")

    transitions = ledger.get("reassessed_fields", [])
    pointers = [row.get("json_pointer") for row in transitions]
    expected_pointers = [f"/practical_control/{field}/state" for field in EXPECTED_FIELDS]
    if pointers != expected_pointers:
        findings["transition_completeness"].append("the six reassessed fields are missing, duplicated, or out of protocol order")

    for field in EXPECTED_FIELDS:
        prior_state = prior["practical_control"][field]["state"]
        current_state = current["practical_control"][field]["state"]
        if prior_state != "supported" or current_state != "partially_supported":
            findings["state_rule"].append(f"unexpected transition for practical_control.{field}: {prior_state} to {current_state}")
    for row in transitions:
        if row.get("prior_state") != "supported" or row.get("current_state") != "partially_supported":
            findings["state_rule"].append(f"ledger state rule failure: {row.get('json_pointer')}")
        if "contempor" not in row.get("material_gap", "").lower():
            findings["state_rule"].append(f"contemporaneity gap missing: {row.get('json_pointer')}")

    if current.get("autonomy") != prior.get("autonomy"):
        findings["carry_forward_integrity"].append("autonomy changed outside the adjudication scope")
    if current.get("trust_evidence") != prior.get("trust_evidence"):
        findings["carry_forward_integrity"].append("trust_evidence changed outside the adjudication scope")
    for field in ("correction", "repair", "reform"):
        if current["practical_control"].get(field) != prior["practical_control"].get(field):
            findings["carry_forward_integrity"].append(f"practical_control.{field} changed outside the adjudication scope")

    required_states = [current["practical_control"][field]["state"] for field in ("access", "authority", "feasibility", "exercise", "effect")]
    eligible = ledger.get("dependency_decision", {}).get("practical_force_eligible")
    if eligible is not False or all(state == "supported" for state in required_states):
        findings["dependency_closure"].append("the practical-force conclusion escaped a non-supported required stage")
    return findings


def set_pointer(document: dict[str, Any], pointer: str, replacement: Any) -> None:
    parts = [part for part in pointer.split("/") if part]
    target: Any = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    final = parts[-1]
    if replacement is None and isinstance(target, list):
        target.pop(int(final))
    elif isinstance(target, list):
        target[int(final)] = replacement
    else:
        target[final] = replacement


def negative_controls(
    ledger: dict[str, Any],
    current: dict[str, Any],
    prior: dict[str, Any],
) -> list[dict[str, Any]]:
    suite = read_json(MUTATIONS_PATH)
    results = []
    for control in suite["controls"]:
        mutated_ledger = copy.deepcopy(ledger)
        mutated_current = copy.deepcopy(current)
        pointer = control["target"]
        if pointer.startswith("/current_assessment/"):
            set_pointer(mutated_current, pointer.removeprefix("/current_assessment"), control["replacement"])
        else:
            set_pointer(mutated_ledger, pointer, control["replacement"])
        findings = evaluate(mutated_ledger, mutated_current, prior)
        expected = control["expected_check"]
        results.append(
            {
                "control_id": control["control_id"],
                "expected_check": expected,
                "detected": bool(findings[expected]),
                "finding": findings[expected][0] if findings[expected] else "",
            }
        )
    return results


def main() -> int:
    prior = read_json(PRIOR_PATH)
    current = read_json(CURRENT_PATH)
    ledger = read_json(LEDGER_PATH)
    findings = evaluate(ledger, current, prior)
    controls = negative_controls(ledger, current, prior)
    failures = [f"{check}: {message}" for check, messages in findings.items() for message in messages]
    failures.extend(
        f"negative control escaped: {row['control_id']} expected {row['expected_check']}"
        for row in controls
        if not row["detected"]
    )
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print(f"v0.6.0 adjudication validation: FAIL ({len(failures)} error(s))")
        return 1
    detected = sum(1 for row in controls if row["detected"])
    print(f"v0.6.0 adjudication validation: PASS (6 transitions; {detected}/6 controls detected)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
