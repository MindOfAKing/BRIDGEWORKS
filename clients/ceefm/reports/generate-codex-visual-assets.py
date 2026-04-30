from __future__ import annotations

from pathlib import Path
from math import cos, sin, pi
import json
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "charts" / "2026-04"
OUT.mkdir(parents=True, exist_ok=True)

NAVY = "#0F1A2E"
GOLD = "#B8860B"
IVORY = "#F5F0E8"
SAGE = "#4A6741"
CHARCOAL = "#1C2B3A"
MUTED = "#6B6560"
GRID = "#D8CFC2"
RED = "#B33A3A"
WHITE = "#FFFFFF"


def font(size: int, bold: bool = False):
    candidates = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


F_TITLE = font(38, True)
F_H2 = font(26, True)
F_BODY = font(20)
F_SMALL = font(16)
F_TINY = font(14)


def canvas(w=1200, h=800):
    img = Image.new("RGB", (w, h), IVORY)
    draw = ImageDraw.Draw(img)
    return img, draw


def t(draw, xy, text, fill=CHARCOAL, f=F_BODY, anchor=None):
    draw.text(xy, text, fill=fill, font=f, anchor=anchor)


def title(draw, heading, sub=None):
    t(draw, (60, 45), heading, NAVY, F_TITLE)
    if sub:
        t(draw, (60, 92), sub, MUTED, F_BODY)


def save(img, name):
    img.save(OUT / name)


def bar_label(draw, x, y, label, value):
    t(draw, (x, y), label, CHARCOAL, F_SMALL)
    t(draw, (x + 360, y), str(value), NAVY, F_SMALL)


def chart_01_geo_progression():
    points = [("Mar", 16), ("Apr 3", 29), ("Apr 22", 47), ("Apr 30", 61)]
    img, draw = canvas()
    title(draw, "GEO Score Progression", "CEEFM moved from Critical to Fair in Month 1.")
    left, top, right, bottom = 120, 150, 1120, 660
    bands = [
        (0, 39, "#F3D8D8", "Critical"),
        (40, 59, "#F1E2C6", "Poor"),
        (60, 74, "#E9E5C9", "Fair"),
        (75, 89, "#DDEAD6", "Good"),
        (90, 100, "#D3E7DC", "Excellent"),
    ]
    for lo, hi, color, label in bands:
        y1 = bottom - (hi / 100) * (bottom - top)
        y2 = bottom - (lo / 100) * (bottom - top)
        draw.rectangle((left, y1, right, y2), fill=color)
        t(draw, (right - 100, (y1 + y2) / 2 - 10), label, MUTED, F_TINY)
    for i in range(0, 101, 20):
        y = bottom - (i / 100) * (bottom - top)
        draw.line((left, y, right, y), fill=GRID, width=1)
        t(draw, (70, y - 10), str(i), MUTED, F_TINY)
    xs = [left + i * (right - left) / (len(points) - 1) for i in range(len(points))]
    ys = [bottom - (score / 100) * (bottom - top) for _, score in points]
    draw.line(list(zip(xs, ys)), fill=NAVY, width=5)
    for x, y, (label, score) in zip(xs, ys, points):
        draw.ellipse((x - 9, y - 9, x + 9, y + 9), fill=GOLD, outline=NAVY, width=2)
        t(draw, (x, y - 42), str(score), NAVY, F_H2, anchor="mm")
        t(draw, (x, bottom + 30), label, MUTED, F_SMALL, anchor="mm")
    save(img, "01-geo-score-progression.png")


