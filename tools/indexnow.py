#!/usr/bin/env python3
"""IndexNow 일괄 URL 통보 스크립트.

sitemap.xml 에서 모든 URL을 읽어 Bing·Naver IndexNow API에 즉시 통보합니다.

사용법:
    python tools/indexnow.py

요건:
    - Python 3.7+
    - 표준 라이브러리만 사용 (추가 패키지 불필요)
"""
import json
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

# ── 설정 ────────────────────────────────────────────────────────────────────
BASE_URL     = "https://88yongin-massage.pages.dev"
INDEXNOW_KEY = "9336bfc7e52bfcac05be5caa22addea"
KEY_LOCATION = f"{BASE_URL}/{INDEXNOW_KEY}.txt"

# IndexNow 지원 엔진
ENDPOINTS = [
    "https://www.bing.com/indexnow",
    "https://searchadvisor.naver.com/indexnow",
]

SITEMAP_PATH = Path(__file__).parent.parent / "sitemap.xml"
# ────────────────────────────────────────────────────────────────────────────


def load_urls_from_sitemap(path: Path) -> list:
    if not path.exists():
        print(f"[오류] sitemap.xml 을 찾을 수 없습니다: {path}")
        print("       먼저 'python build.py' 를 실행하세요.")
        sys.exit(1)
    tree = ET.parse(path)
    root = tree.getroot()
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [loc.text.strip() for loc in root.findall("s:url/s:loc", ns) if loc.text]
    return urls


def indexnow_post(endpoint: str, urls: list) -> None:
    payload = json.dumps({
        "host": urllib.parse.urlparse(BASE_URL).netloc,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }, ensure_ascii=False).encode("utf-8")

    req = urllib.request.Request(
        endpoint,
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            status = resp.status
    except urllib.error.HTTPError as e:
        status = e.code
    except Exception as e:
        print(f"  [실패] {endpoint}: {e}")
        return

    if status in (200, 202):
        print(f"  [성공] {endpoint} → HTTP {status}")
    else:
        print(f"  [경고] {endpoint} → HTTP {status}")


def ping_sitemap() -> None:
    """Google·Naver 사이트맵 핑 전송."""
    sitemap_url = f"{BASE_URL}/sitemap.xml"
    ping_targets = [
        f"https://www.google.com/ping?sitemap={urllib.parse.quote(sitemap_url, safe='')}",
    ]
    for url in ping_targets:
        try:
            with urllib.request.urlopen(url, timeout=10) as resp:
                print(f"  [핑 성공] {url.split('?')[0]} → HTTP {resp.status}")
        except Exception as e:
            print(f"  [핑 실패] {url.split('?')[0]}: {e}")


def main() -> None:
    print("=" * 60)
    print("88마사지 — IndexNow 일괄 URL 통보")
    print(f"키: {INDEXNOW_KEY}")
    print("=" * 60)

    urls = load_urls_from_sitemap(SITEMAP_PATH)
    if not urls:
        print("[오류] sitemap.xml 에서 URL을 찾을 수 없습니다.")
        sys.exit(1)

    print(f"\n총 {len(urls)}개 URL 발견:\n")
    for u in urls:
        print(f"  {u}")

    print(f"\n── IndexNow POST ({len(urls)}개 URL) ──")
    for endpoint in ENDPOINTS:
        indexnow_post(endpoint, urls)

    print("\n── Google 사이트맵 핑 ──")
    ping_sitemap()

    print("\n완료. 색인 반영에는 수 시간~수일이 소요될 수 있습니다.")
    print("Bing Webmaster Tools: https://www.bing.com/webmasters")
    print("Naver Search Advisor: https://searchadvisor.naver.com")
    print("Google Search Console: https://search.google.com/search-console")


if __name__ == "__main__":
    main()
