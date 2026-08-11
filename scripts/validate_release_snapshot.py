#!/usr/bin/env python3
"""Validate frozen releases against their Git tags while the working tree advances."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOTS = {
    "v0.6.0": {
        "manifest": "release/v0.6.0-manifest.json",
        "immutable": (
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
        ),
    },
    "v0.7.0": {
        "manifest": "release/v0.7.0-manifest.json",
        "immutable": (
            "release/v0.7.0-manifest.json",
            "figures/v0.7.0-manifest.json",
            "figures/v0.7.0-claim-evidence-manifest.json",
            "paper/formal-literature-search-protocol-v0.7.0.md",
            "paper/formal-citation-chain-v0.7.0.md",
            "paper/formal-search-screening-v0.7.0.md",
            "paper/data/formal-search-v0.7.0.json",
            "paper/data/formal-screening-proposals-v0.7.0.json",
            "paper/data/formal-metadata-verification-v0.7.0.json",
            "paper/data/author-screening-queue-v0.7.0.csv",
            "paper/literature-support-audit-v0.7.0.json",
            "paper/literature-support-audit-v0.7.0.md",
        ),
    },
    "v0.9.0": {
        "manifest": "release/v0.9.0-manifest.json",
        "immutable": (
            "release/v0.9.0-manifest.json",
            "audits/v0.9.0/audit-plan.md",
            "audits/v0.9.0/audit-results.json",
            "audits/v0.9.0/audit-report.md",
            "audits/v0.9.0/exceptions.md",
            "figures/v0.9.0-manifest.json",
            "figures/v0.9.0-claim-evidence-manifest.json",
            "paper/review-record-v0.9.0.md",
            "paper/data/author-screening-decisions-v0.9.0.csv",
            "paper/data/author-screening-gate-v0.9.0.json",
            "paper/literature-support-audit-v0.9.0.json",
            "paper/literature-support-audit-v0.9.0.md",
        ),
    },
}


def tagged_bytes(tag: str, path: str) -> bytes:
    result = subprocess.run(
        ["git", "show", f"{tag}:{path}"],
        cwd=ROOT,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"cannot read {tag}:{path}: {detail}")
    return result.stdout


def sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def main() -> None:
    failures: list[str] = []
    sealed_count = 0
    immutable_count = 0
    for tag, specification in SNAPSHOTS.items():
        manifest_path = specification["manifest"]
        try:
            tagged_manifest_bytes = tagged_bytes(tag, manifest_path)
        except RuntimeError as exc:
            failures.append(str(exc))
            continue
        current_manifest = ROOT / manifest_path
        if not current_manifest.is_file():
            failures.append(f"missing current historical manifest: {manifest_path}")
        elif current_manifest.read_bytes() != tagged_manifest_bytes:
            failures.append(f"historical manifest differs from {tag}: {manifest_path}")

        manifest = json.loads(tagged_manifest_bytes)
        if manifest.get("version") != tag.removeprefix("v"):
            failures.append(f"tagged release manifest version mismatch: {tag}")
        artifacts = manifest.get("artifacts", [])
        sealed_count += len(artifacts)
        for artifact in artifacts:
            path = artifact.get("path")
            if not isinstance(path, str):
                failures.append(f"{tag} manifest contains an invalid artifact path")
                continue
            try:
                payload = tagged_bytes(tag, path)
            except RuntimeError as exc:
                failures.append(str(exc))
                continue
            if len(payload) != artifact.get("bytes"):
                failures.append(f"{tag} artifact size mismatch: {path}")
            if sha256(payload) != artifact.get("sha256"):
                failures.append(f"{tag} artifact hash mismatch: {path}")

        immutable = specification["immutable"]
        immutable_count += len(immutable)
        for relative in immutable:
            current = ROOT / relative
            if not current.is_file():
                failures.append(f"missing immutable historical artifact: {relative}")
                continue
            try:
                historical = tagged_bytes(tag, relative)
            except RuntimeError as exc:
                failures.append(str(exc))
                continue
            if current.read_bytes() != historical:
                failures.append(f"immutable historical artifact differs from {tag}: {relative}")

    if failures:
        raise SystemExit("release snapshot validation: FAIL\n" + "\n".join(failures))
    print(
        "release snapshot validation: PASS "
        f"({len(SNAPSHOTS)} tags; {sealed_count} sealed artifacts; "
        f"{immutable_count} immutable working copies)"
    )


if __name__ == "__main__":
    main()
