#!/usr/bin/env python3
"""Build the publication figure set from committed research artifacts."""

from __future__ import annotations

import argparse
import csv
import json
import os
import tempfile
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIGURE_CACHE = Path(tempfile.gettempdir()) / "trust-autonomy-evidence-figure-cache"
FIGURE_CACHE.mkdir(parents=True, exist_ok=True)
os.environ.setdefault(
    "MPLCONFIGDIR", str(FIGURE_CACHE / "matplotlib")
)
os.environ.setdefault("XDG_CACHE_HOME", str(FIGURE_CACHE))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.colors import BoundaryNorm, ListedColormap  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Patch  # noqa: E402


FIGURE_SET_VERSION = "0.1.0"
SOURCE_RELEASE = "0.3.0"

CASE_DIRECTORIES = (
    "cases/TAE-PUB-001-oko-1983",
    "cases/TAE-PUB-002-patriot-zg710-2003",
    "cases/TAE-PUB-003-patriot-fa18-2003",
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
    "partially_supported": "PS",
    "unsupported": "U",
    "indeterminate": "I",
    "outside_scope": "O",
}
STATE_COLORS = {
    "supported": "#0072B2",
    "partially_supported": "#56B4E9",
    "unsupported": "#D55E00",
    "indeterminate": "#CC79A7",
    "outside_scope": "#B7B7B7",
}

INK = "#17212B"
MUTED = "#5A6772"
GRID = "#D7DEE5"
PAPER = "#FFFFFF"
PALE_BLUE = "#EAF3F8"
PALE_GRAY = "#F4F6F8"
TEAL = "#009E73"
ORANGE = "#D55E00"
PURPLE = "#8E5AA9"

FIGURE_STUBS = (
    "fig-1-selection-and-stopping",
    "fig-2-practical-control-chain",
    "fig-3-decision-paths",
    "fig-4-trust-evidence-states",
    "fig-a1-mutation-response",
    "fig-a2-reproducibility-lineage",
)


def configure_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 10,
            "axes.titlesize": 16,
            "axes.labelcolor": INK,
            "axes.edgecolor": GRID,
            "text.color": INK,
            "xtick.color": INK,
            "ytick.color": INK,
            "figure.facecolor": PAPER,
            "axes.facecolor": PAPER,
            "savefig.facecolor": PAPER,
            "svg.hashsalt": "trust-autonomy-evidence-figure-set-v0.1.0",
        }
    )


def read_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def load_assessments() -> list[dict]:
    assessments = []
    for relative in CASE_DIRECTORIES:
        assessments.append(read_json(f"{relative}/assessment.json"))
    return sorted(assessments, key=lambda row: row["case_id"])


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def save_figure(fig: plt.Figure, output_dir: Path, stub: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        output_dir / f"{stub}.png",
        dpi=200,
        bbox_inches="tight",
        metadata={"Software": "Trust, Autonomy, and Evidence figure builder"},
    )
    fig.savefig(
        output_dir / f"{stub}.svg",
        bbox_inches="tight",
        metadata={
            "Creator": "Trust, Autonomy, and Evidence figure builder",
            "Date": None,
        },
    )
    plt.close(fig)


def add_title(fig: plt.Figure, title: str, subtitle: str) -> None:
    fig.text(0.06, 0.965, title, ha="left", va="top", fontsize=17, weight="semibold")
    fig.text(0.06, 0.922, subtitle, ha="left", va="top", fontsize=10.5, color=MUTED)


def add_source_note(fig: plt.Figure, note: str, y: float = 0.02) -> None:
    fig.text(0.06, y, note, ha="left", va="bottom", fontsize=8.5, color=MUTED)


