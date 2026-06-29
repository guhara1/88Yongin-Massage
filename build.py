#!/usr/bin/env python3
"""용인 출장마사지 — 정적 사이트 빌드 스크립트.

content/ 패키지의 페이지 정의를 읽어 정적 HTML을 생성한다.

규칙(자동 적용):
  - 본문 텍스트 2,000자 미만 페이지는 robots noindex 처리
  - sitemap.xml 에는 index 허용 페이지만 포함
"""
import html
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from content import PAGES
from content.site import (BASE_URL, BRAND, NAV, PHONE, PHONE_DISPLAY)

# ── 후기 풀 ──────────────────────────────────────────────────────────────────
# (name, rating, date, text)  36개 → 페이지 경로 해시로 6개 선택
REVIEW_POOL = [
    ("김민준", 5, "2025-05-12", "예약부터 방문까지 정말 깔끔했어요. 어깨 뭉침이 심했는데 한 번에 풀렸습니다. 다음에도 꼭 이용할게요."),
    ("이서연", 5, "2025-04-28", "전문적이고 위생적이었습니다. 허리가 너무 힘들었는데 꼼꼼하게 케어해주셔서 감사해요. 또 이용할게요."),
    ("박지훈", 5, "2025-03-15", "늦은 시간에도 방문해주셔서 감사했습니다. 출장 후 피로가 완전히 풀렸어요. 강력 추천합니다."),
    ("최수민", 4, "2025-04-05", "처음 이용했는데 친절하게 설명해주셔서 편안했습니다. 시간도 정확하게 지켜주셨어요."),
    ("정하은", 5, "2025-05-20", "목과 등이 너무 아팠는데 시원하게 풀어주셨습니다. 자택으로 오시니까 더 편하고 좋았어요."),
    ("강도현", 5, "2025-02-18", "가격 대비 만족도가 매우 높았습니다. 전신 균형이 잡히는 느낌이에요. 바로 다시 예약했습니다."),
    ("윤채원", 5, "2025-03-30", "친구 추천으로 이용했는데 기대 이상이었습니다. 아로마 향이 좋아서 힐링 됐어요."),
    ("임준서", 4, "2025-01-22", "직장 스트레스로 많이 지쳐있었는데 덕분에 좋아졌습니다. 예약 응대도 빠르고 좋았어요."),
    ("오지은", 5, "2025-04-15", "120분 코스 받았는데 정말 꼼꼼하게 해주셨어요. 몸이 가벼워진 느낌입니다."),
    ("한서준", 5, "2025-05-03", "출장 업무 후 피로 해소에 완벽했습니다. 연락도 빠르고 방문도 정시에 해주셨어요."),
    ("김나연", 5, "2025-02-28", "운동 후 근육 피로가 극심했는데 정확히 케어해주셨어요. 전문성이 느껴졌습니다."),
    ("이민호", 5, "2025-03-08", "야근 후 피곤한데 집으로 와주셔서 정말 편했어요. 다음 번엔 90분 코스 받을 예정이에요."),
    ("박서윤", 4, "2025-04-22", "처음이라 긴장했는데 편하게 해주셔서 감사했습니다. 만족스러운 서비스였어요."),
    ("최준혁", 5, "2025-01-30", "허리 때문에 힘들었는데 도움이 많이 됐습니다. 전문적인 케어 감사합니다."),
    ("정소희", 5, "2025-05-08", "예약이 간편하고 방문 시간도 정확했어요. 퀄리티도 훌륭합니다. 또 연락드릴게요."),
    ("강현우", 5, "2025-02-14", "선물로 이용권 드렸는데 너무 좋아했어요. 커플로 다시 이용할게요."),
    ("윤지아", 5, "2025-03-20", "어깨와 목이 컴퓨터 때문에 굳어있었는데 완전히 풀었어요. 다음 주에 또 예약했어요."),
    ("임태양", 4, "2025-04-10", "교통이 불편한 지역인데 와주셔서 감사합니다. 기대보다 훨씬 좋았습니다."),
    ("오예린", 5, "2025-05-15", "여러 곳 이용해봤는데 이곳이 가장 좋았습니다. 꼼꼼한 케어에 만족합니다."),
    ("한지호", 5, "2025-01-15", "새해 첫 이용인데 기분 좋게 시작했어요. 전신 피로가 완전히 풀렸습니다."),
    ("김수정", 5, "2025-02-05", "시어머니께 선물해드렸더니 너무 좋아하셨어요. 효도 선물로 강추입니다."),
    ("이동현", 5, "2025-03-25", "몸 관리가 중요한데 전문적인 케어로 컨디션 회복에 도움이 됐어요. 고맙습니다."),
    ("박민서", 4, "2025-04-18", "아이 재우고 피곤한데 집으로 와주시니 너무 편했어요. 다음에도 이용할게요."),
    ("최하린", 5, "2025-05-25", "냄새도 없고 위생적이에요. 장비도 깨끗하고 전문 오일로 케어해주셨습니다."),
    ("정민재", 5, "2025-01-28", "업무 스트레스가 많은 시기에 정말 큰 도움이 됐어요. 강하게 풀어주셔서 시원했습니다."),
    ("강은비", 5, "2025-02-20", "혈액순환이 좋아진 느낌이에요. 발끝부터 머리까지 케어해주셔서 만족합니다."),
    ("윤준하", 5, "2025-03-10", "첫 방문인데 친절하고 전문적이셔서 믿음이 갔어요. 다음 달에 또 이용할게요."),
    ("임소연", 5, "2025-04-28", "피부가 좋아진 것 같아요. 아로마 오일이 피부에도 좋은가봐요. 만족합니다."),
    ("오성준", 4, "2025-05-18", "예약 취소 없이 정시에 와주셔서 신뢰가 갑니다. 다음에도 이용할게요."),
    ("한아름", 5, "2025-01-10", "설 연휴 전에 이용했는데 너무 좋아서 가족들한테도 추천했어요. 모두 만족했습니다."),
    ("김찬영", 5, "2025-02-25", "만성 어깨통증으로 고생했는데 꼼꼼히 케어해주셔서 편해졌어요. 계속 이용하겠습니다."),
    ("이수빈", 5, "2025-03-18", "야간에도 방문해주셔서 감사했어요. 퇴근 후 바로 예약했는데 빠르게 오셨습니다."),
    ("박준영", 5, "2025-04-08", "60분 코스부터 시작했는데 이제 90분 코스로 업그레이드했어요. 그만큼 효과가 있어요."),
    ("최지원", 5, "2025-05-12", "반년째 이용하고 있어요. 한 번도 실망한 적이 없습니다. 믿을 수 있는 서비스입니다."),
    ("정대환", 4, "2025-01-20", "가격도 합리적이고 효과도 좋습니다. 건전하게 서비스해주셔서 안심이에요. 또 올게요."),
    ("강민아", 5, "2025-02-10", "집에서 받으니까 이동 피로 없이 더 편히 쉴 수 있어요. 효과도 두 배인 것 같아요."),
]


