#!/usr/bin/env python3
"""Run the v0.2.0 solo-validation suite and reproduce its report."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

from assessment import assess_case


ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.2.0"
CASES_PATH = ROOT / "fixtures/synthetic/cases.json"
MUTATIONS_PATH = ROOT / "fixtures/mutations/mutations.json"
ORACLE_PATH = ROOT / "oracles/solo-validation-v0.2.0.json"
MANIFEST_PATH = ROOT / "oracles/manifest.json"
RESULTS_PATH = ROOT / "assessments/generated-results.json"
REPORT_PATH = ROOT / "reports/solo-validation-v0.2.0.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def validate_schema(schema: dict) -> Draft202012Validator:
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def validate_inputs(cases_document: dict, mutations_document: dict) -> None:
    if cases_document.get("version") != VERSION:
        raise ValueError("case fixture version mismatch")
    if mutations_document.get("version") != VERSION:
        raise ValueError("mutation fixture version mismatch")

    case_validator = validate_schema(load_json(ROOT / "schemas/solo-case.schema.json"))
    autonomy_validator = validate_schema(load_json(ROOT / "schemas/autonomy-profile.schema.json"))
    mutation_validator = validate_schema(load_json(ROOT / "schemas/mutation-suite.schema.json"))
    mutation_validator.validate(mutations_document)

    case_ids = []
    for case in cases_document["cases"]:
        case_validator.validate(case)
        autonomy_validator.validate(case["autonomy"])
        case_ids.append(case["case_id"])

    if len(case_ids) != len(set(case_ids)):
        raise ValueError("duplicate synthetic case identifiers")

    mutation_ids = [item["mutation_id"] for item in mutations_document["mutations"]]
    if len(mutation_ids) != len(set(mutation_ids)):
        raise ValueError("duplicate mutation identifiers")

    missing_bases = sorted(
        {
            item["base_case_id"]
            for item in mutations_document["mutations"]
            if item["base_case_id"] not in case_ids
        }
    )
    if missing_bases:
        raise ValueError(f"mutation base cases missing: {', '.join(missing_bases)}")


def validate_manifest() -> dict:
    manifest = load_json(MANIFEST_PATH)
    if manifest.get("version") != VERSION:
        raise ValueError("oracle manifest version mismatch")
    for relative, expected in manifest["sha256"].items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise ValueError(f"sealed artifact hash mismatch: {relative}")
    return manifest


def compare_oracle(cases: list[dict], oracle: dict) -> tuple[list[dict], int]:
    trust_validator = validate_schema(load_json(ROOT / "schemas/trust-evidence-assessment.schema.json"))
    control_validator = validate_schema(load_json(ROOT / "schemas/practical-control-assessment.schema.json"))
    results = []
    comparisons = 0

    expected_cases = oracle["expected"]
    actual_ids = {case["case_id"] for case in cases}
    if actual_ids != set(expected_cases):
        raise ValueError("oracle and fixture case identifiers differ")

    for case in cases:
        result = assess_case(case)
        trust_validator.validate(result["trust"])
        control_validator.validate(result["control"])
        expected = expected_cases[case["case_id"]]
        if result["trust"] != expected["trust"]:
            raise AssertionError(f"trust oracle mismatch: {case['case_id']}")
        if result["control"] != expected["control"]:
            raise AssertionError(f"control oracle mismatch: {case['case_id']}")
        comparisons += len(result["trust"]) + len(result["control"])
        results.append(result)

    return results, comparisons


def set_path(document: dict, dotted_path: str, value: object) -> None:
    parts = dotted_path.split(".")
    target = document
    for part in parts[:-1]:
        target = target[part]
    target[parts[-1]] = value


def assessment_deltas(before: dict, after: dict) -> list[dict]:
    deltas = []
    for assessment in ("trust", "control"):
        for field in before[assessment]:
            old = before[assessment][field]
            new = after[assessment][field]
            if old != new:
                deltas.append(
                    {
                        "assessment": assessment,
                        "field": field,
                        "from": old,
                        "to": new,
                    }
                )
    return sorted(deltas, key=lambda item: (item["assessment"], item["field"]))


def run_mutations(cases: list[dict], mutations: list[dict]) -> list[dict]:
    by_id = {case["case_id"]: case for case in cases}
    results = []
    for mutation in mutations:
        base = by_id[mutation["base_case_id"]]
        changed = copy.deepcopy(base)
        for change in mutation["changes"]:
            set_path(changed, change["path"], change["value"])

        before = assess_case(base)
        after = assess_case(changed)
        actual = assessment_deltas(before, after)
        expected = sorted(
            mutation["expected_deltas"],
            key=lambda item: (item["assessment"], item["field"]),
        )
        if actual != expected:
            raise AssertionError(
                f"mutation delta mismatch: {mutation['mutation_id']}\n"
                f"expected={expected}\nactual={actual}"
            )
        results.append(
            {
                "mutation_id": mutation["mutation_id"],
                "base_case_id": mutation["base_case_id"],
                "delta_count": len(actual),
                "deltas": actual,
                "status": "pass",
            }
        )
    return results


def build_results(
    case_results: list[dict],
    mutation_results: list[dict],
    oracle_comparisons: int,
    manifest: dict,
) -> dict:
    return {
        "version": VERSION,
        "method": "deterministic synthetic and mutation validation",
        "sealed_artifacts": manifest["sha256"],
        "summary": {
            "synthetic_cases": len(case_results),
            "trust_determinations": sum(len(item["trust"]) for item in case_results),
            "control_determinations": sum(len(item["control"]) for item in case_results),
            "oracle_comparisons": oracle_comparisons,
            "mutation_tests": len(mutation_results),
            "mutation_delta_assertions": sum(item["delta_count"] for item in mutation_results),
            "invariance_tests": sum(item["delta_count"] == 0 for item in mutation_results),
            "failures": 0,
        },
        "case_results": case_results,
        "mutation_results": mutation_results,
        "claim_boundary": (
            "The results establish deterministic behavior for committed synthetic fixtures and mutation properties. "
            "They do not establish independent reliability, field validity, institutional effectiveness, or improved outcomes."
        ),
    }


def build_report(results: dict) -> str:
    summary = results["summary"]
    return f"""# Solo Validation Report, v{VERSION}