def draw_box(
    ax: plt.Axes,
    xy: tuple[float, float],
    width: float,
    height: float,
    title: str,
    detail: str,
    facecolor: str = PAPER,
    edgecolor: str = INK,
    title_size: float = 11,
) -> None:
    x, y = xy
    box = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.012,rounding_size=0.014",
        linewidth=1.2,
        edgecolor=edgecolor,
        facecolor=facecolor,
        transform=ax.transAxes,
        clip_on=False,
    )
    ax.add_patch(box)
    ax.text(
        x + width / 2,
        y + height * 0.67,
        title,
        ha="center",
        va="center",
        fontsize=title_size,
        weight="semibold",
        transform=ax.transAxes,
    )
    ax.text(
        x + width / 2,
        y + height * 0.32,
        detail,
        ha="center",
        va="center",
        fontsize=9,
        color=MUTED,
        linespacing=1.25,
        transform=ax.transAxes,
    )


def draw_arrow(
    ax: plt.Axes,
    start: tuple[float, float],
    end: tuple[float, float],
    color: str = MUTED,
    connectionstyle: str = "arc3",
) -> None:
    arrow = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=12,
        linewidth=1.2,
        color=color,
        connectionstyle=connectionstyle,
        transform=ax.transAxes,
        clip_on=False,
    )
    ax.add_patch(arrow)


def build_selection_figure(data_dir: Path, figure_dir: Path) -> None:
    candidates = read_json("cases/data/candidate-search-output.json")
    decisions = read_json("figures/specifications/selection-decisions.json")["screening"]

    first_five = [row["candidate_id"] for row in candidates["candidates"][:5]]
    declared_five = [row["candidate_id"] for row in decisions]
    if first_five != declared_five:
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

    fig, ax = plt.subplots(figsize=(12.5, 7.3))
    ax.set_axis_off()
    add_title(
        fig,
        "The frozen stopping rule selected three cases after five screenings",
        "Counts describe candidate records and frozen decisions; 923 records remained unscreened.",
    )

    draw_box(
        ax,
        (0.03, 0.61),
        0.23,
        0.19,
        "AI Incident Database",
        f"{aiid['incident_records']:,} incidents, {aiid['report_records']:,} reports\n{aiid['candidate_records']:,} matched candidate records",
        facecolor=PALE_BLUE,
        edgecolor="#4C86A8",
    )
    draw_box(
        ax,
        (0.03, 0.28),
        0.23,
        0.19,
        "OECD export",
        f"{oecd['exported_unique_records']:,} exported records\nno pre-2020 result in frozen probes",
        facecolor=PALE_BLUE,
        edgecolor="#4C86A8",
    )
    draw_box(
        ax,
        (0.35, 0.475),
        0.22,
        0.20,
        f"{total:,} preserved records",
        "fixed vocabulary and ordering\narticle text excluded from output",
        facecolor="#EEF5F1",
        edgecolor=TEAL,
    )
    draw_box(
        ax,
        (0.65, 0.475),
        0.17,
        0.20,
        f"{screened} screened",
        "first five AIID candidates\nin frozen order",
        facecolor="#FFF5E9",
        edgecolor="#C77822",
    )
    draw_box(
        ax,
        (0.86, 0.64),
        0.12,
        0.16,
        f"{selected} selected",
        "one case in\neach stratum",
        facecolor="#E7F4EF",
        edgecolor=TEAL,
        title_size=10.5,
    )
    draw_box(
        ax,
        (0.86, 0.37),
        0.12,
        0.16,
        f"{excluded} excluded",
        "source and\nboundary rules",
        facecolor="#FBEDE7",
        edgecolor=ORANGE,
        title_size=10.5,
    )
    draw_box(
        ax,
        (0.35, 0.12),
        0.22,
        0.16,
        f"{unscreened:,} unscreened",
        "preserved for later cycles\nno exclusion decision assigned",
        facecolor=PALE_GRAY,
        edgecolor="#8C969F",
    )

    draw_arrow(ax, (0.26, 0.70), (0.35, 0.60))
    draw_arrow(ax, (0.26, 0.375), (0.35, 0.55))
    draw_arrow(ax, (0.57, 0.575), (0.65, 0.575))
    draw_arrow(ax, (0.82, 0.59), (0.86, 0.70))
    draw_arrow(ax, (0.82, 0.54), (0.86, 0.45))
    draw_arrow(ax, (0.46, 0.475), (0.46, 0.28))

    ax.text(
        0.92,
        0.565,
        "STOP",
        ha="center",
        va="center",
        fontsize=9.5,
        weight="bold",
        color=PURPLE,
        transform=ax.transAxes,
    )
    ax.text(
        0.92,
        0.285,
        "All three prespecified strata were filled.",
        ha="center",
        va="center",
        fontsize=8.5,
        color=PURPLE,
        transform=ax.transAxes,
    )
    add_source_note(
        fig,
        "Source: v0.3.0 candidate-search output and public-case selection register. Purposeful stopping supplies no population estimate.",
    )
    save_figure(fig, figure_dir, "fig-1-selection-and-stopping")


