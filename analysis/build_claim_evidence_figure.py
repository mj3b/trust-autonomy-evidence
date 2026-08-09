#!/usr/bin/env python3
"""Build and validate the v0.6.0 claim-evidence integrity matrix."""

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
from matplotlib.colors import ListedColormap  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402


STUB = "fig-a3-claim-evidence-integrity"
CSV_PATH = Path("figures/data") / f"{STUB}.csv"
PNG_PATH = Path("figures/generated") / f"{STUB}.png"
SVG_PATH = Path("figures/generated") / f"{STUB}.svg"
MANIFEST_PATH = Path("figures/v0.6.0-manifest.json")
INPUTS = (
    Path("analysis/build_claim_evidence_figure.py"),
    Path("figures/specifications/claim-evidence-integrity.json"),
    Path("evidence/claim-evidence-map.json"),
    Path("audits/v0.6.0/audit-results.json"),
)
OUTPUTS = (CSV_PATH, PNG_PATH, SVG_PATH)
GATES = (
    ("traceability", "Traceability"),
    ("integrity", "Integrity"),
    ("support", "Support review"),
    ("evidence_fitness", "Evidence fitness"),
    ("dependency_closure", "Dependency closure"),
    ("conclusion_eligible", "Conclusion eligible"),
)
STATE_ORDER = ("pass", "fail", "indeterminate", "outside_scope", "eligible", "blocked")
STATE_CODE = {"pass": "P", "fail": "F", "indeterminate": "I", "outside_scope": "O", "eligible": "E", "blocked": "B"}
STATE_LABEL = {
    "pass": "Pass",
    "fail": "Fail",
    "indeterminate": "Indeterminate",
    "outside_scope": "Outside scope",
    "eligible": "Eligible",
    "blocked": "Ineligible",
}
STATE_COLOR = {
    "pass": "#0072B2",
    "fail": "#D55E00",
    "indeterminate": "#8E5AA9",
    "outside_scope": "#B7B7B7",
    "eligible": "#009E73",
    "blocked": "#5A6772",
}


def read_json(relative: Path) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_rows() -> list[dict[str, str]]:
    result = read_json(Path("audits/v0.6.0/audit-results.json"))
    rows = []
    for claim in result["claim_results"]:
        row = {"claim_id": claim["claim_id"]}
        for gate, _ in GATES:
            if gate == "conclusion_eligible":
                row[gate] = "eligible" if claim[gate] else "blocked"
            else:
                row[gate] = claim[gate]
        rows.append(row)
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["claim_id", *[gate for gate, _ in GATES]], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_figure(output_root: Path) -> None:
    rows = table_rows()
    csv_path = output_root / CSV_PATH
    png_path = output_root / PNG_PATH
    svg_path = output_root / SVG_PATH
    write_csv(csv_path, rows)

    values = []
    states = []
    for row in rows:
        row_states = [row[gate] for gate, _ in GATES]
        states.append(row_states)
        values.append([STATE_ORDER.index(state) for state in row_states])

    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "text.color": "#17212B",
        "svg.hashsalt": "trust-autonomy-evidence-coe-v0.6.0",
    })
    fig, ax = plt.subplots(figsize=(12.6, 9.5))
    cmap = ListedColormap([STATE_COLOR[state] for state in STATE_ORDER])
    ax.imshow(values, aspect="auto", cmap=cmap, vmin=-0.5, vmax=len(STATE_ORDER) - 0.5)
    ax.set_xticks(range(len(GATES)))
    ax.set_xticklabels([label for _, label in GATES], fontsize=9.5)
    ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False, length=0, pad=9)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([row["claim_id"] for row in rows], fontsize=9.5)
    ax.tick_params(axis="y", length=0, pad=8)
    ax.set_xticks([value - 0.5 for value in range(1, len(GATES))], minor=True)
    ax.set_yticks([value - 0.5 for value in range(1, len(rows))], minor=True)
    ax.grid(which="minor", color="#FFFFFF", linewidth=1.5)
    ax.tick_params(which="minor", bottom=False, left=False)
    for spine in ax.spines.values():
        spine.set_visible(False)

    for y, row_states in enumerate(states):
        for x, state in enumerate(row_states):
            text_color = "#17212B" if state == "outside_scope" else "#FFFFFF"
            ax.text(x, y, STATE_CODE[state], ha="center", va="center", color=text_color, weight="bold", fontsize=9.5)

    fig.subplots_adjust(left=0.16, right=0.98, top=0.78, bottom=0.16)
    fig.text(0.16, 0.94, "Evidence fitness determines conclusion eligibility", ha="left", va="top", fontsize=17, weight="bold")
    fig.text(0.16, 0.905, "Fifteen material claims across five evidence gates and one conclusion-eligibility decision", ha="left", va="top", fontsize=10.5, color="#5A6772")
    fig.text(0.16, 0.865, "The versioned Oko correction closes the prior fitness failure; independent validity remains outside scope.", ha="left", va="top", fontsize=10.5, color="#0072B2", weight="bold")

    legend_states = ("pass", "fail", "indeterminate", "outside_scope", "eligible", "blocked")
    legend = [Patch(facecolor=STATE_COLOR[state], label=f"{STATE_CODE[state]}  {STATE_LABEL[state]}") for state in legend_states]
    fig.legend(handles=legend, loc="lower left", bbox_to_anchor=(0.155, 0.07), ncol=3, frameon=False, fontsize=9, columnspacing=1.5)
    fig.text(0.16, 0.025, "Source: v0.6.0 claim map and integrity audit. States are categorical. No numeric score is calculated.", ha="left", va="bottom", fontsize=8.5, color="#5A6772")

    png_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(png_path, dpi=200, bbox_inches="tight", metadata={"Software": "Trust, Autonomy, and Evidence v0.6 figure builder"})
    fig.savefig(svg_path, bbox_inches="tight", metadata={"Creator": "Trust, Autonomy, and Evidence v0.6 figure builder", "Date": None})
    svg_text = svg_path.read_text(encoding="utf-8")
    svg_path.write_text("\n".join(line.rstrip() for line in svg_text.splitlines()) + "\n", encoding="utf-8")
    plt.close(fig)


def manifest_entry(path: Path, relative: Path) -> dict:
    return {"path": relative.as_posix(), "bytes": path.stat().st_size, "sha256": sha256(path)}


def write_manifest(output_root: Path) -> None:
    manifest = {
        "version": "0.6.0",
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
        rebuilt_csv = rebuilt / CSV_PATH
        if not (ROOT / CSV_PATH).is_file() or (ROOT / CSV_PATH).read_bytes() != rebuilt_csv.read_bytes():
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
        errors.append("v0.6 figure manifest is missing")
        return errors
    manifest = read_json(MANIFEST_PATH)
    for group, paths in (("artifacts", OUTPUTS), ("inputs", INPUTS)):
        indexed = {row["path"]: row for row in manifest.get(group, [])}
        if set(indexed) != {path.as_posix() for path in paths}:
            errors.append(f"v0.6 figure manifest {group} path set mismatch")
            continue
        for relative in paths:
            path = ROOT / relative
            row = indexed[relative.as_posix()]
            if not path.is_file() or path.stat().st_size != row["bytes"] or sha256(path) != row["sha256"]:
                errors.append(f"v0.6 figure manifest mismatch: {relative.as_posix()}")
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
    print("claim-evidence figure: PASS (15 claims; 6 categorical decisions per claim)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
