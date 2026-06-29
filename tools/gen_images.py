#!/usr/bin/env python3
"""사이트 이미지 생성기.

- assets/hero.webp     : 히어로 비주얼 (≤50KB WebP)
- assets/og-image.png  : 소셜 공유 카드 (1200×630, OG/카카오 호환용 PNG)
- assets/og-image.webp : 소셜 공유 카드 WebP (≤50KB)

실제 촬영 사진을 쓰려면 assets/hero.webp 를 같은 경로로 교체하면 된다.
(권장: 1200×900 내외, cwebp -q 70 로 50KB 이하 인코딩)
"""
import math
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")

# 브랜드 팔레트 (style.css 와 동일 계열)
BG_TOP = (11, 19, 34)      # #0b1322
BG_BOT = (6, 10, 18)       # 거의 검정
AMBER = (255, 168, 92)     # 따뜻한 촛불빛
ORANGE = (255, 107, 53)    # --orange-primary


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _vertical_gradient(w, h, top, bot):
    img = Image.new("RGB", (w, h))
    px = img.load()
    for y in range(h):
        t = y / max(1, h - 1)
        c = _lerp(top, bot, t)
        for x in range(w):
            px[x, y] = c
    return img


def _radial_glow(w, h, cx, cy, radius, color, strength):
    """부드러운 방사형 글로우 레이어(RGBA)를 반환."""
    glow = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(glow)
    d.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=255)
    glow = glow.filter(ImageFilter.GaussianBlur(radius * 0.55))
    layer = Image.new("RGBA", (w, h), color + (0,))
    alpha = glow.point(lambda v: int(v * strength))
    layer.putalpha(alpha)
    return layer


def _font(size, bold=True):
    candidates = [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "NanumGothicBold.ttf"),
        "/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf",
        "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
        "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except OSError:
                continue
    return ImageFont.load_default()


def build_hero(w=1200, h=900):
    img = _vertical_gradient(w, h, BG_TOP, BG_BOT).convert("RGBA")
    # 따뜻한 촛불빛 글로우 — 우상단 + 중앙 하단
    img.alpha_composite(_radial_glow(w, h, int(w * 0.78), int(h * 0.20), int(w * 0.46), AMBER, 0.55))
    img.alpha_composite(_radial_glow(w, h, int(w * 0.30), int(h * 0.92), int(w * 0.40), (28, 45, 86), 0.65))
    img.alpha_composite(_radial_glow(w, h, int(w * 0.62), int(h * 0.62), int(w * 0.30), ORANGE, 0.22))

    # 은은한 촛불 점광원 몇 개
    d = ImageDraw.Draw(img)
    for cx, cy, r in [(0.84, 0.32, 9), (0.70, 0.46, 6), (0.90, 0.55, 5)]:
        x, y = int(w * cx), int(h * cy)
        img.alpha_composite(_radial_glow(w, h, x, y, r * 6, (255, 214, 150), 0.9))
        d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 234, 196, 255))

    # 하단 비네팅으로 텍스트 가독성 확보
    vig = Image.new("L", (w, h), 0)
    ImageDraw.Draw(vig).rectangle([0, int(h * 0.55), w, h], fill=120)
    vig = vig.filter(ImageFilter.GaussianBlur(h * 0.12))
    dark = Image.new("RGBA", (w, h), (3, 6, 12, 0))
    dark.putalpha(vig)
    img.alpha_composite(dark)

    out = os.path.join(ASSETS, "hero.webp")
    _save_webp(img.convert("RGB"), out, max_kb=50, start_q=80)
    return out


def build_og(w=1200, h=630):
    img = _vertical_gradient(w, h, BG_TOP, BG_BOT).convert("RGBA")
    img.alpha_composite(_radial_glow(w, h, int(w * 0.85), int(h * 0.18), int(w * 0.42), AMBER, 0.5))
    img.alpha_composite(_radial_glow(w, h, int(w * 0.18), int(h * 0.9), int(w * 0.4), ORANGE, 0.28))

    d = ImageDraw.Draw(img)
    # 상단 배지
    badge = "용인시 전지역 방문 관리 · 24시간 상담"
    bf = _font(26)
    d.text((80, 96), badge, font=bf, fill=(255, 180, 120, 255))
    # 메인 카피
    tf = _font(78)
    d.text((78, 150), "용인 출장마사지", font=tf, fill=(245, 248, 255, 255))
    d.text((78, 250), "홈타이 지역별 안내", font=tf, fill=(245, 248, 255, 255))
    # 강조 라인
    d.rectangle([80, 370, 360, 378], fill=ORANGE + (255,))
    sf = _font(34, bold=False)
    d.text((80, 408), "수지 · 기흥 · 처인 전지역 · 78개 지역 안내", font=sf, fill=(200, 210, 228, 255))
    # 브랜드/전화
    pf = _font(40)
    d.text((80, 500), "88마사지  0508-202-4719", font=pf, fill=(255, 168, 92, 255))

    rgb = img.convert("RGB")
    png_out = os.path.join(ASSETS, "og-image.png")
    rgb.save(png_out, "PNG", optimize=True)
    webp_out = os.path.join(ASSETS, "og-image.webp")
    _save_webp(rgb, webp_out, max_kb=50, start_q=82)
    return png_out, webp_out


def _save_webp(img, path, max_kb=50, start_q=80):
    """품질을 낮춰가며 max_kb 이하가 되도록 WebP 저장."""
    q = start_q
    while q >= 30:
        img.save(path, "WEBP", quality=q, method=6)
        kb = os.path.getsize(path) / 1024
        if kb <= max_kb:
            print(f"  {os.path.basename(path)}: {kb:.1f}KB (q={q})")
            return
        q -= 6
    print(f"  {os.path.basename(path)}: {os.path.getsize(path)/1024:.1f}KB (q={q+6}, 최소품질)")


if __name__ == "__main__":
    os.makedirs(ASSETS, exist_ok=True)
    print("이미지 생성:")
    build_hero()
    build_og()
    print("완료.")
