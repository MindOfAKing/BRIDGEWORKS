"""Generate the April 2026 CEEFM monthly report PDF.

Loads MONTHLY-REPORT-CEEFM-2026-04.md, renders to PDF with BridgeWorks brand chrome,
and embeds any visuals present in charts/2026-04/ at the right section anchors.

Run as:
    python generate-monthly-report-pdf.py

Re-runnable. Each run reads the latest markdown and any new charts.
"""
from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Iterable

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image,
    KeepTogether,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

# ---------------------------------------------------------------------------
# Paths and brand constants
# ---------------------------------------------------------------------------

BASE = Path(__file__).resolve().parent
SOURCE_MD = BASE / "MONTHLY-REPORT-CEEFM-2026-04.md"
OUTPUT_PDF = BASE / "MONTHLY-REPORT-CEEFM-2026-04.pdf"
CHARTS_DIR = BASE / "charts" / "2026-04"
CAPTIONS_FILE = CHARTS_DIR / "captions.md"

NAVY = HexColor("#0F1A2E")
GOLD = HexColor("#B8860B")
IVORY = HexColor("#F5F0E8")
SAGE = HexColor("#4A6741")
CHARCOAL = HexColor("#1C2B3A")
WARM_GRAY = HexColor("#6B6560")
WHITE = HexColor("#FFFFFF")
TABLE_HEADER_BG = NAVY
TABLE_ROW_ALT = HexColor("#EFE9DD")

W, H = A4
MARGIN_L = 2.2 * cm
MARGIN_R = 2.2 * cm
MARGIN_T = 2.6 * cm
MARGIN_B = 2.4 * cm

# Image-section anchor mapping. Filename prefix : (section number, after-anchor text)
# `after_anchor` is a sentinel string. The image is inserted in the flowable stream
# immediately after the first paragraph that starts with this text.
IMAGE_ANCHORS = {
    "01-": ("Headline Metrics", "GEO / AI Visibility Score"),
    "02-": ("Headline Metrics", "Category breakdown today:"),
    "03-": ("Headline Metrics", "Marketing Audit Score"),
    "04-": ("Headline Metrics", "LinkedIn Company Page Baseline"),
    "05-": ("Headline Metrics", "LinkedIn Company Page Baseline"),
    "06-": ("Headline Metrics", "LinkedIn Company Page Baseline"),
    "07-": ("What Was Delivered", "Standalone `/contact` page"),
    "08-": ("Strategic Findings from the Marketing Audit", "Finding 1: Full-funnel"),
    "A-": ("What Was Delivered", "Full ProfessionalService schema"),
    "B-": ("What Was Delivered", "Five security headers"),
    "C-": ("Headline Metrics", "Marketing Audit Score"),
    "D-": ("Engagement Progress Overview", ""),
    "E-": ("What Was Delivered", "Standalone `/contact` page"),
    "F-": ("What Was Delivered", "Standalone `/contact` page"),
    "G-": ("Headline Metrics", "LinkedIn Company Page Baseline"),
    "H-": ("What Was Delivered", "robots.txt explicit Allow"),
    "I-": ("Headline Metrics", "LinkedIn Company Page Baseline"),
    "X1-": ("What Was Delivered", "Full ProfessionalService schema"),
    "X2-": ("What Was Delivered", "Placeholder stat counters fixed"),
    "X3-": ("What Was Delivered", "3 HU production typos"),
}

# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------

base_styles = getSampleStyleSheet()