def chart_02_geo_delta():
    categories = [
        ("AI Citability", 58, 72),
        ("Brand Authority", 18, 28),
        ("Content E-E-A-T", 34, 57),
        ("Technical GEO", 78, 88),
        ("Schema", 52, 71),
        ("Platform", 54, 57),
    ]
    img, draw = canvas()
    title(draw, "GEO Category Delta", "Apr 22 vs Apr 30 after schema, imprint, headers, and stat fixes.")
    left, top, right, bottom = 120, 170, 1120, 650
    for i in range(0, 101, 20):
        y = bottom - (i / 100) * (bottom - top)
        draw.line((left, y, right, y), fill=GRID, width=1)
        t(draw, (75, y - 8), str(i), MUTED, F_TINY)
    group_w = (right - left) / len(categories)
    bar_w = 28
    for i, (label, old, new) in enumerate(categories):
        cx = left + i * group_w + group_w / 2
        for value, color, offset in [(old, MUTED, -18), (new, GOLD, 18)]:
            y = bottom - (value / 100) * (bottom - top)
            draw.rectangle((cx + offset - bar_w / 2, y, cx + offset + bar_w / 2, bottom), fill=color)
        t(draw, (cx, bottom + 26), label, CHARCOAL, F_TINY, anchor="mm")
        t(draw, (cx, bottom - (new / 100) * (bottom - top) - 25), f"+{new-old}", SAGE, F_SMALL, anchor="mm")
    t(draw, (840, 110), "Apr 22", MUTED, F_SMALL)
    draw.rectangle((910, 111, 935, 126), fill=MUTED)
    t(draw, (970, 110), "Apr 30", MUTED, F_SMALL)
    draw.rectangle((1040, 111, 1065, 126), fill=GOLD)
    save(img, "02-geo-categories-delta.png")


def chart_03_marketing_radar():
    data = [
        ("Content", 67),
        ("Conversion", 54),
        ("SEO", 80),
        ("Competitive", 72),
        ("Brand", 68),
        ("Growth", 64),
    ]
    img, draw = canvas()
    title(draw, "Marketing Audit Radar", "Current marketing effectiveness score: 67.6 out of 100.")
    cx, cy, radius = 600, 420, 250
    for r in [50, 100, 150, 200, 250]:
        pts = []
        for i in range(len(data)):
            angle = -pi / 2 + i * 2 * pi / len(data)
            pts.append((cx + r * cos(angle), cy + r * sin(angle)))
        draw.polygon(pts, outline=GRID)
    pts = []
    for i, (label, score) in enumerate(data):
        angle = -pi / 2 + i * 2 * pi / len(data)
        end = (cx + radius * cos(angle), cy + radius * sin(angle))
        draw.line((cx, cy, *end), fill=GRID, width=1)
        label_pos = (cx + (radius + 75) * cos(angle), cy + (radius + 55) * sin(angle))
        t(draw, label_pos, f"{label}\n{score}", NAVY, F_SMALL, anchor="mm")
        pts.append((cx + radius * score / 100 * cos(angle), cy + radius * score / 100 * sin(angle)))
    draw.polygon(pts, fill="#D9C185", outline=GOLD)
    draw.line(pts + [pts[0]], fill=GOLD, width=3)
    save(img, "03-marketing-audit-radar.png")


def linkedin_data():
    parsed = json.loads((ROOT / "linkedin-analytics" / "parsed-linkedin-exports.json").read_text(encoding="utf-8"))
    return parsed


def chart_04_linkedin_impressions():
    parsed = linkedin_data()
    rows = parsed["cee-facility-management_content_1777555091040.xls"]["Metrics"]
    header = rows[1]
    idx_date = header.index("Date")
    idx = header.index("Impressions (total)")
    data = []
    for row in rows[2:]:
        dt = datetime.strptime(row[idx_date], "%m/%d/%Y")
        if datetime(2026, 4, 1) <= dt <= datetime(2026, 4, 28):
            data.append((dt.day, float(row[idx])))
    img, draw = canvas()
    title(draw, "LinkedIn Daily Impressions", "April 1 to April 28, native LinkedIn export.")
    left, top, right, bottom = 110, 160, 1120, 650
    max_v = max(v for _, v in data)
    for i in range(5):
        y = bottom - i * (bottom - top) / 4
        draw.line((left, y, right, y), fill=GRID)
        t(draw, (45, y - 8), f"{int(max_v*i/4):,}", MUTED, F_TINY)
    step = (right - left) / len(data)
    prev = None
    for i, (day, value) in enumerate(data):
        x = left + i * step + step / 2
        y = bottom - value / max_v * (bottom - top)
        if prev:
            draw.line((prev[0], prev[1], x, y), fill=NAVY, width=4)
        draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=GOLD)
        if i % 3 == 0:
            t(draw, (x, bottom + 25), f"{day:02d}", MUTED, F_TINY, anchor="mm")
        prev = (x, y)
    save(img, "04-linkedin-impressions-april.png")


