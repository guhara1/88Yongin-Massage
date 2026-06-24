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

cheoin_gu = create_area_page(
    path="cheoin-gu/",
    title="처인구 출장마사지｜역북·김량장·포곡·양지 생활권 안내",
    desc="처인구 출장마사지 예약 전 역북, 김량장, 포곡, 양지 생활권을 확인하세요.",
    h1="처인구 출장마사지",
    breadcrumb=[("용인", "/"), ("구별 안내", "/")],
    body_content="<p>처인구는 용인의 서부와 남부 지역으로, 용인시청을 중심으로 한 원도심과 포곡, 양지, 남사 등 농촌 지역을 포함합니다. 처인구 전역에서 88마사지 출장마사지 서비스를 이용하실 수 있습니다. 구체적인 지역별 정보는 아래 링크를 참조하세요.</p>"
)

giheung_gu = create_area_page(
    path="giheung-gu/",
    title="기흥구 출장마사지｜기흥역·동백·신갈·보정 생활권 안내",
    desc="기흥구 출장마사지 예약 전 기흥역, 동백, 신갈, 보정 생활권을 확인하세요.",
    h1="기흥구 출장마사지",
    breadcrumb=[("용인", "/"), ("구별 안내", "/")],
    body_content="<p>기흥구는 수인분당선과 에버라인의 환승역을 중심으로 발전한 역세권 중심 지역입니다. 기흥역, 동백역, 신갈역 등이 주요 교통 거점이며, 다양한 생활권이 형성되어 있습니다.</p>"
)

suji_gu = create_area_page(
    path="suji-gu/",
    title="수지구 출장마사지｜죽전·동천·성복·상현 홈타이 안내",
    desc="수지구 출장마사지 예약 전 죽전, 동천, 성복, 상현 생활권을 확인하세요.",
    h1="수지구 출장마사지",
    breadcrumb=[("용인", "/"), ("구별 안내", "/")],
    body_content="<p>수지구는 신분당선 중심의 신주거 지역으로, 수지구청역, 죽전역, 성복역 등이 주요 역세권입니다. 서울 강남과의 교통 접근성이 우수하며, 고급 주거 지역으로 발전하고 있습니다.</p>"
)

# ===== 처인구 지역 페이지 (12개) =====

jungang_dong = create_area_page(
    path="cheoin-gu/jungang-dong/",
    title="중앙동 출장마사지｜용인시청·중앙 생활권 안내",
    desc="중앙동 출장마사지 예약 전 용인시청, 중앙동 생활권을 확인하세요.",
    h1="중앙동 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("중앙동", "")],
    body_content="<p>중앙동은 처인구의 중심 지역으로, 용인시청이 위치한 행정·상업 중심지입니다. 용인 원도심의 주요 생활권으로, 다양한 상점과 시설이 집중되어 있습니다. 88마사지 출장마사지 서비스를 이용하실 수 있습니다.</p>"
)

yeokbuk_dong = create_area_page(
    path="cheoin-gu/yeokbuk-dong/",
    title="역북동 출장마사지｜명지대·김량장 인접 생활권 안내",
    desc="역북동 출장마사지 예약 전 명지대, 김량장 생활권을 확인하세요.",
    h1="역북동 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("역북동", "")],
    body_content="<p>역북동은 용인역 근처의 주거 지역으로, 명지대학교와 인접한 교육 거점입니다. 용인 원도심의 동쪽 지역으로, 교통 접근성이 우수합니다.</p>"
)

samga_dong = create_area_page(
    path="cheoin-gu/samga-dong/",
    title="삼가동 출장마사지｜용인시청·삼가역 생활권 안내",
    desc="삼가동 출장마사지 예약 전 용인시청, 삼가역을 확인하세요.",
    h1="삼가동 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("삼가동", "")],
    body_content="<p>삼가동은 용인시청과 인접한 행정 지역으로, 다양한 공공 기관이 위치해 있습니다.</p>"
)

dongbu_dong = create_area_page(
    path="cheoin-gu/dongbu-dong/",
    title="동부동 출장마사지｜처인구 동부 생활권 안내",
    desc="동부동 출장마사지 예약 전 처인구 동부 생활권을 확인하세요.",
    h1="동부동 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("동부동", "")],
    body_content="<p>동부동은 처인구의 동쪽 생활권입니다.</p>"
)

