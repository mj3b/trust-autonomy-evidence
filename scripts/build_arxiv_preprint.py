#!/usr/bin/env python3
"""Build a venue-ready LaTeX review package from the reader manuscript."""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "paper/manuscript-reader.md"
OUTPUT_DIR = ROOT / "paper/arxiv"
TEX_OUTPUT = OUTPUT_DIR / "main.tex"
PDF_OUTPUT = OUTPUT_DIR / "preprint-v0.14.0.pdf"

TITLE = "From Formal Authority to Practical Human Control"
SUBTITLE = "A traceable method for reconstructing human control in automated decisions"
AUTHOR = "Mark Julius Banasihan"
ORCID = "0009-0001-8121-2878"
AFFILIATION = "Independent Researcher, Node & Norm, United States"
CORRESPONDING_EMAIL = "mab7898@g.harvard.edu"
ALTERNATE_EMAIL = "markjuliusbanasihan@gmail.com"
STUDENT_STATUS = "ALB candidate in Extension Studies, Harvard University"
VERSION = "0.14.0"
BLUE_HEX = "#0B1F3A"

FIGURES = {
    "Figure 1.": "figures/generated/fig-1-selection-and-stopping.png",
    "Figure 2.": "figures/generated/fig-2-practical-control-chain.png",
    "Figure 3.": "figures/generated/fig-3-decision-paths.png",
    "Figure 4.": "figures/generated/fig-4-trust-evidence-states.png",
    "Figure 5.": "figures/generated/fig-5-formal-search-and-screening.png",
    "Figure 6.": "figures/generated/fig-6-evidence-boundaries.png",
    "Figure A1.": "figures/generated/fig-a1-mutation-response.png",
    "Figure A2.": "figures/generated/fig-a2-reproducibility-lineage.png",
    "Figure A3.": "figures/generated/fig-a3-claim-evidence-integrity.png",
    "Figure A4.": "figures/generated/fig-a4-oko-versioned-correction.png",
}

MARKDOWN_LINK = re.compile(r"\[([^\]]+)\]\(([^()]*(?:\([^()]*\)[^()]*)*)\)")
TABLE_CAPTION = re.compile(r"^Table\s+(A?\d+)\.\s*(.+)$")
WIDE_TABLES = {"2", "A1", "3", "4", "5", "A3"}

TABLE_SPECS = {
    "1": r"@{}>{\raggedright\arraybackslash}p{0.24\columnwidth}>{\centering\arraybackslash}p{0.10\columnwidth}>{\raggedright\arraybackslash}X@{}",
    "2": r"@{}>{\raggedright\arraybackslash}X*{3}{>{\centering\arraybackslash}p{0.16\textwidth}}@{}",
    "A1": r"@{}>{\raggedright\arraybackslash}p{0.20\textwidth}>{\centering\arraybackslash}p{0.09\textwidth}>{\centering\arraybackslash}p{0.09\textwidth}>{\raggedright\arraybackslash}X@{}",
    "3": r"@{}>{\raggedright\arraybackslash}p{0.16\textwidth}>{\raggedright\arraybackslash}p{0.18\textwidth}>{\raggedleft\arraybackslash}p{0.08\textwidth}>{\raggedright\arraybackslash}X@{}",
    "4": r"@{}>{\raggedright\arraybackslash}X*{5}{>{\centering\arraybackslash}p{0.11\textwidth}}@{}",
    "5": r"@{}>{\raggedright\arraybackslash}p{0.20\textwidth}>{\raggedright\arraybackslash}p{0.22\textwidth}>{\raggedleft\arraybackslash}p{0.09\textwidth}>{\raggedright\arraybackslash}X@{}",
    "A3": r"@{}>{\raggedright\arraybackslash}X*{3}{>{\centering\arraybackslash}p{0.16\textwidth}}@{}",
}


