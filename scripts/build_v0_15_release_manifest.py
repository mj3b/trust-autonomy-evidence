#!/usr/bin/env python3
"""Seal the v0.15.0 venue-package checkpoint."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "release" / "v0.15.0-manifest.json"

ARTIFACTS = (
    "release/v0.14.0-manifest.json",
    "release/v0.14.0-release-notes.md",
    "release/v0.15.0-release-notes.md",
    "README.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "paper/manuscript.md",
    "paper/manuscript-reader.md",
    "paper/submission-notes.md",
    "paper/preprints/README.md",
    "paper/preprints/00README.XXX",
    "paper/preprints/metadata.yaml",
    "paper/preprints/main.tex",
    "paper/preprints/source-manifest.json",
    "paper/preprints/overleaf-compile-receipt.json",
    "paper/preprints/preprints-source-v0.15.0.zip",
    "paper/preprints/preprints-compiled-v0.15.0.pdf",
    "evidence/claim-evidence-map.json",
    "evidence/human-review-attestation-v0.15.0.json",
    "audits/v0.15.0/audit-plan.md",
    "audits/v0.15.0/audit-results.json",
    "audits/v0.15.0/audit-report.md",
    "audits/v0.15.0/exceptions.md",
    "scripts/build_v0_15_claim_map.py",
    "scripts/build_preprints_source_archive.py",
    "scripts/run_coe_integrity_audit.py",
    "scripts/validate_preprints_package.py",
    "scripts/validate_paper.py",
)


def main() -> int:
    rows = []
    for name in ARTIFACTS:
        path = ROOT / name
        payload = path.read_bytes()
        rows.append(
            {
                "path": name,
                "bytes": len(payload),
                "sha256": hashlib.sha256(payload).hexdigest(),
            }
        )
    manifest = {
        "version": "0.15.0",
        "created": "2026-08-18",
        "scope": "venue package, carried-forward evidence controls, and publication metadata",
        "hash_algorithm": "SHA-256",
        "artifact_count": len(rows),
        "artifacts": rows,
        "boundary": (
            "This focused manifest seals the v0.15 venue checkpoint. Earlier full research "
            "snapshots remain governed by their version tags and manifests."
        ),
    }
    OUTPUT.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"sealed {len(rows)} v0.15.0 artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