def categorical_matrix(
    assessments: list[dict],
    section: str,
    fields: tuple[str, ...],
    labels: dict[str, str],
    title: str,
    subtitle: str,
    stub: str,
    data_dir: Path,
    figure_dir: Path,
) -> None:
    rows = []
    matrix = []
    for field in fields:
        matrix_row = []
        for assessment in assessments:
            finding = assessment[section][field]
            state = finding["state"]
            matrix_row.append(STATE_ORDER.index(state))
            rows.append(
                {
                    "case_id": assessment["case_id"],
                    "case_title": assessment["title"],
                    "proposition": field,
                    "state": state,
                    "evidence_refs": ";".join(finding["evidence_refs"]),
                }
            )
        matrix.append(matrix_row)

    write_csv(
        data_dir / f"{stub}.csv",
        ["case_id", "case_title", "proposition", "state", "evidence_refs"],
        rows,
    )

    height = 7.5 if len(fields) <= 9 else 9.1
    fig, ax = plt.subplots(figsize=(10.5, height))
    fig.subplots_adjust(left=0.31, right=0.94, top=0.84, bottom=0.17)
    add_title(fig, title, subtitle)

    cmap = ListedColormap([STATE_COLORS[state] for state in STATE_ORDER])
    norm = BoundaryNorm([value - 0.5 for value in range(len(STATE_ORDER) + 1)], cmap.N)
    ax.imshow(matrix, cmap=cmap, norm=norm, aspect="auto")

    ax.set_xticks(range(len(assessments)))
    ax.set_xticklabels([CASE_LABELS[row["case_id"]] for row in assessments], fontsize=10.5)
    ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False, length=0, pad=10)
    ax.set_yticks(range(len(fields)))
    ax.set_yticklabels([labels[field] for field in fields], fontsize=10.2)
    ax.tick_params(axis="y", length=0, pad=10)

    ax.set_xticks([x - 0.5 for x in range(1, len(assessments))], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, len(fields))], minor=True)
    ax.grid(which="minor", color=PAPER, linewidth=2.2)
    ax.tick_params(which="minor", bottom=False, left=False)
    for spine in ax.spines.values():
        spine.set_visible(False)

    for y, field in enumerate(fields):
        for x, assessment in enumerate(assessments):
            state = assessment[section][field]["state"]
            text_color = INK if state in {"partially_supported", "outside_scope"} else PAPER
            ax.text(
                x,
                y,
                STATE_CODES[state],
                ha="center",
                va="center",
                fontsize=10.5,
                weight="bold",
                color=text_color,
            )

    if section == "practical_control":
        ax.axhline(5.5, color=INK, linewidth=1.2)
        ax.text(
            -0.52,
            2.5,
            "pre-action chain",
            ha="right",
            va="center",
            fontsize=8.5,
            color=MUTED,
            rotation=90,
        )
        ax.text(
            -0.52,
            7.0,
            "post-action chain",
            ha="right",
            va="center",
            fontsize=8.5,
            color=MUTED,
            rotation=90,
        )

    legend = [Patch(facecolor=STATE_COLORS[state], edgecolor="none", label=STATE_LABELS[state]) for state in STATE_ORDER]
    fig.legend(
        handles=legend,
        loc="lower left",
        bbox_to_anchor=(0.305, 0.075),
        ncol=3,
        frameon=False,
        fontsize=8.8,
        columnspacing=1.4,
        handlelength=1.2,
    )
    add_source_note(
        fig,
        f"Source: three v{SOURCE_RELEASE} public-case assessment files. States are categorical and carry no numeric distance.",
        y=0.025,
    )
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
    write_csv(
        data_dir / "fig-3-decision-paths.csv",
        ["case_id", "case_title", "order", "event", "kind", "evidence_refs", "case_annotation"],
        rows,
    )

    kind_colors = {
        "system_output": "#4C78A8",
        "evidence_check": "#72B7B2",
        "human_decision": "#2F6B9A",
        "human_action": "#009E73",
        "system_action": "#E68635",
        "bounded_effect": "#009E73",
        "harm_outcome": "#C44E52",
    }
    legend_labels = {
        "system_output": "System output",
        "evidence_check": "Evidence check",
        "human_decision": "Human decision",
        "human_action": "Human action",
        "system_action": "System action",
        "bounded_effect": "Bounded protective effect",
        "harm_outcome": "Harm outcome",
    }

    fig, ax = plt.subplots(figsize=(14.5, 8.4))
    fig.subplots_adjust(left=0.13, right=0.97, top=0.84, bottom=0.20)
    add_title(
        fig,
        "The intervention path remains visible until public evidence runs out",
        "Fifteen source-linked events are shown in relative order. Horizontal distance has no elapsed-time scale.",
    )
    ax.set_xlim(-0.45, 4.45)
    ax.set_ylim(-0.90, 2.65)
    ax.set_axis_off()

    y_positions = {"TAE-PUB-001": 2.0, "TAE-PUB-002": 1.0, "TAE-PUB-003": 0.0}
    for case in specification["cases"]:
        y = y_positions[case["case_id"]]
        ax.annotate(
            "",
            xy=(4.20, y),
            xytext=(-0.15, y),
            arrowprops={"arrowstyle": "-|>", "color": GRID, "linewidth": 2.2},
        )
        ax.text(-0.28, y, case["short_title"], ha="right", va="center", fontsize=10.5, weight="semibold")

        for event in case["events"]:
            x = event["order"] - 1
            color = kind_colors[event["kind"]]
            ax.scatter([x], [y], s=380, color=color, edgecolor=PAPER, linewidth=1.5, zorder=3)
            ax.text(x, y, str(event["order"]), ha="center", va="center", color=PAPER, fontsize=9.5, weight="bold", zorder=4)
            label_y = y + 0.25 if event["order"] % 2 else y - 0.25
            va = "bottom" if event["order"] % 2 else "top"
            ax.text(
                x,
                label_y,
                textwrap.fill(event["event"], width=23),
                ha="center",
                va=va,
                fontsize=8.4,
                linespacing=1.15,
            )
            refs_y = y + 0.13 if va == "bottom" else y - 0.13
            refs_va = "bottom" if va == "bottom" else "top"
            ax.text(
                x,
                refs_y,
                " ".join(event["evidence_refs"]),
                ha="center",
                va=refs_va,
                fontsize=7.2,
                color=MUTED,
            )

        if case["case_id"] == "TAE-PUB-002":
            ax.text(1.5, y + 0.10, "about 1 minute", ha="center", va="bottom", fontsize=8.5, color=PURPLE, weight="semibold")
        if case["case_id"] == "TAE-PUB-003":
            ax.plot([1.15, 2.85], [y - 0.65, y - 0.65], color=PURPLE, linestyle=(0, (4, 3)), linewidth=1.4)
            ax.text(
                2.0,
                y - 0.60,
                "timing, displays, report independence, and feasible challenge unresolved",
                ha="center",
                va="bottom",
                fontsize=8.2,
                color=PURPLE,
            )

    present_kinds = [
        "system_output",
        "evidence_check",
        "human_decision",
        "human_action",
        "system_action",
        "bounded_effect",
        "harm_outcome",
    ]
    handles = [
        Line2D([0], [0], marker="o", color="none", markerfacecolor=kind_colors[kind], markeredgecolor="none", markersize=9, label=legend_labels[kind])
        for kind in present_kinds
    ]
    fig.legend(
        handles=handles,
        loc="lower left",
        bbox_to_anchor=(0.125, 0.075),
        ncol=4,
        frameon=False,
        fontsize=8.5,
        columnspacing=1.3,
        handletextpad=0.45,
    )
    add_source_note(
        fig,
        "Source: v0.3.0 case chronologies and source references. Relative placement preserves sequence and avoids invented timing.",
        y=0.025,
    )
    save_figure(fig, figure_dir, "fig-3-decision-paths")