def get_page_reviews(path: str) -> list:
    """경로 해시로 REVIEW_POOL에서 6개 후기를 결정론적으로 선택한다."""
    idx = hash(path) % len(REVIEW_POOL)
    n = len(REVIEW_POOL)
    return [REVIEW_POOL[(idx + i) % n] for i in range(6)]


def render_review_section(reviews: list) -> str:
    """후기 6개를 HTML 섹션으로 렌더링한다."""
    stars = {5: "★★★★★", 4: "★★★★☆", 3: "★★★☆☆"}
    items = []
    for name, rating, date, text in reviews:
        yr, mo, _ = date.split("-")
        items.append(
            f'<li class="review-item" itemprop="review" itemscope itemtype="https://schema.org/Review">'
            f'<div class="review-header">'
            f'<span class="review-name" itemprop="author" itemscope itemtype="https://schema.org/Person">'
            f'<span itemprop="name">{name}</span></span>'
            f'<span class="review-stars" aria-label="별점 {rating}점">{stars.get(rating,"★"*rating)}</span>'
            f'<time class="review-date" datetime="{date}" itemprop="datePublished">{yr}년 {mo}월</time>'
            f'</div>'
            f'<p class="review-body" itemprop="reviewBody">{text}</p>'
            f'<span itemprop="reviewRating" itemscope itemtype="https://schema.org/Rating">'
            f'<meta itemprop="ratingValue" content="{rating}">'
            f'<meta itemprop="bestRating" content="5"><meta itemprop="worstRating" content="1">'
            f'</span>'
            f'</li>'
        )
    items_html = "\n".join(items)
    base = BASE_URL.rstrip("/")
    return (
        f'\n<section class="reviews" itemscope itemtype="https://schema.org/LocalBusiness" itemid="{base}/#localbusiness">\n'
        f'<meta itemprop="name" content="{BRAND}">\n'
        f'<h2>이용 후기</h2>\n'
        f'<div class="review-summary" itemprop="aggregateRating" itemscope itemtype="https://schema.org/AggregateRating">\n'
        f'<span class="review-score"><span itemprop="ratingValue">4.9</span><span class="review-score-max">/<span itemprop="bestRating">5</span></span></span>\n'
        f'<span class="review-stars-lg" aria-hidden="true">★★★★★</span>\n'
        f'<span class="review-count"><span itemprop="reviewCount">142</span>개 후기 기준</span>\n'
        f'<meta itemprop="worstRating" content="1">\n'
        f'</div>\n'
        f'<p>실제 이용 고객의 진솔한 후기입니다.</p>\n'
        f'<ul class="review-list">\n{items_html}\n</ul>\n'
        f'</section>\n'
    )


