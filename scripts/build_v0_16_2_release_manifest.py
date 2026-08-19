#!/usr/bin/env python3
"""Seal the v0.16.2 paper-workspace organization candidate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "release" / "v0.16.2-manifest.json"

ARTIFACTS = (
    "release/v0.16.1-manifest.json",
    "release/v0.16.2-release-notes.md",
    "README.md",
    "RESEARCH_STATUS.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "paper/README.md",
    "paper/REVIEW.md",
    "paper/preprints/README.md",
    "paper/arxiv/README.md",
    "paper/arxiv/source-manifest.json",
    "paper/arxiv/arxiv-source-v0.14.0.zip",
    "paper/arxiv/preprint-v0.14.0.pdf",
    "paper/arxiv/overleaf-compiled-v0.14.0.pdf",
    "paper/arxiv/overleaf-compile-receipt.json",
    "paper/archive/README.md",
    "paper/archive/v0.15.0/README.md",
    "paper/archive/v0.15.0/preprints-compiled-v0.15.0.pdf",
    "paper/archive/v0.15.0/preprints-source-v0.15.0.zip",
    "paper/archive/v0.15.0/overleaf-compile-receipt-v0.15.0.json",
    "evidence/claim-evidence-map.json",
    "figures/manifest.json",
    "figures/v0.16.0-claim-evidence-manifest.json",
    "scripts/build_v0_16_2_release_manifest.py",
    "scripts/validate_arxiv_package.py",
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
        "version": "0.16.2",
        "created": "2026-08-19",
        "scope": "paper-workspace navigation, external-review routing, v0.15.0 delivery-package archiving, current-paper labeling, and validation-path updates",
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
            "This maintenance manifest seals paper-workspace organization for the v0.16.0 research package. "
            "It changes no manuscript claim, case state, case result, figure data, or interpretation boundary. "
            "It does not establish historical truth, independent reliability, external validity, "
            "institutional effect, peer review, or publication acceptance."
        ),
    }
    OUTPUT.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"sealed {len(rows)} v0.16.2 maintenance artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
