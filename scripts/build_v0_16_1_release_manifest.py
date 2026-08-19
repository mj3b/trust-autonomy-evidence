#!/usr/bin/env python3
"""Seal the v0.16.1 repository-alignment maintenance candidate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "release" / "v0.16.1-manifest.json"

ARTIFACTS = (
    "release/v0.16.0-manifest.json",
    "release/v0.16.1-release-notes.md",
    "README.md",
    "RESEARCH_STATUS.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "formulas/README.md",
    "formulas/formula-register-v0.16.0.json",
    "formulas/formulas-v0.16.0.tex",
    "schemas/formula-register.schema.json",
    "evidence/claim-evidence-map.json",
    "figures/README.md",
    "figures/manifest.json",
    "figures/specifications/figure-register.json",
    "figures/v0.16.0-claim-evidence-manifest.json",
    "analysis/build_figures.py",
    "analysis/build_claim_evidence_figure.py",
    "protocols/coe-integrity-audit.md",
    "paper/preprints/README.md",
    "paper/preprints/overleaf-compile-receipt.json",
    "paper/preprints/overleaf-compile-receipt-v0.15.0.json",
    "scripts/build_v0_16_1_release_manifest.py",
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
        "version": "0.16.1",
        "created": "2026-08-19",
        "scope": "citation, formula, figure-metadata, audit-link, compile-receipt, and validation alignment for the v0.16.0 research package",
        "hash_algorithm": "SHA-256",
        "artifact_count": len(rows),
        "artifacts": rows,
        "inherited_research_result": {
            "source_release": "0.16.0",
            "event_control": {"pass": 0, "fail": 2, "unresolved": 1},
            "claim_count": 40,
            "mutation_controls_detected": "39/39",
        },
        "boundary": (
            "This maintenance manifest seals repository alignment for the v0.16.0 research package. "
            "It changes no manuscript claim, case state, case result, or figure interpretation. "
            "It does not establish historical truth, independent reliability, external validity, "
            "institutional effect, peer review, or publication acceptance."
        ),
    }
    OUTPUT.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"sealed {len(rows)} v0.16.1 maintenance artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