def strip_markdown(text: str) -> str:
    text = re.sub(r"<!--.*?-->", "", text)
    text = MARKDOWN_LINK.sub(r"\1", text)
    return text.replace("**", "").replace("*", "").replace(chr(96), "").strip()


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_table_separator(line: str) -> bool:
    cells = split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def blocks(lines: list[str]):
    index = 0
    while index < len(lines):
        line = lines[index].rstrip()
        if not line or line.startswith("<!--"):
            index += 1
            continue
        if line.startswith("|") and index + 1 < len(lines) and is_table_separator(lines[index + 1]):
            rows = [split_table_row(line)]
            index += 2
            while index < len(lines) and lines[index].lstrip().startswith("|"):
                rows.append(split_table_row(lines[index]))
                index += 1
            yield "table", rows
            continue
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            yield "heading", (level, line[level:].strip())
            index += 1
            continue
        if re.match(r"^[-*] ", line):
            items = []
            while index < len(lines) and re.match(r"^[-*] ", lines[index].rstrip()):
                items.append(lines[index].rstrip()[2:].strip())
                index += 1
            yield "list", items
            continue
        if re.match(r"^\d+\. ", line):
            items = []
            while index < len(lines) and re.match(r"^\d+\. ", lines[index].rstrip()):
                items.append(re.sub(r"^\d+\. ", "", lines[index].rstrip()).strip())
                index += 1
            yield "numbered", items
            continue
        if line.startswith(">"):
            quote = []
            while index < len(lines) and lines[index].rstrip().startswith(">"):
                quote.append(lines[index].rstrip().lstrip("> ").strip())
                index += 1
            yield "quote", " ".join(quote)
            continue
        paragraph = [line]
        index += 1
        while index < len(lines):
            candidate = lines[index].rstrip()
            if (
                not candidate
                or candidate.startswith("#")
                or candidate.startswith("|")
                or candidate.startswith(">")
                or re.match(r"^[-*] ", candidate)
                or re.match(r"^\d+\. ", candidate)
            ):
                break
            paragraph.append(candidate)
            index += 1
        yield "paragraph", " ".join(paragraph)


def html_inline(text: str) -> str:
    tokens: dict[str, str] = {}

    def link(match: re.Match[str]) -> str:
        token = f"LINKTOKEN{len(tokens)}"
        label = html.escape(match.group(1), quote=False)
        url = html.escape(match.group(2), quote=True)
        tokens[token] = f'<link href="{url}" color="{BLUE_HEX}">{label}</link>'
        return token

    text = MARKDOWN_LINK.sub(link, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\x60([^\x60]+)\x60", r"<font face='Courier'>\1</font>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    for token in sorted(tokens, key=len, reverse=True):
        text = text.replace(token, tokens[token])
    return text


def latex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(character, character) for character in text)


