# 용인시 구별·지역별 페이지 — 33개 (3개 구 + 30개 지역)

from .site import BASE_URL, PHONE

_BASE = BASE_URL.rstrip("/")

def create_area_page(path, title, desc, h1, breadcrumb, body_content):
    """지역 페이지 생성 헬퍼 함수"""
    return {
        "path": path,
        "title": title,
        "desc": desc,
        "h1": h1,
        "breadcrumb": breadcrumb,
        "body": body_content,
    }

# ===== 구별 페이지 (3개) =====
# 주: 상세 콘텐츠는 yongin_areas_gu.py에서 제공

cheoin_gu = create_area_page(
    path="cheoin-gu/",
    title="처인구 출장마사지｜역북·김량장·포곡 생활권 홈타이 안내",
    desc="처인구 출장마사지·홈타이 예약 전 역북동, 포곡읍, 에버라인 생활권을 확인하세요.",
    h1="처인구 출장마사지",
    breadcrumb=[("용인", "/"), ("구별 안내", "/cheoin-gu/")],
    body_content="""
<section>
<h2>처인구 소개</h2>
<p>용인시 처인구는 용인의 서쪽과 남쪽에 위치한 광역 생활권으로, 에버라인과 차량 이동을 중심으로 발전하고 있습니다. 역북동의 명지대역, 삼가동의 용인시청, 포곡읍의 에버랜드 등 주요 거점이 분포하며, 용인의 원도심과 외곽 차량 이동권을 아우르고 있습니다.</p>
<p>88마사지에서는 처인구 전역에 출장마사지·홈타이 서비스를 제공합니다.</p>
</section>

<section>
<h2>처인구 주요 지역</h2>
<ul>
<li><a href="/cheoin-gu/jungang-dong/">중앙동</a></li>
<li><a href="/cheoin-gu/yeokbuk-dong/">역북동</a></li>
<li><a href="/cheoin-gu/samga-dong/">삼가동</a></li>
<li><a href="/cheoin-gu/dongbu-dong/">동부동</a></li>
<li><a href="/cheoin-gu/pogok-eup/">포곡읍</a></li>
<li><a href="/cheoin-gu/mohyeon-eup/">모현읍</a></li>
<li><a href="/cheoin-gu/idong-eup/">이동읍</a></li>
<li><a href="/cheoin-gu/namsa-eup/">남사읍</a></li>
<li><a href="/cheoin-gu/yangji-eup/">양지읍</a></li>
<li><a href="/cheoin-gu/wonsam-myeon/">원삼면</a></li>
<li><a href="/cheoin-gu/baekam-myeon/">백암면</a></li>
<li><a href="/cheoin-gu/yurim-area/">유림</a></li>
</ul>
</section>
"""
)

giheung_gu = create_area_page(
    path="giheung-gu/",
    title="기흥구 출장마사지｜신갈역·동백역·기흥역 생활권 홈타이 안내",
    desc="기흥구 출장마사지·홈타이 예약 전 신갈역, 동백역, 기흥역 생활권을 확인하세요.",
    h1="기흥구 출장마사지",
    breadcrumb=[("용인", "/"), ("구별 안내", "/giheung-gu/")],
    body_content="""
<section>
<h2>기흥구 소개</h2>
<p>용인시 기흥구는 용인의 중앙 및 남부에 위치한 역세권·주거 중심 생활권입니다. 수인분당선과 에버라인이 만나는 환승역 중심으로 발전했으며, 기흥역, 신갈역, 동백역, 구성역, 보정역 등이 주요 교통 거점입니다. 기흥구는 용인 3개 구 중에서 대중교통 접근성이 가장 우수합니다.</p>
<p>88마사지에서는 기흥구 모든 역세권에 빠르고 안정적인 출장마사지 서비스를 제공합니다.</p>
</section>

<section>
<h2>기흥구 주요 지역</h2>
<ul>
<li><a href="/giheung-gu/singal-dong/">신갈동</a></li>
<li><a href="/giheung-gu/yeongdeok-dong/">영덕동</a></li>
<li><a href="/giheung-gu/gugal-dong/">구갈동</a></li>
<li><a href="/giheung-gu/sanggal-dong/">상갈동</a></li>
<li><a href="/giheung-gu/bora-dong/">보라동</a></li>
<li><a href="/giheung-gu/giheung-dong/">기흥동</a></li>
<li><a href="/giheung-gu/seonong-dong/">서농동</a></li>
<li><a href="/giheung-gu/guseong-dong/">구성동</a></li>
<li><a href="/giheung-gu/mabuk-dong/">마북동</a></li>
<li><a href="/giheung-gu/dongbaek-dong/">동백동</a></li>
<li><a href="/giheung-gu/sangha-dong/">상하동</a></li>
<li><a href="/giheung-gu/bojeong-dong/">보정동</a></li>
</ul>
</section>
"""
)

