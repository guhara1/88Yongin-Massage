# 용인시 생활권 페이지 — 16개 (지역·역 통합 생활권)

from .site import BASE_URL, PHONE

_BASE = BASE_URL.rstrip("/")

def create_area_page(path, title, desc, h1, breadcrumb, body_content):
    """생활권 페이지 생성 헬퍼 함수"""
    return {
        "path": path,
        "title": title,
        "desc": desc,
        "h1": h1,
        "breadcrumb": breadcrumb,
        "body": body_content,
    }

# ===== 16개 생활권 페이지 =====

# 임시: 스켈레톤 페이지들
# TODO: 각 생활권별 상세 콘텐츠 추가 필요

PAGES = [
    create_area_page(
        path="area/suji-gu-office-pungdeokcheon/",
        title="수지구청·풍덕천 생활권 출장마사지｜신분당선 중심 안내",
        desc="수지구청·풍덕천 생활권 출장마사지 예약 전 수지구청역, 풍덕천동을 확인하세요.",
        h1="수지구청·풍덕천 생활권 출장마사지",
        breadcrumb=[("홈", "/"), ("생활권 안내", "/"), ("수지구청·풍덕천", "")],
        body_content="<p>수지구청·풍덕천 생활권 페이지 (준비 중)</p>"
    ),
    create_area_page(
        path="area/jukjeon-bojeong/",
        title="죽전·보정 생활권 출장마사지｜분당선 환승권 안내",
        desc="죽전·보정 생활권 출장마사지 예약 전 죽전역, 보정역을 확인하세요.",
        h1="죽전·보정 생활권 출장마사지",
        breadcrumb=[("홈", "/"), ("생활권 안내", "/"), ("죽전·보정", "")],
        body_content="<p>죽전·보정 생활권 페이지 (준비 중)</p>"
    ),
    create_area_page(
        path="area/dongcheon-gogi/",
        title="동천·고기동 생활권 출장마사지｜수지 북부권 안내",
        desc="동천·고기동 생활권 출장마사지 예약 전 동천역, 고기동을 확인하세요.",
        h1="동천·고기동 생활권 출장마사지",
        breadcrumb=[("홈", "/"), ("생활권 안내", "/"), ("동천·고기동", "")],
        body_content="<p>동천·고기동 생활권 페이지 (준비 중)</p>"
    ),
    create_area_page(
        path="area/seongbok-sinbong/",
        title="성복·신봉 생활권 출장마사지｜수지 서부권 안내",
        desc="성복·신봉 생활권 출장마사지 예약 전 성복역, 신봉동을 확인하세요.",
        h1="성복·신봉 생활권 출장마사지",
        breadcrumb=[("홈", "/"), ("생활권 안내", "/"), ("성복·신봉", "")],
        body_content="<p>성복·신봉 생활권 페이지 (준비 중)</p>"
    ),
    create_area_page(
        path="area/sanghyeon-gwanggyo-nearby/",
        title="상현·광교 인접 생활권 출장마사지｜수원 인접권 안내",
        desc="상현·광교 인접 생활권 출장마사지 예약 전 상현역, 광교를 확인하세요.",
        h1="상현·광교 인접 생활권 출장마사지",
        breadcrumb=[("홈", "/"), ("생활권 안내", "/"), ("상현·광교 인접", "")],
        body_content="<p>상현·광교 인접 생활권 페이지 (준비 중)</p>"
    ),
    create_area_page(
        path="area/giheung-gugal/",
        title="기흥역·구갈 생활권 출장마사지｜역세권 중심 안내",
        desc="기흥역·구갈 생활권 출장마사지 예약 전 기흥역, 구갈동을 확인하세요.",
        h1="기흥역·구갈 생활권 출장마사지",
        breadcrumb=[("홈", "/"), ("생활권 안내", "/"), ("기흥역·구갈", "")],
        body_content="<p>기흥역·구갈 생활권 페이지 (준비 중)</p>"
    ),
    create_area_page(
        path="area/singal-yeongdeok/",
        title="신갈·영덕 생활권 출장마사지｜기흥구 북부권 안내",
        desc="신갈·영덕 생활권 출장마사지 예약 전 신갈역, 영덕동을 확인하세요.",
        h1="신갈·영덕 생활권 출장마사지",
        breadcrumb=[("홈", "/"), ("생활권 안내", "/"), ("신갈·영덕", "")],
        body_content="<p>신갈·영덕 생활권 페이지 (준비 중)</p>"
    ),
    create_area_page(
        path="area/dongbaek-eojeong/",
        title="동백·어정 생활권 출장마사지｜기흥구 동부권 안내",
        desc="동백·어정 생활권 출장마사지 예약 전 동백역, 어정역을 확인하세요.",
        h1="동백·어정 생활권 출장마사지",
        breadcrumb=[("홈", "/"), ("생활권 안내", "/"), ("동백·어정", "")],
        body_content="<p>동백·어정 생활권 페이지 (준비 중)</p>"
    ),
    create_area_page(
        path="area/guseong-mabuk/",
        title="구성·마북 생활권 출장마사지｜기흥구 중부권 안내",
        desc="구성·마북 생활권 출장마사지 예약 전 구성역, 마북동을 확인하세요.",
        h1="구성·마북 생활권 출장마사지",
        breadcrumb=[("홈", "/"), ("생활권 안내", "/"), ("구성·마북", "")],
        body_content="<p>구성·마북 생활권 페이지 (준비 중)</p>"
    ),
    create_area_page(
        path="area/bora-sanggal/",
        title="보라·상갈 생활권 출장마사지｜기흥구 서부권 안내",
        desc="보라·상갈 생활권 출장마사지 예약 전 보라동, 상갈역을 확인하세요.",
        h1="보라·상갈 생활권 출장마사지",
        breadcrumb=[("홈", "/"), ("생활권 안내", "/"), ("보라·상갈", "")],
        body_content="<p>보라·상갈 생활권 페이지 (준비 중)</p>"
    ),
    create_area_page(
        path="area/yeokbuk-gimnyangjang/",
        title="역북·김량장 생활권 출장마사지｜처인구 원도심 안내",
        desc="역북·김량장 생활권 출장마사지 예약 전 역북동, 김량장역을 확인하세요.",
        h1="역북·김량장 생활권 출장마사지",
        breadcrumb=[("홈", "/"), ("생활권 안내", "/"), ("역북·김량장", "")],
        body_content="<p>역북·김량장 생활권 페이지 (준비 중)</p>"
    ),
    create_area_page(
        path="area/samga-yongin-cityhall/",
        title="삼가·용인시청 생활권 출장마사지｜처인구 중심권 안내",
        desc="삼가·용인시청 생활권 출장마사지 예약 전 삼가동, 용인시청을 확인하세요.",
        h1="삼가·용인시청 생활권 출장마사지",
        breadcrumb=[("홈", "/"), ("생활권 안내", "/"), ("삼가·용인시청", "")],
        body_content="<p>삼가·용인시청 생활권 페이지 (준비 중)</p>"
    ),
    create_area_page(
        path="area/pogok-everland/",
        title="포곡·에버랜드 생활권 출장마사지｜처인구 남부권 안내",
        desc="포곡·에버랜드 생활권 출장마사지 예약 전 포곡읍, 에버랜드를 확인하세요.",
        h1="포곡·에버랜드 생활권 출장마사지",
        breadcrumb=[("홈", "/"), ("생활권 안내", "/"), ("포곡·에버랜드", "")],
        body_content="<p>포곡·에버랜드 생활권 페이지 (준비 중)</p>"
    ),
    create_area_page(
        path="area/yangji-wonsam/",
        title="양지·원삼 생활권 출장마사지｜처인구 남서부권 안내",
        desc="양지·원삼 생활권 출장마사지 예약 전 양지읍, 원삼면을 확인하세요.",
        h1="양지·원삼 생활권 출장마사지",
        breadcrumb=[("홈", "/"), ("생활권 안내", "/"), ("양지·원삼", "")],
        body_content="<p>양지·원삼 생활권 페이지 (준비 중)</p>"
    ),
    create_area_page(
        path="area/namsa-idong/",
        title="남사·이동 생활권 출장마사지｜처인구 남부 농촌권 안내",
        desc="남사·이동 생활권 출장마사지 예약 전 남사읍, 이동읍을 확인하세요.",
        h1="남사·이동 생활권 출장마사지",
        breadcrumb=[("홈", "/"), ("생활권 안내", "/"), ("남사·이동", "")],
        body_content="<p>남사·이동 생활권 페이지 (준비 중)</p>"
    ),
    create_area_page(
        path="area/baegam-wonsam/",
        title="백암·원삼 외곽 생활권 출장마사지｜처인구 동부 외곽권 안내",
        desc="백암·원삼 외곽 생활권 출장마사지 예약 전 백암면, 원삼면을 확인하세요.",
        h1="백암·원삼 외곽 생활권 출장마사지",
        breadcrumb=[("홈", "/"), ("생활권 안내", "/"), ("백암·원삼 외곽", "")],
        body_content="<p>백암·원삼 외곽 생활권 페이지 (준비 중)</p>"
    ),
]