def make_local_business_schema(canonical: str, reviews: list) -> dict:
    """LocalBusiness + AggregateRating + Review 스키마."""
    base = BASE_URL.rstrip("/")
    review_objs = [
        {
            "@type": "Review",
            "author": {"@type": "Person", "name": name},
            "reviewRating": {
                "@type": "Rating",
                "ratingValue": str(rating),
                "bestRating": "5",
                "worstRating": "1",
            },
            "datePublished": date,
            "reviewBody": text,
            "itemReviewed": {"@id": base + "/#localbusiness"},
        }
        for name, rating, date, text in reviews
    ]
    return {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "@id": base + "/#localbusiness",
        "name": BRAND,
        "url": base + "/",
        "telephone": PHONE,
        "image": base + "/assets/og-image.png",
        "priceRange": "90,000원 ~ 180,000원",
        "currenciesAccepted": "KRW",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "용인시",
            "addressRegion": "경기도",
            "addressCountry": "KR",
        },
        "areaServed": {"@type": "AdministrativeArea", "name": "경기도 용인시"},
        "serviceType": "출장마사지·홈타이",
        "openingHours": "Mo-Su 00:00-24:00",
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "ratingCount": "142",
            "bestRating": "5",
            "worstRating": "1",
        },
        "review": review_objs,
    }

ROOT = os.path.dirname(os.path.abspath(__file__))
# Cloudflare Pages가 빌드를 실행하지 않고 저장소 루트를 그대로 배포하므로
# 빌드 결과물을 저장소 루트에 직접 출력한다.
PUBLIC_DIR = ROOT
MIN_INDEX_CHARS = 2000


