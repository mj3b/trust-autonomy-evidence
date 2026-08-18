#!/usr/bin/env python3
"""Build the deterministic Preprints.org v0.15.0 LaTeX source archive."""

from __future__ import annotations

import hashlib
import io
import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "paper/preprints"
VERSION = "0.15.0"
OUTPUT = PACKAGE / f"preprints-source-v{VERSION}.zip"
MANIFEST = PACKAGE / "source-manifest.json"
FIGURE_NAMES = (
    "fig-1-selection-and-stopping.png",
    "fig-2-practical-control-chain.png",
    "fig-3-decision-paths.png",
    "fig-4-trust-evidence-states.png",
    "fig-5-formal-search-and-screening.png",
    "fig-6-evidence-boundaries.png",
    "fig-a1-mutation-response.png",
    "fig-a2-reproducibility-lineage.png",
    "fig-a3-claim-evidence-integrity.png",
    "fig-a4-oko-versioned-correction.png",
)
MEMBERS = [
    (PACKAGE / "main.tex", "main.tex"),
    (PACKAGE / "00README.XXX", "00README.XXX"),
    *[(ROOT / "figures/generated" / name, f"figures/{name}") for name in FIGURE_NAMES],
]


def sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def build() -> tuple[bytes, dict[str, object]]:
    missing = [str(source.relative_to(ROOT)) for source, _ in MEMBERS if not source.is_file()]
    if missing:
        raise SystemExit("missing source members: " + ", ".join(missing))

    member_rows = []
    for source, archive_path in MEMBERS:
        payload = source.read_bytes()
        member_rows.append({
            "archive_path": archive_path,
            "source_path": str(source.relative_to(ROOT)),
            "bytes": len(payload),
            "sha256": sha256(payload),
        })

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for source, archive_path in MEMBERS:
            info = zipfile.ZipInfo(archive_path, date_time=(2000, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, source.read_bytes())
    payload = buffer.getvalue()
    manifest = {
        "version": VERSION,
        "venue": "Preprints.org",
        "archive": str(OUTPUT.relative_to(ROOT)),
        "archive_bytes": len(payload),
        "archive_sha256": sha256(payload),
        "member_count": len(member_rows),
        "members": member_rows,
        "prior_preprint_doi": "10.5281/zenodo.21926005",
        "submission_state": "AUTHOR_CONFIRMATION_REQUIRED",
    }
    return payload, manifest


def main() -> int:
    payload, manifest = build()
    PACKAGE.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(payload)
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Preprints.org source archive: built {manifest['member_count']} members")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