## Decision

The v{VERSION} assessment contract produced the expected result for all {summary['oracle_comparisons']} prespecified case determinations and all {summary['mutation_tests']} mutation tests. This result demonstrates deterministic behavior for the committed synthetic fixtures and declared mutation properties.

## Test surface

| Measure | Result |
|---|---:|
| Synthetic cases | {summary['synthetic_cases']} |
| Trust-evidence determinations | {summary['trust_determinations']} |
| Practical-control determinations | {summary['control_determinations']} |
| Oracle comparisons | {summary['oracle_comparisons']} |
| Mutation tests | {summary['mutation_tests']} |
| Expected mutation deltas | {summary['mutation_delta_assertions']} |
| Invariance tests | {summary['invariance_tests']} |
| Failures | {summary['failures']} |

## Properties exercised

The suite tests positive, partial, indeterminate, unsupported, and outside-scope assessment states. It separates formal authority from feasible intervention, pre-action access from post-action notification, process evidence from outcome, integrity from truth, correction from reform, and autonomy profile changes from evidence-assessment changes.

The mutation suite tests eleven expected classification changes and three invariance conditions. Title, reported outcome, and impact-radius changes leave the trust and practical-control assessments unchanged under the current contract. Impact radius remains visible in the autonomy profile.

## Reproduction

```bash
python analysis/run_solo_validation.py --check
```

The command validates the JSON Schemas, verifies the sealed artifact hashes, evaluates every case, compares each determination with the committed oracle, applies every mutation, and confirms that the generated result and report are current.

## Claim boundary

The author designed the constructs, fixtures, rules, and oracle. Exact agreement therefore establishes internal artifact behavior. It does not estimate inter-rater reliability, independent usability, population validity, operational effectiveness, legal sufficiency, or outcome improvement.

The next evidence step available without volunteer reviewers is reconstruction of prespecified public cases using contemporaneous source packets and a published source-selection rule.
"""


def render_json(document: dict) -> str:
    return json.dumps(document, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="write deterministic outputs")
    mode.add_argument("--check", action="store_true", help="verify committed outputs")
    args = parser.parse_args()

    cases_document = load_json(CASES_PATH)
    mutations_document = load_json(MUTATIONS_PATH)
    oracle = load_json(ORACLE_PATH)
    validate_inputs(cases_document, mutations_document)
    manifest = validate_manifest()
    case_results, comparisons = compare_oracle(cases_document["cases"], oracle)
    mutation_results = run_mutations(cases_document["cases"], mutations_document["mutations"])
    results = build_results(case_results, mutation_results, comparisons, manifest)
    expected_results = render_json(results)
    expected_report = build_report(results)

    if args.write:
        RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
        REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
        RESULTS_PATH.write_text(expected_results, encoding="utf-8")
        REPORT_PATH.write_text(expected_report, encoding="utf-8")
    else:
        if RESULTS_PATH.read_text(encoding="utf-8") != expected_results:
            raise AssertionError("generated assessment results are stale")
        if REPORT_PATH.read_text(encoding="utf-8") != expected_report:
            raise AssertionError("solo-validation report is stale")

    print(
        "solo validation: PASS "
        f"({comparisons} oracle comparisons, {len(mutation_results)} mutation tests)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