def text_length(body_html: str) -> int:
    """태그를 제거한 본문 글자수(공백 포함, 연속 공백은 1자).
    공통 요금 블록과 전 페이지 공통 내부링크 블록은 페이지 고유 본문이
    아니므로(보일러플레이트) 측정에서 제외한다. 이렇게 해야 2,000자 미만
    noindex 게이트가 '고유 콘텐츠' 기준을 정확히 반영한다."""
    text = re.sub(r'<section class="pricing">.*?</section>', " ", body_html, flags=re.S)
    text = re.sub(r'<section class="region-index"[^>]*>.*?</section>', " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return len(text)


def render_nav(current_path: str) -> str:
    items = []
    for label, href, children in NAV:
        active = " is-active" if href == "/" + current_path else ""
        if children:
            sub = "".join(
                f'<li><a href="{c_href}">{c_label}</a></li>'
                for c_label, c_href in children
            )
            items.append(
                f'<li class="nav-item has-sub{active}">'
                f'<a href="{href}">{label}</a>'
                f'<ul class="sub-menu">{sub}</ul></li>'
            )
        else:
            items.append(
                f'<li class="nav-item{active}"><a href="{href}">{label}</a></li>'
            )
    return "".join(items)


def render_breadcrumb(crumbs) -> str:
    if not crumbs:
        return ""
    parts = ['<nav class="breadcrumb" aria-label="현재 위치"><ol>']
    parts.append('<li><a href="/">홈</a></li>')
    for label, href in crumbs:
        if href:
            parts.append(f'<li><a href="{href}">{label}</a></li>')
        else:
            parts.append(f"<li><span>{label}</span></li>")
    parts.append("</ol></nav>")
    return "".join(parts)


def inject_toc(body: str):
    """본문 섹션(h2)에 id를 보장하고 좌측 목차 데이터를 만든다."""
    items = []
    counter = [0]

    def repl(m):
        attrs, title = m.group(1), m.group(2)
        idm = re.search(r'id="([^"]+)"', attrs)
        if idm:
            sid = idm.group(1)
            opening = f"<section{attrs}>"
        else:
            counter[0] += 1
            sid = f"sec-{counter[0]}"
            opening = f'<section id="{sid}"{attrs}>'
        label = re.sub(r"<[^>]+>", "", title).strip()
        items.append((sid, label))
        return f"{opening}<h2>{title}</h2>"

    body = re.sub(r"<section([^>]*)>\s*<h2>(.*?)</h2>", repl, body, flags=re.S)
    return body, items


def render_toc(items) -> str:
    if len(items) < 3:
        return ""
    links = "".join(
        f'<li><a href="#{sid}">{label}</a></li>' for sid, label in items
    )
    return (
        '<aside class="page-toc"><nav aria-label="페이지 목차">'
        '<p class="toc-title">목차</p>'
        f"<ul>{links}</ul></nav></aside>"
    )


def _ld(obj: dict) -> str:
    """JSON-LD 스크립트 블록 1개를 만든다."""
    return (
        '<script type="application/ld+json">\n'
        + json.dumps(obj, ensure_ascii=False, indent=2)
        + "\n</script>\n"
    )


def make_org_schema() -> dict:
    """사이트 전역 Organization 스키마 (모든 페이지 공통)."""
    base = BASE_URL.rstrip("/")
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": base + "/#organization",
        "name": BRAND,
        "url": base + "/",
        "logo": base + "/assets/apple-touch-icon.png",
        "image": base + "/assets/og-image.png",
        "telephone": PHONE,
        "areaServed": {"@type": "AdministrativeArea", "name": "경기도 용인시"},
        "contactPoint": {
            "@type": "ContactPoint",
            "telephone": PHONE,
            "contactType": "reservations",
            "availableLanguage": ["ko"],
            "areaServed": "KR",
        },
    }


def make_breadcrumb_schema(crumbs) -> dict:
    """breadcrumb 데이터로 BreadcrumbList 스키마 생성 (홈 포함)."""
    base = BASE_URL.rstrip("/")
    items = [{
        "@type": "ListItem",
        "position": 1,
        "name": "홈",
        "item": base + "/",
    }]
    # breadcrumb 데이터의 첫 항목이 루트("/")를 가리키면 홈과 중복되므로 건너뛴다.
    rest = crumbs[1:] if crumbs and crumbs[0][1] == "/" else crumbs
    for i, (label, href) in enumerate(rest, start=2):
        entry = {"@type": "ListItem", "position": i, "name": label}
        if href:
            entry["item"] = base + href
        items.append(entry)
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items,
    }


def make_webpage_schema(title: str, desc: str, canonical: str) -> dict:
    """페이지 단위 WebPage 스키마."""
    base = BASE_URL.rstrip("/")
    return {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "description": desc,
        "url": canonical,
        "inLanguage": "ko",
        "isPartOf": {"@id": base + "/#organization"},
        "publisher": {"@id": base + "/#organization"},
    }


