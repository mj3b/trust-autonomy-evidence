#!/usr/bin/env python3
"""Validate the v0.14 arXiv review package without submitting it."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

try:
    from pypdf import PdfReader
except ModuleNotFoundError:  # pragma: no cover - exercised in the macOS system-Python fallback
    PdfReader = None


ROOT = Path(__file__).resolve().parents[1]
ARXIV = ROOT / "paper/arxiv"
AUTHOR = "Mark Julius Banasihan"
ORCID = "0009-0001-8121-2878"
REQUIRED = (
    "paper/arxiv/main.tex",
    "paper/arxiv/preprint-v0.14.0.pdf",
    "paper/arxiv/overleaf-compiled-v0.14.0.pdf",
    "paper/arxiv/overleaf-compile-receipt.json",
    "paper/arxiv/arxiv-source-v0.14.0.zip",
    "paper/arxiv/source-manifest.json",
    "paper/arxiv/figures-bw-manifest.json",
    "paper/arxiv/metadata.yaml",
    "paper/arxiv/00README.XXX",
    "paper/arxiv/README.md",
    "paper/preprint-readiness-v0.14.0.md",
)


def sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def extract_pdf_pages(path: Path, page_count: int) -> list[str]:
    """Extract per-page text with pypdf or the local Poppler fallback."""
    if PdfReader is not None:
        return [page.extract_text() or "" for page in PdfReader(path).pages]
    if not shutil.which("pdftotext"):
        raise RuntimeError("neither pypdf nor pdftotext is available for display-placement validation")
    pages = []
    for page_number in range(1, page_count + 1):
        completed = subprocess.run(
            ["pdftotext", "-f", str(page_number), "-l", str(page_number), "-layout", str(path), "-"],
            text=True,
            capture_output=True,
            check=False,
        )
        if completed.returncode:
            raise RuntimeError(completed.stderr.strip() or f"pdftotext failed on page {page_number}")
        pages.append(completed.stdout)
    return pages


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED:
        path = ROOT / relative
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"missing or empty file: {relative}")

    proposition = subprocess.run(
        [sys.executable, "scripts/validate_forward_citation_proposition_review_v0_14_0.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if proposition.returncode:
        errors.append("proposition-review validator failed: " + (proposition.stdout + proposition.stderr).strip())

    tex = (ARXIV / "main.tex").read_text(encoding="utf-8")
    abstract_match = re.search(
        r"\\begin\{TAEAbstractBox\}.*?\\small\s*\n(.*?)\n\\textbf\{Keywords:",
        tex,
        flags=re.DOTALL,
    )
    if abstract_match is None:
        abstract_words = 0
        errors.append("historical LaTeX abstract could not be located")
    else:
        abstract_text = re.sub(r"\\[A-Za-z]+(?:\[[^]]*\])?", " ", abstract_match.group(1))
        abstract_text = re.sub(r"[{}~]", " ", abstract_text)
        abstract_words = len(re.findall(r"\b[\w'-]+\b", abstract_text))
    if not 150 <= abstract_words <= 250:
        errors.append(f"abstract contains {abstract_words} words; expected 150 to 250")
    for marker in (
        AUTHOR,
        ORCID,
        "Preprint candidate v0.14.0",
        "Five received bounded manuscript permission",
        "All 76 recovered-content records have a screening decision",
    ):
        if marker not in tex:
            errors.append(f"historical LaTeX marker missing: {marker}")

    for marker in (
        r"\documentclass[11pt]{article}",
        r"\usepackage{XCharter}",
        r"\usepackage{placeins}",
        r"\begin{TAETitleBox}",
        r"\begin{TAEAbstractBox}",
        AUTHOR,
        ORCID,
        r"\section*{1. Introduction}",
        r"\section*{8. Conclusion}",
        r"\section*{References}",
        r"\end{document}",
    ):
        if marker not in tex:
            errors.append(f"LaTeX marker missing: {marker}")
    if re.search(r"\[@[A-Za-z0-9_:.+-]+", tex) or "LINKTOKEN" in tex:
        errors.append("LaTeX source contains unresolved citation or link tokens")
    begins = re.findall(r"\\begin\{([^}]+)\}", tex)
    ends = re.findall(r"\\end\{([^}]+)\}", tex)
    if sorted(begins) != sorted(ends):
        errors.append("LaTeX environment counts are unbalanced")
    headings = list(re.finditer(r"^\\section\*\{", tex, flags=re.MULTILINE))
    for heading in headings:
        prior_lines = tex[: heading.start()].rstrip().splitlines()
        if not prior_lines or prior_lines[-1] != r"\FloatBarrier":
            errors.append("LaTeX major heading lacks an immediate float barrier")
            break

    figure_paths = re.findall(r"\\includegraphics\[[^]]*\]\{figures/([^}]+)\}", tex)
    if len(figure_paths) != 10 or len(set(figure_paths)) != 10:
        errors.append(f"LaTeX source references {len(figure_paths)} figures; expected 10")
    for name in figure_paths:
        if not (ROOT / "figures/generated" / name).is_file():
            errors.append(f"LaTeX figure source is missing: {name}")

    monochrome = json.loads((ARXIV / "figures-bw-manifest.json").read_text(encoding="utf-8"))
    if monochrome.get("figure_count") != 10:
        errors.append("monochrome figure manifest must contain ten derivatives")
    for row in monochrome.get("figures", []):
        output = ROOT / row.get("output", "")
        if (
            row.get("mode") != "L"
            or not output.is_file()
            or row.get("bytes") != output.stat().st_size
            or row.get("output_sha256") != sha256(output.read_bytes())
        ):
            errors.append(f"monochrome figure mismatch: {row.get('name', '')}")

    pdf = (ARXIV / "preprint-v0.14.0.pdf").read_bytes()
    if not pdf.startswith(b"%PDF-") or len(pdf) < 100_000:
        errors.append("review PDF is invalid or unexpectedly small")
    review_page_count = len(re.findall(rb"/Type\s*/Page\b", pdf))
    if not 12 <= review_page_count <= 50:
        errors.append(f"review PDF contains {review_page_count} page objects; expected 12 to 50")

    overleaf_pdf = (ARXIV / "overleaf-compiled-v0.14.0.pdf").read_bytes()
    if not overleaf_pdf.startswith(b"%PDF-") or len(overleaf_pdf) < 100_000:
        errors.append("Overleaf PDF is invalid or unexpectedly small")
    overleaf_page_count = len(re.findall(rb"/Type\s*/Page\b", overleaf_pdf))
    if not 12 <= overleaf_page_count <= 50:
        errors.append(f"Overleaf PDF contains {overleaf_page_count} page objects; expected 12 to 50")
    if pdf != overleaf_pdf:
        errors.append("canonical preprint PDF differs from the approved Overleaf PDF")

    receipt = json.loads((ARXIV / "overleaf-compile-receipt.json").read_text(encoding="utf-8"))
    try:
        extracted_pages = [
            re.sub(r"\bT\s+able\b", "Table", text)
            for text in extract_pdf_pages(ARXIV / "overleaf-compiled-v0.14.0.pdf", overleaf_page_count)
        ]
    except RuntimeError as error:
        extracted_pages = []
        errors.append(f"display-placement extraction failed: {error}")
    placement = receipt.get("placement_audit", {})
    reference_page = placement.get("references_page")
    expected_displays = placement.get("display_pages", {})
    if not isinstance(reference_page, int) or len(expected_displays) != 17:
        errors.append("display-placement receipt must record all ten figures, seven tables, and the References page")
    elif not (1 <= reference_page <= len(extracted_pages)) or "References" not in extracted_pages[reference_page - 1]:
        errors.append("References heading differs from its recorded page")
    else:
        for label, page_number in expected_displays.items():
            if not (1 <= page_number < reference_page) or label not in extracted_pages[page_number - 1]:
                errors.append(f"display placement differs: {label} is not on recorded page {page_number}")
        post_reference = "\n".join(extracted_pages[reference_page - 1 :])
        for label in expected_displays:
            if label in post_reference:
                errors.append(f"display appears in or after References: {label}")

    expected_receipt = {
        "project_url": "https://www.overleaf.com/project/6a7e1b42384861803d9c9825",
        "errors": 0,
        "pages": overleaf_page_count,
        "source_sha256": sha256((ARXIV / "arxiv-source-v0.14.0.zip").read_bytes()),
        "pdf_sha256": sha256(overleaf_pdf),
    }
    observed_receipt = {
        "project_url": receipt.get("project_url"),
        "errors": receipt.get("compile_result", {}).get("errors"),
        "pages": receipt.get("compiled_pdf", {}).get("pages"),
        "source_sha256": receipt.get("source_archive", {}).get("sha256"),
        "pdf_sha256": receipt.get("compiled_pdf", {}).get("sha256"),
    }
    if observed_receipt != expected_receipt or not isinstance(receipt.get("compile_result", {}).get("warning_groups"), int):
        errors.append("Overleaf compile receipt differs from the preserved source or output")

    if tex.count(r"\begin{table}") != 7 or r"\begin{table*}" in tex:
        errors.append("single-column LaTeX source must contain seven standard tables and no double-column tables")
    if tex.count(r"\begin{figure}") != 10 or r"\begin{figure*}" in tex:
        errors.append("single-column LaTeX source must contain ten standard figures and no double-column figures")
    for marker in (
        r"\begin{tabularx}",
        r"\toprule",
        r"\midrule",
        r"\bottomrule",
        r"\usepackage[table]{xcolor}",
        r"\definecolor{TAENavy}{HTML}{0B1F3A}",
        r"\definecolor{TAEPaleNavy}{HTML}{EDF1F5}",
        r"colorlinks=true",
        r"\rowcolor{TAEPaleNavy}",
        r"\textcolor{TAENavy}",
    ):
        if marker not in tex:
            errors.append(f"LaTeX presentation marker missing: {marker}")
    if r"\begin{longtable}" in tex:
        errors.append("LaTeX source contains the retired single-column table style")

    manifest = json.loads((ARXIV / "source-manifest.json").read_text(encoding="utf-8"))
    archive_path = ARXIV / "arxiv-source-v0.14.0.zip"
    archive_payload = archive_path.read_bytes()
    if manifest.get("archive_sha256") != sha256(archive_payload):
        errors.append("source archive digest differs from its manifest")
    with zipfile.ZipFile(archive_path) as archive:
        names = archive.namelist()
        if names != [row["archive_path"] for row in manifest.get("members", [])]:
            errors.append("source archive membership or order differs from its manifest")
        if names.count("main.tex") != 1 or len(names) != 12:
            errors.append("source archive must contain main.tex, 00README.XXX, and ten figures")
        for row in manifest.get("members", []):
            payload = archive.read(row["archive_path"])
            if len(payload) != row["bytes"] or sha256(payload) != row["sha256"]:
                errors.append(f"archive member mismatch: {row['archive_path']}")
            if row["archive_path"].startswith("figures/") and not row["source_path"].startswith("figures/generated/"):
                errors.append(f"archive figure is not the color source derivative: {row['archive_path']}")

    metadata = (ARXIV / "metadata.yaml").read_text(encoding="utf-8")
    for marker in (AUTHOR, ORCID, 'primary_category: "cs.CY"', 'license: "AUTHOR_SELECTION_REQUIRED"'):
        if marker not in metadata:
            errors.append(f"metadata marker missing: {marker}")

    if errors:
        print("arXiv package validation: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "arXiv package validation: PASS "
        f"({abstract_words}-word abstract; {review_page_count}-page canonical preprint; "
        f"{overleaf_page_count}-page matching Overleaf build; single-column navy template; "
        f"10 color figures; 17 placement checks; {manifest['member_count']} source members)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