def chart_05_linkedin_followers():
    parsed = linkedin_data()
    rows = parsed["cee-facility-management_followers_1777555120439.xls"]["New followers"]
    header = rows[0]
    idx_date = header.index("Date")
    idx_total = header.index("Total followers")
    cumulative = 0
    data = []
    for row in rows[1:]:
        dt = datetime.strptime(row[idx_date], "%m/%d/%Y")
        cumulative += int(float(row[idx_total]))
        data.append((dt.strftime("%m/%d"), cumulative))
    img, draw = canvas()
    title(draw, "LinkedIn Follower Growth", "Cumulative new followers across the export window.")
    left, top, right, bottom = 120, 170, 1120, 650
    max_v = max(v for _, v in data) or 1
    for i in range(5):
        y = bottom - i * (bottom - top) / 4
        draw.line((left, y, right, y), fill=GRID)
        t(draw, (75, y - 8), str(int(max_v * i / 4)), MUTED, F_TINY)
    step = (right - left) / (len(data) - 1)
    pts = []
    for i, (_, value) in enumerate(data):
        x = left + i * step
        y = bottom - value / max_v * (bottom - top)
        pts.append((x, y))
    draw.line(pts, fill=NAVY, width=5)
    for i, (label, _) in enumerate(data):
        if i % 4 == 0:
            t(draw, (left + i * step, bottom + 25), label, MUTED, F_TINY, anchor="mm")
    t(draw, (right - 60, top + 10), f"+{max_v} followers", GOLD, F_H2)
    save(img, "05-linkedin-followers-cumulative.png")


def top_rows(parsed, file, sheet, limit=5):
    rows = parsed[file][sheet]
    return [(str(r[0]), int(float(r[1]))) for r in rows[1:limit+1]]


def chart_06_demographics():
    parsed = linkedin_data()
    file = "cee-facility-management_followers_1777555120439.xls"
    panels = [
        ("Job functions", top_rows(parsed, file, "Job function")),
        ("Industries", top_rows(parsed, file, "Industry")),
        ("Locations", top_rows(parsed, file, "Location")),
    ]
    clean = {
        "Budapest Metropolitan Area, Hungary": "Budapest, Hungary",
        "Greater Delhi Area, India": "Delhi, India",
        "Dubai, United Arab Emirates": "Dubai, UAE",
        "Nairobi County, Kenya": "Nairobi, Kenya",
        "Jakarta Metropolitan Area, Indonesia": "Jakarta, Indonesia",
    }
    img, draw = canvas()
    title(draw, "LinkedIn Audience Demographics", "Follower demographics used as proxy. Visitor demographic export was not available.")
    for p, (heading, rows) in enumerate(panels):
        x = 70 + p * 380
        y = 165
        draw.rounded_rectangle((x, y, x + 330, 690), radius=8, fill=WHITE, outline=GRID)
        t(draw, (x + 25, y + 25), heading, NAVY, F_H2)
        max_v = max(v for _, v in rows)
        for i, (label, value) in enumerate(rows):
            label = clean.get(label, label)[:28]
            by = y + 90 + i * 75
            t(draw, (x + 25, by), label, CHARCOAL, F_TINY)
            w = int(210 * value / max_v)
            draw.rounded_rectangle((x + 25, by + 28, x + 25 + w, by + 48), radius=5, fill=GOLD if p == 2 else SAGE)
            t(draw, (x + 250, by + 25), str(value), NAVY, F_SMALL)
    save(img, "06-linkedin-visitor-demographics.png")