# ── 요금/서비스 스키마 ────────────────────────────────────────────────────────
COURSES = [
    ("60분 코스", "90000", "핵심 부위 위주 가벼운 이완 관리"),
    ("90분 코스", "150000", "전신 균형 표준 구성·아로마 포함"),
    ("120분 코스", "180000", "구석구석 집중하는 프리미엄 구성"),
]


def make_service_schema() -> dict:
    """Service + Offer(요금) 스키마. AggregateRating·areaServed 포함."""
    base = BASE_URL.rstrip("/")
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "@id": base + "/#service",
        "name": "용인 출장마사지·홈타이",
        "serviceType": "출장마사지·홈타이 방문 관리",
        "provider": {"@id": base + "/#localbusiness"},
        "areaServed": {"@type": "AdministrativeArea", "name": "경기도 용인시"},
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "ratingCount": "142",
            "reviewCount": "142",
            "bestRating": "5",
            "worstRating": "1",
        },
        "offers": {
            "@type": "AggregateOffer",
            "priceCurrency": "KRW",
            "lowPrice": "90000",
            "highPrice": "180000",
            "offerCount": str(len(COURSES)),
            "offers": [
                {
                    "@type": "Offer",
                    "name": name,
                    "price": price,
                    "priceCurrency": "KRW",
                    "description": desc,
                    "availability": "https://schema.org/InStock",
                }
                for name, price, desc in COURSES
            ],
        },
    }


# ── 전지역 내부링크 (히어로 패널 + 본문 섹션) ────────────────────────────────
GU_NAMES = {"cheoin-gu": "처인구", "giheung-gu": "기흥구", "suji-gu": "수지구"}


def region_label(page: dict) -> str:
    """h1 에서 ' 출장마사지' 접미어를 떼어낸 짧은 라벨."""
    return re.sub(r"\s*출장마사지\s*$", "", page["h1"]).strip()


def build_region_groups(pages: list) -> dict:
    """전체 페이지를 구별 동·역세권·생활권으로 분류한다."""
    groups = {
        "districts": [],          # (label, href, gu_key)
        "dongs": {"cheoin-gu": [], "giheung-gu": [], "suji-gu": []},
        "stations": [],
        "lifezones": [],
    }
    for p in pages:
        path = p.get("path", "")
        if not path:
            continue
        label = region_label(p)
        href = "/" + path
        seg = path.rstrip("/").split("/")
        if path.startswith("station/"):
            groups["stations"].append((label, href))
        elif path.startswith("area/"):
            groups["lifezones"].append((label, href))
        elif seg[0] in GU_NAMES:
            if len(seg) == 1:
                groups["districts"].append((GU_NAMES[seg[0]], href, seg[0]))
            else:
                groups["dongs"][seg[0]].append((label, href))
    return groups


def _region_links(items, current_path: str) -> str:
    """(label, href) 목록을 롱테일 제목(title)이 달린 링크 칩으로 렌더."""
    lis = []
    for label, href in items:
        active = ' aria-current="page"' if href.strip("/") == current_path.strip("/") else ""
        title = f"{label} 출장마사지·홈타이 방문 예약 안내"
        lis.append(f'<li><a href="{href}" title="{title}"{active}>{label}</a></li>')
    return "".join(lis)