pogok_eup = create_area_page(
    path="cheoin-gu/pogok-eup/",
    title="포곡읍 출장마사지｜둔전·에버랜드 생활권 안내",
    desc="포곡읍 출장마사지 예약 전 둔전, 에버랜드 생활권을 확인하세요.",
    h1="포곡읍 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("포곡읍", "")],
    body_content="<p>포곡읍은 처인구 남부의 농촌 지역으로, 에버랜드에 인접해 있습니다.</p>"
)

mohyeon_eup = create_area_page(
    path="cheoin-gu/mohyeon-eup/",
    title="모현읍 출장마사지｜외대·모현 인접 생활권 안내",
    desc="모현읍 출장마사지 예약 전 외대, 모현 인접권을 확인하세요.",
    h1="모현읍 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("모현읍", "")],
    body_content="<p>모현읍은 처인구 동부의 읍 지역입니다.</p>"
)

idong_eup = create_area_page(
    path="cheoin-gu/idong-eup/",
    title="이동읍 출장마사지｜이동·송전 생활권 안내",
    desc="이동읍 출장마사지 예약 전 이동, 송전 생활권을 확인하세요.",
    h1="이동읍 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("이동읍", "")],
    body_content="<p>이동읍은 처인구의 남동부 농촌 지역입니다.</p>"
)

namsa_eup = create_area_page(
    path="cheoin-gu/namsa-eup/",
    title="남사읍 출장마사지｜남사·아곡 생활권 안내",
    desc="남사읍 출장마사지 예약 전 남사, 아곡 생활권을 확인하세요.",
    h1="남사읍 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("남사읍", "")],
    body_content="<p>남사읍은 처인구 남부의 농촌 지역입니다.</p>"
)

yangji_eup = create_area_page(
    path="cheoin-gu/yangji-eup/",
    title="양지읍 출장마사지｜양지·원삼 인접 생활권 안내",
    desc="양지읍 출장마사지 예약 전 양지, 원삼 인접권을 확인하세요.",
    h1="양지읍 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("양지읍", "")],
    body_content="<p>양지읍은 처인구의 고급 주택 밀집 지역입니다.</p>"
)

wonsam_myeon = create_area_page(
    path="cheoin-gu/wonsam-myeon/",
    title="원삼면 출장마사지｜용인 동부 외곽 생활권 안내",
    desc="원삼면 출장마사지 예약 전 원삼, 용인 동부를 확인하세요.",
    h1="원삼면 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("원삼면", "")],
    body_content="<p>원삼면은 처인구의 동부 외곽 지역입니다.</p>"
)

baegam_myeon = create_area_page(
    path="cheoin-gu/baegam-myeon/",
    title="백암면 출장마사지｜백암·원삼 인접 생활권 안내",
    desc="백암면 출장마사지 예약 전 백암, 원삼을 확인하세요.",
    h1="백암면 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("백암면", "")],
    body_content="<p>백암면은 처인구의 산림 자연 보호 지역입니다.</p>"
)

yurim_area = create_area_page(
    path="cheoin-gu/yurim-area/",
    title="유림 생활권 출장마사지｜유림동 신도시 개발 지역 안내",
    desc="유림 생활권 출장마사지 예약 전 유림동을 확인하세요.",
    h1="유림 생활권 출장마사지",
    breadcrumb=[("용인", "/"), ("처인구", "/cheoin-gu/"), ("유림 생활권", "")],
    body_content="<p>유림 생활권은 처인구의 신도시 개발 지역입니다.</p>"
)

# ===== 기흥구 지역 페이지 (12개) =====

singal_dong = create_area_page(
    path="giheung-gu/singal-dong/",
    title="신갈동 출장마사지｜신갈역·기흥역 인접 생활권 안내",
    desc="신갈동 출장마사지 예약 전 신갈역, 기흥역을 확인하세요.",
    h1="신갈동 출장마사지",
    breadcrumb=[("용인", "/"), ("기흥구", "/giheung-gu/"), ("신갈동", "")],
    body_content="<p>신갈동은 신갈역 중심의 역세권 지역입니다.</p>"
)

yeongdeok_dong = create_area_page(
    path="giheung-gu/yeongdeok-dong/",
    title="영덕동 출장마사지｜영덕·기흥 인접 생활권 안내",
    desc="영덕동 출장마사지 예약 전 영덕, 기흥을 확인하세요.",
    h1="영덕동 출장마사지",
    breadcrumb=[("용인", "/"), ("기흥구", "/giheung-gu/"), ("영덕동", "")],
    body_content="<p>영덕동은 기흥구의 주거 지역입니다.</p>"
)

