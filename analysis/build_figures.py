#!/usr/bin/env python3
"""Build the v0.9.0 journal-style publication figures from committed artifacts."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import struct
import tempfile
import textwrap
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CACHE = Path(tempfile.gettempdir()) / "trust-autonomy-evidence-figure-cache"
CACHE.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(CACHE / "matplotlib"))
os.environ.setdefault("XDG_CACHE_HOME", str(CACHE))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import FancyArrowPatch, Rectangle  # noqa: E402


FIGURE_SET_VERSION = "0.9.0"
SOURCE_RELEASE = "0.8.0"

CASE_ASSESSMENT_PATHS = (
    "assessments/v0.6.0/TAE-PUB-001-oko-1983.json",
    "cases/TAE-PUB-002-patriot-zg710-2003/assessment.json",
    "cases/TAE-PUB-003-patriot-fa18-2003/assessment.json",
)
CASE_LABELS = {
    "TAE-PUB-001": "Oko\n1983",
    "TAE-PUB-002": "Patriot ZG710\n2003",
    "TAE-PUB-003": "Patriot F/A-18C\n2003",
}
CONTROL_FIELDS = (
    "access",
    "comprehension",
    "authority",
    "feasibility",
    "exercise",
    "effect",
    "correction",
    "repair",
    "reform",
)
PRE_ACTION_FIELDS = CONTROL_FIELDS[:6]
CONTROL_LABELS = {
    "access": "Access before action",
    "comprehension": "Comprehension",
    "authority": "Formal authority",
    "feasibility": "Feasible challenge",
    "exercise": "Exercised challenge",
    "effect": "Protective effect",
    "correction": "Correction",
    "repair": "Repair",
    "reform": "Institutional reform",
}
TRUST_FIELDS = (
    "identity",
    "scope",
    "capability",
    "reliability",
    "uncertainty",
    "evidence_completeness",
    "monitoring",
    "human_authority",
    "integrity",
    "reconstructability",
    "harm_correction",
    "governance_update",
)
TRUST_LABELS = {
    "identity": "System identity",
    "scope": "Use and authority scope",
    "capability": "Relevant capability",
    "reliability": "Conditional reliability",
    "uncertainty": "Calibrated uncertainty",
    "evidence_completeness": "Evidence completeness",
    "monitoring": "Independent monitoring",
    "human_authority": "Human authority",
    "integrity": "Record integrity",
    "reconstructability": "Reconstructability",
    "harm_correction": "Harm correction",
    "governance_update": "Governance update",
}

STATE_ORDER = (
    "supported",
    "partially_supported",
    "unsupported",
    "indeterminate",
    "outside_scope",
)
STATE_LABELS = {
    "supported": "Supported",
    "partially_supported": "Partially supported",
    "unsupported": "Unsupported",
    "indeterminate": "Indeterminate",
    "outside_scope": "Outside scope",
}
STATE_CODES = {
    "supported": "S",
    "partially_supported": "P",
    "unsupported": "U",
    "indeterminate": "I",
    "outside_scope": "O",
}

INK = "#202124"
MUTED = "#666B73"
LIGHT = "#D8DCE2"
PALE = "#F5F6F7"
BLUE = "#2F6FB0"
MID_BLUE = "#7FA6CF"
NAVY = "#0B1F3A"
PAPER = "#FFFFFF"

FIGURE_STUBS = (
    "fig-1-selection-and-stopping",
    "fig-2-practical-control-chain",
    "fig-3-decision-paths",
    "fig-4-trust-evidence-states",
    "fig-5-formal-search-and-screening",
    "fig-6-evidence-boundaries",
    "fig-a1-mutation-response",
    "fig-a2-reproducibility-lineage",
    "fig-a4-oko-versioned-correction",
)

SOURCE_INPUTS = (
    "analysis/build_figures.py",
    "figures/specifications/decision-paths.json",
    "figures/specifications/reproducibility-lineage.json",
    "figures/specifications/selection-decisions.json",
    "assessments/generated-results.json",
    "fixtures/mutations/mutations.json",
    "cases/data/candidate-search-output.json",
    "cases/public-case-selection-register.md",
    "assessments/v0.6.0/TAE-PUB-001-oko-1983.json",
    "assessments/v0.6.0/oko-change-ledger.json",
    "protocols/oko-evidence-adjudication-v0.6.0.md",
    "cases/TAE-PUB-002-patriot-zg710-2003/assessment.json",
    "cases/TAE-PUB-003-patriot-fa18-2003/assessment.json",
    "cases/TAE-PUB-001-oko-1983/case-report.md",
    "cases/TAE-PUB-002-patriot-zg710-2003/case-report.md",
    "cases/TAE-PUB-003-patriot-fa18-2003/case-report.md",
    "paper/data/formal-search-v0.7.0.json",
    "paper/data/formal-screening-proposals-v0.7.0.json",
    "paper/data/author-screening-queue-v0.7.0.csv",
    "paper/data/author-screening-decisions-v0.9.0.csv",
    "paper/data/author-screening-gate-v0.9.0.json",
)


def configure_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 8.5,
            "axes.labelcolor": INK,
            "axes.edgecolor": INK,
            "axes.linewidth": 0.7,
            "text.color": INK,
            "xtick.color": INK,
            "ytick.color": INK,
            "xtick.major.width": 0.7,
            "ytick.major.width": 0.7,
            "figure.facecolor": PAPER,
            "axes.facecolor": PAPER,
            "savefig.facecolor": PAPER,
            "svg.hashsalt": "trust-autonomy-evidence-figure-set-v0.9.0",
        }
    )


def read_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def load_assessments() -> list[dict]:
    return sorted((read_json(path) for path in CASE_ASSESSMENT_PATHS), key=lambda row: row["case_id"])


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def save_figure(fig: plt.Figure, output_dir: Path, stub: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    metadata_version = FIGURE_SET_VERSION
    fig.savefig(
        output_dir / f"{stub}.png",
        dpi=220,
        bbox_inches="tight",
        metadata={"Software": f"Trust, Autonomy, and Evidence v{metadata_version} figure builder"},
    )
    svg_path = output_dir / f"{stub}.svg"
    fig.savefig(
        svg_path,
        bbox_inches="tight",
        metadata={"Creator": f"Trust, Autonomy, and Evidence v{metadata_version} figure builder", "Date": None},
    )
    svg_text = svg_path.read_text(encoding="utf-8")
    svg_path.write_text("\n".join(line.rstrip() for line in svg_text.splitlines()) + "\n", encoding="utf-8")
    plt.close(fig)


def square_box(
    ax: plt.Axes,
    xy: tuple[float, float],
    width: float,
    height: float,
    title: str,
    detail: str,
    title_size: float = 8.5,
    detail_size: float = 7.1,
    title_width: int = 18,
    detail_width: int = 22,
) -> None:
    x, y = xy
    ax.add_patch(Rectangle((x, y), width, height, facecolor=PAPER, edgecolor=INK, linewidth=0.8, transform=ax.transAxes))
    ax.text(
        x + width / 2,
        y + height * 0.67,
        textwrap.fill(title, width=title_width),
        ha="center",
        va="center",
        fontsize=title_size,
        weight="semibold",
        linespacing=1.0,
        transform=ax.transAxes,
    )
    ax.text(
        x + width / 2,
        y + height * 0.28,
        textwrap.fill(detail, width=detail_width, replace_whitespace=False),
        ha="center",
        va="center",
        fontsize=detail_size,
        color=MUTED,
        linespacing=1.08,
        transform=ax.transAxes,
    )


def arrow(ax: plt.Axes, start: tuple[float, float], end: tuple[float, float], color: str = MUTED) -> None:
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=8,
            linewidth=0.8,
            color=color,
            transform=ax.transAxes,
            clip_on=False,
        )
    )


def build_selection_figure(data_dir: Path, figure_dir: Path) -> None:
    candidates = read_json("cases/data/candidate-search-output.json")
    decisions = read_json("figures/specifications/selection-decisions.json")["screening"]
    if [row["candidate_id"] for row in candidates["candidates"][:5]] != [row["candidate_id"] for row in decisions]:
        raise ValueError("Selection figure input does not match the frozen candidate order")

    aiid = candidates["inputs"]["aiid"]["counts"]
    oecd = candidates["inputs"]["oecd_counts"]
    total = candidates["candidate_count"]
    screened = len(decisions)
    selected = sum(row["result"] == "selected" for row in decisions)
    excluded = sum(row["result"] == "excluded" for row in decisions)
    unscreened = total - screened
    rows = [
        {"metric": "AIID incident records", "value": aiid["incident_records"], "source": "candidate-search-output.json"},
        {"metric": "AIID report records", "value": aiid["report_records"], "source": "candidate-search-output.json"},
        {"metric": "AIID candidate records", "value": aiid["candidate_records"], "source": "candidate-search-output.json"},
        {"metric": "OECD exported candidate records", "value": oecd["candidate_records"], "source": "candidate-search-output.json"},
        {"metric": "Preserved candidate records", "value": total, "source": "candidate-search-output.json"},
        {"metric": "Screened records", "value": screened, "source": "selection-decisions.json"},
        {"metric": "Selected records", "value": selected, "source": "selection-decisions.json"},
        {"metric": "Excluded records", "value": excluded, "source": "selection-decisions.json"},
        {"metric": "Unscreened records", "value": unscreened, "source": "derived: preserved minus screened"},
        {"metric": "Filled strata", "value": selected, "source": "selection-decisions.json"},
    ]
    write_csv(data_dir / "fig-1-selection-and-stopping.csv", ["metric", "value", "source"], rows)

    fig, ax = plt.subplots(figsize=(7.25, 3.15))
    ax.set_axis_off()
    square_box(ax, (0.01, 0.62), 0.20, 0.23, "AIID", f"{aiid['candidate_records']:,} matched\nrecords")
    square_box(ax, (0.01, 0.20), 0.20, 0.23, "OECD export", f"{oecd['candidate_records']:,} candidate\nrecords")
    square_box(ax, (0.29, 0.41), 0.20, 0.25, f"{total:,} preserved", "fixed vocabulary\nand ordering")
    square_box(ax, (0.58, 0.41), 0.16, 0.25, f"{screened} screened", "first five AIID\nrecords")
    square_box(ax, (0.82, 0.64), 0.16, 0.20, f"{selected} selected", "three strata filled")
    square_box(ax, (0.82, 0.34), 0.16, 0.20, f"{excluded} excluded", "source or boundary", detail_size=6.5)
    square_box(ax, (0.29, 0.05), 0.20, 0.20, f"{unscreened:,} unscreened", "no decision assigned")
    arrow(ax, (0.21, 0.735), (0.29, 0.57))
    arrow(ax, (0.21, 0.315), (0.29, 0.49))
    arrow(ax, (0.49, 0.535), (0.58, 0.535))
    arrow(ax, (0.74, 0.56), (0.82, 0.71))
    arrow(ax, (0.74, 0.49), (0.82, 0.43))
    arrow(ax, (0.39, 0.41), (0.39, 0.25))
    ax.text(0.90, 0.22, "Stopping rule met", ha="center", va="center", fontsize=7.3, color=BLUE, weight="semibold", transform=ax.transAxes)
    save_figure(fig, figure_dir, "fig-1-selection-and-stopping")


def state_marker(ax: plt.Axes, x: float, y: float, state: str, size: float = 290) -> None:
    if state == "supported":
        ax.scatter(x, y, s=size, marker="o", facecolor=BLUE, edgecolor=BLUE, linewidth=1.0, zorder=3)
        color = PAPER
    elif state == "partially_supported":
        ax.scatter(x, y, s=size, marker="o", facecolor=PAPER, edgecolor=BLUE, linewidth=1.4, zorder=3)
        color = BLUE
    elif state == "unsupported":
        ax.scatter(x, y, s=size, marker="X", facecolor=MUTED, edgecolor=MUTED, linewidth=0.8, zorder=3)
        color = PAPER
    elif state == "indeterminate":
        ax.scatter(x, y, s=size, marker="D", facecolor=PAPER, edgecolor=MUTED, linewidth=1.2, zorder=3)
        color = MUTED
    else:
        ax.scatter(x, y, s=size * 0.75, marker="s", facecolor=PAPER, edgecolor=LIGHT, linewidth=1.0, zorder=3)
        color = MUTED
    ax.text(x, y, STATE_CODES[state], ha="center", va="center", fontsize=6.6, weight="bold", color=color, zorder=4)


def state_legend() -> list[Line2D]:
    return [
        Line2D([0], [0], marker="o", color="none", markerfacecolor=BLUE, markeredgecolor=BLUE, markersize=7.5, label="S  Supported"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor=PAPER, markeredgecolor=BLUE, markersize=7.5, label="P  Partially supported"),
        Line2D([0], [0], marker="X", color="none", markerfacecolor=MUTED, markeredgecolor=MUTED, markersize=7.5, label="U  Unsupported"),
        Line2D([0], [0], marker="D", color="none", markerfacecolor=PAPER, markeredgecolor=MUTED, markersize=6.8, label="I  Indeterminate"),
        Line2D([0], [0], marker="s", color="none", markerfacecolor=PAPER, markeredgecolor=LIGHT, markersize=6.8, label="O  Outside scope"),
    ]


def categorical_matrix(
    assessments: list[dict],
    section: str,
    fields: tuple[str, ...],
    labels: dict[str, str],
    stub: str,
    data_dir: Path,
    figure_dir: Path,
) -> None:
    rows = []
    for field in fields:
        for assessment in assessments:
            finding = assessment[section][field]
            rows.append(
                {
                    "case_id": assessment["case_id"],
                    "case_title": assessment["title"],
                    "proposition": field,
                    "state": finding["state"],
                    "evidence_refs": ";".join(finding["evidence_refs"]),
                }
            )
    write_csv(data_dir / f"{stub}.csv", ["case_id", "case_title", "proposition", "state", "evidence_refs"], rows)

    height = 4.9 if len(fields) <= 9 else 5.9
    fig, ax = plt.subplots(figsize=(7.25, height))
    fig.subplots_adjust(left=0.34, right=0.98, top=0.84, bottom=0.15)
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(len(fields) - 0.5, -0.5)
    ax.set_xticks(range(3), [CASE_LABELS[row["case_id"]] for row in assessments], fontsize=8.2)
    ax.tick_params(axis="x", top=True, labeltop=True, bottom=False, labelbottom=False, length=0, pad=8)
    ax.set_yticks(range(len(fields)), [labels[field] for field in fields], fontsize=8.1)
    ax.tick_params(axis="y", length=0, pad=8)
    for y in range(len(fields) + 1):
        ax.axhline(y - 0.5, color=LIGHT, linewidth=0.55, zorder=0)
    for x in (0.5, 1.5):
        ax.axvline(x, color=LIGHT, linewidth=0.55, zorder=0)
    if section == "practical_control":
        ax.axhline(5.5, color=INK, linewidth=0.8, zorder=1)
    for y, field in enumerate(fields):
        for x, assessment in enumerate(assessments):
            state_marker(ax, x, y, assessment[section][field]["state"], size=265)
    for spine in ax.spines.values():
        spine.set_visible(False)
    fig.legend(handles=state_legend(), loc="lower center", bbox_to_anchor=(0.58, 0.015), ncol=3, frameon=False, fontsize=6.8, columnspacing=1.2, handletextpad=0.35)
    save_figure(fig, figure_dir, stub)


def build_decision_paths(data_dir: Path, figure_dir: Path) -> None:
    specification = read_json("figures/specifications/decision-paths.json")
    rows = []
    for case in specification["cases"]:
        for event in case["events"]:
            rows.append(
                {
                    "case_id": case["case_id"],
                    "case_title": case["short_title"],
                    "order": event["order"],
                    "event": event["event"],
                    "kind": event["kind"],
                    "evidence_refs": ";".join(event["evidence_refs"]),
                    "case_annotation": case["annotation"],
                }
            )
    write_csv(data_dir / "fig-3-decision-paths.csv", ["case_id", "case_title", "order", "event", "kind", "evidence_refs", "case_annotation"], rows)

    kinds = {
        "system_output": (BLUE, "System output"),
        "evidence_check": (MID_BLUE, "Evidence check"),
        "human_decision": (BLUE, "Human decision"),
        "human_action": (BLUE, "Human action"),
        "system_action": (MUTED, "System action"),
        "bounded_effect": (BLUE, "Bounded effect"),
        "harm_outcome": (MUTED, "Harm outcome"),
    }
    fig, ax = plt.subplots(figsize=(7.25, 4.65))
    fig.subplots_adjust(left=0.15, right=0.98, top=0.96, bottom=0.15)
    ax.set_xlim(-0.35, 4.35)
    ax.set_ylim(-0.60, 2.55)
    ax.set_axis_off()
    y_positions = {"TAE-PUB-001": 2.0, "TAE-PUB-002": 1.0, "TAE-PUB-003": 0.0}
    for case in specification["cases"]:
        y = y_positions[case["case_id"]]
        ax.annotate("", xy=(4.25, y), xytext=(-0.10, y), arrowprops={"arrowstyle": "-|>", "color": LIGHT, "linewidth": 0.9})
        ax.text(-0.18, y, case["short_title"], ha="right", va="center", fontsize=7.7, weight="semibold")
        for event in case["events"]:
            x = event["order"] - 1
            color = kinds[event["kind"]][0]
            ax.scatter(x, y, s=105, facecolor=PAPER, edgecolor=color, linewidth=1.3, zorder=3)
            ax.text(x, y, str(event["order"]), ha="center", va="center", fontsize=6.7, weight="bold", color=color, zorder=4)
            label_y = y + 0.18 if event["order"] % 2 else y - 0.18
            va = "bottom" if event["order"] % 2 else "top"
            ax.text(x, label_y, textwrap.fill(event["event"], width=18), ha="center", va=va, fontsize=6.6, linespacing=1.1)
        if case["case_id"] == "TAE-PUB-002":
            ax.text(1.5, y + 0.08, "≈1 minute", ha="center", va="bottom", fontsize=6.5, color=BLUE)
        if case["case_id"] == "TAE-PUB-003":
            ax.plot([1.15, 2.85], [y - 0.48, y - 0.48], color=MUTED, linestyle=(0, (2, 2)), linewidth=0.8)
            ax.text(2.0, y - 0.44, "public record gap", ha="center", va="bottom", fontsize=6.5, color=MUTED)
    legend = [Line2D([0], [0], marker="o", color="none", markerfacecolor=PAPER, markeredgecolor=color, markersize=6, label=label) for color, label in dict(kinds.values()).items()]
    fig.legend(handles=legend, loc="lower center", bbox_to_anchor=(0.56, 0.015), ncol=4, frameon=False, fontsize=6.5, columnspacing=1.0, handletextpad=0.3)
    save_figure(fig, figure_dir, "fig-3-decision-paths")


def build_formal_search(data_dir: Path, figure_dir: Path) -> None:
    search = read_json("paper/data/formal-search-v0.7.0.json")
    proposals = read_json("paper/data/formal-screening-proposals-v0.7.0.json")
    gate = read_json("paper/data/author-screening-gate-v0.9.0.json")
    direct = sum(run["record_count"] for run in search["search_runs"].values())
    chain = sum(item["reference_count"] + item["citation_count"] for item in search["citation_chains"].values())
    pooled = search["pooled_record_count"]
    deduplicated = search["deduplicated_record_count"]
    proposal_counts = proposals["counts"]
    author_counts = gate["author_counts"]
    author_queue = gate["records"]
    final_counts = {
        "retain-close": author_counts["retain-close"],
        "retain-background": proposal_counts["retain-background"] + author_counts["retain-background"],
        "exclude-single-component": author_counts["exclude-single-component"],
        "exclude-topic": proposal_counts["exclude-topic"] + author_counts["exclude-topic"],
        "inaccessible": proposal_counts["inaccessible"],
        "exclude-outside-cutoff": proposal_counts["exclude-outside-cutoff"],
    }
    rows = [
        {"stage": "Direct queries", "decision": "retrieved", "count": direct, "author_attention": "no", "source": "formal-search-v0.7.0.json"},
        {"stage": "Citation chains", "decision": "retrieved", "count": chain, "author_attention": "no", "source": "formal-search-v0.7.0.json"},
        {"stage": "Combined pool", "decision": "pooled", "count": pooled, "author_attention": "no", "source": "formal-search-v0.7.0.json"},
        {"stage": "Deduplicated pool", "decision": "deduplicated", "count": deduplicated, "author_attention": "no", "source": "formal-search-v0.7.0.json"},
    ]
    labels = [
        ("Retain close", "retain-close"),
        ("Retain background", "retain-background"),
        ("Exclude single component", "exclude-single-component"),
        ("Exclude topic", "exclude-topic"),
        ("Inaccessible", "inaccessible"),
        ("Outside cutoff", "exclude-outside-cutoff"),
    ]
    for _, key in labels:
        rows.append({"stage": "Preliminary triage", "decision": key, "count": proposal_counts[key], "author_attention": "yes" if key in {"retain-close", "exclude-single-component"} else "no", "source": "formal-screening-proposals-v0.7.0.json"})
    for _, key in labels:
        rows.append({"stage": "Final screening", "decision": key, "count": final_counts[key], "author_attention": "complete" if key not in {"inaccessible"} else "separate gate", "source": "derived from author-screening-decisions-v0.9.0.csv and formal-screening-proposals-v0.7.0.json"})
    rows.append({"stage": "Author gate", "decision": "closed queue", "count": author_queue, "author_attention": "complete", "source": "author-screening-gate-v0.9.0.json"})
    write_csv(data_dir / "fig-5-formal-search-and-screening.csv", ["stage", "decision", "count", "author_attention", "source"], rows)

    fig = plt.figure(figsize=(7.25, 4.45))
    gs = fig.add_gridspec(1, 2, width_ratios=(0.92, 1.38), wspace=0.40)
    left = fig.add_subplot(gs[0, 0])
    left.set_axis_off()
    square_box(left, (0.05, 0.73), 0.38, 0.18, "Direct queries", f"{direct:,} records", title_size=7.5)
    square_box(left, (0.57, 0.73), 0.38, 0.18, "Citation chains", f"{chain:,} records", title_size=7.5)
    square_box(left, (0.31, 0.42), 0.38, 0.18, "Combined", f"{pooled:,} records", title_size=7.5)
    square_box(left, (0.31, 0.12), 0.38, 0.18, "Deduplicated", f"{deduplicated:,} records", title_size=7.5)
    arrow(left, (0.24, 0.73), (0.42, 0.60))
    arrow(left, (0.76, 0.73), (0.58, 0.60))
    arrow(left, (0.50, 0.42), (0.50, 0.30))
    left.text(0.50, 0.98, "Retrieval", ha="center", va="top", fontsize=8.2, weight="semibold", transform=left.transAxes)

    right = fig.add_subplot(gs[0, 1])
    y = list(range(len(labels)))
    values = [final_counts[key] for _, key in labels]
    colors = [BLUE if key in {"retain-close", "retain-background"} else MUTED for _, key in labels]
    right.set_xscale("log")
    right.hlines(y, 1, values, color=LIGHT, linewidth=1.0, zorder=1)
    right.scatter(values, y, s=42, facecolor=colors, edgecolor=colors, zorder=2)
    for yi, value in zip(y, values):
        right.text(value * 1.16, yi, f"{value:,}", va="center", ha="left", fontsize=7.2)
    right.set_yticks(y, [label for label, _ in labels], fontsize=7.5)
    right.invert_yaxis()
    right.set_xlim(1, 2200)
    right.set_xlabel("Records (log scale)", fontsize=7.2)
    right.grid(axis="x", color=LIGHT, linewidth=0.55)
    right.tick_params(axis="y", length=0, pad=6)
    right.tick_params(axis="x", labelsize=6.8)
    right.spines[["top", "right", "left"]].set_visible(False)
    right.text(0.50, 1.02, "Final screening state", ha="center", va="bottom", fontsize=8.2, weight="semibold", transform=right.transAxes)
    right.text(0.02, -0.20, f"Author gate: {author_queue}/{author_queue} decisions complete", ha="left", va="top", fontsize=7.2, color=BLUE, weight="semibold", transform=right.transAxes)
    fig.subplots_adjust(left=0.04, right=0.96, top=0.91, bottom=0.21)
    save_figure(fig, figure_dir, "fig-5-formal-search-and-screening")


def build_evidence_boundaries(assessments: list[dict], data_dir: Path, figure_dir: Path) -> None:
    displayed_states = ("supported", "partially_supported", "unsupported", "indeterminate")
    rows = []
    for assessment in assessments:
        findings = assessment["practical_control"]
        for state in displayed_states:
            stages = [field for field in PRE_ACTION_FIELDS if findings[field]["state"] == state]
            rows.append(
                {
                    "case_id": assessment["case_id"],
                    "case_title": assessment["title"],
                    "state": state,
                    "count": len(stages),
                    "stages": ";".join(stages),
                    "denominator": len(PRE_ACTION_FIELDS),
                }
            )
        outside = [field for field in PRE_ACTION_FIELDS if findings[field]["state"] == "outside_scope"]
        if outside:
            raise ValueError(f"pre-action evidence-boundary figure contains outside-scope fields: {outside}")
    write_csv(
        data_dir / "fig-6-evidence-boundaries.csv",
        ["case_id", "case_title", "state", "count", "stages", "denominator"],
        rows,
    )

    styles = {
        "supported": {"color": BLUE, "edgecolor": BLUE, "hatch": "", "text": PAPER},
        "partially_supported": {"color": MID_BLUE, "edgecolor": BLUE, "hatch": "///", "text": INK},
        "unsupported": {"color": MUTED, "edgecolor": MUTED, "hatch": "xx", "text": PAPER},
        "indeterminate": {"color": PAPER, "edgecolor": MUTED, "hatch": "..", "text": INK},
    }
    fig, ax = plt.subplots(figsize=(7.25, 3.35))
    fig.subplots_adjust(left=0.25, right=0.98, top=0.80, bottom=0.22)
    for y, assessment in enumerate(assessments):
        left = 0
        for state in displayed_states:
            count = sum(
                assessment["practical_control"][field]["state"] == state
                for field in PRE_ACTION_FIELDS
            )
            if count == 0:
                continue
            style = styles[state]
            ax.barh(
                y,
                count,
                left=left,
                height=0.58,
                color=style["color"],
                edgecolor=style["edgecolor"],
                hatch=style["hatch"],
                linewidth=0.8,
                zorder=2,
            )
            ax.text(
                left + count / 2,
                y,
                f"{STATE_CODES[state]} {count}",
                ha="center",
                va="center",
                fontsize=7.3,
                weight="semibold",
                color=style["text"],
                zorder=3,
            )
            left += count
    ax.set_xlim(0, len(PRE_ACTION_FIELDS))
    ax.set_xticks(range(len(PRE_ACTION_FIELDS) + 1))
    ax.set_xlabel("Pre-action practical-control stages (six per case)", fontsize=7.6)
    ax.set_yticks(
        range(len(assessments)),
        [CASE_LABELS[item["case_id"]].replace("\n", " ") for item in assessments],
        fontsize=7.8,
    )
    ax.invert_yaxis()
    ax.grid(axis="x", color=LIGHT, linewidth=0.5, zorder=0)
    ax.tick_params(axis="y", length=0, pad=8)
    ax.tick_params(axis="x", labelsize=7.0)
    ax.spines[["top", "right", "left"]].set_visible(False)
    legend = [
        Rectangle(
            (0, 0),
            1,
            1,
            facecolor=styles[state]["color"],
            edgecolor=styles[state]["edgecolor"],
            hatch=styles[state]["hatch"],
            label=f"{STATE_CODES[state]}  {STATE_LABELS[state]}",
        )
        for state in displayed_states
    ]
    fig.legend(
        handles=legend,
        loc="upper center",
        bbox_to_anchor=(0.62, 0.97),
        ncol=4,
        frameon=False,
        fontsize=6.9,
        columnspacing=1.1,
        handlelength=1.5,
    )
    save_figure(fig, figure_dir, "fig-6-evidence-boundaries")


def build_mutation_response(data_dir: Path, figure_dir: Path) -> None:
    fixture = read_json("fixtures/mutations/mutations.json")
    results = read_json("assessments/generated-results.json")
    observed = {row["mutation_id"]: row for row in results["mutation_results"]}
    rows = []
    for mutation in fixture["mutations"]:
        result = observed.get(mutation["mutation_id"])
        if result is None or result["status"] != "pass":
            raise ValueError(f"Missing passing mutation result: {mutation['mutation_id']}")
        expected = {(row["assessment"], row["field"], row["from"], row["to"]) for row in mutation["expected_deltas"]}
        actual = {(row["assessment"], row["field"], row["from"], row["to"]) for row in result["deltas"]}
        if expected != actual:
            raise ValueError(f"Mutation delta mismatch: {mutation['mutation_id']}")
        if mutation["expected_deltas"]:
            for delta in mutation["expected_deltas"]:
                rows.append({"mutation_id": mutation["mutation_id"], "base_case_id": mutation["base_case_id"], "purpose": mutation["purpose"], "assessment": delta["assessment"], "field": delta["field"], "from": delta["from"], "to": delta["to"], "result": "pass"})
        else:
            rows.append({"mutation_id": mutation["mutation_id"], "base_case_id": mutation["base_case_id"], "purpose": mutation["purpose"], "assessment": "", "field": "", "from": "", "to": "invariant", "result": "pass"})
    write_csv(data_dir / "fig-a1-mutation-response.csv", ["mutation_id", "base_case_id", "purpose", "assessment", "field", "from", "to", "result"], rows)

    field_order = [
        ("control", "access"), ("control", "authority"), ("trust", "human_authority"), ("trust", "integrity"),
        ("control", "correction"), ("trust", "harm_correction"), ("trust", "monitoring"),
        ("trust", "evidence_completeness"), ("control", "repair"), ("control", "reform"), ("trust", "governance_update"),
    ]
    field_labels = ["Access", "Control\nauthority", "Human\nauthority", "Integrity", "Correction", "Harm\ncorrection", "Monitoring", "Evidence\ncompleteness", "Repair", "Reform", "Governance\nupdate", "No delta"]
    mutations = fixture["mutations"]
    fig, ax = plt.subplots(figsize=(7.25, 5.25))
    fig.subplots_adjust(left=0.13, right=0.99, top=0.84, bottom=0.10)
    ax.set_xlim(-0.5, len(field_labels) - 0.5)
    ax.set_ylim(len(mutations) - 0.5, -0.5)
    ax.set_xticks(range(len(field_labels)), field_labels, fontsize=6.1)
    ax.tick_params(axis="x", top=True, labeltop=True, bottom=False, labelbottom=False, length=0, pad=6)
    ax.set_yticks(range(len(mutations)), [row["mutation_id"].replace("TAE-MUT-", "M") for row in mutations], fontsize=6.8)
    ax.tick_params(axis="y", length=0, pad=5)
    for y in range(len(mutations) + 1):
        ax.axhline(y - 0.5, color=LIGHT, linewidth=0.5, zorder=0)
    for x in range(len(field_labels) + 1):
        ax.axvline(x - 0.5, color=LIGHT, linewidth=0.5, zorder=0)
    target_codes = {"unsupported": "U", "partially_supported": "P", "indeterminate": "I", "invariant": "0"}
    for y, mutation in enumerate(mutations):
        expected = mutation["expected_deltas"]
        if not expected:
            x, target = len(field_labels) - 1, "invariant"
            ax.scatter(x, y, s=105, marker="s", facecolor=PAPER, edgecolor=MUTED, linewidth=1.0)
            ax.text(x, y, target_codes[target], ha="center", va="center", fontsize=6.4, weight="bold", color=MUTED)
            continue
        for delta in expected:
            x, target = field_order.index((delta["assessment"], delta["field"])), delta["to"]
            marker = "X" if target == "unsupported" else ("D" if target == "indeterminate" else "o")
            face = MUTED if target == "unsupported" else PAPER
            edge = MUTED if target in {"unsupported", "indeterminate"} else BLUE
            ax.scatter(x, y, s=105, marker=marker, facecolor=face, edgecolor=edge, linewidth=1.0)
            color = PAPER if target == "unsupported" else edge
            ax.text(x, y, target_codes[target], ha="center", va="center", fontsize=6.3, weight="bold", color=color)
    for spine in ax.spines.values():
        spine.set_visible(False)
    save_figure(fig, figure_dir, "fig-a1-mutation-response")


def build_lineage(data_dir: Path, figure_dir: Path) -> None:
    spec = read_json("figures/specifications/reproducibility-lineage.json")
    rows = []
    for node in spec["nodes"]:
        rows.append({"record_type": "node", "node_id": node["node_id"], "lane": node["lane"], "order": node["order"], "title": node["title"], "detail": node["detail"].replace("\n", " | "), "from": "", "to": ""})
    for edge in spec["edges"]:
        rows.append({"record_type": "edge", "node_id": "", "lane": "", "order": "", "title": "", "detail": "", "from": edge["from"], "to": edge["to"], "relationship": edge.get("label", "")})
    write_csv(data_dir / "fig-a2-reproducibility-lineage.csv", ["record_type", "node_id", "lane", "order", "title", "detail", "from", "to", "relationship"], rows)

    fig, ax = plt.subplots(figsize=(7.25, 3.65))
    ax.set_axis_off()
    lane_nodes = {lane: sorted([node for node in spec["nodes"] if node["lane"] == lane], key=lambda row: row["order"]) for lane in ("research", "figures")}
    positions: dict[str, tuple[float, float]] = {}
    sizes = {"research": (0.118, 0.205), "figures": (0.142, 0.205)}
    lane_y = {"research": 0.62, "figures": 0.14}
    for lane, nodes in lane_nodes.items():
        width, height = sizes[lane]
        left, right = 0.17, 0.98 - width
        step = (right - left) / (len(nodes) - 1)
        for index, node in enumerate(nodes):
            x, y = left + index * step, lane_y[lane]
            positions[node["node_id"]] = (x, y)
            square_box(
                ax,
                (x, y),
                width,
                height,
                node["title"],
                node["detail"],
                title_size=6.2,
                detail_size=5.2,
                title_width=13,
                detail_width=16,
            )
    ax.text(0.135, 0.72, "RESEARCH", ha="right", va="center", fontsize=6.6, color=NAVY, weight="bold", transform=ax.transAxes)
    ax.text(0.135, 0.24, "FIGURE\nPIPELINE", ha="right", va="center", fontsize=6.4, color=MUTED, weight="bold", linespacing=1.0, transform=ax.transAxes)
    lookup = {node["node_id"]: node for node in spec["nodes"]}
    for edge in spec["edges"]:
        start, end = lookup[edge["from"]], lookup[edge["to"]]
        sx, sy = positions[start["node_id"]]
        ex, ey = positions[end["node_id"]]
        sw, sh = sizes[start["lane"]]
        ew, eh = sizes[end["lane"]]
        if start["lane"] == end["lane"]:
            arrow(ax, (sx + sw, sy + sh / 2), (ex, ey + eh / 2))
        else:
            start_x = sx + sw / 2
            end_x = ex + ew / 2
            elbow_y = 0.485
            ax.plot([start_x, start_x, end_x], [sy, elbow_y, elbow_y], color=NAVY, linewidth=0.9, transform=ax.transAxes, clip_on=False)
            arrow(ax, (end_x, elbow_y), (end_x, ey + eh), color=NAVY)
            ax.text(
                (start_x + end_x) / 2,
                elbow_y + 0.026,
                edge.get("label", "Assessment outputs feed figure inputs"),
                ha="center",
                va="bottom",
                fontsize=5.8,
                color=NAVY,
                weight="semibold",
                bbox={"facecolor": PAPER, "edgecolor": "none", "pad": 1.2},
                transform=ax.transAxes,
            )
    save_figure(fig, figure_dir, "fig-a2-reproducibility-lineage")


def build_oko_correction(data_dir: Path, figure_dir: Path) -> None:
    ledger = read_json("assessments/v0.6.0/oko-change-ledger.json")
    rows = []
    for item in ledger["reassessed_fields"]:
        field = item["json_pointer"].split("/")[-2]
        rows.append({"proposition": field, "prior_version": "0.3.0", "prior_state": item["prior_state"], "current_version": "0.6.0", "current_state": item["current_state"], "evidence_refs": ";".join(item["evidence_refs"]), "material_gap": item["material_gap"]})
    write_csv(data_dir / "fig-a4-oko-versioned-correction.csv", ["proposition", "prior_version", "prior_state", "current_version", "current_state", "evidence_refs", "material_gap"], rows)

    labels = [CONTROL_LABELS[row["proposition"]] for row in rows]
    fig, ax = plt.subplots(figsize=(7.25, 3.9))
    fig.subplots_adjust(left=0.28, right=0.94, top=0.83, bottom=0.12)
    ax.set_xlim(-0.22, 1.22)
    ax.set_ylim(len(rows) - 0.5, -0.5)
    ax.set_xticks([0, 1], ["v0.3.0\nSupported", "v0.6.0\nPartially supported"], fontsize=8.0)
    ax.tick_params(axis="x", top=True, labeltop=True, bottom=False, labelbottom=False, length=0, pad=8)
    ax.set_yticks(range(len(rows)), labels, fontsize=8.0)
    ax.tick_params(axis="y", length=0, pad=7)
    for y in range(len(rows)):
        ax.plot([0.08, 0.92], [y, y], color=LIGHT, linewidth=0.8, zorder=1)
        ax.annotate("", xy=(0.92, y), xytext=(0.08, y), arrowprops={"arrowstyle": "-|>", "color": LIGHT, "linewidth": 0.8})
        state_marker(ax, 0, y, "supported", size=230)
        state_marker(ax, 1, y, "partially_supported", size=230)
    for y in range(len(rows) + 1):
        ax.axhline(y - 0.5, color=LIGHT, linewidth=0.5, zorder=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    save_figure(fig, figure_dir, "fig-a4-oko-versioned-correction")


def build_all(output_root: Path) -> None:
    configure_style()
    data_dir = output_root / "figures/data"
    figure_dir = output_root / "figures/generated"
    assessments = load_assessments()
    build_selection_figure(data_dir, figure_dir)
    categorical_matrix(assessments, "practical_control", CONTROL_FIELDS, CONTROL_LABELS, "fig-2-practical-control-chain", data_dir, figure_dir)
    build_decision_paths(data_dir, figure_dir)
    categorical_matrix(assessments, "trust_evidence", TRUST_FIELDS, TRUST_LABELS, "fig-4-trust-evidence-states", data_dir, figure_dir)
    build_formal_search(data_dir, figure_dir)
    build_evidence_boundaries(assessments, data_dir, figure_dir)
    build_mutation_response(data_dir, figure_dir)
    build_lineage(data_dir, figure_dir)
    build_oko_correction(data_dir, figure_dir)


def csv_outputs() -> list[Path]:
    return [Path("figures/data") / f"{stub}.csv" for stub in FIGURE_STUBS]


def image_outputs() -> list[Path]:
    return [Path("figures/generated") / f"{stub}.{extension}" for stub in FIGURE_STUBS for extension in ("png", "svg")]


def expected_outputs() -> list[Path]:
    return csv_outputs() + image_outputs()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def manifest_entry(path: Path, relative: Path) -> dict:
    return {"path": relative.as_posix(), "bytes": path.stat().st_size, "sha256": sha256_file(path)}


def write_manifest(output_root: Path) -> None:
    manifest = {
        "version": FIGURE_SET_VERSION,
        "source_release": SOURCE_RELEASE,
        "hash_algorithm": "sha256",
        "artifacts": [manifest_entry(output_root / relative, relative) for relative in expected_outputs()],
        "inputs": [manifest_entry(ROOT / relative, Path(relative)) for relative in SOURCE_INPUTS],
    }
    path = output_root / "figures/manifest.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def validate_manifest(errors: list[str]) -> None:
    for relative in (Path("figures/manifest.json"),):
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"{relative.as_posix()} is missing")
            continue
        try:
            manifest = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            errors.append(f"{relative.as_posix()} is invalid: {exc}")
            continue
        if manifest.get("version") != FIGURE_SET_VERSION or manifest.get("source_release") != SOURCE_RELEASE:
            errors.append(f"{relative.as_posix()} version metadata does not match the builder")
        groups = (("artifacts", expected_outputs()), ("inputs", [Path(item) for item in SOURCE_INPUTS]))
        for group, expected in groups:
            entries = manifest.get(group, [])
            indexed = {entry.get("path"): entry for entry in entries if isinstance(entry, dict)}
            if set(indexed) != {path.as_posix() for path in expected}:
                errors.append(f"{relative.as_posix()} {group} path set mismatch")
                continue
            for item in expected:
                file_path = ROOT / item
                row = indexed[item.as_posix()]
                if not file_path.is_file() or row.get("bytes") != file_path.stat().st_size or row.get("sha256") != sha256_file(file_path):
                    errors.append(f"{relative.as_posix()} mismatch: {item.as_posix()}")


def png_properties(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        raise ValueError("invalid PNG signature or header")
    return struct.unpack(">II", data[16:24])


def svg_properties(path: Path) -> tuple[str, str, str]:
    root = ET.parse(path).getroot()
    if root.tag.split("}")[-1] != "svg":
        raise ValueError("SVG root element is missing")
    values = tuple(root.attrib.get(name, "").strip() for name in ("width", "height", "viewBox"))
    if not all(values):
        raise ValueError("SVG width, height, and viewBox are required")
    return values


def check_current() -> int:
    with tempfile.TemporaryDirectory(prefix="tae-figures-") as directory:
        temporary_root = Path(directory)
        build_all(temporary_root)
        errors: list[str] = []
        for relative in csv_outputs():
            committed, rebuilt = ROOT / relative, temporary_root / relative
            if not committed.is_file() or committed.read_bytes() != rebuilt.read_bytes():
                errors.append(f"derived CSV is missing or stale: {relative.as_posix()}")
        for relative in image_outputs():
            committed, rebuilt = ROOT / relative, temporary_root / relative
            if not committed.is_file():
                errors.append(f"rendered image is missing: {relative.as_posix()}")
                continue
            try:
                committed_properties = png_properties(committed) if relative.suffix == ".png" else svg_properties(committed)
                rebuilt_properties = png_properties(rebuilt) if relative.suffix == ".png" else svg_properties(rebuilt)
                if committed_properties != rebuilt_properties:
                    errors.append(f"rendered image dimensions do not match: {relative.as_posix()}")
            except (OSError, ValueError, ET.ParseError) as exc:
                errors.append(f"rendered image is invalid: {relative.as_posix()}: {exc}")
        validate_manifest(errors)
        if errors:
            print("figure data or artifact integrity check failed:")
            for error in errors:
                print(f"- {error}")
            return 1
    print(f"figure data and artifact integrity v{FIGURE_SET_VERSION}: PASS")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="compare derived data and validate committed figure integrity")
    args = parser.parse_args()
    if args.check:
        return check_current()
    build_all(ROOT)
    write_manifest(ROOT)
    print(f"built {len(FIGURE_STUBS)} figures from source release v{SOURCE_RELEASE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