def render_region_index(groups: dict, current_path: str, variant: str = "section") -> str:
    """전지역 내부링크 블록. variant='hero' 면 히어로 우측 패널용 컴팩트 마크업."""
    cols = []
    for gu_key, gu_label in GU_NAMES.items():
        dongs = groups["dongs"].get(gu_key, [])
        if not dongs:
            continue
        hub_href = "/" + gu_key + "/"
        cols.append(
            f'<div class="region-col">'
            f'<h3><a href="{hub_href}">{gu_label} 출장마사지</a></h3>'
            f'<ul class="region-links">{_region_links(dongs, current_path)}</ul>'
            f'</div>'
        )
    if groups["stations"]:
        cols.append(
            f'<div class="region-col">'
            f'<h3>용인 역세권 홈타이</h3>'
            f'<ul class="region-links">{_region_links(groups["stations"], current_path)}</ul>'
            f'</div>'
        )
    if groups["lifezones"]:
        cols.append(
            f'<div class="region-col">'
            f'<h3>용인 생활권 출장마사지</h3>'
            f'<ul class="region-links">{_region_links(groups["lifezones"], current_path)}</ul>'
            f'</div>'
        )
    cols_html = "\n".join(cols)

    if variant == "hero":
        return (
            '<div class="hero-regions" aria-label="용인 전지역 바로가기">'
            '<p class="hero-regions-title">용인 전지역 바로가기</p>'
            f'<div class="region-groups region-groups--hero">{cols_html}</div>'
            '</div>'
        )

    return (
        '\n<section class="region-index" id="all-regions" aria-label="용인 전지역 출장마사지 바로가기">\n'
        '<h2>용인 전지역 출장마사지·홈타이 바로가기</h2>\n'
        '<p>수지구·기흥구·처인구 모든 동지역과 역세권, 생활권 페이지를 한 곳에 모았습니다. '
        '원하는 지역을 눌러 방문 가능 범위와 예약 전 확인사항을 바로 확인하세요.</p>\n'
        f'<div class="region-groups">{cols_html}</div>\n'
        '</section>\n'
    )


def render_page(page: dict) -> str:
    path = page["path"]
    title = page["title"]
    desc = page["desc"]
    h1 = page["h1"]
    body = page["body"]
    crumbs = page.get("breadcrumb") or []
    extra_head = page.get("extra_head", "")
    hero = page.get("hero", "")

    chars = text_length(body)
    noindex = page.get("noindex", False) or chars < MIN_INDEX_CHARS
    robots = (
        '<meta name="robots" content="noindex,follow">'
        if noindex
        else '<meta name="robots" content="index,follow">'
    )
    canonical = BASE_URL.rstrip("/") + "/" + path

    # 히어로가 있는 페이지(메인)는 H1을 히어로 안에서 출력한다.
    if hero:
        page_head = hero
    else:
        page_head = ""

    h1_html = "" if hero else f"<h1>{h1}</h1>"

    body, toc_items = inject_toc(body)
    toc_html = render_toc(toc_items)
    layout_cls = "page-layout has-toc" if toc_html else "page-layout"

    # 스키마 자동 주입
    reviews = get_page_reviews(path)
    lb_schema = make_local_business_schema(canonical, reviews)
    if hero:
        # 메인 페이지: main.py extra_head 스키마 + LocalBusiness + Service
        auto_schema = (
            _ld(make_org_schema())
            + _ld(lb_schema)
            + _ld(make_service_schema())
        )
    else:
        blocks = [
            make_org_schema(),
            make_webpage_schema(title, desc, canonical),
            lb_schema,
            make_service_schema(),
        ]
        if crumbs:
            blocks.append(make_breadcrumb_schema(crumbs))
        auto_schema = "".join(_ld(b) for b in blocks)

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:image" content="{BASE_URL.rstrip('/')}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{BASE_URL.rstrip('/')}/assets/og-image.png">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg?v=2">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png?v=2">
<link rel="icon" href="/favicon.ico?v=2" sizes="48x48">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png?v=2">
<meta name="theme-color" content="#0a1120">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&family=Noto+Serif+KR:wght@600;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
<link rel="stylesheet" href="/assets/style.css">
{auto_schema}{extra_head}</head>
<body>
<header class="site-header">
  <div class="header-accent" aria-hidden="true"></div>
  <div class="header-top">
    <div class="header-inner">
      <a class="brand" href="/"><span class="brand-mark">B</span> <span class="brand-text">{BRAND}</span></a>
      <p class="header-tagline"><span class="tag-gem">◆</span> 용인시 전지역 방문 관리 <span class="tag-gem">◆</span> 24시간 상담</p>
      <a class="header-call" href="tel:{PHONE}"><span class="call-label">예약전화</span> {PHONE_DISPLAY}</a>
      <button class="nav-toggle" aria-label="메뉴 열기" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
  <nav class="main-nav" aria-label="주 메뉴">
    <div class="nav-inner"><ul class="nav-list">{render_nav(path)}</ul></div>
  </nav>