gugal_dong = create_area_page(
    path="giheung-gu/gugal-dong/",
    title="구갈동 출장마사지｜기흥역·강남대역 생활권 안내",
    desc="구갈동 출장마사지 예약 전 기흥역, 강남대역을 확인하세요.",
    h1="구갈동 출장마사지",
    breadcrumb=[("용인", "/"), ("기흥구", "/giheung-gu/"), ("구갈동", "")],
    body_content="<p>구갈동은 기흥역과 강남대역에 인접한 지역입니다.</p>"
)

sanggal_dong = create_area_page(
    path="giheung-gu/sanggal-dong/",
    title="상갈동 출장마사지｜상갈역·보라동 생활권 안내",
    desc="상갈동 출장마사지 예약 전 상갈역, 보라동을 확인하세요.",
    h1="상갈동 출장마사지",
    breadcrumb=[("용인", "/"), ("기흥구", "/giheung-gu/"), ("상갈동", "")],
    body_content="<p>상갈동은 상갈역 중심의 역세권입니다.</p>"
)

bora_dong = create_area_page(
    path="giheung-gu/bora-dong/",
    title="보라동 출장마사지｜민속촌·보라동 생활권 안내",
    desc="보라동 출장마사지 예약 전 민속촌, 보라동을 확인하세요.",
    h1="보라동 출장마사지",
    breadcrumb=[("용인", "/"), ("기흥구", "/giheung-gu/"), ("보라동", "")],
    body_content="<p>보라동은 기흥구의 주거 지역입니다.</p>"
)

giheung_dong = create_area_page(
    path="giheung-gu/giheung-dong/",
    title="기흥동 출장마사지｜기흥·공세 생활권 안내",
    desc="기흥동 출장마사지 예약 전 기흥, 공세를 확인하세요.",
    h1="기흥동 출장마사지",
    breadcrumb=[("용인", "/"), ("기흥구", "/giheung-gu/"), ("기흥동", "")],
    body_content="<p>기흥동은 기흥구의 주거 지역입니다.</p>"
)

seonong_dong = create_area_page(
    path="giheung-gu/seonong-dong/",
    title="서농동 출장마사지｜서농·영통 인접 생활권 안내",
    desc="서농동 출장마사지 예약 전 서농, 영통을 확인하세요.",
    h1="서농동 출장마사지",
    breadcrumb=[("용인", "/"), ("기흥구", "/giheung-gu/"), ("서농동", "")],
    body_content="<p>서농동은 수원 인접 지역입니다.</p>"
)

guseong_dong = create_area_page(
    path="giheung-gu/guseong-dong/",
    title="구성동 출장마사지｜구성역·마북 인접 생활권 안내",
    desc="구성동 출장마사지 예약 전 구성역, 마북을 확인하세요.",
    h1="구성동 출장마사지",
    breadcrumb=[("용인", "/"), ("기흥구", "/giheung-gu/"), ("구성동", "")],
    body_content="<p>구성동은 구성역 중심의 역세권입니다.</p>"
)

mabuk_dong = create_area_page(
    path="giheung-gu/mabuk-dong/",
    title="마북동 출장마사지｜마북·구성 생활권 안내",
    desc="마북동 출장마사지 예약 전 마북, 구성을 확인하세요.",
    h1="마북동 출장마사지",
    breadcrumb=[("용인", "/"), ("기흥구", "/giheung-gu/"), ("마북동", "")],
    body_content="<p>마북동은 기흥구의 주거 지역입니다.</p>"
)

dongbaek_dong = create_area_page(
    path="giheung-gu/dongbaek-dong/",
    title="동백동 출장마사지｜동백역·어정역 생활권 안내",
    desc="동백동 출장마사지 예약 전 동백역, 어정역을 확인하세요.",
    h1="동백동 출장마사지",
    breadcrumb=[("용인", "/"), ("기흥구", "/giheung-gu/"), ("동백동", "")],
    body_content="<p>동백동은 동백역 중심의 역세권입니다.</p>"
)

sangha_dong = create_area_page(
    path="giheung-gu/sangha-dong/",
    title="상하동 출장마사지｜강남대·구갈 인접 생활권 안내",
    desc="상하동 출장마사지 예약 전 강남대, 구갈을 확인하세요.",
    h1="상하동 출장마사지",
    breadcrumb=[("용인", "/"), ("기흥구", "/giheung-gu/"), ("상하동", "")],
    body_content="<p>상하동은 기흥구의 지역입니다.</p>"
)