suji_gu = create_area_page(
    path="suji-gu/",
    title="수지구 출장마사지｜죽전역·신분당선·상현역 생활권 홈타이 안내",
    desc="수지구 출장마사지·홈타이 예약 전 죽전역, 신분당선, 상현역 생활권을 확인하세요.",
    h1="수지구 출장마사지",
    breadcrumb=[("용인", "/"), ("구별 안내", "/suji-gu/")],
    body_content="""
<section>
<h2>수지구 소개</h2>
<p>용인시 수지구는 신분당선 중심의 신주거 지역으로, 수지구청역, 죽전역, 성복역, 상현역 등이 주요 역세권입니다. 서울 강남과의 교통 접근성이 우수하며, 고급 주거 지역으로 발전하고 있습니다.</p>
<p>88마사지에서는 수지구의 모든 신분당선 역세권에 프리미엄 출장마사지 서비스를 제공합니다.</p>
</section>

<section>
<h2>수지구 주요 지역</h2>
<ul>
<li><a href="/suji-gu/pungdeokcheon-dong/">풍덕천동</a></li>
<li><a href="/suji-gu/sinbong-dong/">신봉동</a></li>
<li><a href="/suji-gu/jukjeon-dong/">죽전동</a></li>
<li><a href="/suji-gu/dongcheon-dong/">동천동</a></li>
<li><a href="/suji-gu/sanghyeon-dong/">상현동</a></li>
<li><a href="/suji-gu/seongbok-dong/">성복동</a></li>
</ul>
</section>
"""
)

# ===== 처인구 지역 페이지 (12개) - 스켈레톤 (상세 콘텐츠 생성 중) =====

jungang_dong = create_area_page(
    path="cheoin-gu/jungang-dong/",
    title="중앙동 출장마사지｜용인시청·중앙 생활권 안내",
    desc="중앙동 출장마사지 예약 전 용인시청, 중앙동 생활권을 확인하세요.",
    h1="처인구 중앙동 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("중앙동", "")],
    body_content="<p>중앙동은 처인구의 중심 지역으로, 용인시청이 위치한 행정·상업 중심지입니다. 88마사지 출장마사지 서비스를 이용하실 수 있습니다.</p>"
)

yeokbuk_dong = create_area_page(
    path="cheoin-gu/yeokbuk-dong/",
    title="역북동 출장마사지｜명지대·김량장 인접 생활권 안내",
    desc="역북동 출장마사지 예약 전 명지대, 김량장 생활권을 확인하세요.",
    h1="처인구 역북동 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("역북동", "")],
    body_content="<p>역북동은 용인역 근처의 주거 지역으로, 명지대학교와 인접한 교육 거점입니다.</p>"
)

samga_dong = create_area_page(
    path="cheoin-gu/samga-dong/",
    title="삼가동 출장마사지｜용인시청·삼가역 생활권 안내",
    desc="삼가동 출장마사지 예약 전 용인시청, 삼가역을 확인하세요.",
    h1="처인구 삼가동 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("삼가동", "")],
    body_content="<p>삼가동은 용인시청과 인접한 행정 지역입니다.</p>"
)

dongbu_dong = create_area_page(
    path="cheoin-gu/dongbu-dong/",
    title="동부동 출장마사지｜처인구 동부 생활권 안내",
    desc="동부동 출장마사지 예약 전 처인구 동부 생활권을 확인하세요.",
    h1="처인구 동부동 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("동부동", "")],
    body_content="<p>동부동은 처인구의 동부 지역으로 포곡읍과 인접한 생활권입니다.</p>"
)