def make_styles() -> dict[str, ParagraphStyle]:
    s: dict[str, ParagraphStyle] = {}
    s["body"] = ParagraphStyle(
        "body",
        parent=base_styles["BodyText"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=CHARCOAL,
        spaceAfter=6,
    )
    s["body_quote"] = ParagraphStyle(
        "body_quote",
        parent=s["body"],
        leftIndent=18,
        rightIndent=18,
        textColor=NAVY,
        fontName="Helvetica-Oblique",
        spaceAfter=8,
        borderColor=GOLD,
        borderWidth=0,
        borderPadding=4,
    )
    s["h1"] = ParagraphStyle(
        "h1",
        parent=s["body"],
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=26,
        textColor=NAVY,
        spaceBefore=14,
        spaceAfter=10,
    )
    s["h2"] = ParagraphStyle(
        "h2",
        parent=s["body"],
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=19,
        textColor=NAVY,
        spaceBefore=14,
        spaceAfter=8,
    )
    s["h3"] = ParagraphStyle(
        "h3",
        parent=s["body"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=15,
        textColor=NAVY,
        spaceBefore=10,
        spaceAfter=6,
    )
    s["h4"] = ParagraphStyle(
        "h4",
        parent=s["body"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=14,
        textColor=NAVY,
        spaceBefore=8,
        spaceAfter=4,
    )
    s["bullet"] = ParagraphStyle(
        "bullet",
        parent=s["body"],
        leftIndent=18,
        bulletIndent=4,
        spaceAfter=3,
    )
    s["caption"] = ParagraphStyle(
        "caption",
        parent=s["body"],
        fontSize=8.5,
        leading=11,
        textColor=WARM_GRAY,
        alignment=1,
        spaceBefore=4,
        spaceAfter=10,
    )
    s["meta"] = ParagraphStyle(
        "meta",
        parent=s["body"],
        fontSize=9,
        textColor=WARM_GRAY,
    )
    s["cover_title"] = ParagraphStyle(
        "cover_title",
        parent=s["body"],
        fontName="Helvetica-Bold",
        fontSize=26,
        leading=30,
        textColor=IVORY,
        alignment=0,
    )
    s["cover_meta"] = ParagraphStyle(
        "cover_meta",
        parent=s["body"],
        fontSize=11,
        textColor=IVORY,
        alignment=0,
        leading=15,
    )
    return s


# ---------------------------------------------------------------------------
# Page chrome
# ---------------------------------------------------------------------------


def draw_page_chrome(canvas, doc):
    """Ivory background, gold left accent rule, navy footer bar with credit."""
    canvas.saveState()
    # Ivory full-bleed background
    canvas.setFillColor(IVORY)
    canvas.rect(0, 0, W, H, fill=1, stroke=0)
    # Gold left accent rule
    canvas.setFillColor(GOLD)
    canvas.rect(0, 0, 6, H, fill=1, stroke=0)
    # Footer
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(WARM_GRAY)
    canvas.drawCentredString(
        W / 2, 18, "office@bridgeworks.agency  ·  bridgeworks.agency"
    )
    # Page number
    canvas.drawRightString(W - MARGIN_R, 18, f"{doc.page}")
    canvas.restoreState()


def draw_cover_chrome(canvas, doc):
    """Cover page: navy header band covering top third, gold accent."""
    canvas.saveState()
    canvas.setFillColor(IVORY)
    canvas.rect(0, 0, W, H, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, 0, 6, H, fill=1, stroke=0)
    # Navy header band (top 35%)
    band_h = H * 0.4
    band_y = H - band_h
    canvas.setFillColor(NAVY)
    canvas.rect(0, band_y, W, band_h, fill=1, stroke=0)
    # Gold thin rule beneath the band
    canvas.setFillColor(GOLD)
    canvas.rect(0, band_y - 4, W, 4, fill=1, stroke=0)
    # Footer
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(WARM_GRAY)
    canvas.drawCentredString(
        W / 2, 18, "office@bridgeworks.agency  ·  bridgeworks.agency"
    )
    canvas.restoreState()


# ---------------------------------------------------------------------------
# Markdown parsing
# ---------------------------------------------------------------------------

INLINE_BOLD = re.compile(r"\*\*(.+?)\*\*")
INLINE_ITALIC = re.compile(r"(?<!\*)\*([^*]+?)\*(?!\*)")
INLINE_CODE = re.compile(r"`([^`]+?)`")
INLINE_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def md_inline_to_html(text: str) -> str:
    """Convert minimal markdown inline syntax to Paragraph-compatible HTML."""
    # Order matters: code, then bold, then italic, then links.
    text = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    text = INLINE_CODE.sub(
        lambda m: f'<font name="Helvetica-Oblique" color="#4A6741">{m.group(1)}</font>',
        text,
    )
    text = INLINE_BOLD.sub(r"<b>\1</b>", text)
    text = INLINE_ITALIC.sub(r"<i>\1</i>", text)
    text = INLINE_LINK.sub(
        r'<link href="\2" color="#4A6741"><u>\1</u></link>', text
    )
    return text


def parse_table_block(lines: list[str]) -> Table | None:
    """Parse a markdown table block into a reportlab Table flowable."""
    rows: list[list[str]] = []
    for line in lines:
        if not line.strip().startswith("|"):
            continue
        # Skip alignment row
        if re.match(r"^\s*\|[\s:|-]+\|\s*$", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows.append(cells)
    if not rows:
        return None
    # Build paragraph cells with inline markdown
    para_style = ParagraphStyle(
        "cell",
        fontName="Helvetica",
        fontSize=8.5,
        leading=11,
        textColor=CHARCOAL,
    )
    header_style = ParagraphStyle(
        "header_cell",
        fontName="Helvetica-Bold",
        fontSize=8.5,
        leading=11,
        textColor=IVORY,
    )
    data: list[list[Paragraph]] = []
    for i, row in enumerate(rows):
        styled = []
        for cell in row:
            html = md_inline_to_html(cell)
            styled.append(Paragraph(html, header_style if i == 0 else para_style))
        data.append(styled)
    # Auto-size columns: equal split with floor minimum
    n_cols = max(len(r) for r in data)
    avail = W - MARGIN_L - MARGIN_R
    col_w = avail / n_cols
    table = Table(data, colWidths=[col_w] * n_cols, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
                ("TEXTCOLOR", (0, 0), (-1, 0), IVORY),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [IVORY, TABLE_ROW_ALT],
                ),
                ("LINEBELOW", (0, 0), (-1, 0), 0.5, GOLD),
                ("BOX", (0, 0), (-1, -1), 0.3, WARM_GRAY),
            ]
        )
    )
    return table


def load_captions() -> dict[str, str]:
    if not CAPTIONS_FILE.exists():
        return {}
    captions: dict[str, str] = {}
    for line in CAPTIONS_FILE.read_text(encoding="utf-8").splitlines():
        m = re.match(r"`([^`]+\.png)`\s*[-:]\s*(.+)", line.strip())
        if m:
            captions[m.group(1)] = m.group(2).strip()
    return captions


def find_chart_files() -> dict[str, list[Path]]:
    """Return {prefix: [Paths]} for every PNG matching a known anchor prefix."""
    if not CHARTS_DIR.exists():
        return {}
    found: dict[str, list[Path]] = {prefix: [] for prefix in IMAGE_ANCHORS}
    for f in sorted(CHARTS_DIR.glob("*.png")):
        for prefix in IMAGE_ANCHORS:
            if f.name.startswith(prefix):
                found[prefix].append(f)
                break
    return found


def make_image_flowable(path: Path, caption: str | None) -> list:
    """Embed image at content width with optional caption."""
    avail = W - MARGIN_L - MARGIN_R
    img = Image(str(path), width=avail, height=avail * 0.55, kind="proportional")
    flow = [img]
    if caption:
        flow.append(Paragraph(md_inline_to_html(caption), make_styles()["caption"]))
    flow.append(Spacer(1, 6))
    return [KeepTogether(flow)]


def parse_markdown(md_text: str, styles: dict[str, ParagraphStyle]) -> list:
    """Convert the report markdown into a list of Platypus flowables."""
    lines = md_text.splitlines()
    flowables: list = []
    i = 0
    pending_table: list[str] = []

    def flush_table():
        nonlocal pending_table
        if pending_table:
            tbl = parse_table_block(pending_table)
            if tbl is not None:
                flowables.append(tbl)
                flowables.append(Spacer(1, 6))
            pending_table = []

    skip_first_h1 = True  # skip the first H1 (used in cover instead)

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Tables
        if stripped.startswith("|"):
            pending_table.append(line)
            i += 1
            continue
        else:
            flush_table()

        # Horizontal rule
        if stripped in ("---", "***"):
            flowables.append(Spacer(1, 4))
            i += 1
            continue

        # Empty line
        if not stripped:
            flowables.append(Spacer(1, 4))
            i += 1
            continue

        # Headings
        if stripped.startswith("#"):
            level = 0
            while level < len(stripped) and stripped[level] == "#":
                level += 1
            text = stripped[level:].strip()
            if level == 1 and skip_first_h1:
                skip_first_h1 = False
                i += 1
                continue
            style_key = {1: "h1", 2: "h2", 3: "h3", 4: "h4"}.get(level, "h4")
            flowables.append(Paragraph(md_inline_to_html(text), styles[style_key]))
            i += 1
            continue

        # Block quote
        if stripped.startswith(">"):
            text = stripped.lstrip(">").strip()
            flowables.append(Paragraph(md_inline_to_html(text), styles["body_quote"]))
            i += 1
            continue

        # Bullet list
        if stripped.startswith(("- ", "* ")):
            bullet_text = stripped[2:].strip()
            flowables.append(
                Paragraph(
                    f"• {md_inline_to_html(bullet_text)}",
                    styles["bullet"],
                )
            )
            i += 1
            continue

        # Numbered list
        m = re.match(r"^\d+\.\s+(.*)", stripped)
        if m:
            flowables.append(
                Paragraph(
                    f"{stripped.split(' ', 1)[0]} {md_inline_to_html(m.group(1))}",
                    styles["bullet"],
                )
            )
            i += 1
            continue

        # Regular paragraph
        para_lines = [stripped]
        j = i + 1
        while j < len(lines) and lines[j].strip() and not lines[j].strip().startswith(
            ("#", "-", "*", "|", ">", "```")
        ) and not re.match(r"^\d+\.\s", lines[j].strip()):
            para_lines.append(lines[j].strip())
            j += 1
        para_text = " ".join(para_lines)
        flowables.append(Paragraph(md_inline_to_html(para_text), styles["body"]))
        i = j

    flush_table()
    return flowables


# ---------------------------------------------------------------------------
# Image insertion
# ---------------------------------------------------------------------------


def insert_images(flowables: list, charts: dict[str, list[Path]], captions: dict[str, str], styles: dict[str, ParagraphStyle]) -> list:
    """Walk the flowable list and insert images after their anchor paragraphs.

    Anchor matching: each image has a (section_text, after_anchor) target. The image
    is inserted immediately after the first paragraph whose plain text starts with
    `after_anchor`. If anchor is empty, image goes at the section heading.
    """
    if not charts:
        return flowables

    # Build a flat list of (anchor_text -> [image_flowables_to_insert_after])
    anchor_to_images: dict[str, list] = {}
    for prefix, paths in charts.items():
        if not paths:
            continue
        section, anchor = IMAGE_ANCHORS[prefix]
        key = anchor if anchor else section
        for path in paths:
            cap = captions.get(path.name, path.stem.replace("-", " ").title())
            anchor_to_images.setdefault(key, []).extend(make_image_flowable(path, cap))

    if not anchor_to_images:
        return flowables

    # Walk flowables; after a Paragraph whose text starts with an anchor, splice images
    out: list = []
    for fl in flowables:
        out.append(fl)
        if isinstance(fl, Paragraph):
            # Reportlab Paragraph stores its source text in `.text`
            try:
                plain = re.sub(r"<[^>]+>", "", fl.text or "")
            except Exception:
                plain = ""
            for anchor_text, imgs in list(anchor_to_images.items()):
                if plain.lstrip().startswith(anchor_text):
                    out.extend(imgs)
                    del anchor_to_images[anchor_text]
                    break
    return out


# ---------------------------------------------------------------------------
# Cover and document assembly
# ---------------------------------------------------------------------------


def cover_flowables(styles: dict[str, ParagraphStyle]) -> list:
    """Cover page flowables sitting on the navy band area."""
    flow = [
        Spacer(1, 1.5 * cm),
        Paragraph(
            '<font name="Helvetica" color="#B8860B" size="10">CONFIDENTIAL · CLIENT REPORT</font>',
            styles["meta"],
        ),
        Spacer(1, 0.4 * cm),
        Paragraph(
            "Engagement Update<br/>Month 1 of 16",
            styles["cover_title"],
        ),
        Spacer(1, 0.5 * cm),
        Paragraph(
            "CEEFM Kft  ·  BridgeWorks",
            styles["cover_meta"],
        ),
        Paragraph(
            "Period: Weeks 1-5, late March to 30 April 2026",
            styles["cover_meta"],
        ),
        Paragraph(
            "Issued: 2026-04-30",
            styles["cover_meta"],
        ),
        # Push the rest below the navy band
        Spacer(1, H * 0.42),
        Paragraph(
            "<b>Prepared for</b><br/>Victor Danmagaji<br/>Managing Director, CEEFM Kft",
            styles["body"],
        ),
        Spacer(1, 0.5 * cm),
        Paragraph(
            "<b>Prepared by</b><br/>Emmanuel Ehigbai<br/>BridgeWorks  ·  office@bridgeworks.agency",
            styles["body"],
        ),
        NextPageTemplate("body"),
        PageBreak(),
    ]
    return flow


def build():
    if not SOURCE_MD.exists():
        raise SystemExit(f"Missing source markdown: {SOURCE_MD}")

    md_text = SOURCE_MD.read_text(encoding="utf-8")
    styles = make_styles()
    captions = load_captions()
    charts = find_chart_files()

    body_flowables = parse_markdown(md_text, styles)
    body_flowables = insert_images(body_flowables, charts, captions, styles)

    flow = cover_flowables(styles) + body_flowables

    # Doc template with two page templates: cover and body
    cover_frame = Frame(
        MARGIN_L,
        MARGIN_B,
        W - MARGIN_L - MARGIN_R,
        H - MARGIN_T - MARGIN_B,
        id="cover",
        showBoundary=0,
    )
    body_frame = Frame(
        MARGIN_L,
        MARGIN_B,
        W - MARGIN_L - MARGIN_R,
        H - MARGIN_T - MARGIN_B,
        id="body",
        showBoundary=0,
    )

    doc = BaseDocTemplate(
        str(OUTPUT_PDF),
        pagesize=A4,
        leftMargin=MARGIN_L,
        rightMargin=MARGIN_R,
        topMargin=MARGIN_T,
        bottomMargin=MARGIN_B,
        title="CEEFM Engagement Update: Month 1 of 16",
        author="Emmanuel Ehigbai / BridgeWorks",
        subject="CEEFM Kft April 2026 Monthly Report",
    )

    doc.addPageTemplates(
        [
            PageTemplate(id="cover", frames=[cover_frame], onPage=draw_cover_chrome),
            PageTemplate(id="body", frames=[body_frame], onPage=draw_page_chrome),
        ]
    )

    # PageTemplates already define onPage chrome callbacks. The first PageTemplate
    # in the list ("cover") is used for page 1; we switch to the "body" template
    # via NextPageTemplate immediately before the cover-flow PageBreak.
    doc.build(flow)

    n_charts = sum(len(v) for v in charts.values())
    print(f"Wrote {OUTPUT_PDF}")
    print(f"Embedded {n_charts} chart(s) from {CHARTS_DIR}")


if __name__ == "__main__":
    build()
