#!/usr/bin/env python3
"""Validate the v0.16.0 working-paper source package and its open gates."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "paper/preprints"
VERSION = "0.16.0"


def digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def main() -> int:
    failures: list[str] = []
    required = (
        "README.md",
        "00README.XXX",
        "metadata.yaml",
        "main.tex",
        "source-manifest.json",
        "preprints-compiled-v0.16.0.pdf",
        "compile-receipt-v0.16.0.json",
        f"preprints-source-v{VERSION}.zip",
    )
    for name in required:
        path = PACKAGE / name
        if not path.is_file() or path.stat().st_size == 0:
            failures.append(f"missing or empty package file: paper/preprints/{name}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    metadata = (PACKAGE / "metadata.yaml").read_text(encoding="utf-8")
    tex = (PACKAGE / "main.tex").read_text(encoding="utf-8")
    markers = (
        "Mark Julius Banasihan",
        "0009-0001-8121-2878",
        r"Independent Researcher, Node \& Norm, United States",
        "ALB candidate in Extension Studies at Harvard University",
        "mab7898@g.harvard.edu",
        "markjuliusbanasihan@gmail.com",
        "no Harvard University sponsorship, supervision, endorsement, or representation",
        "10.5281/zenodo.21926005",
        "Working paper v0.16.0",
        "EventControl(c)",
        "Execution propagation",
        "Conflicts of Interest",
        "The author declares no conflicts of interest.",
    )
    for marker in markers:
        if marker not in tex:
            failures.append(f"LaTeX marker missing: {marker}")
    for marker in (
        'version: "0.16.0"',
        'venue: "Unsubmitted working paper"',
        'affiliation: "Independent Researcher, Node & Norm, United States"',
        'alternate_email: "markjuliusbanasihan@gmail.com"',
        'student_status: "ALB candidate in Extension Studies, Harvard University"',
        'prior_preprint:',
        'doi: "10.5281/zenodo.21926005"',
        'conflicts_of_interest: "The author declares no conflicts of interest."',
        'submission_state: "AUTHOR_REVIEW_REQUIRED"',
    ):
        if marker not in metadata:
            failures.append(f"metadata marker missing: {marker}")

    manifest = json.loads((PACKAGE / "source-manifest.json").read_text(encoding="utf-8"))
    archive_path = ROOT / manifest["archive"]
    archive_payload = archive_path.read_bytes()
    if manifest.get("version") != VERSION or manifest.get("member_count") != 12:
        failures.append("source manifest version or member count mismatch")
    if manifest.get("archive_sha256") != digest(archive_payload):
        failures.append("source archive SHA-256 mismatch")
    with zipfile.ZipFile(archive_path) as archive:
        names = archive.namelist()
        if len(names) != 12 or names.count("main.tex") != 1 or names.count("00README.XXX") != 1:
            failures.append("source archive membership mismatch")
        expected = {row["archive_path"]: row for row in manifest.get("members", [])}
        for name in names:
            row = expected.get(name)
            if row is None or row.get("sha256") != digest(archive.read(name)):
                failures.append(f"source member digest mismatch: {name}")

    receipt = json.loads((PACKAGE / "compile-receipt-v0.16.0.json").read_text(encoding="utf-8"))
    pdf_path = ROOT / receipt["compiled_pdf"]["path"]
    if receipt.get("compiler", {}).get("name") != "Tectonic" or receipt.get("compiler", {}).get("version") != "0.17.0":
        failures.append("compile receipt compiler identity mismatch")
    if receipt["source_archive"].get("sha256") != digest(archive_payload):
        failures.append("compile receipt source archive SHA-256 mismatch")
    if not pdf_path.is_file() or receipt["compiled_pdf"].get("sha256") != digest(pdf_path.read_bytes()):
        failures.append("compiled PDF missing or SHA-256 mismatch")
    if receipt["compiled_pdf"].get("pages", 0) < 1 or receipt["compile_result"].get("errors") != 0:
        failures.append("compiled PDF page count or compile error state mismatch")
    if receipt["compile_result"].get("overfull_or_underfull_boxes") != 0:
        failures.append("compile receipt records an overfull or underfull box")
    if receipt["placement_audit"].get("post_references_displays") != []:
        failures.append("a table or figure appears after References")

    for command in (
        [sys.executable, "analysis/derive_event_control_results.py", "--check"],
        [sys.executable, "scripts/build_v0_16_claim_map.py", "--check"],
        [sys.executable, "scripts/run_coe_integrity_audit.py", "--check"],
    ):
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
        if result.returncode != 0:
            failures.append((result.stdout + result.stderr).strip())

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print(f"Preprints.org package validation: FAIL ({len(failures)} error(s))")
        return 1

    print("working-paper package validation: PASS_WITH_OPEN_GATES (compile and placement review passed; 40 claims; 39/39 mutations detected; author review and external submission remain open)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
