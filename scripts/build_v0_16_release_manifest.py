#!/usr/bin/env python3
"""Seal the v0.16.0 manuscript-rebuild checkpoint."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "release" / "v0.16.0-manifest.json"

ARTIFACTS = (
    "release/v0.15.0-manifest.json",
    "release/v0.16.0-release-notes.md",
    "README.md",
    "RESEARCH_STATUS.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "paper/revision-plan-v0.16.0.md",
    "paper/manuscript.md",
    "paper/manuscript-reader.md",
    "paper/tables.md",
    "paper/tables/manuscript-tables.tex",
    "protocols/practical-human-control-test.md",
    "paper/preprints/README.md",
    "paper/preprints/00README.XXX",
    "paper/preprints/metadata.yaml",
    "paper/preprints/main.tex",
    "paper/preprints/source-manifest.json",
    "paper/preprints/preprints-source-v0.16.0.zip",
    "paper/preprints/preprints-compiled-v0.16.0.pdf",
    "paper/preprints/compile-receipt-v0.16.0.json",
    "assessments/event-control-results-v0.16.0.json",
    "analysis/derive_event_control_results.py",
    "evidence/claim-evidence-map.json",
    "evidence/human-review-attestation-v0.16.0.json",
    "fixtures/coe-audit-mutations.json",
    "audits/v0.16.0/audit-plan.md",
    "audits/v0.16.0/audit-results.json",
    "audits/v0.16.0/audit-report.md",
    "audits/v0.16.0/exceptions.md",
    "figures/manifest.json",
    "figures/specifications/figure-register.json",
    "figures/v0.16.0-claim-evidence-manifest.json",
    "scripts/build_v0_16_claim_map.py",
    "scripts/build_v0_16_release_manifest.py",
    "scripts/build_preprints_source_archive.py",
    "scripts/run_coe_integrity_audit.py",
    "scripts/validate_preprints_package.py",
    "scripts/validate_paper.py",
    "scripts/validate_repository.py",
)


def main() -> int:
    rows = []
    for name in ARTIFACTS:
        path = ROOT / name
        if not path.is_file():
            raise SystemExit(f"missing release artifact: {name}")
        payload = path.read_bytes()
        rows.append(
            {
                "path": name,
                "bytes": len(payload),
                "sha256": hashlib.sha256(payload).hexdigest(),
            }
        )
    manifest = {
        "version": "0.16.0",
        "created": "2026-08-19",
        "scope": "explanatory manuscript rebuild, formal event-control rule, derived case results, current figures, and integrity controls",
        "hash_algorithm": "SHA-256",
        "artifact_count": len(rows),
        "artifacts": rows,
        "result": {
            "event_control": {"pass": 0, "fail": 2, "unresolved": 1},
            "claim_count": 40,
            "mutation_controls_detected": "39/39",
            "compile_errors": 0,
            "post_references_displays": 0,
        },
        "boundary": (
            "This focused manifest seals the v0.16 manuscript-rebuild checkpoint. "
            "It establishes artifact identity, declared derivations, and control response. "
            "It does not establish historical truth, independent reliability, external validity, "
            "institutional effect, or publication acceptance."
        ),
    }
    OUTPUT.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"sealed {len(rows)} v0.16.0 artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