def build_mutation_response(data_dir: Path, figure_dir: Path) -> None:
    fixture = read_json("fixtures/mutations/mutations.json")
    results = read_json("assessments/generated-results.json")
    observed = {row["mutation_id"]: row for row in results["mutation_results"]}

    rows = []
    for mutation in fixture["mutations"]:
        result = observed.get(mutation["mutation_id"])
        if result is None or result["status"] != "pass":
            raise ValueError(f"Missing passing mutation result: {mutation['mutation_id']}")
        expected = {
            (row["assessment"], row["field"], row["from"], row["to"])
            for row in mutation["expected_deltas"]
        }
        actual = {
            (row["assessment"], row["field"], row["from"], row["to"])
            for row in result["deltas"]
        }
        if expected != actual:
            raise ValueError(f"Mutation delta mismatch: {mutation['mutation_id']}")
        if mutation["expected_deltas"]:
            for delta in mutation["expected_deltas"]:
                rows.append(
                    {
                        "mutation_id": mutation["mutation_id"],
                        "base_case_id": mutation["base_case_id"],
                        "purpose": mutation["purpose"],
                        "assessment": delta["assessment"],
                        "field": delta["field"],
                        "from": delta["from"],
                        "to": delta["to"],
                        "result": "pass",
                    }
                )
        else:
            rows.append(
                {
                    "mutation_id": mutation["mutation_id"],
                    "base_case_id": mutation["base_case_id"],
                    "purpose": mutation["purpose"],
                    "assessment": "",
                    "field": "",
                    "from": "",
                    "to": "invariant",
                    "result": "pass",
                }
            )
    write_csv(
        data_dir / "fig-a1-mutation-response.csv",
        ["mutation_id", "base_case_id", "purpose", "assessment", "field", "from", "to", "result"],
        rows,
    )

    field_order = [
        ("control", "access"),
        ("control", "authority"),
        ("trust", "human_authority"),
        ("trust", "integrity"),
        ("control", "correction"),
        ("trust", "harm_correction"),
        ("trust", "monitoring"),
        ("trust", "evidence_completeness"),
        ("control", "repair"),
        ("control", "reform"),
        ("trust", "governance_update"),
    ]
    field_labels = [
        "Access",
        "Control\nauthority",
        "Human\nauthority",
        "Integrity",
        "Correction",
        "Harm\ncorrection",
        "Monitoring",
        "Evidence\ncompleteness",
        "Repair",
        "Reform",
        "Governance\nupdate",
        "No assessment\ndelta",
    ]
    mutations = fixture["mutations"]
    fig, ax = plt.subplots(figsize=(14.5, 8.8))
    fig.subplots_adjust(left=0.18, right=0.97, top=0.83, bottom=0.20)
    add_title(
        fig,
        "All 12 controlled mutations matched the prespecified response",
        "The suite contains 11 delta assertions, 3 invariance tests, and 0 failures.",
    )
    ax.set_xlim(-0.5, len(field_labels) - 0.5)
    ax.set_ylim(len(mutations) - 0.5, -0.5)
    ax.set_xticks(range(len(field_labels)))
    ax.set_xticklabels(field_labels, fontsize=8.4)
    ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False, length=0, pad=8)
    ax.set_yticks(range(len(mutations)))
    ax.set_yticklabels([row["mutation_id"].replace("TAE-MUT-", "M") for row in mutations], fontsize=9)
    ax.tick_params(axis="y", length=0, pad=8)
    ax.set_xticks([x - 0.5 for x in range(1, len(field_labels))], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, len(mutations))], minor=True)
    ax.grid(which="minor", color=GRID, linewidth=0.8)
    ax.tick_params(which="minor", bottom=False, left=False)
    for spine in ax.spines.values():
        spine.set_visible(False)

    target_colors = {
        "unsupported": STATE_COLORS["unsupported"],
        "partially_supported": STATE_COLORS["partially_supported"],
        "indeterminate": STATE_COLORS["indeterminate"],
        "invariant": "#6F7C86",
    }
    target_codes = {
        "unsupported": "U",
        "partially_supported": "PS",
        "indeterminate": "I",
        "invariant": "0",
    }
    for y, mutation in enumerate(mutations):
        expected = mutation["expected_deltas"]
        if not expected:
            x = len(field_labels) - 1
            target = "invariant"
            ax.scatter([x], [y], s=330, marker="s", color=target_colors[target], edgecolor=PAPER, linewidth=1.0)
            ax.text(x, y, target_codes[target], ha="center", va="center", color=PAPER, fontsize=9, weight="bold")
            continue
        for delta in expected:
            x = field_order.index((delta["assessment"], delta["field"]))
            target = delta["to"]
            ax.scatter([x], [y], s=330, marker="s", color=target_colors[target], edgecolor=PAPER, linewidth=1.0)
            text_color = INK if target == "partially_supported" else PAPER
            ax.text(x, y, target_codes[target], ha="center", va="center", color=text_color, fontsize=9, weight="bold")

    legend = [
        Patch(facecolor=target_colors["unsupported"], label="Changed to unsupported"),
        Patch(facecolor=target_colors["partially_supported"], label="Changed to partially supported"),
        Patch(facecolor=target_colors["indeterminate"], label="Changed to indeterminate"),
        Patch(facecolor=target_colors["invariant"], label="Assessment invariant"),
    ]
    fig.legend(
        handles=legend,
        loc="lower left",
        bbox_to_anchor=(0.175, 0.075),
        ncol=2,
        frameon=False,
        fontsize=8.8,
        columnspacing=1.5,
    )
    add_source_note(
        fig,
        "Source: v0.2.0 mutation fixture and generated results. The author designed the fixtures, oracle, and assessment contract.",
        y=0.025,
    )
    save_figure(fig, figure_dir, "fig-a1-mutation-response")