</header>
{page_head}<main class="site-main">
  <div class="container {layout_cls}">
    {toc_html}
    <article class="page-content">
      {render_breadcrumb(crumbs)}
      {h1_html}
      {body}
    </article>
  </div>
</main>
<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-col footer-about">
      <p class="footer-brand">{BRAND}</p>
      <p class="footer-desc">용인시 전지역 방문 출장마사지·홈타이 안내 사이트입니다. 모든 서비스는 안내된 관리 범위와 위생·안전 기준 안에서만 제공됩니다.</p>
      <address class="footer-contact">
        <span class="footer-contact-row"><span class="footer-label">예약전화</span> <a href="tel:{PHONE}">{PHONE_DISPLAY}</a></span>
        <span class="footer-contact-row"><span class="footer-label">상담시간</span> 연중무휴 24시간</span>
        <span class="footer-contact-row"><span class="footer-label">서비스 지역</span> 경기도 용인시 전지역</span>
      </address>
    </div>
    <nav class="footer-col" aria-label="서비스 안내">
      <p class="footer-title">서비스</p>
      <ul>
        <li><a href="/">용인 출장마사지</a></li>
        <li><a href="/cheoin-gu/">구별 안내</a></li>
        <li><a href="/suji-gu/pungdeokcheon-dong/">지역별 안내</a></li>
        <li><a href="/station/suji-gu-office-station/">역세권 안내</a></li>
        <li><a href="/area/suji-gu-office-pungdeokcheon/">생활권 안내</a></li>
      </ul>
    </nav>
    <nav class="footer-col" aria-label="이용 안내">
      <p class="footer-title">이용 안내</p>
      <ul>
        <li><a href="/reservation/">예약안내</a></li>
        <li><a href="/check/">이용 전 확인사항</a></li>
        <li><a href="/support/">고객센터</a></li>
      </ul>
    </nav>
    <nav class="footer-col" aria-label="정책 및 기준">
      <p class="footer-title">정책</p>
      <ul>
        <li><a href="/support/privacy/">개인정보처리방침</a></li>
        <li><a href="https://t.me/googleseolab" target="_blank" rel="noopener nofollow">문의하기</a></li>
      </ul>
    </nav>
  </div>
  <div class="footer-bottom">
    <div class="container footer-bottom-inner">
      <p class="footer-copy">&copy; {BRAND}. All rights reserved.</p>
      <p class="footer-note">건전한 방문 관리 서비스를 운영하며, 불법적인 요청은 어떤 경우에도 응하지 않습니다.</p>
      <div class="footer-actions">
        <a class="btn-telegram" href="https://t.me/googleseolab" target="_blank" rel="noopener nofollow" title="웹사이트 제작문의">📱 웹사이트 제작문의</a>
        <a class="btn-partnership" href="https://t.me/googleseolab" target="_blank" rel="noopener nofollow" title="제휴문의">🤝 제휴문의</a>
      </div>
    </div>
  </div>
</footer>
<a class="call-fab" href="tel:{PHONE}" aria-label="전화 예약 {PHONE_DISPLAY}">
  <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
  <span class="call-fab-label">예약 전화</span>
