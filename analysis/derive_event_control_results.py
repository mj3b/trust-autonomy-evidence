#!/usr/bin/env python3
"""Derive v0.16 case-level event-control results from released assessment states."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assessments/event-control-results-v0.16.0.json"
ASSESSMENTS = (
    ROOT / "assessments/v0.6.0/TAE-PUB-001-oko-1983.json",
    ROOT / "cases/TAE-PUB-002-patriot-zg710-2003/assessment.json",
    ROOT / "cases/TAE-PUB-003-patriot-fa18-2003/assessment.json",
)
FIELDS = ("access", "comprehension", "authority", "feasibility", "exercise", "effect")
ALLOWED = {"supported", "partially_supported", "unsupported", "indeterminate"}


def classify(states: dict[str, str]) -> str:
    if any(value == "unsupported" for value in states.values()):
        return "fail"
    if all(value == "supported" for value in states.values()):
        return "pass"
    return "unresolved"


def build() -> dict:
    cases = []
    for path in ASSESSMENTS:
        assessment = json.loads(path.read_text(encoding="utf-8"))
        states = {field: assessment["practical_control"][field]["state"] for field in FIELDS}
        invalid = sorted(set(states.values()) - ALLOWED)
        if invalid:
            raise ValueError(f"required event stage has an invalid state in {path}: {invalid}")
        result = classify(states)
        cases.append(
            {
                "case_id": assessment["case_id"],
                "source_assessment": path.relative_to(ROOT).as_posix(),
                "required_states": states,
                "result": result,
                "unsupported_stages": [field for field, value in states.items() if value == "unsupported"],
                "unresolved_stages": [
                    field for field, value in states.items() if value in {"partially_supported", "indeterminate"}
                ],
            }
        )
    counts = {state: sum(item["result"] == state for item in cases) for state in ("pass", "fail", "unresolved")}
    return {
        "version": "0.16.0",
        "rule_id": "TAE-EVENT-CONTROL-V0.16.0",
        "required_fields": list(FIELDS),
        "decision_rule": {
            "pass": "all six required states are supported",
            "fail": "at least one required state is unsupported",
            "unresolved": "no required state is unsupported and at least one is partially supported or indeterminate",
        },
        "cases": cases,
        "result_counts": counts,
        "interpretation_limit": (
            "These results apply only to the three purposively selected packets. They are not prevalence, causal, "
            "reliability, safety, legal, or contemporary-system transfer estimates."
        ),
    }


def render() -> str:
    return json.dumps(build(), indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render()
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != expected:
            raise SystemExit("event-control results: FAIL (missing or stale)")
        print("event-control results: PASS (0 pass, 2 fail, 1 unresolved)")
        return 0
    OUTPUT.write_text(expected, encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