def latex_inline(text: str) -> str:
    tokens: dict[str, str] = {}

    def link(match: re.Match[str]) -> str:
        token = f"LINKTOKEN{len(tokens)}"
        label = latex_escape(match.group(1))
        url = match.group(2).replace("%", r"\%").replace("#", r"\#")
        tokens[token] = rf"\href{{{url}}}{{{label}}}"
        return token

    text = MARKDOWN_LINK.sub(link, text)
    text = latex_escape(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\\textbf{\1}", text)
    text = re.sub(r"\x60([^\x60]+)\x60", r"\\texttt{\1}", text)
    def break_long_code(match: re.Match[str]) -> str:
        value = match.group(1)
        chunks = [value[index:index + 8] for index in range(0, len(value), 8)]
        return r"\texttt{" + r"\allowbreak{}".join(chunks) + "}"

    text = re.sub(r"\\texttt\{([A-Za-z0-9]{25,})\}", break_long_code, text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"\\emph{\1}", text)
    for token in sorted(tokens, key=len, reverse=True):
        text = text.replace(token, tokens[token])
    return text


def render_latex(lines: list[str]) -> str:
    output = [
        r"\documentclass[11pt]{article}",
        r"\usepackage[T1]{fontenc}",
        r"\usepackage[utf8]{inputenc}",
        r"\usepackage{XCharter}",
        r"\usepackage[letterpaper,top=0.78in,bottom=0.78in,left=0.86in,right=0.86in]{geometry}",
        r"\usepackage{graphicx}",
        r"\usepackage{tabularx}",
        r"\usepackage{booktabs}",
        r"\usepackage{array}",
        r"\usepackage{microtype}",
        r"\usepackage[table]{xcolor}",
        r"\definecolor{TAENavy}{HTML}{0B1F3A}",
        r"\definecolor{TAENavyMid}{HTML}{486581}",
        r"\definecolor{TAEPaleNavy}{HTML}{EDF1F5}",
        r"\definecolor{TAEInk}{HTML}{202124}",
        r"\usepackage[colorlinks=true,linkcolor=TAENavy,urlcolor=TAENavy,citecolor=TAENavy]{hyperref}",
        r"\usepackage{enumitem}",
        r"\usepackage{caption}",
        r"\usepackage{titlesec}",
        r"\usepackage{fancyhdr}",
        r"\usepackage[most]{tcolorbox}",
        r"\usepackage{placeins}",
        r"\color{TAEInk}",
        r"\titleformat{\section}{\Large\bfseries\color{TAENavy}}{}{0pt}{}",
        r"\titleformat{\subsection}{\large\bfseries\color{TAENavy}}{}{0pt}{}",
        r"\titleformat{\subsubsection}{\normalsize\bfseries\itshape\color{TAENavy}}{}{0pt}{}",
        r"\titlespacing*{\section}{0pt}{1.4em}{0.45em}",
        r"\titlespacing*{\subsection}{0pt}{1.05em}{0.3em}",
        r"\titlespacing*{\subsubsection}{0pt}{0.9em}{0.25em}",
        r"\pagestyle{fancy}",
        r"\fancyhf{}",
        r"\lhead{\small\color{TAENavy} Practical Human Control}",
        r"\rhead{\small\color{TAENavy} Preprint candidate v" + VERSION + r"}",
        r"\cfoot{\thepage}",
        r"\setlength{\headheight}{14pt}",
        r"\setlength{\parindent}{0pt}",
        r"\setlength{\parskip}{0.52em plus 0.08em minus 0.06em}",
        r"\setlength{\textfloatsep}{12pt plus 3pt minus 2pt}",
        r"\setlength{\floatsep}{10pt plus 2pt minus 2pt}",
        r"\setlength{\intextsep}{10pt plus 2pt minus 2pt}",
        r"\renewcommand{\arraystretch}{1.10}",
        r"\captionsetup{font=small,labelfont={bf,color=TAENavy},labelsep=period,justification=raggedright,singlelinecheck=false}",
        r"\newtcolorbox{TAETitleBox}{colback=TAEPaleNavy,colframe=TAENavy,boxrule=0.8pt,arc=2mm,left=12pt,right=12pt,top=14pt,bottom=14pt}",
        r"\newtcolorbox{TAEAbstractBox}{colback=white,colframe=TAENavyMid,boxrule=0.45pt,arc=1.5mm,left=12pt,right=12pt,top=9pt,bottom=9pt}",
        r"\begin{document}",
        r"\begin{TAETitleBox}",
        r"\begin{center}",
        r"{\LARGE\bfseries\color{TAENavy} " + latex_escape(TITLE) + r"\par}",
        r"\vspace{0.45em}",
        r"{\large " + latex_escape(SUBTITLE) + r"\par}",
        r"\vspace{1.0em}",
        r"{\normalsize\bfseries " + latex_escape(AUTHOR) + r"\par}",
        r"{\small " + latex_escape(AFFILIATION) + r"\par}",
        r"{\small ORCID: \href{https://orcid.org/" + ORCID + "}{" + ORCID + r"}\par}",
        r"{\small Correspondence: \href{mailto:" + CORRESPONDING_EMAIL + "}{" + latex_escape(CORRESPONDING_EMAIL) + r"}; \href{mailto:" + ALTERNATE_EMAIL + "}{" + latex_escape(ALTERNATE_EMAIL) + r"}\par}",
        r"\vspace{0.75em}",
        r"{\small Preprint candidate v" + VERSION + r" $\vert$ Not peer reviewed\par}",
        r"\end{center}",
        r"\end{TAETitleBox}",
        r"\vspace{0.75em}",
    ]
    started = False
    abstract_open = False
    pending_table: tuple[str, str] | None = None
    parsed = list(blocks(lines))
    index = 0
    while index < len(parsed):
        kind, value = parsed[index]
        if kind == "heading":
            level, heading = value
            plain = strip_markdown(heading)
            if plain == "Abstract":
                started = True
                abstract_open = True
                output.extend([r"\begin{TAEAbstractBox}", r"{\small\textbf{Abstract}\par\medskip}", r"\small"])
                index += 1
                continue
            if not started:
                index += 1
                continue
            if abstract_open:
                output.append(r"\end{TAEAbstractBox}")
                abstract_open = False
            command = "section*" if level == 2 else "subsection*" if level == 3 else "subsubsection*"
            if level == 2:
                output.append(r"\FloatBarrier")
            output.append(rf"\{command}{{{latex_inline(heading)}}}")
        elif not started:
            index += 1
            continue
        elif kind == "table":
            rows: list[list[str]] = value
            label, caption = pending_table or ("", "")
            pending_table = None
            column_count = max(len(row) for row in rows)
            environment = "table"
            target = r"\linewidth"
            spec = TABLE_SPECS.get(
                label,
                "@{}" + " ".join([r">{\raggedright\arraybackslash}X" for _ in range(column_count)]) + "@{}",
            )
            output.extend([rf"\begin{{{environment}}}[!htbp]", r"\centering"])
            if label:
                output.append(rf"\caption*{{\textcolor{{TAENavy}}{{\textbf{{Table {label}.}}}} {latex_inline(caption)}}}")
            output.extend([r"\footnotesize", r"\arrayrulecolor{TAENavy}", rf"\begin{{tabularx}}{{{target}}}{{{spec}}}", r"\toprule"])
            for row_index, row in enumerate(rows):
                cells = row + [""] * (column_count - len(row))
                rendered = [latex_inline(cell) for cell in cells]
                if row_index == 0:
                    output.append(r"\rowcolor{TAEPaleNavy}")
                    rendered = [rf"\textcolor{{TAENavy}}{{\textbf{{{cell}}}}}" for cell in rendered]
                output.append(" & ".join(rendered) + r" \\")
                if row_index == 0:
                    output.append(r"\midrule")
            output.extend([r"\bottomrule", r"\end{tabularx}", r"\arrayrulecolor{black}"])
            if index + 1 < len(parsed) and parsed[index + 1][0] == "paragraph":
                note = strip_markdown(parsed[index + 1][1])
                if note.startswith("Note."):
                    note_body = note[len("Note."):].strip()
                    output.append(rf"\par\vspace{{2pt}}\footnotesize\textit{{Note.}} {latex_inline(note_body)}")
                    index += 1
            output.append(rf"\end{{{environment}}}")
        elif kind in {"list", "numbered"}:
            environment = "itemize" if kind == "list" else "enumerate"
            output.append(rf"\begin{{{environment}}}[leftmargin=*]")
            for item in value:
                output.append(r"\item " + latex_inline(item))
            output.append(rf"\end{{{environment}}}")
        elif kind == "quote":
            output.extend([r"\begin{quote}\itshape", latex_inline(value), r"\end{quote}"])
        else:
            paragraph = value
            plain = strip_markdown(paragraph)
            table_match = TABLE_CAPTION.match(plain)
            if table_match:
                pending_table = (table_match.group(1), table_match.group(2))
                index += 1
                continue
            figure_path = next((path for label, path in FIGURES.items() if plain.startswith(label)), None)
            if figure_path:
                figure_label, caption = plain.split(".", 1) if "." in plain else ("Figure", plain)
                output.extend([
                    r"\begin{figure}[!htbp]",
                    r"\centering",
                    rf"\includegraphics[width=0.93\linewidth]{{figures/{Path(figure_path).name}}}",
                    rf"\caption*{{\textcolor{{TAENavy}}{{\textbf{{{latex_escape(figure_label)}.}}}} {latex_escape(caption.strip())}}}",
                    r"\end{figure}",
                ])
            elif not plain.startswith(("Author:", "ORCID:", "Status:", "Citation note for repository readers.")):
                if plain.startswith("Note."):
                    output.append(r"{\footnotesize\textit{Note.} " + latex_inline(plain[len("Note."):].strip()) + r"\par}")
                else:
                    output.append(latex_inline(paragraph))
        index += 1
    if abstract_open:
        output.append(r"\end{TAEAbstractBox}")
    output.append(r"\FloatBarrier")
    output.append(r"\end{document}")
    return "\n".join(output) + "\n"


def build_pdf(lines: list[str]) -> None:
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import inch
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas
    from reportlab.platypus import (
        BaseDocTemplate,
        Frame,
        Image,
        KeepTogether,
        LongTable,
        NextPageTemplate,
        PageBreak,
        PageTemplate,
        Paragraph,
        Spacer,
        TableStyle,
    )

    font_roots = [
        Path("/Users/markbanasihan/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype"),
        Path("/usr/share/fonts/truetype/noto"),
        Path("/usr/share/fonts/truetype/dejavu"),
    ]

    def first_font(names: list[str]) -> Path | None:
        for root in font_roots:
            for name in names:
                candidate = root / name
                if candidate.is_file():
                    return candidate
        return None

    regular = first_font(["NotoSerif-Regular.ttf", "DejaVuSerif.ttf"])
    bold = first_font(["NotoSerif-Bold.ttf", "DejaVuSerif-Bold.ttf"])
    italic = first_font(["NotoSerif-Italic.ttf", "DejaVuSerif-Italic.ttf"])
    mono = first_font(["DejaVuSansMono.ttf", "NotoSansMono-Regular.ttf"])
    base_font = "Times-Roman"
    bold_font = "Times-Bold"
    italic_font = "Times-Italic"
    if regular and bold and italic:
        pdfmetrics.registerFont(TTFont("NotoSerif", str(regular)))
        pdfmetrics.registerFont(TTFont("NotoSerif-Bold", str(bold)))
        pdfmetrics.registerFont(TTFont("NotoSerif-Italic", str(italic)))
        pdfmetrics.registerFontFamily("NotoSerif", normal="NotoSerif", bold="NotoSerif-Bold", italic="NotoSerif-Italic", boldItalic="NotoSerif-Bold")
        base_font = "NotoSerif"
        bold_font = "NotoSerif-Bold"
        italic_font = "NotoSerif-Italic"
    if mono:
        pdfmetrics.registerFont(TTFont("NotoMono", str(mono)))
    elif "NotoMono" not in pdfmetrics.getRegisteredFontNames():
        pdfmetrics.registerFontFamily("NotoMono", normal="Courier")

    styles = getSampleStyleSheet()
    blue = colors.HexColor(BLUE_HEX)
    mid_blue = colors.HexColor("#7FA6CF")
    pale_blue = colors.HexColor("#EAF2F8")
    ink = colors.HexColor("#202124")
    body = ParagraphStyle("Body", parent=styles["BodyText"], fontName=base_font, fontSize=8.25, leading=10.7, spaceAfter=4.2, textColor=ink)
    heading1 = ParagraphStyle("Heading1", parent=body, fontName=bold_font, fontSize=11.6, leading=13.5, spaceBefore=9, spaceAfter=4, textColor=blue)
    heading2 = ParagraphStyle("Heading2", parent=body, fontName=bold_font, fontSize=9.6, leading=11.5, spaceBefore=7, spaceAfter=3, textColor=blue)
    caption_style = ParagraphStyle("Caption", parent=body, fontSize=7.35, leading=9.2, spaceBefore=3, spaceAfter=6, textColor=ink)
    table_caption_style = ParagraphStyle("TableCaption", parent=caption_style, fontSize=8, leading=10, spaceBefore=3, spaceAfter=4)
    note_style = ParagraphStyle("Note", parent=caption_style, fontSize=7.2, leading=9, spaceBefore=3, spaceAfter=5)
    quote_style = ParagraphStyle("Quote", parent=body, fontName=italic_font, leftIndent=12, rightIndent=12, borderPadding=4)
    bullet_style = ParagraphStyle("Bullet", parent=body, leftIndent=15, firstLineIndent=-8, bulletIndent=2)
    table_style = ParagraphStyle("TableCell", parent=body, fontSize=7.1, leading=8.8, spaceAfter=0, textColor=ink)
    table_header = ParagraphStyle("TableHeader", parent=table_style, fontName=bold_font, textColor=blue)

    class NumberedCanvas(canvas.Canvas):
        def __init__(self, *args, **kwargs):
            kwargs["invariant"] = 1
            super().__init__(*args, **kwargs)

    def page(canvas_object, document):
        canvas_object.saveState()
        canvas_object.setStrokeColor(mid_blue)
        canvas_object.setLineWidth(0.5)
        canvas_object.line(0.72 * inch, 0.58 * inch, 7.78 * inch, 0.58 * inch)
        canvas_object.setFont(base_font, 7.5)
        canvas_object.setFillColor(blue)
        canvas_object.drawString(0.72 * inch, 0.36 * inch, f"Practical Human Control | Preprint candidate v{VERSION}")
        canvas_object.setFillColor(ink)
        canvas_object.drawRightString(7.78 * inch, 0.36 * inch, f"Page {document.page}")
        canvas_object.restoreState()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    document = BaseDocTemplate(
        str(PDF_OUTPUT),
        pagesize=letter,
        rightMargin=0.72 * inch,
        leftMargin=0.72 * inch,
        topMargin=0.72 * inch,
        bottomMargin=0.76 * inch,
        title=TITLE,
        author=AUTHOR,
        subject=f"Preprint candidate v{VERSION}",
    )
    full_frame = Frame(document.leftMargin, document.bottomMargin, document.width, document.height, id="full")
    gutter = 0.22 * inch
    column_width = (document.width - gutter) / 2
    left_frame = Frame(document.leftMargin, document.bottomMargin, column_width, document.height, id="left")
    right_frame = Frame(document.leftMargin + column_width + gutter, document.bottomMargin, column_width, document.height, id="right")
    document.addPageTemplates([
        PageTemplate(id="first", frames=[full_frame], onPage=page),
        PageTemplate(id="two", frames=[left_frame, right_frame], onPage=page),
        PageTemplate(id="wide", frames=[full_frame], onPage=page),
    ])

    story = [
        Spacer(1, 0.35 * inch),
        Paragraph(html.escape(TITLE), ParagraphStyle("Title", parent=heading1, fontSize=21, leading=24, alignment=TA_CENTER, textColor=blue)),
        Spacer(1, 0.12 * inch),
        Paragraph(html.escape(SUBTITLE), ParagraphStyle("Subtitle", parent=body, fontSize=12, leading=15, alignment=TA_CENTER, textColor=ink)),
        Spacer(1, 0.28 * inch),
        Paragraph(f"<b>{AUTHOR}</b>", ParagraphStyle("Author", parent=body, fontSize=11, alignment=TA_CENTER)),
        Paragraph(f'ORCID: <link href="https://orcid.org/{ORCID}" color="{BLUE_HEX}">{ORCID}</link>', ParagraphStyle("ORCID", parent=body, fontSize=9, alignment=TA_CENTER)),
        Spacer(1, 0.25 * inch),
        Paragraph(f"<b>Preprint candidate v{VERSION}</b><br/>Not peer reviewed", ParagraphStyle("Notice", parent=body, fontSize=9, leading=13, alignment=TA_CENTER, borderColor=blue, borderWidth=0.7, borderPadding=7)),
        Spacer(1, 0.35 * inch),
    ]
    started = False
    switched_to_columns = False
    pending_table: tuple[str, str] | None = None
    parsed = list(blocks(lines))
    index = 0
    while index < len(parsed):
        kind, value = parsed[index]
        if kind == "heading":
            level, heading = value
            if strip_markdown(heading) == "Abstract":
                started = True
            elif started and not switched_to_columns:
                story.extend([NextPageTemplate("two"), PageBreak()])
                switched_to_columns = True
            if started:
                story.append(Paragraph(html_inline(heading), heading1 if level == 2 else heading2))
        elif not started:
            index += 1
            continue
        elif kind == "table":
            rows: list[list[str]] = value
            label, caption = pending_table or ("", "")
            pending_table = None
            column_count = max(len(row) for row in rows)
            wide = label in WIDE_TABLES or column_count > 3
            available_width = document.width if wide else column_width
            fractions = {
                "1": [0.24, 0.10, 0.66],
                "2": [0.25, 0.25, 0.25, 0.25],
                "A1": [0.19, 0.09, 0.09, 0.63],
                "3": [0.16, 0.18, 0.09, 0.57],
                "4": [0.23, 0.13, 0.16, 0.16, 0.16, 0.16],
                "5": [0.20, 0.22, 0.10, 0.48],
                "A3": [0.28, 0.24, 0.24, 0.24],
            }.get(label, [1 / column_count] * column_count)
            formatted = []
            for row_index, row in enumerate(rows):
                cells = row + [""] * (column_count - len(row))
                style = table_header if row_index == 0 else table_style
                formatted.append([Paragraph(html_inline(cell), style) for cell in cells])
            table = LongTable(formatted, colWidths=[available_width * share for share in fractions], repeatRows=1, hAlign=TA_LEFT)
            table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), pale_blue),
                ("LINEABOVE", (0, 0), (-1, 0), 0.8, blue),
                ("LINEBELOW", (0, 0), (-1, 0), 0.4, mid_blue),
                ("LINEBELOW", (0, -1), (-1, -1), 0.8, blue),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 2),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2),
                ("TOPPADDING", (0, 0), (-1, -1), 1.8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.8),
            ]))
            table_items = []
            if label:
                table_items.append(Paragraph(f'<font color="{BLUE_HEX}"><b>Table {label}.</b></font> {html.escape(caption)}', table_caption_style))
            table_items.append(table)
            if index + 1 < len(parsed) and parsed[index + 1][0] == "paragraph":
                note = strip_markdown(parsed[index + 1][1])
                if note.startswith("Note."):
                    table_items.append(Paragraph(f"<i>Note.</i> {html.escape(note[len('Note.'):].strip())}", note_style))
                    index += 1
            if wide:
                story.extend([NextPageTemplate("wide"), PageBreak(), *table_items, NextPageTemplate("two")])
            else:
                story.extend([Spacer(1, 2), *table_items, Spacer(1, 5)])
        elif kind in {"list", "numbered"}:
            for item_index, item in enumerate(value, start=1):
                bullet = "\u2022" if kind == "list" else f"{item_index}."
                story.append(Paragraph(html_inline(item), bullet_style, bulletText=bullet))
        elif kind == "quote":
            story.append(Paragraph(html_inline(value), quote_style))
        else:
            paragraph = value
            plain = strip_markdown(paragraph)
            table_match = TABLE_CAPTION.match(plain)
            if table_match:
                pending_table = (table_match.group(1), table_match.group(2))
                index += 1
                continue
            figure_path = next((path for label, path in FIGURES.items() if plain.startswith(label)), None)
            if figure_path:
                path = ROOT / figure_path
                reader = ImageReader(str(path))
                width, height = reader.getSize()
                scale = min(column_width / width, 3.45 * inch / height)
                image = Image(str(path), width=width * scale, height=height * scale)
                story.append(KeepTogether([image, Paragraph(html_inline(paragraph), caption_style)]))
            elif not plain.startswith(("Author:", "ORCID:", "Status:", "Citation note for repository readers.")):
                story.append(Paragraph(html_inline(paragraph), note_style if plain.startswith("Note.") else body))
        index += 1

    document.build(story, canvasmaker=NumberedCanvas)


