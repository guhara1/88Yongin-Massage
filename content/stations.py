# 용인시 역세권 페이지 — 24개 지하철역

from .site import BASE_URL, PHONE

_BASE = BASE_URL.rstrip("/")

def create_station_page(path, title, desc, h1, breadcrumb, body_content):
    """역세권 페이지 생성 헬퍼 함수"""
    return {
        "path": path,
        "title": title,
        "desc": desc,
        "h1": h1,
        "breadcrumb": breadcrumb,
        "body": body_content,
    }

# ===== 24개 역세권 페이지 =====

# 임시: 스켈레톤 페이지들
# TODO: 각 역별 상세 콘텐츠 추가 필요

PAGES = [
    create_station_page(
        path="station/suji-gu-office-station/",
        title="수지구청역 출장마사지｜풍덕천·신봉 생활권 안내",
        desc="수지구청역 출장마사지 예약 전 풍덕천동, 신봉동, 성복동을 확인하세요.",
        h1="수지구청역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("수지구청역", "")],
        body_content="<p>수지구청역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/jukjeon-station/",
        title="죽전역 출장마사지｜죽전동·보정동 생활권 안내",
        desc="죽전역 출장마사지 예약 전 죽전동, 보정동을 확인하세요.",
        h1="죽전역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("죽전역", "")],
        body_content="<p>죽전역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/dongcheon-station/",
        title="동천역 출장마사지｜동천동·고기동 생활권 안내",
        desc="동천역 출장마사지 예약 전 동천동, 고기동을 확인하세요.",
        h1="동천역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("동천역", "")],
        body_content="<p>동천역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/seongbok-station/",
        title="성복역 출장마사지｜성복동·신봉동 생활권 안내",
        desc="성복역 출장마사지 예약 전 성복동, 신봉동을 확인하세요.",
        h1="성복역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("성복역", "")],
        body_content="<p>성복역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/sanghyeon-station/",
        title="상현역 출장마사지｜상현동·광교 인접 생활권 안내",
        desc="상현역 출장마사지 예약 전 상현동, 광교 인접권을 확인하세요.",
        h1="상현역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("상현역", "")],
        body_content="<p>상현역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/giheung-station/",
        title="기흥역 출장마사지｜구갈동·신갈동 생활권 안내",
        desc="기흥역 출장마사지 예약 전 구갈동, 신갈동을 확인하세요.",
        h1="기흥역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("기흥역", "")],
        body_content="<p>기흥역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/guseong-station/",
        title="구성역 출장마사지｜구성동·마북동 생활권 안내",
        desc="구성역 출장마사지 예약 전 구성동, 마북동을 확인하세요.",
        h1="구성역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("구성역", "")],
        body_content="<p>구성역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/dongbaek-station/",
        title="동백역 출장마사지｜동백동·어정역 생활권 안내",
        desc="동백역 출장마사지 예약 전 동백동, 어정역을 확인하세요.",
        h1="동백역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("동백역", "")],
        body_content="<p>동백역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/bojeong-station/",
        title="보정역 출장마사지｜보정동·죽전 인접 생활권 안내",
        desc="보정역 출장마사지 예약 전 보정동, 죽전을 확인하세요.",
        h1="보정역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("보정역", "")],
        body_content="<p>보정역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/singal-station/",
        title="신갈역 출장마사지｜신갈동·영덕동 생활권 안내",
        desc="신갈역 출장마사지 예약 전 신갈동, 영덕동을 확인하세요.",
        h1="신갈역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("신갈역", "")],
        body_content="<p>신갈역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/sanggal-station/",
        title="상갈역 출장마사지｜상갈동·보라동 생활권 안내",
        desc="상갈역 출장마사지 예약 전 상갈동, 보라동을 확인하세요.",
        h1="상갈역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("상갈역", "")],
        body_content="<p>상갈역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/kangnam-univ-station/",
        title="강남대역 출장마사지｜구갈동·신갈동 인접 생활권 안내",
        desc="강남대역 출장마사지 예약 전 구갈동, 신갈동 인접권을 확인하세요.",
        h1="강남대역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("강남대역", "")],
        body_content="<p>강남대역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/jiseok-station/",
        title="지석역 출장마사지｜지석역 인접 생활권 안내",
        desc="지석역 출장마사지 예약 전 지석역 인접권을 확인하세요.",
        h1="지석역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("지석역", "")],
        body_content="<p>지석역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/eojeong-station/",
        title="어정역 출장마사지｜어정역·동백동 생활권 안내",
        desc="어정역 출장마사지 예약 전 어정역, 동백동을 확인하세요.",
        h1="어정역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("어정역", "")],
        body_content="<p>어정역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/chodang-station/",
        title="초당역 출장마사지｜초당역·동백동 생활권 안내",
        desc="초당역 출장마사지 예약 전 초당역, 동백동을 확인하세요.",
        h1="초당역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("초당역", "")],
        body_content="<p>초당역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/samga-station/",
        title="삼가역 출장마사지｜삼가동·용인시청 생활권 안내",
        desc="삼가역 출장마사지 예약 전 삼가동, 용인시청 생활권을 확인하세요.",
        h1="삼가역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("삼가역", "")],
        body_content="<p>삼가역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/cityhall-yongin-univ-station/",
        title="시청·용인대역 출장마사지｜삼가동·용인 생활권 안내",
        desc="시청·용인대역 출장마사지 예약 전 삼가동, 용인시청을 확인하세요.",
        h1="시청·용인대역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("시청·용인대역", "")],
        body_content="<p>시청·용인대역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/myongji-univ-station/",
        title="명지대역 출장마사지｜역북동·중앙동 생활권 안내",
        desc="명지대역 출장마사지 예약 전 역북동, 중앙동을 확인하세요.",
        h1="명지대역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("명지대역", "")],
        body_content="<p>명지대역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/gimnyangjang-station/",
        title="김량장역 출장마사지｜역북동·중앙동 생활권 안내",
        desc="김량장역 출장마사지 예약 전 역북동, 중앙동을 확인하세요.",
        h1="김량장역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("김량장역", "")],
        body_content="<p>김량장역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/yongin-jungang-market-station/",
        title="용인중앙시장역 출장마사지｜김량장·중앙동 생활권 안내",
        desc="용인중앙시장역 출장마사지 예약 전 김량장, 중앙동을 확인하세요.",
        h1="용인중앙시장역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("용인중앙시장역", "")],
        body_content="<p>용인중앙시장역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/gojin-station/",
        title="고진역 출장마사지｜고진역 인접 생활권 안내",
        desc="고진역 출장마사지 예약 전 고진역 인접권을 확인하세요.",
        h1="고진역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("고진역", "")],
        body_content="<p>고진역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/bopyeong-station/",
        title="보평역 출장마사지｜보평역 인접 생활권 안내",
        desc="보평역 출장마사지 예약 전 보평역 인접권을 확인하세요.",
        h1="보평역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("보평역", "")],
        body_content="<p>보평역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/dunjeon-station/",
        title="둔전역 출장마사지｜포곡읍·에버랜드 생활권 안내",
        desc="둔전역 출장마사지 예약 전 포곡읍, 에버랜드 생활권을 확인하세요.",
        h1="둔전역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("둔전역", "")],
        body_content="<p>둔전역 페이지 (준비 중)</p>"
    ),
    create_station_page(
        path="station/jeondae-everland-station/",
        title="전대·에버랜드역 출장마사지｜포곡읍·에버랜드 생활권 안내",
        desc="전대·에버랜드역 출장마사지 예약 전 포곡읍, 에버랜드 생활권을 확인하세요.",
        h1="전대·에버랜드역 출장마사지",
        breadcrumb=[("홈", "/"), ("역세권 안내", "/"), ("전대·에버랜드역", "")],
        body_content="<p>전대·에버랜드역 페이지 (준비 중)</p>"
    ),
]