def chart_07_sitemap():
    img, draw = canvas()
    title(draw, "Sitemap Before and After", "The contact pages expand the indexable site from 2 URLs to 4 URLs.")
    panels = [
        ("Before", ["https://ceefm.eu/", "https://ceefm.eu/hu/"]),
        ("After", ["https://ceefm.eu/", "https://ceefm.eu/contact/", "https://ceefm.eu/hu/", "https://ceefm.eu/hu/kapcsolat/"]),
    ]
    for i, (heading, urls) in enumerate(panels):
        x = 90 + i * 540
        draw.rounded_rectangle((x, 170, x + 480, 650), radius=8, fill=WHITE, outline=GRID)
        t(draw, (x + 30, 200), heading, NAVY, F_H2)
        for j, url in enumerate(urls):
            y = 270 + j * 75
            draw.rounded_rectangle((x + 30, y, x + 450, y + 48), radius=6, fill=IVORY, outline=GRID)
            t(draw, (x + 50, y + 14), url, CHARCOAL, F_SMALL)
        t(draw, (x + 30, 590), f"{len(urls)} URLs", GOLD, F_H2)
    save(img, "07-sitemap-before-after.png")


def chart_08_funnel():
    stages = [
        ("Awareness", "No blog or case study index"),
        ("Visit", "Single long scroll"),
        ("Engaged", "Form buried late"),
        ("Form Submit", "No calendar booking"),
        ("Walkthrough", "Manual follow-up"),
        ("Contract", "0.13 to 0.45% estimate"),
    ]
    img, draw = canvas()
    title(draw, "Conversion Funnel Leak Points", "Estimated visitor-to-contract range is 0.13 to 0.45%.")
    top = 165
    widths = [920, 780, 640, 500, 360, 230]
    for i, (stage, note) in enumerate(stages):
        y = top + i * 80
        w = widths[i]
        x = 600 - w / 2
        draw.polygon([(x, y), (x + w, y), (x + w - 45, y + 58), (x + 45, y + 58)], fill=GOLD if i == 0 else SAGE)
        t(draw, (600, y + 13), stage, WHITE, F_H2, anchor="mt")
        t(draw, (600, y + 42), note, WHITE, F_TINY, anchor="mt")
    save(img, "08-funnel-diagram.png")


def composite_x1_schema():
    img, draw = canvas(1600, 800)
    title(draw, "Schema Completeness", "The deploy moved CEEFM from a thin local entity to a defensible ProfessionalService entity.")
    panels = [
        ("Before", ["@type: LocalBusiness", "name: CEEFM Kft", "url", "email", "aggregateRating risk"]),
        ("After", ["legalName", "taxID", "foundingDate", "PostalAddress", "geo", "openingHours", "contactPoint", "sameAs", "7 service offers", "speakable", "numberOfEmployees"]),
    ]
    for i, (heading, items) in enumerate(panels):
        x = 90 + i * 760
        draw.rounded_rectangle((x, 170, x + 680, 700), radius=8, fill=WHITE, outline=GRID)
        t(draw, (x + 35, 205), heading, NAVY, F_H2)
        for j, item in enumerate(items):
            y = 270 + j * 38
            draw.ellipse((x + 38, y + 7, x + 48, y + 17), fill=GOLD if i else RED)
            t(draw, (x + 62, y), item, CHARCOAL, F_SMALL)
    save(img, "X1-schema-completeness.png")


