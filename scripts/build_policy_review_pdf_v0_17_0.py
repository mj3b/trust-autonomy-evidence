#!/usr/bin/env python3
"""Build and validate the v0.17.0 policy-extension review PDF."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "paper/drafts/v0.17.0/regulatory-section-review.pdf"


def build() -> None:
    try:
        from reportlab.lib import colors
        from reportlab.lib.enums import TA_CENTER
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
        from reportlab.lib.units import inch
        from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
    except ModuleNotFoundError as exc:
        raise SystemExit(
            "policy review PDF: FAIL (building requires ReportLab; use the configured workspace Python runtime)"
        ) from exc

    navy = colors.HexColor("#0B1F3A")
    pale = colors.HexColor("#EDF1F5")
    ink = colors.HexColor("#202124")

    def footer(canvas, doc) -> None:
        canvas.saveState()
        canvas.setStrokeColor(navy)
        canvas.setLineWidth(0.5)
        canvas.line(0.72 * inch, 0.55 * inch, 7.78 * inch, 0.55 * inch)
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(navy)
        canvas.drawString(0.72 * inch, 0.38 * inch, "Practical Human Control | v0.17.0 policy extension")
        canvas.drawRightString(7.78 * inch, 0.38 * inch, str(doc.page))
        canvas.restoreState()

    def cell(text: str, style: ParagraphStyle) -> Paragraph:
        return Paragraph(text, style)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    styles = getSampleStyleSheet()
    body = ParagraphStyle("body", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.2, leading=12.5, textColor=ink, spaceAfter=7)
    small = ParagraphStyle("small", parent=body, fontSize=7.8, leading=10)
    head = ParagraphStyle("head", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=15, leading=18, textColor=navy, spaceBefore=8, spaceAfter=7)
    subhead = ParagraphStyle("subhead", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=navy, spaceBefore=7, spaceAfter=5)
    title = ParagraphStyle("title", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=navy, alignment=TA_CENTER, spaceAfter=6)
    centered = ParagraphStyle("centered", parent=body, alignment=TA_CENTER, spaceAfter=2)
    table_head = ParagraphStyle("table_head", parent=small, fontName="Helvetica-Bold", textColor=navy)

    doc = SimpleDocTemplate(
        str(OUTPUT), pagesize=letter, rightMargin=0.72 * inch, leftMargin=0.72 * inch,
        topMargin=0.65 * inch, bottomMargin=0.68 * inch,
        title="Regulatory Relevance and Prospective Validation",
        author="Mark Julius Banasihan",
        subject="v0.17.0 policy and standards crosswalk review supplement",
        invariant=1,
    )
    story = [
        Paragraph("Regulatory Relevance and Prospective Validation", title),
        Paragraph("Working section for <i>From Formal Authority to Practical Human Control</i>", centered),
        Spacer(1, 8),
        Paragraph("Mark Julius Banasihan<super>*</super>", centered),
        Paragraph("<super>*</super>Node &amp; Norm", centered),
        Paragraph("corresponding author: <link href='mailto:markjuliusbanasihan@gmail.com'>markjuliusbanasihan@gmail.com</link>", centered),
        Spacer(1, 6),
        Paragraph("v0.17.0 | Bounded manuscript use approved", centered),
        Spacer(1, 12),
        Paragraph("The institutional gap", head),
        Paragraph("Governance instruments can assign oversight duties without producing evidence that a person could influence a particular decision. A policy may require a reviewer, a notice, an audit, or a stop control. The institutional claim becomes stronger only when records show that the person received usable information, understood the system and situation, had authority and time to act, exercised judgment, and changed execution.", body),
        Paragraph("The practical-human-control method tests that connection. It does not issue a legal-compliance or certification finding.", body),
        Paragraph("Relationship to selected instruments", head),
    ]

    core_rows = [
        [cell("Instrument", table_head), cell("Reviewed function", table_head), cell("Research use", table_head)],
        [cell("EU AI Act, Article 14", small), cell("Understanding limits, automation-bias awareness, interpretation, override, reversal, intervention, and stopping", small), cell("Test selected capabilities; record information delivery, opportunity, exercised judgment, and propagation separately", small)],
        [cell("EU AI Act, Article 57", small), cell("Controlled testing and validation under regulatory supervision", small), cell("Capture every stage prospectively before the record becomes incomplete", small)],
        [cell("NIST AI RMF Core", small), cell("Documented roles, assessed operator proficiency, and defined oversight processes", small), cell("Connect organization-level arrangements to event-level evidence requests", small)],
        [cell("ISO/IEC 42001 public overview", small), cell("AI management-system governance, risk, traceability, transparency, reliability, and improvement", small), cell("Place an event-level evidence layer inside an organizational system; no conformity or certification claim", small)],
    ]
    core = Table(core_rows, colWidths=[1.35 * inch, 2.35 * inch, 3.1 * inch], repeatRows=1, hAlign="LEFT")
    core.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), pale), ("TEXTCOLOR", (0, 0), (-1, 0), navy),
        ("LINEABOVE", (0, 0), (-1, 0), 0.8, navy), ("LINEBELOW", (0, 0), (-1, 0), 0.45, navy),
        ("LINEBELOW", (0, -1), (-1, -1), 0.8, navy), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.extend([
        core,
        Spacer(1, 8),
        Paragraph("The reviewed instruments describe capabilities and processes that institutions should establish. Their existence alone does not show that those arrangements had practical force in one event. The six-stage method asks what records show that assigned oversight became timely, informed, exercised, and propagated control.", body),
        Paragraph("Why a sandbox is the next empirical step", head),
        Paragraph("An EU AI Act regulatory sandbox can test the method with evidence collected by design. Before a run, the study should freeze the system and decision boundary, six required stages, timing definitions, intervention controls, evidence states, stopping rule, and output schema.", body),
        Paragraph("During the run, the study should preserve the exact information shown to the overseer, system version and limits, training and role records, complete timestamps, the contemporaneous judgment or intervention, and proof that the intervention reached downstream execution.", body),
        Paragraph("A solo rehearsal can test internal executability. A blinded second assessor is required for reliability. Field validity also requires target-system and task sampling and an external criterion. Work involving participants or protected operational records requires the applicable ethics determination and data authority before collection.", body),
        PageBreak(),
        Paragraph("Prospective evidence plan", head),
    ])
    evidence_rows = [
        [cell("Stage", table_head), cell("Required record", table_head), cell("Prospective test", table_head)],
        [cell("Information access", small), cell("Timestamped interface state and delivered evidence", small), cell("Verify what the overseer could see before irreversible commitment", small)],
        [cell("Comprehension capacity", small), cell("Training basis, limitation disclosure, and task-specific comprehension check", small), cell("Test interpretation of output, uncertainty, and alternatives under study conditions", small)],
        [cell("Intervention authority", small), cell("Role delegation and tested controls", small), cell("Verify that approve, reject, modify, stop, and escalation rights function", small)],
        [cell("Intervention feasibility", small), cell("Workload, latency, staffing, and complete timing inputs", small), cell("Calculate the proposed timing margin and record channel failures", small)],
        [cell("Exercised judgment", small), cell("Contemporaneous decision, challenge, or intervention record", small), cell("Distinguish active judgment from automatic confirmation", small)],
        [cell("Execution propagation", small), cell("Linked downstream state or action record", small), cell("Verify that the intervention changed execution or a binding obligation", small)],
    ]
    evidence = Table(evidence_rows, colWidths=[1.3 * inch, 2.45 * inch, 3.05 * inch], repeatRows=1, hAlign="LEFT")
    evidence.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), pale), ("TEXTCOLOR", (0, 0), (-1, 0), navy),
        ("LINEABOVE", (0, 0), (-1, 0), 0.8, navy), ("LINEBELOW", (0, 0), (-1, 0), 0.45, navy),
        ("LINEBELOW", (0, -1), (-1, -1), 0.8, navy), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.extend([
        evidence,
        Spacer(1, 8),
        Paragraph("The first study should contain a functioning control path, a path with one prespecified operational constraint, and a missing-record path. The third condition checks whether the method returns unresolved when the record cannot decide. These conditions test procedure behavior and supply no prevalence estimate.", body),
        Paragraph("United States applied-policy sites", head),
    ])
    us_rows = [
        [cell("Setting", table_head), cell("Reviewed duty or right", table_head), cell("Current boundary", table_head)],
        [cell("New York City", small), cell("Bias audit, public audit information, and notice for covered employment tools", small), cell("No inference that a named person could alter an individual decision", small)],
        [cell("California", small), cell("Access and opt-out rights for covered ADMT uses", small), cell("Compliance begins 1 January 2027; no event-level case assessed", small)],
        [cell("Colorado", small), cell("Consequential-decision framework effective 1 January 2027", small), cell("Detailed mapping waits for final implementing rules", small)],
        [cell("Illinois and Chicago", small), cell("Employment discrimination prohibition and notice", small), cell("Chicago remains within the state entry until a municipal source is selected", small)],
    ]
    us_table = Table(us_rows, colWidths=[1.2 * inch, 2.65 * inch, 2.95 * inch], repeatRows=1, hAlign="LEFT")
    us_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), pale), ("TEXTCOLOR", (0, 0), (-1, 0), navy),
        ("LINEABOVE", (0, 0), (-1, 0), 0.8, navy), ("LINEBELOW", (0, 0), (-1, 0), 0.45, navy),
        ("LINEBELOW", (0, -1), (-1, -1), 0.8, navy), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.extend([
        us_table,
        Spacer(1, 8),
        Paragraph("Claim boundary", head),
        Paragraph("The crosswalk proposes research uses for selected instruments. It does not interpret every legal obligation, establish compliance, certify an AI management system, provide legal advice, or show that the method improves institutional outcomes. The eight source observations require accountable author review before manuscript inclusion.", body),
        Paragraph("Kevin Baum's private message identifies a possible audience and application setting. It is excluded from the evidence base and supplies no validation or peer-review result.", body),
        Paragraph("Official sources", subhead),
        Paragraph("European Union: <link href='https://eur-lex.europa.eu/eli/reg/2024/1689/oj'>Regulation (EU) 2024/1689, Articles 14 and 57</link><br/>National Institute of Standards and Technology: <link href='https://airc.nist.gov/airmf-resources/airmf/5-sec-core/'>AI RMF Core</link><br/>ISO and IEC: <link href='https://www.iso.org/standard/42001'>ISO/IEC 42001:2023 public overview</link>", small),
    ])
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


def validate() -> None:
    if not OUTPUT.is_file() or OUTPUT.stat().st_size == 0:
        raise SystemExit("policy review PDF: FAIL (missing output)")
    try:
        text_result = subprocess.run(
            ["pdftotext", str(OUTPUT), "-"], text=True, capture_output=True, check=False
        )
        info_result = subprocess.run(
            ["pdfinfo", str(OUTPUT)], text=True, capture_output=True, check=False
        )
    except FileNotFoundError as exc:
        raise SystemExit(
            "policy review PDF: FAIL (validation requires the Poppler pdftotext and pdfinfo tools)"
        ) from exc
    if text_result.returncode != 0 or info_result.returncode != 0:
        raise SystemExit("policy review PDF: FAIL (Poppler could not inspect the output)")
    text = text_result.stdout
    markers = (
        "Regulatory Relevance and Prospective Validation",
        "Mark Julius Banasihan",
        "Node & Norm",
        "EU AI Act, Article 14",
        "EU AI Act, Article 57",
        "NIST AI RMF Core",
        "ISO/IEC 42001",
        "New York City",
        "California",
        "Colorado",
        "Illinois and Chicago",
        "Bounded manuscript use approved",
    )
    missing = [marker for marker in markers if marker not in text]
    if missing:
        raise SystemExit("policy review PDF: FAIL (missing text: " + ", ".join(missing) + ")")
    page_line = next((line for line in info_result.stdout.splitlines() if line.startswith("Pages:")), "")
    try:
        page_count = int(page_line.split(":", 1)[1].strip()) if page_line else 0
    except ValueError as exc:
        raise SystemExit("policy review PDF: FAIL (invalid page-count metadata)") from exc
    if page_count != 2:
        raise SystemExit(f"policy review PDF: FAIL (expected 2 pages, found {page_count})")
    print(f"policy review PDF: PASS ({page_count} pages; {OUTPUT.stat().st_size} bytes)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.check:
        build()
    validate()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
