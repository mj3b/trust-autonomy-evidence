#!/usr/bin/env python3
"""Build the deterministic v0.17.0 release manifest."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "release/v0.17.0-manifest.json"

PATHS = [
    "release/v0.17.0-release-notes.md",
    "README.md",
    "RESEARCH_STATUS.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "paper/README.md",
    "paper/REVIEW.md",
    "paper/policy-and-standards-crosswalk-v0.17.0.md",
    "paper/data/policy-and-standards-source-review-v0.17.0.json",
    "paper/drafts/v0.17.0/README.md",
    "paper/drafts/v0.17.0/regulatory-section.tex",
    "paper/drafts/v0.17.0/regulatory-section-review.pdf",
    "paper/preprints/README.md",
    "paper/preprints/00README.XXX",
    "paper/preprints/main.tex",
    "paper/preprints/metadata.yaml",
    "paper/preprints/source-manifest-v0.17.0.json",
    "paper/preprints/compile-receipt-v0.17.0.json",
    "paper/preprints/preprints-source-v0.17.0.zip",
    "paper/preprints/preprints-compiled-v0.17.0.pdf",
    "evidence/policy-claim-evidence-map-v0.17.0.json",
    "evidence/human-review-attestation-v0.17.0.json",
    "fixtures/policy-crosswalk-mutations-v0.17.0.json",
    "audits/v0.17.0-policy-crosswalk/audit-plan.md",
    "audits/v0.17.0-policy-crosswalk/audit-report.md",
    "audits/v0.17.0-policy-crosswalk/audit-results.json",
    "audits/v0.17.0-policy-crosswalk/exceptions.md",
    "scripts/build_policy_review_pdf_v0_17_0.py",
    "scripts/build_v0_17_policy_claim_map.py",
    "scripts/build_v0_17_preprint_package.py",
    "scripts/run_policy_integrity_audit_v0_17_0.py",
    "scripts/validate_policy_crosswalk_v0_17_0.py",
    "scripts/build_v0_17_release_manifest.py",
]


def record(relative_path: str) -> dict[str, object]:
    path = ROOT / relative_path
    data = path.read_bytes()
    return {
        "path": relative_path,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


def main() -> None:
    missing = [path for path in PATHS if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit(f"missing release artifacts: {missing}")
    payload = {
        "version": "0.17.0",
        "created": "2026-09-06",
        "scope": "bounded policy crosswalk, prospective regulatory-sandbox design, integrity controls, and arXiv-ready preprint package",
        "hash_algorithm": "SHA-256",
        "artifact_count": len(PATHS),
        "artifacts": [record(path) for path in PATHS],
        "result": {
            "policy_claims": 5,
            "official_sources": 8,
            "controlled_mutations": 9,
            "detected_mutations": 9,
            "compiled_pages": 30,
            "case_results_changed": False,
        },
        "claim_boundary": "The manifest establishes artifact identity and declared control results. It does not establish legal compliance, ISO conformity, source truth, independent reliability, external validity, or publication acceptance.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"v0.17.0 release manifest: PASS ({len(PATHS)} artifacts)")


if __name__ == "__main__":
    main()
