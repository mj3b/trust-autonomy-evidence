#!/usr/bin/env python3
"""Validate the frozen v0.6.0 release against its Git tag.

The working tree can advance after a release. Release integrity therefore has
to be checked against the tagged snapshot, instead of comparing an old
manifest with files under active revision.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TAG = "v0.6.0"
MANIFEST_PATH = "release/v0.6.0-manifest.json"
IMMUTABLE_PATHS = (
    "release/v0.3.0-manifest.json",
    "release/v0.4.0-manifest.json",
    "release/v0.5.0-manifest.json",
    "release/v0.6.0-manifest.json",
    "audits/v0.6.0/audit-plan.md",
    "audits/v0.6.0/audit-results.json",
    "audits/v0.6.0/audit-report.md",
    "audits/v0.6.0/exceptions.md",
    "assessments/v0.6.0/TAE-PUB-001-oko-1983.json",
    "assessments/v0.6.0/oko-change-ledger.json",
    "figures/v0.6.0-manifest.json",
    "paper/citation-chain-log-v0.6.0.md",
    "paper/literature-support-audit-v0.6.0.json",
    "paper/literature-support-audit-v0.6.0.md",
    "reports/oko-evidence-adjudication-v0.6.0.md",
    "reports/public-case-reconstruction-v0.6.0.md",
    "reports/claim-evidence-figure-methods-v0.6.0.md",
)


def tagged_bytes(path: str) -> bytes:
    result = subprocess.run(
        ["git", "show", f"{TAG}:{path}"],
        cwd=ROOT,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"cannot read {TAG}:{path}: {detail}")
    return result.stdout


def sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def main() -> None:
    failures: list[str] = []
    try:
        tagged_manifest_bytes = tagged_bytes(MANIFEST_PATH)
    except RuntimeError as exc:
        raise SystemExit(f"release snapshot validation: FAIL\n{exc}") from exc

    current_manifest = ROOT / MANIFEST_PATH
    if not current_manifest.is_file():
        failures.append(f"missing current historical manifest: {MANIFEST_PATH}")
    elif current_manifest.read_bytes() != tagged_manifest_bytes:
        failures.append(f"historical manifest differs from {TAG}: {MANIFEST_PATH}")

    manifest = json.loads(tagged_manifest_bytes)
    if manifest.get("version") != TAG.removeprefix("v"):
        failures.append("tagged release manifest version mismatch")

    for artifact in manifest.get("artifacts", []):
        path = artifact.get("path")
        if not isinstance(path, str):
            failures.append("tagged manifest contains an invalid artifact path")
            continue
        try:
            payload = tagged_bytes(path)
        except RuntimeError as exc:
            failures.append(str(exc))
            continue
        if len(payload) != artifact.get("bytes"):
            failures.append(f"tagged artifact size mismatch: {path}")
        if sha256(payload) != artifact.get("sha256"):
            failures.append(f"tagged artifact hash mismatch: {path}")

    for relative in IMMUTABLE_PATHS:
        current = ROOT / relative
        if not current.is_file():
            failures.append(f"missing immutable historical artifact: {relative}")
            continue
        try:
            historical = tagged_bytes(relative)
        except RuntimeError as exc:
            failures.append(str(exc))
            continue
        if current.read_bytes() != historical:
            failures.append(f"immutable historical artifact differs from {TAG}: {relative}")

    if failures:
        raise SystemExit("release snapshot validation: FAIL\n" + "\n".join(failures))
    print(
        "release snapshot validation: PASS "
        f"({len(manifest.get('artifacts', []))} sealed artifacts; "
        f"{len(IMMUTABLE_PATHS)} immutable working copies)"
    )


if __name__ == "__main__":
    main()