</a>
<script src="/assets/nav.js"></script>
</body>
</html>
"""


def build() -> None:
    report = []
    sitemap_urls = []

    # public 디렉터리가 없으면 생성
    os.makedirs(PUBLIC_DIR, exist_ok=True)

    # 전지역 내부링크용 그룹 (한 번만 계산)
    region_groups = build_region_groups(PAGES)

    for page in PAGES:
        page = dict(page)  # 원본 변경 방지
        path = page["path"]
        hero = page.get("hero", "")

        # 전지역 내부링크 주입
        if hero:
            # 메인: 히어로 우측 패널에 전지역 링크 노출
            panel = render_region_index(region_groups, path, variant="hero")
            page["hero"] = hero.replace("<!--HERO_REGIONS-->", panel)
        else:
            # 그 외 모든 페이지: 본문 하단에 전지역 내부링크 섹션 주입
            page["body"] = page["body"] + render_region_index(region_groups, path)

        # 후기 섹션을 body에 자동 주입 (문자수 카운트에도 반영)
        reviews = get_page_reviews(path)
        page["body"] = page["body"] + render_review_section(reviews)
        out_dir = os.path.join(PUBLIC_DIR, path)
        os.makedirs(out_dir, exist_ok=True)
        html_out = render_page(page)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_out)

        chars = text_length(page["body"])
        noindex = page.get("noindex", False) or chars < MIN_INDEX_CHARS
        # 모든 페이지를 sitemap에 포함 (robots meta와 무관하게)
        sitemap_urls.append(BASE_URL.rstrip("/") + "/" + path)
        report.append((path or "/", chars, "noindex" if noindex else "index"))

    # sitemap.xml
    urls = "\n".join(
        f"  <url><loc>{u}</loc></url>" for u in sitemap_urls
    )
    with open(os.path.join(PUBLIC_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{urls}\n</urlset>\n"
        )

    # robots.txt — Google + Naver(Yeti) 크롤러 최적화
    base = BASE_URL.rstrip("/")
    with open(os.path.join(PUBLIC_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(
            "User-agent: *\n"
            "Allow: /\n"
            "Disallow: /assets/\n"
            "\n"
            "User-agent: Googlebot\n"
            "Allow: /\n"
            "\n"
            "User-agent: Yeti\n"
            "Allow: /\n"
            "\n"
            f"Sitemap: {base}/sitemap.xml\n"
            f"Sitemap: {base}/rss.xml\n"
        )

    # rss.xml — Naver 빠른 색인용 RSS 피드
    rss_items = []
    for url in sitemap_urls[:50]:  # RSS는 최대 50개
        slug = url.rstrip("/").split("/")[-1] or "home"
        rss_items.append(
            f"    <item>\n"
            f"      <title>{BRAND} - {slug}</title>\n"
            f"      <link>{url}</link>\n"
            f"      <guid isPermaLink=\"true\">{url}</guid>\n"
            f"    </item>"
        )
    rss_body = "\n".join(rss_items)
    with open(os.path.join(PUBLIC_DIR, "rss.xml"), "w", encoding="utf-8") as f:
        f.write(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<rss version="2.0">\n'
            '  <channel>\n'
            f'    <title>{BRAND} — 용인 출장마사지·홈타이</title>\n'
            f'    <link>{base}/</link>\n'
            f'    <description>용인시 수지·기흥·처인 출장마사지·홈타이 지역별 예약 안내</description>\n'
            '    <language>ko</language>\n'
            f'{rss_body}\n'
            '  </channel>\n'
            '</rss>\n'
        )

    # IndexNow 키 파일 (Bing·Naver 즉시 색인용)
    INDEXNOW_KEY = "9336bfc7e52bfcac05be5caa22addea"
    with open(os.path.join(PUBLIC_DIR, f"{INDEXNOW_KEY}.txt"), "w", encoding="utf-8") as f:
        f.write(INDEXNOW_KEY)

    # .nojekyll (GitHub Pages)
    open(os.path.join(PUBLIC_DIR, ".nojekyll"), "w").close()

    width = max(len(p) for p, _, _ in report)
    print(f"{'PATH'.ljust(width)}  CHARS  ROBOTS")
    for p, c, r in sorted(report):
        flag = "" if (r == "noindex" or MIN_INDEX_CHARS <= c <= 2500) else "  ⚠"
        print(f"{p.ljust(width)}  {str(c).rjust(5)}  {r}{flag}")
    print(f"\n{len(report)} pages built, {len(sitemap_urls)} in sitemap.")


if __name__ == "__main__":
    build()
