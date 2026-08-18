#!/usr/bin/env python3
"""Synchronize the approved Overleaf build to the canonical preprint path."""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARXIV = ROOT / "paper/arxiv"
SOURCE = ARXIV / "overleaf-compiled-v0.14.0.pdf"
TARGET = ARXIV / "preprint-v0.14.0.pdf"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def valid_pdf(path: Path) -> bool:
    if not path.is_file() or path.stat().st_size < 100_000:
        return False
    payload = path.read_bytes()
    pages = len(re.findall(rb"/Type\s*/Page\b", payload))
    return payload.startswith(b"%PDF-") and 12 <= pages <= 50


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not valid_pdf(SOURCE):
        raise SystemExit("Overleaf PDF is missing or invalid")
    if args.check:
        if not valid_pdf(TARGET) or digest(TARGET) != digest(SOURCE):
            raise SystemExit("canonical preprint differs from the approved Overleaf PDF")
        print(f"canonical preprint sync: PASS ({digest(TARGET)})")
        return 0
    shutil.copyfile(SOURCE, TARGET)
    if digest(TARGET) != digest(SOURCE):
        raise SystemExit("canonical preprint copy failed hash verification")
    print(f"canonical preprint synchronized: {digest(TARGET)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
