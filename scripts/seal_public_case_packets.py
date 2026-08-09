#!/usr/bin/env python3
"""Create deterministic SHA-256 manifests for public-case packets."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASE_ROOT = ROOT / "cases"
PACKET_FILES = ("case-report.md", "source-manifest.json", "assessment.json")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    packet_index: list[dict[str, object]] = []
    for case_dir in sorted(CASE_ROOT.glob("TAE-PUB-*")):
        if not case_dir.is_dir():
            continue
        assessment = json.loads((case_dir / "assessment.json").read_text(encoding="utf-8"))
        artifacts = {name: digest(case_dir / name) for name in PACKET_FILES}
        manifest = {
            "version": "0.3.0",
            "case_id": assessment["case_id"],
            "protocol_freeze_commit": "180ddda1d70f0ee36faaf8875e839bbc99cbbec2",
            "assessment_contract": "schemas/public-case-assessment.schema.json@0.3.0",
            "artifacts": artifacts,
        }
        manifest_path = case_dir / "packet-manifest.json"
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        packet_index.append(
            {
                "case_id": assessment["case_id"],
                "directory": str(case_dir.relative_to(ROOT)),
                "manifest_sha256": digest(manifest_path),
            }
        )

    index = {"version": "0.3.0", "packets": packet_index}
    (CASE_ROOT / "public-case-packet-index.json").write_text(
        json.dumps(index, indent=2) + "\n", encoding="utf-8"
    )
    print(f"sealed {len(packet_index)} public-case packets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