def composite_x2_stats():
    img, draw = canvas(1600, 800)
    title(draw, "Stat Counter Fix", "Crawlers now see the real proof points in raw HTML.")
    panels = [
        ("Before", [("0+", "Properties"), ("0%", "Retention"), ("0+", "Years")], RED),
        ("After", [("50+", "Properties"), ("98%", "Retention"), ("10+", "Years")], SAGE),
    ]
    for i, (heading, stats, color) in enumerate(panels):
        x = 100 + i * 760
        draw.rounded_rectangle((x, 190, x + 660, 630), radius=8, fill=WHITE, outline=GRID)
        t(draw, (x + 35, 225), heading, NAVY, F_H2)
        for j, (num, label) in enumerate(stats):
            sx = x + 50 + j * 200
            draw.rounded_rectangle((sx, 330, sx + 160, 470), radius=8, fill=IVORY, outline=GRID)
            t(draw, (sx + 80, 360), num, color, font(40, True), anchor="mt")
            t(draw, (sx + 80, 425), label, MUTED, F_SMALL, anchor="mt")
    save(img, "X2-stat-counters.png")


def composite_x3_typos():
    pairs = [
        ("márkareputaéció", "márkareputáció"),
        ("szabányait", "szabványait"),
        ("szabányainak", "szabványainak"),
    ]
    img, draw = canvas(1600, 800)
    title(draw, "Hungarian Copy Corrections", "Three production typo fixes shipped with the contact-page package.")
    t(draw, (260, 165), "Before", NAVY, F_H2, anchor="mm")
    t(draw, (1040, 165), "After", NAVY, F_H2, anchor="mm")
    for i, (before, after) in enumerate(pairs):
        y = 230 + i * 150
        draw.rounded_rectangle((100, y, 700, y + 95), radius=8, fill=WHITE, outline=GRID)
        draw.rounded_rectangle((880, y, 1480, y + 95), radius=8, fill=WHITE, outline=GRID)
        t(draw, (130, y + 30), before, RED, F_H2)
        draw.line((130, y + 66, 130 + 15 * len(before), y + 66), fill=RED, width=3)
        t(draw, (910, y + 30), after, SAGE, F_H2)
    save(img, "X3-hu-typos.png")


def captions():
    entries = {
        "01-geo-score-progression.png": "GEO score progression across Month 1. CEEFM moved from Critical to Fair after schema, imprint, security headers, and stat-counter fixes.",
        "02-geo-categories-delta.png": "Category-level GEO movement from Apr 22 to Apr 30. Content E-E-A-T and Schema produced the largest lifts.",
        "03-marketing-audit-radar.png": "Marketing audit radar showing current strength in SEO and competitive positioning, with conversion as the main drag.",
        "04-linkedin-impressions-april.png": "Daily LinkedIn impressions from the native Page admin export. The mid-April spike came from hospitality operations content.",
        "05-linkedin-followers-cumulative.png": "Cumulative new LinkedIn followers across the export window. All 54 new followers were organic.",
        "06-linkedin-visitor-demographics.png": "Audience quality signals from LinkedIn follower demographics. Visitor demographic export was not available.",
        "07-sitemap-before-after.png": "Sitemap expansion from two URLs to four URLs after adding the contact pages.",
        "08-funnel-diagram.png": "Six-stage conversion funnel with the current leak points identified in the marketing audit.",
        "X1-schema-completeness.png": "Before and after view of schema completeness. The site now exposes a defensible ProfessionalService entity.",
        "X2-stat-counters.png": "Before and after view of stat counters. Crawlers no longer see zero-value placeholders.",
        "X3-hu-typos.png": "Three Hungarian production typo corrections prepared for the next deploy.",
    }
    body = ["# CEEFM April 2026 Visual Captions", ""]
    for name, caption in entries.items():
        body.append(f"## {name}")
        body.append(caption)
        body.append("")
    (OUT / "captions.md").write_text("\n".join(body), encoding="utf-8")


def main():
    chart_01_geo_progression()
    chart_02_geo_delta()
    chart_03_marketing_radar()
    chart_04_linkedin_impressions()
    chart_05_linkedin_followers()
    chart_06_demographics()
    chart_07_sitemap()
    chart_08_funnel()
    composite_x1_schema()
    composite_x2_stats()
    composite_x3_typos()
    captions()
    print(f"Generated visuals in {OUT}")


if __name__ == "__main__":
    main()
