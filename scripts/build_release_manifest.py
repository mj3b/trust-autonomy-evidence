#!/usr/bin/env python3
"""Seal the v0.4.0 publication artifacts with SHA-256 digests."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "release" / "v0.4.0-manifest.json"
ARTIFACTS = (
    "release/v0.3.0-manifest.json",
    "analysis/build_figures.py",
    "reports/figure-methods.md",
    "figures/README.md",
    "figures/manifest.json",
    "figures/specifications/figure-register.json",
    "figures/specifications/selection-decisions.json",
    "figures/specifications/decision-paths.json",
    "figures/specifications/reproducibility-lineage.json",
    "figures/data/fig-1-selection-and-stopping.csv",
    "figures/data/fig-2-practical-control-chain.csv",
    "figures/data/fig-3-decision-paths.csv",
    "figures/data/fig-4-trust-evidence-states.csv",
    "figures/data/fig-a1-mutation-response.csv",
    "figures/data/fig-a2-reproducibility-lineage.csv",
    "figures/generated/fig-1-selection-and-stopping.png",
    "figures/generated/fig-1-selection-and-stopping.svg",
    "figures/generated/fig-2-practical-control-chain.png",
    "figures/generated/fig-2-practical-control-chain.svg",
    "figures/generated/fig-3-decision-paths.png",
    "figures/generated/fig-3-decision-paths.svg",
    "figures/generated/fig-4-trust-evidence-states.png",
    "figures/generated/fig-4-trust-evidence-states.svg",
    "figures/generated/fig-a1-mutation-response.png",
    "figures/generated/fig-a1-mutation-response.svg",
    "figures/generated/fig-a2-reproducibility-lineage.png",
    "figures/generated/fig-a2-reproducibility-lineage.svg",
    "requirements-dev.txt",
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
        "version": "0.4.0",
        "created": "2026-08-07",
        "hash_algorithm": "SHA-256",
        "artifacts": artifacts,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"sealed {len(artifacts)} release artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
