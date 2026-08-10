#!/usr/bin/env python3
"""Seal the v0.8.0 manuscript pressure-test candidate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "release" / "v0.8.0-manifest.json"

CORE = (
    "release/v0.3.0-manifest.json",
    "release/v0.4.0-manifest.json",
    "release/v0.5.0-manifest.json",
    "release/v0.6.0-manifest.json",
    "release/v0.7.0-manifest.json",
    "README.md",
    "RESEARCH_STATUS.md",
    "CLAIMS.md",
    "LIMITATIONS.md",
    "SOURCES.md",
    "CITATION.cff",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "LICENSE",
    "requirements-dev.txt",
    "protocols/public-case-reconstruction-protocol.md",
    "protocols/practical-human-control-test.md",
    "protocols/coe-integrity-audit.md",
    "protocols/oko-evidence-adjudication-v0.6.0.md",
    "schemas/claim-evidence-map.schema.json",
    "schemas/research-lineage.schema.json",
    "schemas/coe-audit-result.schema.json",
    "schemas/coe-audit-mutations.schema.json",
    "fixtures/coe-audit-mutations.json",
    "research/trust-autonomy-and-evidence.md",
    "research/chain-of-evidence-adaptation.md",
    "evidence/claim-evidence-map.json",
    "evidence/research-lineage.json",
    "evidence/research-activity-log.json",
    "assessments/generated-results.json",
    "assessments/v0.6.0/TAE-PUB-001-oko-1983.json",
    "assessments/v0.6.0/oko-change-ledger.json",
    "audits/v0.6.0/audit-plan.md",
    "audits/v0.6.0/audit-results.json",
    "audits/v0.6.0/audit-report.md",
    "audits/v0.6.0/exceptions.md",
    "audits/v0.8.0/audit-plan.md",
    "audits/v0.8.0/audit-results.json",
    "audits/v0.8.0/audit-report.md",
    "audits/v0.8.0/exceptions.md",
    "reports/public-case-reconstruction-v0.6.0.md",
    "reports/oko-evidence-adjudication-v0.6.0.md",
    "reports/figure-methods.md",
)

PAPER = (
    "paper/README.md",
    "paper/paper-charter.md",
    "paper/manuscript.md",
    "paper/manuscript-reader.md",
    "paper/manuscript-pressure-test-v0.8.0.md",
    "paper/review-record-v0.8.0.md",
    "paper/author-screening-completion-gate.md",
    "paper/tables.md",
    "paper/tables/manuscript-tables.tex",
    "paper/literature-matrix.md",
    "paper/literature-search-log.md",
    "paper/formal-literature-search-protocol-v0.7.0.md",
    "paper/formal-citation-chain-v0.7.0.md",
    "paper/formal-search-screening-v0.7.0.md",
    "paper/data/formal-search-v0.7.0.json",
    "paper/data/formal-screening-proposals-v0.7.0.json",
    "paper/data/formal-metadata-verification-v0.7.0.json",
    "paper/data/author-screening-queue-v0.7.0.csv",
    "paper/data/author-screening-decisions-v0.8.0.csv",
    "paper/data/author-screening-gate-v0.8.0.json",
    "paper/literature-support-audit-v0.7.0.json",
    "paper/literature-support-audit-v0.7.0.md",
    "paper/novelty-audit.md",
    "paper/references.bib",
    "paper/claim-evidence-register.md",
    "paper/claim-crosswalk.md",
    "paper/scientistone-artifact-pressure-test.md",
    "paper/submission-notes.md",
    "paper/review-record-pr11.md",
)

FIGURES = (
    "analysis/build_figures.py",
    "analysis/build_claim_evidence_figure.py",
    "figures/README.md",
    "figures/manifest.json",
    "figures/v0.7.0-manifest.json",
    "figures/v0.7.0-claim-evidence-manifest.json",
    "figures/v0.8.0-manifest.json",
    "figures/v0.8.0-claim-evidence-manifest.json",
    "figures/specifications/figure-register.json",
    "figures/specifications/selection-decisions.json",
    "figures/specifications/decision-paths.json",
    "figures/specifications/reproducibility-lineage.json",
    "figures/specifications/claim-evidence-integrity.json",
    *tuple(f"figures/data/{stub}.csv" for stub in (
        "fig-1-selection-and-stopping",
        "fig-2-practical-control-chain",
        "fig-3-decision-paths",
        "fig-4-trust-evidence-states",
        "fig-5-formal-search-and-screening",
        "fig-6-evidence-boundaries",
        "fig-a1-mutation-response",
        "fig-a2-reproducibility-lineage",
        "fig-a3-claim-evidence-integrity",
        "fig-a4-oko-versioned-correction",
    )),
    *tuple(f"figures/generated/{stub}.{extension}" for stub in (
        "fig-1-selection-and-stopping",
        "fig-2-practical-control-chain",
        "fig-3-decision-paths",
        "fig-4-trust-evidence-states",
        "fig-5-formal-search-and-screening",
        "fig-6-evidence-boundaries",
        "fig-a1-mutation-response",
        "fig-a2-reproducibility-lineage",
        "fig-a3-claim-evidence-integrity",
        "fig-a4-oko-versioned-correction",
    ) for extension in ("png", "svg")),
)

VALIDATION = (
    "scripts/build_release_manifest.py",
    "scripts/render_reader_manuscript.py",
    "scripts/validate_author_screening_gate.py",
    "scripts/validate_repository.py",
    "scripts/validate_release_snapshot.py",
    "scripts/validate_paper.py",
    "scripts/validate_literature_support.py",
    "scripts/validate_formal_search.py",
    "scripts/validate_v060_adjudication.py",
    "scripts/run_coe_integrity_audit.py",
    "scripts/run_formal_literature_search.py",
    "scripts/propose_formal_search_screening.py",
    "scripts/verify_formal_search_metadata.py",
    ".github/workflows/validate.yml",
)

ARTIFACTS = CORE + PAPER + FIGURES + VALIDATION


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    if len(ARTIFACTS) != len(set(ARTIFACTS)):
        raise ValueError("release artifact list contains a duplicate path")
    artifacts = []
    for relative in ARTIFACTS:
        path = ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(relative)
        artifacts.append({"path": relative, "bytes": path.stat().st_size, "sha256": digest(path)})
    result = {
        "version": "0.8.0",
        "created": "2026-08-10",
        "hash_algorithm": "SHA-256",
        "artifacts": artifacts,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"sealed {len(artifacts)} release artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