def build_lineage(data_dir: Path, figure_dir: Path) -> None:
    spec = read_json("figures/specifications/reproducibility-lineage.json")
    rows = []
    for node in spec["nodes"]:
        rows.append(
            {
                "record_type": "node",
                "node_id": node["node_id"],
                "lane": node["lane"],
                "order": node["order"],
                "title": node["title"],
                "detail": node["detail"].replace("\n", " | "),
                "from": "",
                "to": "",
            }
        )
    for edge in spec["edges"]:
        rows.append(
            {
                "record_type": "edge",
                "node_id": "",
                "lane": "",
                "order": "",
                "title": "",
                "detail": "",
                "from": edge["from"],
                "to": edge["to"],
            }
        )
    write_csv(
        data_dir / "fig-a2-reproducibility-lineage.csv",
        ["record_type", "node_id", "lane", "order", "title", "detail", "from", "to"],
        rows,
    )

    fig, ax = plt.subplots(figsize=(15.5, 7.8))
    ax.set_axis_off()
    add_title(
        fig,
        "Every plotted state traces to a frozen input or prespecified test",
        "The upper lane records research provenance. The lower lane records figure generation and freshness checks.",
    )

    lane_nodes = {
        lane: sorted([node for node in spec["nodes"] if node["lane"] == lane], key=lambda row: row["order"])
        for lane in ("research", "figures")
    }
    positions: dict[str, tuple[float, float]] = {}
    box_sizes = {"research": (0.135, 0.18), "figures": (0.15, 0.18)}
    lane_y = {"research": 0.57, "figures": 0.20}
    lane_face = {"research": PALE_BLUE, "figures": "#EEF5F1"}
    lane_edge = {"research": "#4C86A8", "figures": TEAL}

    for lane, nodes in lane_nodes.items():
        width, height = box_sizes[lane]
        left = 0.08
        right = 0.97 - width
        step = (right - left) / (len(nodes) - 1)
        for index, node in enumerate(nodes):
            x = left + index * step
            y = lane_y[lane]
            positions[node["node_id"]] = (x, y)
            draw_box(
                ax,
                (x, y),
                width,
                height,
                node["title"],
                node["detail"],
                facecolor=lane_face[lane],
                edgecolor=lane_edge[lane],
                title_size=9.6,
            )

    ax.text(0.02, 0.66, "RESEARCH", ha="left", va="center", fontsize=8.5, weight="bold", color="#4C86A8", transform=ax.transAxes)
    ax.text(0.02, 0.29, "FIGURES", ha="left", va="center", fontsize=8.5, weight="bold", color=TEAL, transform=ax.transAxes)

    for edge in spec["edges"]:
        start_id = edge["from"]
        end_id = edge["to"]
        start_node = next(node for node in spec["nodes"] if node["node_id"] == start_id)
        end_node = next(node for node in spec["nodes"] if node["node_id"] == end_id)
        start_x, start_y = positions[start_id]
        end_x, end_y = positions[end_id]
        start_w, start_h = box_sizes[start_node["lane"]]
        end_w, end_h = box_sizes[end_node["lane"]]
        if start_node["lane"] == end_node["lane"]:
            draw_arrow(ax, (start_x + start_w, start_y + start_h / 2), (end_x, end_y + end_h / 2))
        else:
            draw_arrow(
                ax,
                (start_x + start_w / 2, start_y),
                (end_x + end_w / 2, end_y + end_h),
                color=PURPLE,
                connectionstyle="arc3,rad=0.10",
            )

    add_source_note(
        fig,
        "Integrity boundary: hashes and deterministic transformations support ordering and traceability; source truth and completeness remain separate claims.",
        y=0.025,
    )
    save_figure(fig, figure_dir, "fig-a2-reproducibility-lineage")


