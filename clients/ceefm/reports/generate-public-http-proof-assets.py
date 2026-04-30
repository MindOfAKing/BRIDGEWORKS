from __future__ import annotations

from pathlib import Path
from urllib.request import Request, urlopen
from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parent / "charts" / "2026-04"
OUT.mkdir(parents=True, exist_ok=True)

NAVY = "#0F1A2E"
GOLD = "#B8860B"
IVORY = "#F5F0E8"
SAGE = "#4A6741"
CHARCOAL = "#1C2B3A"
MUTED = "#6B6560"
GRID = "#D8CFC2"
WHITE = "#FFFFFF"


def font(size: int, bold: bool = False):
    paths = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
    ]
    for path in paths:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


F_TITLE = font(34, True)
F_H2 = font(24, True)
F_BODY = font(18)
F_SMALL = font(14)


def fetch(url: str):
    req = Request(url, headers={"User-Agent": "BridgeWorks-Codex-Proof/1.0"})
    with urlopen(req, timeout=30) as response:
        return response.status, dict(response.headers), response.read().decode("utf-8", "replace")


def t(draw, xy, value, fill=CHARCOAL, f=F_BODY):
    draw.text(xy, value, fill=fill, font=f)


def wrapped(draw, xy, value, width, fill=CHARCOAL, f=F_SMALL, line_height=22, max_lines=18):
    words = value.split()
    line = ""
    x, y = xy
    lines = 0
    for word in words:
        test = (line + " " + word).strip()
        if draw.textlength(test, font=f) > width and line:
            t(draw, (x, y), line, fill, f)
            y += line_height
            lines += 1
            line = word
            if lines >= max_lines:
                t(draw, (x, y), "...", fill, f)
                return
        else:
            line = test
    if line and lines < max_lines:
        t(draw, (x, y), line, fill, f)


def security_headers():
    status, headers, _ = fetch("https://ceefm.eu/")
    wanted = [
        "strict-transport-security",
        "x-frame-options",
        "x-content-type-options",
        "referrer-policy",
        "content-security-policy",
        "permissions-policy",
    ]
    lower = {k.lower(): v for k, v in headers.items()}
    img = Image.new("RGB", (1200, 800), IVORY)
    draw = ImageDraw.Draw(img)
    t(draw, (60, 45), "Security Headers Proof", NAVY, F_TITLE)
    t(draw, (60, 88), "Live HTTP response from https://ceefm.eu/ captured by Codex.", MUTED, F_BODY)
    t(draw, (60, 130), f"HTTP status: {status}", NAVY, F_H2)
    y = 190
    for name in wanted:
        present = name in lower
        draw.rounded_rectangle((60, y, 1140, y + 64), radius=8, fill=WHITE, outline=GRID)
        draw.ellipse((85, y + 22, 105, y + 42), fill=SAGE if present else GOLD)
        t(draw, (125, y + 16), name, NAVY, F_H2)
        value = lower.get(name, "Not present in response")
        wrapped(draw, (440, y + 20), value, 660, MUTED, F_SMALL, 20, 2)
        y += 78
    img.save(OUT / "B-security-headers-grade.png")


def llms_and_robots():
    _, _, llms = fetch("https://ceefm.eu/llms.txt")
    _, _, robots = fetch("https://ceefm.eu/robots.txt")
    img = Image.new("RGB", (1200, 1200), IVORY)
    draw = ImageDraw.Draw(img)
    t(draw, (60, 40), "AI Crawler Files", NAVY, F_TITLE)
    for i, (heading, content) in enumerate([("https://ceefm.eu/llms.txt", llms), ("https://ceefm.eu/robots.txt", robots)]):
        y = 115 + i * 520
        draw.rounded_rectangle((60, y, 1140, y + 470), radius=8, fill=WHITE, outline=GRID)
        draw.rectangle((60, y, 1140, y + 48), fill=NAVY)
        t(draw, (82, y + 12), heading, WHITE, F_H2)
        y_text = y + 72
        for line in content.splitlines()[:22]:
            if not line.strip():
                y_text += 18
                continue
            wrapped(draw, (82, y_text), line, 1010, CHARCOAL, F_SMALL, 18, 3)
            approx_lines = max(1, int(draw.textlength(line, font=F_SMALL) // 1010) + 1)
            y_text += 18 * min(approx_lines, 3)
    img.save(OUT / "H-llms-and-robots.png")


def main():
    security_headers()
    llms_and_robots()
    print("Generated public HTTP proof assets.")


if __name__ == "__main__":
    main()
