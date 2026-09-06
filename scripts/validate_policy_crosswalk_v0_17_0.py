#!/usr/bin/env python3
"""Validate the v0.17.0 policy crosswalk and sandbox protocol."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
SOURCE_REVIEW = ROOT / "paper/data/policy-and-standards-source-review-v0.17.0.json"
CROSSWALK = ROOT / "paper/policy-and-standards-crosswalk-v0.17.0.md"
PROTOCOL = ROOT / "protocols/regulatory-sandbox-validation-protocol-v0.17.0.md"
MANUSCRIPT = ROOT / "paper/preprints/main.tex"
ATTESTATION = ROOT / "evidence/human-review-attestation-v0.17.0.json"
AUDIT_RESULT = ROOT / "audits/v0.17.0-policy-crosswalk/audit-results.json"
EXPECTED_STAGES = (
    "information access",
    "comprehension capacity",
    "intervention authority",
    "intervention feasibility",
    "exercised judgment",
    "execution propagation",
)
OFFICIAL_HOSTS = {
    "eur-lex.europa.eu",
    "airc.nist.gov",
    "www.iso.org",
    "www.nyc.gov",
    "cppa.ca.gov",
    "coag.gov",
    "www.ilga.gov",
}
EXPECTED_URLS = {
    "POL-EU-AIA-14": "https://eur-lex.europa.eu/eli/reg/2024/1689/oj",
    "POL-EU-AIA-57": "https://eur-lex.europa.eu/eli/reg/2024/1689/oj",
    "POL-NIST-AI-RMF-CORE": "https://airc.nist.gov/airmf-resources/airmf/5-sec-core/",
    "POL-ISO-IEC-42001": "https://www.iso.org/standard/42001",
    "POL-NYC-LL144": "https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page",
    "POL-CA-ADMT": "https://cppa.ca.gov/regulations/ccpa_updates.html",
    "POL-CO-ADMT": "https://coag.gov/ai/",
    "POL-IL-HB3773": "https://www.ilga.gov/documents/legislation/103/HB/PDF/10300HB3773lv.pdf",
}
EXPECTED_SUPPORTING_URLS = {
    "POL-CA-ADMT": "https://cppa.ca.gov/announcements/2025/20250923.html",
}


def main() -> int:
    failures: list[str] = []
    for path in (SOURCE_REVIEW, CROSSWALK, PROTOCOL, MANUSCRIPT, ATTESTATION):
        if not path.is_file() or path.stat().st_size == 0:
            failures.append(f"missing or empty file: {path.relative_to(ROOT)}")
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    review = json.loads(SOURCE_REVIEW.read_text(encoding="utf-8"))
    crosswalk = CROSSWALK.read_text(encoding="utf-8")
    protocol = PROTOCOL.read_text(encoding="utf-8")
    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    attestation = json.loads(ATTESTATION.read_text(encoding="utf-8"))
    records = review.get("records", [])
    if review.get("source_count") != 8 or len(records) != 8:
        failures.append("official-source count must equal eight")
    ids = [record.get("source_id") for record in records]
    if len(ids) != len(set(ids)):
        failures.append("source identifiers must be unique")
    for record in records:
        source_id = record.get("source_id")
        official_url = record.get("official_url", "")
        host = urlparse(official_url).hostname
        if host not in OFFICIAL_HOSTS:
            failures.append(f"source is not on the declared official-host list: {source_id}")
        if EXPECTED_URLS.get(source_id) != official_url:
            failures.append(f"source URL differs from the reviewed endpoint: {source_id}")
        supporting_url = record.get("supporting_url")
        if source_id in EXPECTED_SUPPORTING_URLS:
            if supporting_url != EXPECTED_SUPPORTING_URLS[source_id]:
                failures.append(f"supporting source URL differs from the reviewed endpoint: {source_id}")
            elif urlparse(supporting_url).hostname not in OFFICIAL_HOSTS:
                failures.append(f"supporting source is not on the declared official-host list: {source_id}")
        for field in ("locator", "accessed_on", "source_version", "observed_proposition", "permitted_use", "limits"):
            if not str(record.get(field, "")).strip():
                failures.append(f"{source_id} lacks {field}")
        if record.get("accessed_on") != "2026-09-05":
            failures.append(f"{source_id} has an unexpected access date")
        if record.get("human_review") != "recorded":
            failures.append(f"{source_id} lacks recorded bounded author review")
        if record.get("human_review_basis") != "evidence/human-review-attestation-v0.17.0.json":
            failures.append(f"{source_id} does not resolve to the v0.17.0 author attestation")

    if attestation.get("decision") != "APPROVE_BOUNDED_MANUSCRIPT_INCLUSION":
        failures.append("author attestation does not approve bounded manuscript inclusion")
    if set(attestation.get("approved_claims", [])) != {f"PAPER-C{number}" for number in range(47, 52)}:
        failures.append("author attestation does not cover all five v0.17.0 claims")

    for stage in EXPECTED_STAGES:
        if stage not in protocol.lower():
            failures.append(f"sandbox protocol stage missing: {stage}")
    for marker in (
        "The first reliability study should use a blinded second assessor",
        "Construct and criterion validity",
        "external criterion that was not produced from the same stage labels",
        "Ethics, privacy, and study authority",
        "applicable research-ethics or institutional-review determination",
        "t_{commit}$ and $t_{access}$ are event timestamps",
        "elapsed durations under the notation inherited from v0.16.0",
    ):
        if marker not in protocol:
            failures.append(f"sandbox protocol safeguard missing: {marker}")
    for marker in (
        "EU AI Act, Article 14",
        "EU AI Act, Article 57",
        "NIST AI RMF Core",
        "ISO/IEC 42001:2023",
        "New York City Local Law 144",
        "California CCPA ADMT regulations",
        "Colorado ADMT framework",
        "Illinois Public Act 103-0804",
        "Kevin Baum's private message is excluded from the evidence base",
        "Primarily comprehension and intervention authority",
        "Field validity also requires sampling across the intended systems and tasks",
    ):
        if marker not in crosswalk:
            failures.append(f"crosswalk marker missing: {marker}")

    for marker in (
        "Preprint v0.17.0",
        "6. Regulatory relevance and prospective validation",
        "EU AI Act Article 57 provides for controlled environments",
        "NIST AI RMF outcomes GOVERN 2.1",
        "ISO/IEC 42001:2023 public overview",
        "United States application boundaries",
        "A nonnegative margin is necessary",
        "elapsed durations expressed in the same unit",
    ):
        if marker not in manuscript:
            failures.append(f"v0.17.0 manuscript marker missing: {marker}")

    prohibited = (
        "the method complies with",
        "the method is certified",
        "establishes legal sufficiency",
        "proves regulatory compliance",
    )
    combined = (crosswalk + "\n" + protocol + "\n" + manuscript).lower()
    for phrase in prohibited:
        if phrase in combined:
            failures.append(f"prohibited scope claim: {phrase}")

    for command in (
        [sys.executable, "scripts/build_v0_17_policy_claim_map.py", "--check"],
        [sys.executable, "scripts/run_policy_integrity_audit_v0_17_0.py", "--check"],
        [sys.executable, "scripts/build_policy_review_pdf_v0_17_0.py", "--check"],
    ):
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
        if result.returncode != 0:
            failures.append((result.stdout + result.stderr).strip())

    if AUDIT_RESULT.is_file():
        audit = json.loads(AUDIT_RESULT.read_text(encoding="utf-8"))
        for check in audit.get("checks", []):
            if check.get("failed") != 0:
                failures.append(f"audit check contains a failed item: {check.get('name')}")
        for claim in audit.get("claim_results", []):
            if claim.get("traceability") != "pass" or claim.get("integrity") != "pass":
                failures.append(f"claim does not have a complete local evidence path: {claim.get('claim_id')}")
            if claim.get("support") != "pass" or claim.get("conclusion_eligible") is not True:
                failures.append(f"author-approved policy claim did not clear the bounded manuscript gate: {claim.get('claim_id')}")
    else:
        failures.append("policy audit result is missing")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print(f"policy crosswalk validation: FAIL ({len(failures)} error(s))")
        return 1
    print("policy crosswalk validation: PASS_WITH_EXCEPTIONS (8 official sources; 5 bounded claims; 9 controlled mutations; author inclusion recorded)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
