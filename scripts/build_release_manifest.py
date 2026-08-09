#!/usr/bin/env python3
"""Seal the v0.6.0 protocol-consistency and paper-readiness artifacts."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "release" / "v0.6.0-manifest.json"
ARTIFACTS = (
    "release/v0.3.0-manifest.json",
    "release/v0.4.0-manifest.json",
    "release/v0.5.0-manifest.json",
    "README.md",
    "RESEARCH_STATUS.md",
    "CLAIMS.md",
    "LIMITATIONS.md",
    "SOURCES.md",
    "CITATION.cff",
    "CHANGELOG.md",
    "protocols/coe-integrity-audit.md",
    "protocols/oko-evidence-adjudication-v0.6.0.md",
    "research/chain-of-evidence-adaptation.md",
    "evidence/claim-evidence-map.json",
    "evidence/research-lineage.json",
    "evidence/research-activity-log.json",
    "schemas/claim-evidence-map.schema.json",
    "schemas/research-lineage.schema.json",
    "schemas/coe-audit-result.schema.json",
    "schemas/coe-audit-mutations.schema.json",
    "schemas/adjudication-ledger.schema.json",
    "schemas/literature-support-audit.schema.json",
    "fixtures/coe-audit-mutations.json",
    "fixtures/adjudication-mutations-v0.6.0.json",
    "assessments/v0.6.0/TAE-PUB-001-oko-1983.json",
    "assessments/v0.6.0/oko-change-ledger.json",
    "audits/v0.6.0/audit-plan.md",
    "audits/v0.6.0/audit-results.json",
    "audits/v0.6.0/audit-report.md",
    "audits/v0.6.0/exceptions.md",
    "analysis/build_claim_evidence_figure.py",
    "figures/specifications/claim-evidence-integrity.json",
    "figures/data/fig-a3-claim-evidence-integrity.csv",
    "figures/generated/fig-a3-claim-evidence-integrity.png",
    "figures/generated/fig-a3-claim-evidence-integrity.svg",
    "figures/v0.6.0-manifest.json",
    "reports/oko-evidence-adjudication-v0.6.0.md",
    "reports/public-case-reconstruction-v0.6.0.md",
    "reports/claim-evidence-figure-methods-v0.6.0.md",
    "paper/README.md",
    "paper/paper-charter.md",
    "paper/manuscript.md",
    "paper/literature-matrix.md",
    "paper/literature-search-log.md",
    "paper/citation-chain-log-v0.6.0.md",
    "paper/literature-support-audit-v0.6.0.json",
    "paper/literature-support-audit-v0.6.0.md",
    "paper/novelty-audit.md",
    "paper/references.bib",
    "paper/claim-evidence-register.md",
    "paper/claim-crosswalk.md",
    "paper/scientistone-artifact-pressure-test.md",
    "paper/submission-notes.md",
    "paper/review-record-pr11.md",
    "requirements-dev.txt",
    "scripts/run_coe_integrity_audit.py",
    "scripts/validate_v060_adjudication.py",
    "scripts/validate_literature_support.py",
    "scripts/validate_paper.py",
    "scripts/validate_repository.py",
    "scripts/build_release_manifest.py",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    artifacts = []
    for relative in ARTIFACTS:
        path = ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(relative)
        artifacts.append(
            {
                "path": relative,
                "bytes": path.stat().st_size,
                "sha256": digest(path),
            }
        )

    result = {
        "version": "0.6.0",
        "created": "2026-08-09",
        "hash_algorithm": "SHA-256",
        "artifacts": artifacts,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"sealed {len(artifacts)} release artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
