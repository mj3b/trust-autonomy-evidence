#!/usr/bin/env python3
"""Build and validate the v0.9.0 journal-style claim-evidence matrix."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import struct
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CACHE = Path(tempfile.gettempdir()) / "trust-autonomy-evidence-coe-figure-cache"
CACHE.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(CACHE / "matplotlib"))
os.environ.setdefault("XDG_CACHE_HOME", str(CACHE))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402


STUB = "fig-a3-claim-evidence-integrity"
CSV_PATH = Path("figures/data") / f"{STUB}.csv"
PNG_PATH = Path("figures/generated") / f"{STUB}.png"
SVG_PATH = Path("figures/generated") / f"{STUB}.svg"
MANIFEST_PATH = Path("figures/v0.9.0-claim-evidence-manifest.json")
INPUTS = (
    Path("analysis/build_claim_evidence_figure.py"),
    Path("figures/specifications/claim-evidence-integrity.json"),
    Path("evidence/claim-evidence-map.json"),
    Path("audits/v0.9.0/audit-results.json"),
)
OUTPUTS = (CSV_PATH, PNG_PATH, SVG_PATH)
GATES = (
    ("traceability", "Traceability"),
    ("integrity", "Integrity"),
    ("support", "Support\nreview"),
    ("evidence_fitness", "Evidence\nfitness"),
    ("dependency_closure", "Dependency\nclosure"),
    ("conclusion_eligible", "Conclusion\neligible"),
)
STATE_CODE = {"pass": "P", "fail": "F", "indeterminate": "I", "outside_scope": "O", "eligible": "E", "blocked": "B"}
STATE_LABEL = {
    "pass": "Pass",
    "fail": "Fail",
    "indeterminate": "Indeterminate",
    "outside_scope": "Outside scope",
    "eligible": "Eligible",
    "blocked": "Ineligible",
}
INK = "#202124"
MUTED = "#666B73"
LIGHT = "#D8DCE2"
BLUE = "#2F6FB0"
PAPER = "#FFFFFF"


def read_json(relative: Path) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_rows() -> list[dict[str, str]]:
    result = read_json(Path("audits/v0.9.0/audit-results.json"))
    rows = []
    for claim in result["claim_results"]:
        row = {"claim_id": claim["claim_id"]}
        for gate, _ in GATES:
            row[gate] = ("eligible" if claim[gate] else "blocked") if gate == "conclusion_eligible" else claim[gate]
        rows.append(row)
    return sorted(
        rows,
        key=lambda row: (
            0 if row["claim_id"].startswith("PAPER-") else 1,
            int(row["claim_id"].rsplit("C", 1)[1]),
        ),
    )


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["claim_id", *[gate for gate, _ in GATES]], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def draw_state(ax: plt.Axes, x: int, y: int, state: str) -> None:
    if state in {"pass", "eligible"}:
        ax.scatter(x, y, s=135, marker="o", facecolor=BLUE, edgecolor=BLUE, linewidth=1.0, zorder=3)
        color = PAPER
    elif state in {"fail", "blocked"}:
        ax.scatter(x, y, s=135, marker="X", facecolor=MUTED, edgecolor=MUTED, linewidth=0.8, zorder=3)
        color = PAPER
    elif state == "indeterminate":
        ax.scatter(x, y, s=135, marker="D", facecolor=PAPER, edgecolor=MUTED, linewidth=1.0, zorder=3)
        color = MUTED
    else:
        ax.scatter(x, y, s=120, marker="s", facecolor=PAPER, edgecolor=LIGHT, linewidth=1.0, zorder=3)
        color = MUTED
    ax.text(x, y, STATE_CODE[state], ha="center", va="center", color=color, weight="bold", fontsize=6.4, zorder=4)


def build_figure(output_root: Path) -> None:
    rows = table_rows()
    csv_path, png_path, svg_path = output_root / CSV_PATH, output_root / PNG_PATH, output_root / SVG_PATH
    write_csv(csv_path, rows)

    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 8.5,
        "text.color": INK,
        "figure.facecolor": PAPER,
        "axes.facecolor": PAPER,
        "savefig.facecolor": PAPER,
        "svg.hashsalt": "trust-autonomy-evidence-coe-v0.9.0",
    })
    fig, ax = plt.subplots(figsize=(7.25, 7.35))
    fig.subplots_adjust(left=0.14, right=0.99, top=0.84, bottom=0.12)
    ax.set_xlim(-0.5, len(GATES) - 0.5)
    ax.set_ylim(len(rows) - 0.5, -0.5)
    ax.set_xticks(range(len(GATES)), [label for _, label in GATES], fontsize=7.2)
    ax.tick_params(axis="x", top=True, labeltop=True, bottom=False, labelbottom=False, length=0, pad=7)
    ax.set_yticks(range(len(rows)), [row["claim_id"] for row in rows], fontsize=7.2)
    ax.tick_params(axis="y", length=0, pad=6)
    for y in range(len(rows) + 1):
        ax.axhline(y - 0.5, color=LIGHT, linewidth=0.5, zorder=0)
    for x in range(len(GATES) + 1):
        ax.axvline(x - 0.5, color=LIGHT, linewidth=0.5, zorder=0)
    for y, row in enumerate(rows):
        for x, (gate, _) in enumerate(GATES):
            draw_state(ax, x, y, row[gate])
    for spine in ax.spines.values():
        spine.set_visible(False)
    legend = [
        Line2D([0], [0], marker="o", color="none", markerfacecolor=BLUE, markeredgecolor=BLUE, markersize=7, label="P/E  Pass or eligible"),
        Line2D([0], [0], marker="X", color="none", markerfacecolor=MUTED, markeredgecolor=MUTED, markersize=7, label="F/B  Fail or ineligible"),
        Line2D([0], [0], marker="D", color="none", markerfacecolor=PAPER, markeredgecolor=MUTED, markersize=6.5, label="I  Indeterminate"),
        Line2D([0], [0], marker="s", color="none", markerfacecolor=PAPER, markeredgecolor=LIGHT, markersize=6.5, label="O  Outside scope"),
    ]
    fig.legend(handles=legend, loc="lower center", bbox_to_anchor=(0.56, 0.015), ncol=2, frameon=False, fontsize=6.7, columnspacing=1.2, handletextpad=0.35)
    png_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(png_path, dpi=220, bbox_inches="tight", metadata={"Software": "Trust, Autonomy, and Evidence v0.9 figure builder"})
    fig.savefig(svg_path, bbox_inches="tight", metadata={"Creator": "Trust, Autonomy, and Evidence v0.9 figure builder", "Date": None})
    svg_text = svg_path.read_text(encoding="utf-8")
    svg_path.write_text("\n".join(line.rstrip() for line in svg_text.splitlines()) + "\n", encoding="utf-8")
    plt.close(fig)


def manifest_entry(path: Path, relative: Path) -> dict:
    return {"path": relative.as_posix(), "bytes": path.stat().st_size, "sha256": sha256(path)}


def write_manifest(output_root: Path) -> None:
    manifest = {
        "version": "0.9.0",
        "source_audit": "0.9.0",
        "figure_id": "FIG-A3",
        "hash_algorithm": "sha256",
        "artifacts": [manifest_entry(output_root / relative, relative) for relative in OUTPUTS],
        "inputs": [manifest_entry(ROOT / relative, relative) for relative in INPUTS],
    }
    path = output_root / MANIFEST_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def png_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("invalid PNG signature")
    return struct.unpack(">II", data[16:24])


def validate() -> list[str]:
    errors = []
    with tempfile.TemporaryDirectory() as temporary:
        rebuilt = Path(temporary)
        build_figure(rebuilt)
        if not (ROOT / CSV_PATH).is_file() or (ROOT / CSV_PATH).read_bytes() != (rebuilt / CSV_PATH).read_bytes():
            errors.append(f"{CSV_PATH.as_posix()} differs from regenerated data")
        for relative in (PNG_PATH, SVG_PATH):
            if not (ROOT / relative).is_file():
                errors.append(f"missing figure artifact: {relative.as_posix()}")
        try:
            if png_dimensions(ROOT / PNG_PATH) != png_dimensions(rebuilt / PNG_PATH):
                errors.append("PNG dimensions differ from regenerated figure")
        except (OSError, ValueError) as exc:
            errors.append(f"PNG validation failed: {exc}")
        try:
            ET.parse(ROOT / SVG_PATH)
            ET.parse(rebuilt / SVG_PATH)
        except (OSError, ET.ParseError) as exc:
            errors.append(f"SVG validation failed: {exc}")
    if not (ROOT / MANIFEST_PATH).is_file():
        errors.append("v0.9 claim-evidence figure manifest is missing")
        return errors
    manifest = read_json(MANIFEST_PATH)
    if manifest.get("version") != "0.9.0" or manifest.get("source_audit") != "0.9.0":
        errors.append("v0.9 claim-evidence figure manifest version metadata mismatch")
    for group, paths in (("artifacts", OUTPUTS), ("inputs", INPUTS)):
        indexed = {row["path"]: row for row in manifest.get(group, [])}
        if set(indexed) != {path.as_posix() for path in paths}:
            errors.append(f"v0.9 claim-evidence figure manifest {group} path set mismatch")
            continue
        for relative in paths:
            path = ROOT / relative
            row = indexed[relative.as_posix()]
            if not path.is_file() or path.stat().st_size != row["bytes"] or sha256(path) != row["sha256"]:
                errors.append(f"v0.9 claim-evidence figure manifest mismatch: {relative.as_posix()}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        errors = validate()
        if errors:
            for error in errors:
                print(f"FAIL: {error}")
            return 1
    else:
        build_figure(ROOT)
        write_manifest(ROOT)
    print(f"claim-evidence figure: PASS ({len(table_rows())} claims; 6 categorical decisions per claim)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
