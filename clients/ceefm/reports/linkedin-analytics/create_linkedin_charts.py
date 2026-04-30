from __future__ import annotations

from pathlib import Path
import json
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
CHART_DIR = ROOT / "charts"
CHART_DIR.mkdir(exist_ok=True)

PAGE_BG = "#FFFFFF"
PANEL_BG = "#FFFFFF"
LINKEDIN_BLUE = "#0A66C2"
LINKEDIN_DARK = "#000000E6"
TEXT = "#191919"
MUTED = "#666666"
LIGHT_TEXT = "#86888A"
GRID = "#E0E0E0"
BORDER = "#D6D6D6"
SOFT_BLUE = "#DCEBFA"
GREEN = "#057642"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


F_TITLE = font(42, True)
F_H2 = font(26, True)
F_BODY = font(22)
F_SMALL = font(18)
F_TINY = font(15)
F_NUM = font(38, True)


def text(draw: ImageDraw.ImageDraw, xy, value: str, fill=TEXT, fnt=F_BODY, anchor=None):
    draw.text(xy, value, fill=fill, font=fnt, anchor=anchor)


def card(draw: ImageDraw.ImageDraw, box, title: str, value: str, note: str | None = None):
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=4, fill=PANEL_BG, outline=BORDER, width=1)
    text(draw, (x1 + 22, y1 + 20), title, MUTED, F_SMALL)
    text(draw, (x1 + 22, y1 + 56), value, LINKEDIN_DARK, F_NUM)
    if note:
        text(draw, (x1 + 22, y2 - 34), note, LIGHT_TEXT, F_TINY)


def table(filename: str, sheet: str):
    data = json.loads((ROOT / "parsed-linkedin-exports.json").read_text(encoding="utf-8"))
    return data[filename][sheet]


def numeric(value):
    try:
        return float(value)
    except Exception:
        return 0.0


def april_metrics():
    rows = table("cee-facility-management_content_1777555091040.xls", "Metrics")
    header = rows[1]
    records = []
    for row in rows[2:]:
        if not row or not row[0]:
            continue
        date = datetime.strptime(row[0], "%m/%d/%Y")
        if datetime(2026, 4, 1) <= date <= datetime(2026, 4, 28):
            item = dict(zip(header, row))
            item["date"] = date
            records.append(item)
    return records


def follower_demo(sheet: str, limit=6):
    rows = table("cee-facility-management_followers_1777555120439.xls", sheet)
    clean_labels = {
        "Budapest Metropolitan Area, Hungary": "Budapest, Hungary",
        "Greater Delhi Area, India": "Delhi, India",
        "Dubai, United Arab Emirates": "Dubai, UAE",
        "Nairobi County, Kenya": "Nairobi, Kenya",
        "Jakarta Metropolitan Area, Indonesia": "Jakarta, Indonesia",
        "Abu Dhabi, United Arab Emirates": "Abu Dhabi, UAE",
    }
    return [
        (clean_labels.get(str(row[0]), str(row[0])), int(numeric(row[1])))
        for row in rows[1 : limit + 1]
    ]


def visitor_totals():
    rows = table("cee-facility-management_visitors_1777555105564.xls", "Visitor metrics")
    header = rows[0]
    page_views = 0
    unique = 0
    mobile = 0
    desktop = 0
    for row in rows[1:]:
        if not row or not row[0]:
            continue
        date = datetime.strptime(row[0], "%m/%d/%Y")
        if datetime(2026, 4, 1) <= date <= datetime(2026, 4, 28):
            item = dict(zip(header, row))
            page_views += numeric(item["Total page views (total)"])
            unique += numeric(item["Total unique visitors (total)"])
            mobile += numeric(item["Total page views (mobile)"])
            desktop += numeric(item["Total page views (desktop)"])
    return int(page_views), int(unique), int(mobile), int(desktop)


