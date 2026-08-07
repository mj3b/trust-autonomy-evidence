#!/usr/bin/env python3
"""Seal the v0.3.0 research artifacts with SHA-256 digests."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "release" / "v0.3.0-manifest.json"
ARTIFACTS = (
    "research/frozen-research-agenda.md",
    "protocols/public-case-reconstruction-protocol.md",
    "cases/public-case-selection-register.md",
    "cases/data/candidate-search-output.json",
    "cases/TAE-PUB-001-oko-1983/case-report.md",
    "cases/TAE-PUB-001-oko-1983/source-manifest.json",
    "cases/TAE-PUB-001-oko-1983/assessment.json",
    "cases/TAE-PUB-001-oko-1983/packet-manifest.json",
    "cases/TAE-PUB-002-patriot-zg710-2003/case-report.md",
    "cases/TAE-PUB-002-patriot-zg710-2003/source-manifest.json",
    "cases/TAE-PUB-002-patriot-zg710-2003/assessment.json",
    "cases/TAE-PUB-002-patriot-zg710-2003/packet-manifest.json",
    "cases/TAE-PUB-003-patriot-fa18-2003/case-report.md",
    "cases/TAE-PUB-003-patriot-fa18-2003/source-manifest.json",
    "cases/TAE-PUB-003-patriot-fa18-2003/assessment.json",
    "cases/TAE-PUB-003-patriot-fa18-2003/packet-manifest.json",
    "cases/public-case-packet-index.json",
    "reports/public-case-reconstruction-v0.3.0.md",
    "schemas/public-case-assessment.schema.json",
    "schemas/source-manifest.schema.json",
    "scripts/build_public_case_candidates.py",
    "scripts/seal_public_case_packets.py",
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
        "version": "0.3.0",
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