bojeong_dong = create_area_page(
    path="giheung-gu/bojeong-dong/",
    title="보정동 출장마사지｜보정역·죽전 인접 생활권 안내",
    desc="보정동 출장마사지 예약 전 보정역, 죽전을 확인하세요.",
    h1="보정동 출장마사지",
    breadcrumb=[("용인", "/"), ("기흥구", "/giheung-gu/"), ("보정동", "")],
    body_content="<p>보정동은 보정역 중심의 역세권입니다.</p>"
)

# ===== 수지구 지역 페이지 (6개) =====

pungdeokcheon_dong = create_area_page(
    path="suji-gu/pungdeokcheon-dong/",
    title="풍덕천동 출장마사지｜수지구청역 생활권 안내",
    desc="풍덕천동 출장마사지 예약 전 수지구청역을 확인하세요.",
    h1="풍덕천동 출장마사지",
    breadcrumb=[("용인", "/"), ("수지구", "/suji-gu/"), ("풍덕천동", "")],
    body_content="<p>풍덕천동은 수지구청역 중심의 역세권입니다.</p>"
)

sinbong_dong = create_area_page(
    path="suji-gu/sinbong-dong/",
    title="신봉동 출장마사지｜신봉·풍덕천 생활권 안내",
    desc="신봉동 출장마사지 예약 전 신봉, 풍덕천을 확인하세요.",
    h1="신봉동 출장마사지",
    breadcrumb=[("용인", "/"), ("수지구", "/suji-gu/"), ("신봉동", "")],
    body_content="<p>신봉동은 수지구의 주거 지역입니다.</p>"
)

jukjeon_dong = create_area_page(
    path="suji-gu/jukjeon-dong/",
    title="죽전동 출장마사지｜죽전역·보정역 생활권 안내",
    desc="죽전동 출장마사지 예약 전 죽전역, 보정역을 확인하세요.",
    h1="죽전동 출장마사지",
    breadcrumb=[("용인", "/"), ("수지구", "/suji-gu/"), ("죽전동", "")],
    body_content="<p>죽전동은 죽전역 중심의 역세권입니다.</p>"
)

dongcheon_dong = create_area_page(
    path="suji-gu/dongcheon-dong/",
    title="동천동 출장마사지｜동천역·고기동 생활권 안내",
    desc="동천동 출장마사지 예약 전 동천역, 고기동을 확인하세요.",
    h1="동천동 출장마사지",
    breadcrumb=[("용인", "/"), ("수지구", "/suji-gu/"), ("동천동", "")],
    body_content="<p>동천동은 동천역 중심의 역세권입니다.</p>"
)

sanghyeon_dong = create_area_page(
    path="suji-gu/sanghyeon-dong/",
    title="상현동 출장마사지｜상현역·광교 인접 생활권 안내",
    desc="상현동 출장마사지 예약 전 상현역, 광교를 확인하세요.",
    h1="상현동 출장마사지",
    breadcrumb=[("용인", "/"), ("수지구", "/suji-gu/"), ("상현동", "")],
    body_content="<p>상현동은 상현역 중심의 역세권입니다.</p>"
)

seongbok_dong = create_area_page(
    path="suji-gu/seongbok-dong/",
    title="성복동 출장마사지｜성복역·신봉동 생활권 안내",
    desc="성복동 출장마사지 예약 전 성복역, 신봉동을 확인하세요.",
    h1="성복동 출장마사지",
    breadcrumb=[("용인", "/"), ("수지구", "/suji-gu/"), ("성복동", "")],
    body_content="<p>성복동은 성복역 중심의 역세권입니다.</p>"
)

# PAGES 리스트에 모든 페이지 집계
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
    baegam_myeon,
    yurim_area,
    singal_dong,
    yeongdeok_dong,
    gugal_dong,
    sanggal_dong,
    bora_dong,
    giheung_dong,
    seonong_dong,
    guseong_dong,
    mabuk_dong,
    dongbaek_dong,
    sangha_dong,
    bojeong_dong,
    pungdeokcheon_dong,
    sinbong_dong,
    jukjeon_dong,
    dongcheon_dong,
    sanghyeon_dong,
    seongbok_dong,
]
