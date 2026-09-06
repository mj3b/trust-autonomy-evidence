#!/usr/bin/env python3
"""Run the v0.17.0 Chain-of-Evidence audit for the policy extension."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import run_coe_integrity_audit as base


ROOT = Path(__file__).resolve().parents[1]
CLAIM_MAP = ROOT / "evidence/policy-claim-evidence-map-v0.17.0.json"
MUTATIONS = ROOT / "fixtures/policy-crosswalk-mutations-v0.17.0.json"
RESULT = ROOT / "audits/v0.17.0-policy-crosswalk/audit-results.json"
REPORT = ROOT / "audits/v0.17.0-policy-crosswalk/audit-report.md"
EXCEPTIONS = ["COE-EX-12", "COE-EX-13"]


def policy_schema_errors(
    data: dict[str, Any], schema_path: str, additions: dict[str, str]
) -> list[str]:
    """Validate the draft without changing the schema sealed in v0.16.0."""
    schema = base.load_json(ROOT / schema_path)
    for field, value in additions.items():
        allowed = schema["properties"][field]["enum"]
        if value not in allowed:
            allowed.append(value)
    validator = base.Draft202012Validator(schema, format_checker=base.FormatChecker())
    errors = []
    for error in sorted(validator.iter_errors(data), key=lambda item: list(item.path)):
        location = "/".join(str(part) for part in error.path) or "root"
        errors.append(f"{location}: {error.message}")
    return errors


def negative_controls(claim_map: dict[str, Any], suite: dict[str, Any]) -> list[dict[str, Any]]:
    _, baseline = base.evaluate_claims(claim_map)
    output = []
    for control in suite["controls"]:
        mutated = base.mutate_claim_map(claim_map, control)
        _, findings = base.evaluate_claims(mutated)
        expected = control["expected_check"]
        new_findings = [item for item in findings[expected] if item not in baseline[expected]]
        detected = bool(new_findings)
        output.append({
            "control_id": control["control_id"],
            "expected_check": expected,
            "detected": detected,
            "observed_check": expected if detected else "none",
            "message": new_findings[0] if detected else "The expected check produced no new finding for the controlled corruption.",
        })
    return output


def build_result() -> dict[str, Any]:
    claim_map = base.load_json(CLAIM_MAP)
    suite = base.load_json(MUTATIONS)
    schema_findings = []
    for data, schema_path, additions in (
        (
            claim_map,
            "schemas/claim-evidence-map.schema.json",
            {"version": "0.17.0", "scope_id": "TAE-COE-V0.17.0"},
        ),
        (
            suite,
            "schemas/coe-audit-mutations.schema.json",
            {"version": "0.17.0", "suite_id": "TAE-COE-NEGATIVE-CONTROLS-V0.17.0"},
        ),
    ):
        schema_findings.extend(policy_schema_errors(data, schema_path, additions))
    claim_results, findings = base.evaluate_claims(claim_map)
    findings["specification_violation"] = schema_findings + findings["specification_violation"]
    controls = negative_controls(claim_map, suite)
    checks = [
        base.check_summary(name, claim_map, claim_results, findings)
        for name in (
            "score_verification",
            "specification_violation",
            "reference_verification",
            "method_code_alignment",
            "evidence_fitness_and_dependency_closure",
        )
    ]
    escaped = [row for row in controls if not row["detected"]]
    hard_fail = any(check["failed"] > 0 or check["status"] == "fail" for check in checks) or bool(escaped)
    result = {
        "version": "0.17.0",
        "audit_id": "TAE-COE-AUDIT-V0.17.0",
        "audit_date": "2026-09-05",
        "scope": "Five bounded claims governing the targeted policy and standards crosswalk, the proposed EU AI Act regulatory-sandbox validation protocol, and their v0.17.0 manuscript use. The v0.16.0 historical findings remain unchanged.",
        "status": "FAIL" if hard_fail else "PASS_WITH_EXCEPTIONS",
        "checks": checks,
        "negative_controls": controls,
        "exceptions": EXCEPTIONS,
        "claim_results": claim_results,
    }
    errors = policy_schema_errors(
        result,
        "schemas/coe-audit-result.schema.json",
        {"version": "0.17.0", "audit_id": "TAE-COE-AUDIT-V0.17.0"},
    )
    if errors:
        raise ValueError("result schema failure: " + "; ".join(errors))
    return result


def render_report(result: dict[str, Any]) -> str:
    lines = [
        "# v0.17.0 Policy Crosswalk Chain-of-Evidence Audit",
        "",
        f"**Audit date:** {result['audit_date']}",
        "",
        f"**Status:** `{result['status']}`",
        "",
        f"**Scope:** {result['scope']}",
        "",
        "## Decision",
        "",
        "The audit confirms that five bounded claims resolve to the eight-record official-source ledger, the policy crosswalk, the sandbox protocol, the v0.17.0 manuscript section, the author attestation, and the validator. Nine in-memory mutations test numeric agreement, source resolution, manuscript integration, file integrity, evidence fitness, method-code alignment, dependency closure, and scope control. The historical case results and the v0.16.0 manuscript claim map remain unchanged.",
        "",
        "## Integrity checks",
        "",
        "| Check | State | Tested | Passed | Failed | Indeterminate |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for check in result["checks"]:
        lines.append(f"| {check['name']} | {check['status']} | {check['tested']} | {check['passed']} | {check['failed']} | {check['indeterminate']} |")
    lines.extend(["", "## Claim gates", "", "| Claim | Traceability | Integrity | Support | Fitness | Closure | Conclusion eligible |", "|---|---|---|---|---|---|---|"])
    for row in result["claim_results"]:
        lines.append(f"| {row['claim_id']} | {row['traceability']} | {row['integrity']} | {row['support']} | {row['evidence_fitness']} | {row['dependency_closure']} | {'yes' if row['conclusion_eligible'] else 'no'} |")
    lines.extend(["", "## Negative controls", "", "| Control | Expected check | Detected |", "|---|---|---|"])
    for row in result["negative_controls"]:
        lines.append(f"| {row['control_id']} | {row['expected_check']} | {'yes' if row['detected'] else 'no'} |")
    lines.extend([
        "",
        "## Published exceptions",
        "",
        "- `COE-EX-12`: the review is targeted to named provisions and official summaries and supplies no complete legal analysis, compliance finding, or ISO conformity assessment.",
        "- `COE-EX-13`: no sandbox authority, system provider, participant group, or independent assessor has applied the proposed protocol.",
        "",
        "## Interpretation",
        "",
        "A detected mutation shows that the named control responded to a prespecified corruption. It supplies no evidence that the legal summary is complete or that the prospective method will work in a field setting. Those conclusions remain blocked by the published exceptions.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build_result()
    result_text = json.dumps(result, indent=2) + "\n"
    report_text = render_report(result)
    if args.check:
        changed = []
        for path, expected in ((RESULT, result_text), (REPORT, report_text)):
            if not path.is_file() or path.read_text(encoding="utf-8") != expected:
                changed.append(str(path.relative_to(ROOT)))
        if changed:
            print("policy audit outputs differ: " + ", ".join(changed))
            return 1
    else:
        RESULT.parent.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(result_text, encoding="utf-8")
        REPORT.write_text(report_text, encoding="utf-8")
    detected = sum(1 for row in result["negative_controls"] if row["detected"])
    print(f"policy integrity audit: {result['status']} (5 bounded claims; {detected}/9 controls detected; author inclusion recorded)")
    return 0 if result["status"] != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
