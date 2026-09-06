#!/usr/bin/env python3
"""Build the deterministic v0.17.0 arXiv source package and manifest."""

from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "paper/preprints"
ARCHIVE = PACKAGE / "preprints-source-v0.17.0.zip"
MANIFEST = PACKAGE / "source-manifest-v0.17.0.json"
FIXED_TIME = (2000, 1, 1, 0, 0, 0)

MEMBERS = [
    ("main.tex", PACKAGE / "main.tex"),
    ("00README.XXX", PACKAGE / "00README.XXX"),
    *[
        (f"figures/{name}", ROOT / "figures/generated" / name)
        for name in (
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
    ],
]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    missing = [str(path.relative_to(ROOT)) for _, path in MEMBERS if not path.is_file()]
    if missing:
        raise SystemExit("missing package member(s): " + ", ".join(missing))

    rows = []
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for archive_path, source_path in MEMBERS:
            data = source_path.read_bytes()
            info = zipfile.ZipInfo(archive_path, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
            rows.append({
                "archive_path": archive_path,
                "source_path": str(source_path.relative_to(ROOT)),
                "bytes": len(data),
                "sha256": sha256(data),
            })

    archive_data = ARCHIVE.read_bytes()
    manifest = {
        "version": "0.17.0",
        "venue": "arXiv submission candidate, cs.CY",
        "archive": str(ARCHIVE.relative_to(ROOT)),
        "archive_bytes": len(archive_data),
        "archive_sha256": sha256(archive_data),
        "member_count": len(rows),
        "members": rows,
        "prior_preprint_doi": "10.5281/zenodo.21926005",
        "submission_state": "AUTHOR_APPROVED_PENDING_ARXIV_UPLOAD",
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(
        f"v0.17.0 source package: PASS ({len(rows)} members; "
        f"{len(archive_data)} bytes; {manifest['archive_sha256']})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
