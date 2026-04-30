from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter


OUT = Path(__file__).resolve().parent / "linkedin"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1128, 191
GREEN_1 = (28, 61, 42)
GREEN_2 = (45, 89, 66)
NAVY = (15, 26, 46)
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


def gradient(start=GREEN_1, end=GREEN_2) -> Image.Image:
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
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    for x in range(-160, W, 120):
        draw.line((x, H, x + 250, 0), fill=(255, 255, 255, 18), width=1)
    for x in range(740, W + 100, 54):
        draw.line((x, 28, x, H - 20), fill=(255, 255, 255, 12), width=1)
    for y in range(34, H, 42):
        draw.line((720, y, W - 45, y), fill=(255, 255, 255, 10), width=1)
    return Image.alpha_composite(img.convert("RGBA"), overlay)


def draw_banner(name: str, start=GREEN_1, end=GREEN_2):
    img = add_subtle_grid(gradient(start, end))
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow)
    sdraw.rectangle((0, 0, W, H), fill=(0, 0, 0, 34))
    sdraw.ellipse((-180, -180, 460, 420), fill=(0, 0, 0, 40))
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))
    img = Image.alpha_composite(img, shadow)

    draw = ImageDraw.Draw(img)

    # Safe area leaves room for LinkedIn's company logo overlay on the left.
    x = 220
    y = 43
    title = "Premium Facility Management"
    subtitle = "for Property and Hospitality"
    proof = "Trusted by Limehome | 9.4 cleanliness score | 24 months above 9.0"

    draw.text((x + 1, y + 1), title, font=TITLE, fill=(0, 0, 0, 80))
    draw.text((x, y), title, font=TITLE, fill=WHITE)
    draw.text((x, y + 44), subtitle, font=SUB, fill=MUTED)
    draw.rounded_rectangle((x, y + 76, x + 305, y + 79), radius=1, fill=GOLD)
    draw.text((x, y + 101), proof, font=SMALL, fill=IVORY)

    # Small right-side mark, abstract building grid.
    grid_x, grid_y = 920, 54
    for row in range(3):
        for col in range(4):
            alpha = 210 - row * 35 - col * 14
            color = (*IVORY, max(60, alpha))
            draw.rounded_rectangle(
                (grid_x + col * 32, grid_y + row * 25, grid_x + col * 32 + 18, grid_y + row * 25 + 12),
                radius=2,
                fill=color,
            )
    draw.rounded_rectangle((904, 37, 1078, 151), radius=3, outline=(*GOLD, 165), width=2)

    out = OUT / name
    img.convert("RGB").save(out, quality=95)
    print(out)


if __name__ == "__main__":
    draw_banner("ceefm-linkedin-banner-green-1128x191.png", GREEN_1, GREEN_2)
    draw_banner("ceefm-linkedin-banner-navy-1128x191.png", NAVY, (28, 47, 78))