def main() -> int:
    global OUTPUT_DIR, TEX_OUTPUT, PDF_OUTPUT, VERSION
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--version", default=VERSION)
    parser.add_argument("--output-dir", default=str(OUTPUT_DIR))
    args = parser.parse_args()
    VERSION = args.version
    requested_output = Path(args.output_dir)
    OUTPUT_DIR = requested_output if requested_output.is_absolute() else ROOT / requested_output
    TEX_OUTPUT = OUTPUT_DIR / "main.tex"
    PDF_OUTPUT = OUTPUT_DIR / f"preprint-v{VERSION}.pdf"
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    latex = render_latex(lines)
    if args.check:
        failures = []
        if not TEX_OUTPUT.is_file() or TEX_OUTPUT.read_text(encoding="utf-8") != latex:
            failures.append("paper/arxiv/main.tex")
        overleaf_pdf = OUTPUT_DIR / "overleaf-compiled-v0.14.0.pdf"
        if not PDF_OUTPUT.is_file() or PDF_OUTPUT.stat().st_size < 100_000:
            failures.append("paper/arxiv/preprint-v0.14.0.pdf")
        if not overleaf_pdf.is_file() or overleaf_pdf.stat().st_size < 100_000:
            failures.append("paper/arxiv/overleaf-compiled-v0.14.0.pdf")
        elif PDF_OUTPUT.is_file() and PDF_OUTPUT.read_bytes() != overleaf_pdf.read_bytes():
            failures.append("canonical and Overleaf PDFs differ")
        if failures:
            raise SystemExit("arXiv preprint outputs differ or are missing: " + ", ".join(failures))
        print("arXiv preprint package: PASS (LaTeX source current; canonical PDF matches Overleaf)")
        return 0
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TEX_OUTPUT.write_text(latex, encoding="utf-8")
    print(f"built {TEX_OUTPUT.relative_to(ROOT)}; compile in Overleaf before synchronizing the canonical PDF")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