def build_all(output_root: Path) -> None:
    configure_style()
    data_dir = output_root / "figures/data"
    figure_dir = output_root / "figures/generated"
    assessments = load_assessments()

    build_selection_figure(data_dir, figure_dir)
    categorical_matrix(
        assessments,
        "practical_control",
        CONTROL_FIELDS,
        CONTROL_LABELS,
        "Formal authority appears in all three cases; practical force diverges downstream",
        "Twenty-seven declared states from nine propositions across three purposefully selected public cases.",
        "fig-2-practical-control-chain",
        data_dir,
        figure_dir,
    )
    build_decision_paths(data_dir, figure_dir)
    categorical_matrix(
        assessments,
        "trust_evidence",
        TRUST_FIELDS,
        TRUST_LABELS,
        "Each case leaves material trust-evidence propositions unresolved or unsupported",
        "Thirty-six declared states from twelve propositions across three purposefully selected public cases.",
        "fig-4-trust-evidence-states",
        data_dir,
        figure_dir,
    )
    build_mutation_response(data_dir, figure_dir)
    build_lineage(data_dir, figure_dir)


def expected_outputs() -> list[Path]:
    outputs = []
    for stub in FIGURE_STUBS:
        outputs.append(Path("figures/data") / f"{stub}.csv")
        outputs.append(Path("figures/generated") / f"{stub}.png")
        outputs.append(Path("figures/generated") / f"{stub}.svg")
    return outputs


def check_current() -> int:
    with tempfile.TemporaryDirectory(prefix="tae-figures-") as directory:
        temporary_root = Path(directory)
        build_all(temporary_root)
        stale = []
        for relative in expected_outputs():
            committed = ROOT / relative
            rebuilt = temporary_root / relative
            if not committed.is_file() or committed.read_bytes() != rebuilt.read_bytes():
                stale.append(str(relative))
        if stale:
            print("figure set is missing or stale:")
            for relative in stale:
                print(f"- {relative}")
            return 1
    print(f"figure set v{FIGURE_SET_VERSION}: PASS")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="rebuild in a temporary directory and compare with committed outputs")
    args = parser.parse_args()
    if args.check:
        return check_current()
    build_all(ROOT)
    print(f"built {len(FIGURE_STUBS)} figures from source release v{SOURCE_RELEASE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