pogok_eup = create_area_page(
    path="cheoin-gu/pogok-eup/",
    title="포곡읍 출장마사지｜에버랜드·전대 생활권 안내",
    desc="포곡읍 출장마사지 예약 전 에버랜드, 에버라인 생활권을 확인하세요.",
    h1="처인구 포곡읍 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("포곡읍", "")],
    body_content="<p>포곡읍은 에버랜드와 인접한 관광 및 외곽 주거 생활권입니다.</p>"
)

mohyeon_eup = create_area_page(
    path="cheoin-gu/mohyeon-eup/",
    title="모현읍 출장마사지｜처인구 외곽 생활권 안내",
    desc="모현읍 출장마사지 예약 전 처인구 외곽 생활권을 확인하세요.",
    h1="처인구 모현읍 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("모현읍", "")],
    body_content="<p>모현읍은 차량 이동 기반의 외곽 주거 지역입니다.</p>"
)

idong_eup = create_area_page(
    path="cheoin-gu/idong-eup/",
    title="이동읍 출장마사지｜에버라인 동백역 생활권 안내",
    desc="이동읍 출장마사지 예약 전 에버라인, 동백역 생활권을 확인하세요.",
    h1="처인구 이동읍 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("이동읍", "")],
    body_content="<p>이동읍은 에버라인 동백역 인근 산업·주거 생활권입니다.</p>"
)

namsa_eup = create_area_page(
    path="cheoin-gu/namsa-eup/",
    title="남사읍 출장마사지｜처인구 남부 외곽 생활권 안내",
    desc="남사읍 출장마사지 예약 전 처인구 남부 외곽 생활권을 확인하세요.",
    h1="처인구 남사읍 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("남사읍", "")],
    body_content="<p>남사읍은 외곽 생활권 차량 중심의 지역입니다.</p>"
)

yangji_eup = create_area_page(
    path="cheoin-gu/yangji-eup/",
    title="양지읍 출장마사지｜경기 남부 외곽 생활권 안내",
    desc="양지읍 출장마사지 예약 전 경기 남부 외곽 생활권을 확인하세요.",
    h1="처인구 양지읍 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("양지읍", "")],
    body_content="<p>양지읍은 경기 남부의 외곽 광역 이동권입니다.</p>"
)

wonsam_myeon = create_area_page(
    path="cheoin-gu/wonsam-myeon/",
    title="원삼면 출장마사지｜조용한 전원주거 생활권 안내",
    desc="원삼면 출장마사지 예약 전 전원 주거 생활권을 확인하세요.",
    h1="처인구 원삼면 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("원삼면", "")],
    body_content="<p>원삼면은 조용한 전원 주거 생활권입니다.</p>"
)

baekam_myeon = create_area_page(
    path="cheoin-gu/baekam-myeon/",
    title="백암면 출장마사지｜광역 외곽 차량중심 생활권 안내",
    desc="백암면 출장마사지 예약 전 광역 외곽 생활권을 확인하세요.",
    h1="처인구 백암면 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("백암면", "")],
    body_content="<p>백암면은 광역 외곽 지역으로 용인에서도 가장 접근이 어려운 지역입니다.</p>"
)

yurim_area = create_area_page(
    path="cheoin-gu/yurim-area/",
    title="유림 출장마사지｜처인구 특정 개발 생활권 안내",
    desc="유림 출장마사지 예약 전 유림 생활권을 확인하세요.",
    h1="처인구 유림 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("유림", "")],
    body_content="<p>유림은 처인구의 특정 개발 지역입니다.</p>"
)

# ===== 기흥구 지역 페이지 (12개) - 상세 콘텐츠 제공 =====
# (giheung_areas.py에서 제공되는 12개 페이지는 별도 처리)

# ===== 수지구 지역 페이지 (6개) - 상세 콘텐츠 제공 =====
# (suji_areas.py에서 제공되는 6개 페이지는 별도 처리)

PAGES = [
    cheoin_gu,
    giheung_gu,
    suji_gu,
    jungang_dong,
    yeokbuk_dong,
    samga_dong,
    dongbu_dong,
    pogok_eup,
    mohyeon_eup,
    idong_eup,
    namsa_eup,
    yangji_eup,
    wonsam_myeon,
    baekam_myeon,
    yurim_area,
]
