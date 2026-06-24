# 용인시 출장마사지 사이트 공통 설정

BASE_URL = "https://yongin-massage.pages.dev"

BRAND = "88마사지"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 상단 메뉴 — 키워드 반복 없음, 지역명·역명만 표시
NAV = [
    ("용인", "/", []),
    ("구별 안내", "/", [
        ("처인구", "/cheoin-gu/"),
        ("기흥구", "/giheung-gu/"),
        ("수지구", "/suji-gu/"),
    ]),
    ("지역별 안내", "/", [
        ("수지구청역", "/suji-gu/pungdeokcheon-dong/"),
        ("죽전동", "/suji-gu/jukjeon-dong/"),
        ("동천동", "/suji-gu/dongcheon-dong/"),
        ("성복동", "/suji-gu/seongbok-dong/"),
        ("상현동", "/suji-gu/sanghyeon-dong/"),
        ("신갈동", "/giheung-gu/singal-dong/"),
        ("구갈동", "/giheung-gu/gugal-dong/"),
        ("동백동", "/giheung-gu/dongbaek-dong/"),
        ("보정동", "/giheung-gu/bojeong-dong/"),
        ("역북동", "/cheoin-gu/yeokbuk-dong/"),
        ("삼가동", "/cheoin-gu/samga-dong/"),
        ("포곡읍", "/cheoin-gu/pogok-eup/"),
    ]),
    ("역세권 안내", "/", [
        ("수지구청역", "/station/suji-gu-office-station/"),
        ("죽전역", "/station/jukjeon-station/"),
        ("기흥역", "/station/giheung-station/"),
        ("동백역", "/station/dongbaek-station/"),
        ("성복역", "/station/seongbok-station/"),
        ("상현역", "/station/sanghyeon-station/"),
        ("신갈역", "/station/singal-station/"),
        ("구성역", "/station/guseong-station/"),
    ]),
    ("생활권 안내", "/", [
        ("수지구청·풍덕천", "/area/suji-gu-office-pungdeokcheon/"),
        ("죽전·보정", "/area/jukjeon-bojeong/"),
        ("기흥역·구갈", "/area/giheung-gugal/"),
        ("동천·고기동", "/area/dongcheon-gogi/"),
    ]),
    ("예약 안내", "/reservation/", []),
    ("이용 전 확인사항", "/check/", []),
    ("고객센터", "/support/", [
        ("개인정보처리방침", "/support/privacy/"),
    ]),
]
