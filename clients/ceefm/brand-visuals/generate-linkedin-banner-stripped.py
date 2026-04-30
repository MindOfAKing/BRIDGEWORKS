"""Generate a stripped CEEFM LinkedIn banner (no right-side motif).

Sibling to generate-linkedin-banner.py (Codex's original). Keeps the same
typographic composition (Georgia serif tagline, two-line stack, gold rule,
bottom-left credibility) but removes the right-side abstract grid motif and
the gold rectangle outline so the right half of the banner is clean gradient.

Per Emmanuel's direction 2026-04-30: cleaner banner reads as more disciplined
on a LinkedIn company page where LinkedIn overlays its own page logo on the
left and adding a graphic on the right competes for attention.

Output:
    linkedin/ceefm-linkedin-banner-stripped-green-1128x191.png
    linkedin/ceefm-linkedin-banner-stripped-navy-1128x191.png
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT = Path(__file__).resolve().parent / "linkedin"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1128, 191
GREEN_1 = (28, 61, 42)
GREEN_2 = (45, 89, 66)
NAVY = (15, 26, 46)
NAVY_TAIL = (28, 47, 78)
GOLD = (184, 134, 11)
IVORY = (245, 240, 232)
WHITE = (255, 255, 255)
MUTED = (226, 221, 211)


def font(size: int, bold: bool = False):
    candidates = [
        "C:/Windows/Fonts/georgiab.ttf" if bold else "C:/Windows/Fonts/georgia.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


TITLE = font(33, True)
SUB = font(18)
SMALL = font(15)


def gradient(start, end) -> Image.Image:
    img = Image.new("RGB", (W, H), start)
    px = img.load()
    for x in range(W):
        t = x / (W - 1)
        for y in range(H):
            v = y / (H - 1)
            mix = min(1, t * 0.75 + v * 0.35)
            r = int(start[0] * (1 - mix) + end[0] * mix)
            g = int(start[1] * (1 - mix) + end[1] * mix)
            b = int(start[2] * (1 - mix) + end[2] * mix)
            px[x, y] = (r, g, b)
    return img


def add_subtle_grid(img: Image.Image):
    """Light diagonal lines across the whole banner. No right-side dense grid."""
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    for x in range(-160, W, 120):
        draw.line((x, H, x + 250, 0), fill=(255, 255, 255, 18), width=1)
    return Image.alpha_composite(img.convert("RGBA"), overlay)


def draw_banner(name: str, start, end):
    img = add_subtle_grid(gradient(start, end))
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow)
    sdraw.rectangle((0, 0, W, H), fill=(0, 0, 0, 34))
    sdraw.ellipse((-180, -180, 460, 420), fill=(0, 0, 0, 40))
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))
    img = Image.alpha_composite(img, shadow)

    draw = ImageDraw.Draw(img)

    x = 220
    y = 43
    title = "Premium Facility Management"
    subtitle = "for Property and Hospitality"
    proof = "Trusted by Limehome  ·  9.4 cleanliness score  ·  24 months above 9.0"

    draw.text((x + 1, y + 1), title, font=TITLE, fill=(0, 0, 0, 80))
    draw.text((x, y), title, font=TITLE, fill=WHITE)
    draw.text((x, y + 44), subtitle, font=SUB, fill=MUTED)
    draw.rounded_rectangle((x, y + 76, x + 305, y + 79), radius=1, fill=GOLD)
    draw.text((x, y + 101), proof, font=SMALL, fill=IVORY)

    out = OUT / name
    img.convert("RGB").save(out, quality=95)
    print(out)


if __name__ == "__main__":
    draw_banner("ceefm-linkedin-banner-stripped-green-1128x191.png", GREEN_1, GREEN_2)
    draw_banner("ceefm-linkedin-banner-stripped-navy-1128x191.png", NAVY, NAVY_TAIL)
