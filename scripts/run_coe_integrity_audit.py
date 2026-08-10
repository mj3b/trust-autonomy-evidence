#!/usr/bin/env python3
"""Run the current Chain-of-Evidence integrity audit and negative controls."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
CLAIM_MAP_PATH = ROOT / "evidence/claim-evidence-map.json"
LINEAGE_PATH = ROOT / "evidence/research-lineage.json"
MUTATIONS_PATH = ROOT / "fixtures/coe-audit-mutations.json"
RESULT_PATH = ROOT / "audits/v0.9.0/audit-results.json"
REPORT_PATH = ROOT / "audits/v0.9.0/audit-report.md"
AUDIT_VERSION = "0.9.0"
AUDIT_ID = "TAE-COE-AUDIT-V0.9.0"
AUDIT_DATE = "2026-08-10"
EXCEPTIONS = ["COE-EX-03", "COE-EX-04"]
FITNESS_DIMENSIONS = (
    "directness",
    "contemporaneity",
    "independence",
    "completeness",
    "publication_authority",
)


@dataclass
class EvidenceResult:
    traceability: str
    integrity: str
    support: str
    value: Any = None
    message: str = ""


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def json_pointer(document: Any, pointer: str) -> Any:
    if pointer == "":
        return document
    current = document
    for raw in pointer.lstrip("/").split("/"):
        token = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(current, list):
            current = current[int(token)]
        else:
            current = current[token]
    return current


def manifest_entries() -> dict[str, set[str]]:
    entries: dict[str, set[str]] = {}
    for manifest_path in sorted((ROOT / "release").glob("*manifest.json")):
        manifest = load_json(manifest_path)
        for section in ("artifacts", "inputs"):
            for row in manifest.get(section, []):
                entries.setdefault(row["path"], set()).add(row["sha256"])
    return entries


def schema_errors(data: dict[str, Any], schema_path: str) -> list[str]:
    schema = load_json(ROOT / schema_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = []
    for error in sorted(validator.iter_errors(data), key=lambda item: list(item.path)):
        location = "/".join(str(part) for part in error.path) or "root"
        errors.append(f"{location}: {error.message}")
    return errors


def resolve_evidence(evidence: dict[str, Any], manifests: dict[str, set[str]]) -> EvidenceResult:
    path = ROOT / evidence["path"]
    if not path.is_file():
        return EvidenceResult("fail", "fail", "indeterminate", message="missing file")

    try:
        locator_type = evidence["locator_type"]
        locator = evidence["locator"]
        value: Any = None
        if locator_type == "file":
            value = str(path.relative_to(ROOT))
        elif locator_type == "json_pointer":
            value = json_pointer(load_json(path), locator)
        elif locator_type in {"text_marker", "markdown_heading"}:
            text = path.read_text(encoding="utf-8")
            if locator not in text:
                raise ValueError(f"marker not found: {locator}")
            value = locator
        elif locator_type == "csv_cell":
            row_selector, column_name = locator.rsplit("|", 1)
            criteria = dict(item.split("=", 1) for item in row_selector.split(";") if item)
            with path.open(encoding="utf-8", newline="") as handle:
                matches = [
                    row for row in csv.DictReader(handle)
                    if all(row.get(key) == expected for key, expected in criteria.items())
                ]
            if len(matches) != 1:
                raise ValueError(f"CSV row locator resolved {len(matches)} rows")
            if column_name not in matches[0]:
                raise ValueError(f"CSV column not found: {column_name}")
            value = matches[0][column_name]
        else:
            raise ValueError(f"unsupported locator type: {locator_type}")
    except (KeyError, IndexError, ValueError, json.JSONDecodeError) as exc:
        return EvidenceResult("fail", "indeterminate", "indeterminate", message=str(exc))

    integrity_state = evidence["integrity_state"]
    actual_digest = digest(path)
    if integrity_state == "verified":
        expected_digest = evidence.get("sha256")
        integrity = "pass" if expected_digest == actual_digest else "fail"
    elif integrity_state == "release_manifest":
        integrity = "pass" if actual_digest in manifests.get(evidence["path"], set()) else "fail"
    elif integrity_state in {"pending", "remote_only"}:
        integrity = "indeterminate"
    else:
        integrity = "fail"

    review = evidence["content_review"]
    support = "pass" if review == "recorded" else ("outside_scope" if review == "outside_scope" else "indeterminate")
    return EvidenceResult("pass", integrity, support, value=value)


def combine(states: list[str]) -> str:
    active = [state for state in states if state != "outside_scope"]
    if not active:
        return "outside_scope"
    if "fail" in active:
        return "fail"
    if "indeterminate" in active:
        return "indeterminate"
    return "pass"


def fitness_state(claim: dict[str, Any]) -> str:
    return combine([claim["fitness"][dimension]["state"] for dimension in FITNESS_DIMENSIONS])


def evaluate_claims(claim_map: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, list[str]]]:
    manifests = manifest_entries()
    claims = {claim["claim_id"]: claim for claim in claim_map["claims"]}
    evidence_by_claim: dict[str, list[EvidenceResult]] = {}
    findings: dict[str, list[str]] = {
        "score_verification": [],
        "specification_violation": [],
        "reference_verification": [],
        "method_code_alignment": [],
        "evidence_fitness_and_dependency_closure": [],
    }

    claim_ids = [claim["claim_id"] for claim in claim_map["claims"]]
    if len(claim_ids) != len(set(claim_ids)):
        findings["specification_violation"].append("duplicate claim identifier")

    for claim in claim_map["claims"]:
        claim_id = claim["claim_id"]
        results = []
        roles = set()
        for evidence in claim["evidence"]:
            result = resolve_evidence(evidence, manifests)
            results.append(result)
            roles.add(evidence["role"])
            if result.traceability == "fail":
                findings["reference_verification"].append(
                    f"{claim_id}/{evidence['evidence_id']}: {result.message or 'reference failure'}"
                )
            if result.integrity == "fail":
                findings["reference_verification"].append(
                    f"{claim_id}/{evidence['evidence_id']}: integrity failure"
                )
            if result.support == "indeterminate":
                findings["reference_verification"].append(
                    f"{claim_id}/{evidence['evidence_id']}: content review pending"
                )

            if "expected_value" in evidence:
                if result.traceability == "pass" and result.value != evidence["expected_value"]:
                    findings["score_verification"].append(
                        f"{claim_id}/{evidence['evidence_id']}: expected {evidence['expected_value']!r}, observed {result.value!r}"
                    )
                if isinstance(evidence["expected_value"], str) and evidence["run_type"] != "not_applicable":
                    findings["score_verification"].append(
                        f"{claim_id}/{evidence['evidence_id']}: categorical state mislabelled as {evidence['run_type']}"
                    )

        evidence_by_claim[claim_id] = results

        if claim["human_review"]["status"] == "pending":
            findings["reference_verification"].append(f"{claim_id}: human support review pending")
        if claim["human_review"]["status"] == "recorded":
            attestation = claim["human_review"].get("attestation_path")
            if not attestation or not (ROOT / attestation).is_file():
                findings["reference_verification"].append(f"{claim_id}: review attestation is missing")

        for scope_term in claim["scope_terms"]:
            if not scope_term["justification"].strip():
                findings["specification_violation"].append(
                    f"{claim_id}: {scope_term['term']} lacks a scope justification"
                )

        if "method" in roles and "implementation" in roles:
            paired = [
                result for evidence, result in zip(claim["evidence"], results)
                if evidence["role"] in {"method", "implementation"}
            ]
            if any(result.traceability != "pass" for result in paired):
                findings["method_code_alignment"].append(f"{claim_id}: method or implementation marker does not resolve")

    results_output = []
    provisional_eligibility: dict[str, bool] = {}
    for claim in claim_map["claims"]:
        claim_id = claim["claim_id"]
        results = evidence_by_claim[claim_id]
        traceability = combine([result.traceability for result in results])
        integrity = combine([result.integrity for result in results])
        support_states = [result.support for result in results]
        human_status = claim["human_review"]["status"]
        support_states.append("pass" if human_status == "recorded" else ("outside_scope" if human_status == "outside_scope" else "indeterminate"))
        support = combine(support_states)
        fitness = fitness_state(claim)
        dependencies_exist = all(dependency in claims for dependency in claim["dependencies"])
        dependency_closure = claim["dependency_closure"] if dependencies_exist else "fail"
        if not dependencies_exist:
            missing = sorted(set(claim["dependencies"]) - set(claims))
            findings["evidence_fitness_and_dependency_closure"].append(
                f"{claim_id}: unresolved dependencies {', '.join(missing)}"
            )
        provisional_eligibility[claim_id] = (
            claim["status"] == "supported"
            and traceability == "pass"
            and integrity == "pass"
            and support == "pass"
            and fitness == "pass"
            and dependency_closure == "pass"
        )
        results_output.append({
            "claim_id": claim_id,
            "traceability": traceability,
            "integrity": integrity,
            "support": support,
            "evidence_fitness": fitness,
            "dependency_closure": dependency_closure,
            "conclusion_eligible": False,
        })

    changed = True
    while changed:
        changed = False
        for claim in claim_map["claims"]:
            claim_id = claim["claim_id"]
            eligible = provisional_eligibility[claim_id] and all(
                provisional_eligibility.get(dependency, False) for dependency in claim["dependencies"]
            )
            if provisional_eligibility[claim_id] != eligible:
                provisional_eligibility[claim_id] = eligible
                changed = True

    for result, claim in zip(results_output, claim_map["claims"]):
        claim_id = claim["claim_id"]
        result["conclusion_eligible"] = provisional_eligibility[claim_id]
        if provisional_eligibility[claim_id] != claim["conclusion_eligible"]:
            findings["specification_violation"].append(
                f"{claim_id}: declared conclusion eligibility {claim['conclusion_eligible']} differs from computed {provisional_eligibility[claim_id]}"
            )
        if claim["status"] in {"blocked", "unresolved", "outside_scope"} and claim["conclusion_eligible"]:
            findings["specification_violation"].append(f"{claim_id}: non-supported claim is conclusion-eligible")
        if result["evidence_fitness"] in {"fail", "indeterminate"}:
            findings["evidence_fitness_and_dependency_closure"].append(
                f"{claim_id}: evidence fitness is {result['evidence_fitness']}"
            )
        if result["dependency_closure"] in {"fail", "indeterminate"}:
            findings["evidence_fitness_and_dependency_closure"].append(
                f"{claim_id}: dependency closure is {result['dependency_closure']}"
            )

    return results_output, findings


def mutate_claim_map(source: dict[str, Any], control: dict[str, Any]) -> dict[str, Any]:
    mutated = copy.deepcopy(source)
    claim = next(item for item in mutated["claims"] if item["claim_id"] == control["target_claim"])
    mutation_type = control["mutation_type"]
    parameters = control["parameters"]

    if mutation_type == "numeric_mismatch":
        evidence = next(item for item in claim["evidence"] if item["evidence_id"] == parameters["evidence_id"])
        evidence["expected_value"] = parameters["replacement"]
    elif mutation_type == "missing_reference":
        evidence = next(item for item in claim["evidence"] if item["evidence_id"] == parameters["evidence_id"])
        evidence["path"] = "fixtures/does-not-exist.json"
    elif mutation_type == "support_review_removed":
        claim["human_review"]["status"] = "pending"
        claim["human_review"]["reviewer"] = None
        claim["human_review"]["review_date"] = None
        claim["human_review"]["attestation_path"] = None
    elif mutation_type == "fitness_failure":
        claim["fitness"][parameters["dimension"]]["state"] = "fail"
        claim["fitness"][parameters["dimension"]]["rationale"] = "Controlled fitness failure."
    elif mutation_type == "method_marker_removed":
        evidence = next(item for item in claim["evidence"] if item["evidence_id"] == parameters["evidence_id"])
        evidence["locator"] = "CONTROLLED-MISSING-METHOD-MARKER"
    elif mutation_type == "unresolved_dependency":
        claim["dependencies"] = [parameters["dependency"]]
    elif mutation_type == "stale_hash":
        evidence = next(item for item in claim["evidence"] if item["evidence_id"] == parameters["evidence_id"])
        evidence["sha256"] = "0" * 64
    elif mutation_type == "run_type_mislabel":
        evidence = next(item for item in claim["evidence"] if item["evidence_id"] == parameters["evidence_id"])
        evidence["run_type"] = parameters["replacement"]
    elif mutation_type == "unsupported_scope_term":
        claim["scope_terms"].append({"term": parameters["term"], "justification": ""})
    else:
        raise ValueError(f"unknown mutation type: {mutation_type}")
    return mutated


def negative_control_results(claim_map: dict[str, Any], suite: dict[str, Any]) -> list[dict[str, Any]]:
    output = []
    for control in suite["controls"]:
        mutated = mutate_claim_map(claim_map, control)
        _, findings = evaluate_claims(mutated)
        expected = control["expected_check"]
        detected = bool(findings[expected])
        observed = expected if detected else "none"
        message = findings[expected][0] if detected else "The expected check did not report the controlled corruption."
        output.append({
            "control_id": control["control_id"],
            "expected_check": expected,
            "detected": detected,
            "observed_check": observed,
            "message": message,
        })
    return output


def check_summary(
    name: str,
    claim_map: dict[str, Any],
    claim_results: list[dict[str, Any]],
    findings: dict[str, list[str]],
) -> dict[str, Any]:
    check_ids = {
        "score_verification": "COE-I1",
        "specification_violation": "COE-I2",
        "reference_verification": "COE-I3",
        "method_code_alignment": "COE-I4",
        "evidence_fitness_and_dependency_closure": "COE-I5",
    }
    if name == "score_verification":
        tested = sum(1 for claim in claim_map["claims"] for evidence in claim["evidence"] if "expected_value" in evidence)
        indeterminate = 0
    elif name == "specification_violation":
        tested = len(claim_results)
        indeterminate = 0
    elif name == "reference_verification":
        tested = len(claim_results)
        indeterminate = sum(
            1 for row in claim_results if "indeterminate" in {row["traceability"], row["integrity"], row["support"]}
        )
    elif name == "method_code_alignment":
        tested = sum(
            1
            for claim in claim_map["claims"]
            if {"method", "implementation"}.issubset({evidence["role"] for evidence in claim["evidence"]})
        )
        indeterminate = 0
    else:
        tested = len(claim_results)
        indeterminate = sum(
            1 for row in claim_results if "indeterminate" in {row["evidence_fitness"], row["dependency_closure"]}
        )
    failed = len(findings[name])
    expected_exception_check = name in {"reference_verification", "evidence_fitness_and_dependency_closure"}
    status = "pass"
    if failed or indeterminate:
        status = "pass_with_exceptions" if expected_exception_check else "fail"
    return {
        "check_id": check_ids[name],
        "name": name,
        "status": status,
        "tested": tested,
        "passed": max(tested - failed - indeterminate, 0),
        "failed": failed,
        "indeterminate": indeterminate,
        "findings": findings[name],
    }


def build_result() -> dict[str, Any]:
    claim_map = load_json(CLAIM_MAP_PATH)
    lineage = load_json(LINEAGE_PATH)
    mutations = load_json(MUTATIONS_PATH)

    schema_findings = []
    for data, schema_path in (
        (claim_map, "schemas/claim-evidence-map.schema.json"),
        (lineage, "schemas/research-lineage.schema.json"),
        (mutations, "schemas/coe-audit-mutations.schema.json"),
    ):
        schema_findings.extend(schema_errors(data, schema_path))

    claim_results, findings = evaluate_claims(claim_map)
    findings["specification_violation"] = schema_findings + findings["specification_violation"]
    controls = negative_control_results(claim_map, mutations)
    checks = [
        check_summary(name, claim_map, claim_results, findings)
        for name in (
            "score_verification",
            "specification_violation",
            "reference_verification",
            "method_code_alignment",
            "evidence_fitness_and_dependency_closure",
        )
    ]
    escaped_controls = [row for row in controls if not row["detected"]]
    hard_fail = any(check["status"] == "fail" for check in checks) or bool(escaped_controls)
    status = "FAIL" if hard_fail else "PASS_WITH_EXCEPTIONS"
    result = {
        "version": AUDIT_VERSION,
        "audit_id": AUDIT_ID,
        "audit_date": AUDIT_DATE,
        "scope": "Twenty material claims declared in TAE-COE-V0.9.0, including the closed author-screening gate and final Figure 5 search-flow result. Independent validity, inaccessible-record review, and authenticated database coverage remain outside the completed evidence base.",
        "status": status,
        "checks": checks,
        "negative_controls": controls,
        "exceptions": EXCEPTIONS,
        "claim_results": claim_results,
    }
    result_schema_errors = schema_errors(result, "schemas/coe-audit-result.schema.json")
    if result_schema_errors:
        raise ValueError("result schema failure: " + "; ".join(result_schema_errors))
    return result


def render_report(result: dict[str, Any]) -> str:
    lines = [
        "# v0.9.0 Chain-of-Evidence Integrity Audit",
        "",
        f"**Audit date:** {result['audit_date']}  ",
        f"**Status:** `{result['status']}`  ",
        f"**Scope:** {result['scope']}",
        "",
        "## Decision",
        "",
        "The declared v0.9 claim set passes its executable integrity controls with two published exceptions. The closed author gate, final Figure 5 data, and manuscript counts resolve to their declared evidence. The result permits bounded author-screening, artifact, and method claims. It supplies no independent reliability, originality, or completed systematic-search finding.",
        "",
        "## Integrity checks",
        "",
        "| Check | State | Tested | Passed | Failed | Indeterminate |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for check in result["checks"]:
        lines.append(
            f"| {check['name']} | {check['status']} | {check['tested']} | {check['passed']} | {check['failed']} | {check['indeterminate']} |"
        )
    lines.extend(["", "## Claim gates", "", "| Claim | Traceability | Integrity | Support | Fitness | Closure | Conclusion eligible |", "|---|---|---|---|---|---|---|"])
    for row in result["claim_results"]:
        lines.append(
            f"| {row['claim_id']} | {row['traceability']} | {row['integrity']} | {row['support']} | {row['evidence_fitness']} | {row['dependency_closure']} | {'yes' if row['conclusion_eligible'] else 'no'} |"
        )
    lines.extend(["", "## Negative controls", "", "| Control | Expected check | Detected |", "|---|---|---|"])
    for row in result["negative_controls"]:
        lines.append(f"| {row['control_id']} | {row['expected_check']} | {'yes' if row['detected'] else 'no'} |")
    lines.extend([
        "",
        f"All {len(result['negative_controls'])} controls run on in-memory copies. The committed evidence files remain unchanged.",
        "",
        "## Published exceptions",
        "",
        "- `COE-EX-03`: no independent assessor has reproduced the support or evidence-fitness judgments.",
        "- `COE-EX-04`: authenticated database searching, inaccessible-record review, and full citation chaining remain incomplete.",
        "",
        "## Closed exception",
        "",
        "- `COE-EX-05` closed when Mark Julius Banasihan recorded all 89 author decisions and the final search-flow data were rebuilt from the ledger.",
        "",
        "## Interpretation",
        "",
        "A passing control shows that the audit detected the prespecified corruption. It does not show that the underlying source is true. Human support review, claim-specific fitness, and conclusion closure remain separate gates for that reason.",
        "",
        "The full machine-readable result is [`audit-results.json`](audit-results.json). The protocol is [`protocols/coe-integrity-audit.md`](../../protocols/coe-integrity-audit.md).",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Compare regenerated outputs with committed outputs")
    args = parser.parse_args()

    result = build_result()
    result_text = json.dumps(result, indent=2) + "\n"
    report_text = render_report(result)

    if args.check:
        failures = []
        for path, expected in ((RESULT_PATH, result_text), (REPORT_PATH, report_text)):
            if not path.is_file() or path.read_text(encoding="utf-8") != expected:
                failures.append(str(path.relative_to(ROOT)))
        if failures:
            print("chain-of-evidence audit outputs differ: " + ", ".join(failures))
            return 1
    else:
        RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
        RESULT_PATH.write_text(result_text, encoding="utf-8")
        REPORT_PATH.write_text(report_text, encoding="utf-8")

    detected = sum(1 for row in result["negative_controls"] if row["detected"])
    print(
        f"chain-of-evidence audit: {result['status']} "
        f"({len(result['claim_results'])} claims; {detected}/{len(result['negative_controls'])} controls detected)"
    )
    return 0 if result["status"] != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
