#!/usr/bin/env python3
"""Generate entry.png: a front-page-style summary of 18 November 2026 world news.

Dev-time generator only (needs Pillow + DejaVu fonts on this machine). The
submitted program is main.py, which copies the generated entry.png to
/output/entry.png. Re-run: python3 generate_image.py
Sources (checked 2026-11-18): Nikkei Asia / Japan Times on the Quad summit in
Manila; Reuters via Devdiscourse and NY Post on the Crimea bridge strikes;
Reuters / Outlook India on the Iran drone attack in Bahrain; The Manila Times
and NDTV world pages for the day's other headlines.
"""
import textwrap

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (248, 244, 234)
INK = (24, 24, 24)
NAVY = (26, 46, 74)
RED = (176, 42, 30)
TEAL = (14, 110, 110)
GOLD = (176, 132, 24)
MUTED = (90, 90, 90)
RULE = (24, 24, 24)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap measured in pixels, not characters."""
    out = []
    for para in text.split("\n"):
        words = para.split(" ")
        line = ""
        for word in words:
            trial = (line + " " + word).strip()
            if draw.textlength(trial, font=fnt) <= width or not line:
                line = trial
            else:
                out.append(line)
                line = word
        if line:
            out.append(line)
    return out


def text_block(draw, x, y, text, fnt, fill, width, leading=6):
    lines = wrap(draw, text, fnt, width)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + leading
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # border
    d.rectangle([10, 10, W - 11, H - 11], outline=RULE, width=3)

    # ---- masthead ----
    y = 24
    d.text((W // 2, y), "THE WORLD", font=font(SERIF_B, 88),
           fill=INK, anchor="ma")
    y = 126
    d.line([40, y, W - 40, y], fill=RULE, width=3)
    y += 10
    d.text((W // 2, y), "WEDNESDAY  •  18 NOVEMBER 2026  •  THE DAY IN ONE IMAGE",
           font=font(SANS_B, 23), fill=NAVY, anchor="ma")
    y += 34
    d.line([40, y, W - 40, y], fill=RULE, width=2)
    y += 12

    # ---- lead story ----
    d.text((40, y), "DIPLOMACY  —  MANILA", font=font(SANS_B, 22), fill=RED)
    y += 30
    y = text_block(d, 40, y, "QUAD MEETS IN MANILA",
                   font(SERIF_B, 58), INK, W - 80, leading=4)
    y += 2
    y = text_block(
        d, 40, y,
        "Trump, Modi, Takaichi and Albanese agree critical-minerals deals at "
        "the first Quad leaders' summit in two years — then Trump heads on "
        "to Shenzhen for APEC.",
        font(SERIF, 25), INK, W - 80, leading=5)
    y += 12

    # ---- map panel: three flashpoints ----
    panel_y0, panel_y1 = y, y + 168
    d.rectangle([40, panel_y0, W - 40, panel_y1], fill=NAVY)
    d.text((W // 2, panel_y0 + 12), "THREE FLASHPOINTS, ONE DAY",
           font=font(SANS_B, 21), fill=(232, 220, 180), anchor="ma")
    cities = [
        ("MANILA", "Quad summit", 200, 0.30),
        ("KYIV", "Bridge war", 512, 0.42),
        ("BAHRAIN", "Iran drones", 824, 0.32),
    ]
    for name, label, cx, frac in cities:
        cy = panel_y0 + 84 + int(44 * frac)
        d.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], fill=RED,
                  outline=(255, 255, 255), width=3)
        d.text((cx, cy + 20), name, font=font(SANS_B, 23),
               fill=(255, 255, 255), anchor="ma")
        d.text((cx, cy + 44), label, font=font(SANS, 19),
               fill=(200, 210, 225), anchor="ma")
    # arcs between the points (kept below the title)
    for (x1, x2) in [(200, 512), (512, 824)]:
        d.arc([x1, panel_y0 + 78, x2, panel_y0 + 190], start=200, end=340,
              fill=(120, 140, 170), width=3)
    y = panel_y1 + 16

    # ---- two-column stories ----
    col_w = (W - 80 - 36) // 2
    left_x, right_x = 40, 40 + col_w + 36
    d.line([W // 2, y, W // 2, y + 200], fill=(180, 175, 160), width=2)

    d.text((left_x, y), "WAR IN UKRAINE  —  KERCH", font=font(SANS_B, 20),
           fill=RED)
    y1 = text_block(d, left_x, y + 28, "Ukraine strikes\nCrimea bridge",
                    font(SERIF_B, 33), INK, col_w, leading=2)
    y1 = text_block(
        d, left_x, y1 + 4,
        "A road span of the Kerch Bridge collapsed in Kyiv's biggest drone "
        "attack of the war. Russia hit bridges in Kyiv in reply.",
        font(SERIF, 22), INK, col_w, leading=4)

    d.text((right_x, y), "MIDDLE EAST  —  BAHRAIN", font=font(SANS_B, 20),
           fill=RED)
    y2 = text_block(d, right_x, y + 28, "Iran drones target\nU.S. radar",
                    font(SERIF_B, 33), INK, col_w, leading=2)
    y2 = text_block(
        d, right_x, y2 + 4,
        "The IRGC claimed a drone strike on the U.S. radar at Sheikh Isa Air "
        "Base. Bahrain said its defences intercepted the attack, with no "
        "damage reported.",
        font(SERIF, 22), INK, col_w, leading=4)
    y = max(y1, y2) + 14
    d.line([40, y, W - 40, y], fill=RULE, width=2)
    y += 12

    # ---- also today ----
    d.text((40, y), "ALSO TODAY", font=font(SANS_B, 23), fill=NAVY)
    y += 32
    items = [
        ("Canada & China extend trade deals as Xi meets Carney ahead of APEC.",
         TEAL),
        ("Britain sanctions Israeli settlement firms in a two-state push.",
         GOLD),
        ("U.S. loses measles-free status as cases and deaths mount.", RED),
        ("Nvidia beats estimates as Jensen Huang's return is debated.", NAVY),
        ("Mongolia's president resigns amid graft charges.", TEAL),
        ("Dhoni retires from the IPL — to mentor Chennai Super Kings.", GOLD),
    ]
    col2_w = (W - 80 - 36) // 2
    for i, (text, color) in enumerate(items):
        x = 40 if i % 2 == 0 else 40 + col2_w + 36
        yy = y + (i // 2) * 48
        d.ellipse([x, yy + 7, x + 13, yy + 20], fill=color)
        text_block(d, x + 22, yy, text, font(SERIF, 20), INK, col2_w - 22,
                   leading=3)
    y += 3 * 48 + 2
    d.line([40, y, W - 40, y], fill=RULE, width=2)
    y += 8
    d.text((W // 2, y), "Compiled 18 November 2026 from world news reports",
           font=font(SANS, 18), fill=MUTED, anchor="ma")

    img.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()