def post_rows():
    rows = table("cee-facility-management_content_1777555091040.xls", "All posts")
    header = rows[1]
    out = []
    for row in rows[2:]:
        if len(row) < len(header):
            continue
        item = dict(zip(header, row))
        impressions = numeric(item.get("Impressions"))
        if impressions <= 0:
            continue
        title = str(item.get("Post title", "")).split("\n")[0].strip()
        if not title:
            if int(impressions) == 137:
                title = "Eco-friendly cleaning products"
            elif int(impressions) == 133:
                title = "What 5 AM looks like at a Budapest hotel"
            else:
                title = "April LinkedIn post"
        out.append(
            {
                "title": title[:52],
                "impressions": int(impressions),
                "clicks": int(numeric(item.get("Clicks"))),
                "engagement": numeric(item.get("Engagement rate")) * 100,
            }
        )
    return sorted(out, key=lambda x: x["impressions"], reverse=True)


def save_kpi_overview():
    metrics = april_metrics()
    impressions = int(sum(numeric(r["Impressions (total)"]) for r in metrics))
    unique = int(sum(numeric(r["Unique impressions (organic)"]) for r in metrics))
    clicks = int(sum(numeric(r["Clicks (total)"]) for r in metrics))
    reactions = int(sum(numeric(r["Reactions (total)"]) for r in metrics))
    comments = int(sum(numeric(r["Comments (total)"]) for r in metrics))
    reposts = int(sum(numeric(r["Reposts (total)"]) for r in metrics))
    engagement = (clicks + reactions + comments + reposts) / impressions * 100
    page_views, unique_visitors, mobile_views, desktop_views = visitor_totals()

    img = Image.new("RGB", (1400, 900), PAGE_BG)
    draw = ImageDraw.Draw(img)
    text(draw, (70, 56), "CEEFM LinkedIn Analytics", LINKEDIN_DARK, F_TITLE)
    text(draw, (70, 112), "Native LinkedIn admin export, April 1-28. LinkedIn analytics lag by up to 2 days.", MUTED, F_BODY)

    cards = [
        ("Content impressions", f"{impressions:,}", "Organic + sponsored total"),
        ("Unique impressions", f"{unique:,}", "Organic reach proxy"),
        ("Clicks", f"{clicks:,}", "Post-level clicks"),
        ("Engagement rate", f"{engagement:.2f}%", "Weighted by impressions"),
        ("New followers", "54", "All organic"),
        ("Page visitors", f"{unique_visitors}", f"{page_views} total page views"),
    ]
    x, y = 70, 180
    w, h = 395, 170
    gap = 35
    for i, (title, value, note) in enumerate(cards):
        cx = x + (i % 3) * (w + gap)
        cy = y + (i // 3) * (h + gap)
        card(draw, (cx, cy, cx + w, cy + h), title, value, note)

    draw.rounded_rectangle((70, 620, 1330, 790), radius=4, fill=SOFT_BLUE, outline=BORDER, width=1)
    text(draw, (105, 655), "What the numbers say", LINKEDIN_DARK, F_H2)
    text(draw, (105, 700), "The page has early authority traction, not yet conversion volume.", TEXT, F_BODY)
    text(draw, (105, 735), "The strongest evidence is hospitality operations content, led by one breakout housekeeping post.", TEXT, F_BODY)

    img.save(CHART_DIR / "linkedin-kpi-overview-2026-04.png")


def save_daily_impressions():
    metrics = april_metrics()
    values = [int(numeric(r["Impressions (total)"])) for r in metrics]
    dates = [r["date"].strftime("%d") for r in metrics]
    max_value = max(values) if values else 1

    img = Image.new("RGB", (1400, 820), PAGE_BG)
    draw = ImageDraw.Draw(img)
    text(draw, (70, 56), "Daily Content Impressions", LINKEDIN_DARK, F_TITLE)
    text(draw, (70, 112), "The April spike came from the hotel housekeeping standards post.", MUTED, F_BODY)

    left, top, right, bottom = 110, 180, 1320, 700
    draw.line((left, bottom, right, bottom), fill=BORDER, width=2)
    draw.line((left, top, left, bottom), fill=BORDER, width=2)
    for i in range(5):
        y = bottom - (bottom - top) * i / 4
        val = int(max_value * i / 4)
        draw.line((left, y, right, y), fill=GRID, width=1)
        text(draw, (40, y - 10), f"{val:,}", MUTED, F_TINY)

    bar_w = max(8, int((right - left) / len(values) * 0.62))
    step = (right - left) / len(values)
    for i, value in enumerate(values):
        x = left + i * step + step * 0.19
        h = (bottom - top) * value / max_value
        color = LINKEDIN_BLUE if value == max_value else LINKEDIN_BLUE
        draw.rounded_rectangle((x, bottom - h, x + bar_w, bottom), radius=3, fill=color)
        if i % 3 == 0:
            text(draw, (x + bar_w / 2, bottom + 18), dates[i], MUTED, F_TINY, anchor="mt")

    text(draw, ((left + right) / 2, 755), "April day", MUTED, F_SMALL, anchor="mm")
    img.save(CHART_DIR / "linkedin-daily-impressions-2026-04.png")


def save_top_posts():
    posts = post_rows()[:6]
    img = Image.new("RGB", (1400, 860), PAGE_BG)
    draw = ImageDraw.Draw(img)
    text(draw, (70, 56), "Top LinkedIn Posts by Impressions", LINKEDIN_DARK, F_TITLE)
    text(draw, (70, 112), "Hospitality operations outperformed generic FM topics.", MUTED, F_BODY)

    left, top = 560, 190
    max_value = max(p["impressions"] for p in posts) if posts else 1
    for i, post in enumerate(posts):
        y = top + i * 95
        title = post["title"]
        text(draw, (70, y + 8), title, TEXT, F_SMALL)
        width = int(700 * post["impressions"] / max_value)
        color = LINKEDIN_BLUE if i == 0 else "#8AB4E8"
        draw.rounded_rectangle((left, y, left + width, y + 38), radius=3, fill=color)
        text(draw, (left + width + 18, y + 5), f"{post['impressions']:,}", LINKEDIN_DARK, F_SMALL)
        text(draw, (left, y + 48), f"{post['clicks']} clicks · {post['engagement']:.2f}% engagement", MUTED, F_TINY)

    draw.rounded_rectangle((70, 735, 1330, 805), radius=4, fill=SOFT_BLUE, outline=BORDER, width=1)
    text(draw, (100, 755), "Content takeaway: repeat the hotel/aparthotel operations lane in May.", LINKEDIN_DARK, F_H2)
    img.save(CHART_DIR / "linkedin-top-posts-2026-04.png")


def save_follower_signals():
    panels = [
        ("Top Locations", follower_demo("Location", 6), LINKEDIN_BLUE),
        ("Top Job Functions", follower_demo("Job function", 6), LINKEDIN_BLUE),
        ("Top Industries", follower_demo("Industry", 6), LINKEDIN_BLUE),
    ]
    img = Image.new("RGB", (1400, 920), PAGE_BG)
    draw = ImageDraw.Draw(img)
    text(draw, (70, 56), "Follower Quality Signals", LINKEDIN_DARK, F_TITLE)
    text(draw, (70, 112), "Early audience is useful but still too broad. May should narrow toward Hungarian hospitality and property operators.", MUTED, F_BODY)

    panel_w = 400
    max_bar = 245
    for idx, (title, rows, color) in enumerate(panels):
        x = 70 + idx * 440
        y = 185
        draw.rounded_rectangle((x, y, x + panel_w, 800), radius=4, fill=PANEL_BG, outline=BORDER, width=1)
        text(draw, (x + 24, y + 24), title, LINKEDIN_DARK, F_H2)
        max_val = max(v for _, v in rows) if rows else 1
        for i, (label, value) in enumerate(rows):
            by = y + 90 + i * 78
            text(draw, (x + 24, by), label[:33], TEXT, F_TINY)
            bar_w = int(max_bar * value / max_val)
            draw.rounded_rectangle((x + 24, by + 28, x + 24 + bar_w, by + 50), radius=5, fill=color)
            text(draw, (x + 285, by + 25), str(value), LINKEDIN_DARK, F_SMALL)

    img.save(CHART_DIR / "linkedin-follower-signals-2026-04.png")


def main():
    save_kpi_overview()
    save_daily_impressions()
    save_top_posts()
    save_follower_signals()
    print("Created chart pack:")
    for path in sorted(CHART_DIR.glob("*.png")):
        print(path)


if __name__ == "__main__":
    main()
