import json
from .site import BRAND, BASE_URL, PHONE

_BASE = BASE_URL.rstrip("/")

# 메타 설명 (80자 이내)
DESC = "용인 출장마사지·홈타이 예약 전 수지, 기흥, 처인, 죽전, 동백, 역북 생활권을 확인하세요."

# 자주 묻는 질문 (FAQ 스키마)
_FAQ = [
    ("용인 출장마사지는 어떤 서비스인가요?",
     "방문형 마사지 서비스로, 고객의 자택, 숙소, 오피스텔 등으로 전문가가 방문하여 관리하는 서비스입니다. 처인구, 기흥구, 수지구 전지역으로 방문 가능합니다."),

    ("처인구, 기흥구, 수지구의 생활권 차이가 뭔가요?",
     "수지구는 신분당선 중심의 신주거 생활권, 기흥구는 수인분당선·에버라인 중심의 역세권 생활권, 처인구는 에버라인과 차량 이동 중심의 광역 생활권입니다."),

    ("예약 전 꼭 확인해야 할 사항은?",
     "방문 가능 주소, 예약 가능 시간, 추가 이동비 여부, 건물 출입 방식, 결제 방식을 먼저 확인하고 예약하는 방식이 좋습니다."),

    ("수지구 죽전동과 죽전역은 어떻게 다른가요?",
     "죽전동은 수지구 중심 주거지를 중심으로, 죽전역은 분당선 환승역 중심의 이동 기준으로 구성됩니다."),

    ("추가 이동비는 어떻게 계산되나요?",
     "지역별로 기본 이동권이 정해져 있으며, 그 외 먼 거리는 추가 이동비가 발생할 수 있습니다. 예약 시 정확히 확인하세요."),
]

# FAQ 스키마 생성
_faq_schema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "@id": f"#faq-{i+1}",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        }
        for i, (q, a) in enumerate(_FAQ)
    ]
}

_faq_schema_str = json.dumps(_faq_schema, ensure_ascii=False, indent=2)

# Organization 스키마
_org_schema = {
    "@context": "https://schema.org",
    "@type": "HealthAndBeautyBusiness",
    "name": BRAND,
    "telephone": PHONE,
    "url": _BASE + "/",
    "image": _BASE + "/assets/og-image.png",
    "description": "용인시 출장마사지·홈타이 안내 사이트",
    "areaServed": {
        "@type": "AdministrativeArea",
        "name": "경기도 용인시"
    },
    "openingHoursSpecification": {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "opens": "00:00",
        "closes": "23:59"
    }
}

_org_schema_str = json.dumps(_org_schema, ensure_ascii=False, indent=2)

# BreadcrumbList 스키마 (메인 페이지는 홈만)
_breadcrumb_schema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "홈",
            "item": _BASE + "/"
        }
    ]
}

_breadcrumb_schema_str = json.dumps(_breadcrumb_schema, ensure_ascii=False, indent=2)

_EXTRA_HEAD = f"""<script type="application/ld+json">
{_org_schema_str}
</script>
<script type="application/ld+json">
{_breadcrumb_schema_str}
</script>
<script type="application/ld+json">
{_faq_schema_str}
</script>"""

_HERO = """<div class="hero">
  <div class="hero-content">
    <div class="hero-badge">용인시 전지역 방문 관리</div>
    <h1 class="hero-title">용인 출장마사지<br><span class="hero-accent">용인 홈타이</span><br>지역별 예약 안내</h1>
    <p class="hero-lead">수지, 기흥, 처인, 죽전, 동백, 역북, 기흥역, 수지구청역, 에버라인 주요 생활권별 방문 가능 지역과 예약 전 확인사항을 안내합니다.</p>
    <div class="hero-cta">
      <a href="#coverage" class="btn btn-primary">지역별 안내 보기</a>
      <a href="#stations" class="btn btn-secondary">가까운 역 찾기</a>
      <a href="/reservation/" class="btn btn-secondary">예약 안내 보기</a>
      <a href="/check/" class="btn btn-secondary">이용 전 확인사항</a>
    </div>
  </div>
  <div class="hero-stats">
    <div class="stat">
      <div class="stat-number">3</div>
      <div class="stat-label">구별 안내</div>
    </div>
    <div class="stat">
      <div class="stat-number">30</div>
      <div class="stat-label">지역 페이지</div>
    </div>
    <div class="stat">
      <div class="stat-number">24</div>
      <div class="stat-label">역세권 안내</div>
    </div>
    <div class="stat">
      <div class="stat-number">24H</div>
      <div class="stat-label">상담 가능</div>
    </div>
  </div>
</div>"""

PAGE = {
    "path": "",
    "title": "용인 출장마사지｜수지·기흥·처인 홈타이 지역 안내",
    "desc": DESC,
    "h1": "용인 출장마사지·홈타이 지역별 예약 안내",
    "hero": _HERO,
    "breadcrumb": [],
    "extra_head": _EXTRA_HEAD,
    "body": """
<section id="criteria">
  <h2>용인에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
  <p>용인시는 경기도 중부에 위치한 광역 도시로, 처인구, 기흥구, 수지구 세 개 구로 나뉘며 각 구의 생활권이 뚜렷하게 구분됩니다. 출장마사지를 예약하기 전에 자신의 위치가 어느 구의 어느 생활권에 해당하는지 정확히 파악하는 것이 예약 과정에서 가장 중요한 첫 번째 단계입니다.</p>
  <p>수지구는 신분당선과 주거 생활권을 중심으로 구성되어 있습니다. 수지구청역, 죽전역, 동천역, 성복역, 상현역, 풍덕천동, 신봉동, 죽전동, 동천동, 상현동, 성복동 중심으로 신주거지와 역세권이 밀접하게 연결되어 있습니다. 이곳은 분당신도시와 인접한 신흥 주거 지역으로, 교통 접근성이 매우 우수합니다. 수지구 지역으로 예약 시에는 신분당선 역의 접근성과 오피스텔·아파트 기반의 주거 환경을 고려하는 것이 중요합니다.</p>
  <p>기흥구는 수인분당선과 에버라인이 만나는 역세권 중심의 생활권입니다. 기흥역, 동백역, 구성역, 보정역, 신갈역, 구갈동, 신갈동, 동백동, 보정동, 구성동, 마북동 중심으로 구성되어 있습니다. 이곳은 주로 용인시의 중앙과 남부 생활권으로 알려져 있으며, 여러 환승역을 중심으로 광역 교통이 발달해 있습니다. 기흥구 지역으로 예약 시에는 각 역의 환승 연결성과 지역별 특성을 확인하는 것이 중요합니다.</p>
  <p>처인구는 에버라인과 차량 이동을 중심으로 하는 광역 생활권입니다. 역북동, 김량장역, 용인중앙시장역, 삼가동, 삼가역, 포곡읍, 양지읍, 남사읍, 이동읍, 원삼면, 백암면 중심으로 구성되어 있습니다. 이곳은 용인의 원도심과 외곽 차량 이동권을 중심으로 하므로, 차량 이동 기준과 추가 이동비를 사전에 확인하는 것이 필수입니다. 또한 에버랜드 인접 지역의 경우 관광객 방문객들을 위한 특별한 예약 기준이 있을 수 있습니다.</p>
  <p>용인시 전역으로 방문이 가능하며, 자택·숙소·오피스텔 등 다양한 방문 장소에 대응합니다. 예약 전에 자신의 주소가 어느 동에 해당하고, 가장 가까운 지하철역이 무엇인지, 그리고 기본 이동권 범위 내에 있는지를 사전에 확인하면 예약 과정이 훨씬 원활해집니다.</p>
</section>

<section id="coverage">
  <h2>처인구·기흥구·수지구 생활권 차이</h2>
  <div class="card-grid">
    <a href="/cheoin-gu/" class="card">
      <h3>처인구</h3>
      <p>역북, 김량장, 삼가, 포곡, 양지, 남사, 백암 중심 차량 이동 생활권</p>
      <span class="card-arrow">→</span>
    </a>
    <a href="/giheung-gu/" class="card">
      <h3>기흥구</h3>
      <p>기흥역, 신갈, 구갈, 동백, 보정, 구성, 마북 중심 역세권·주거 생활권</p>
      <span class="card-arrow">→</span>
    </a>
    <a href="/suji-gu/" class="card">
      <h3>수지구</h3>
      <p>수지구청, 죽전, 동천, 성복, 상현, 신봉 중심 신분당선·주거 생활권</p>
      <span class="card-arrow">→</span>
    </a>
  </div>
</section>

<section id="areas">
  <h2>용인 대표 지역별 방문 가능 지역 안내</h2>
  <div class="card-grid">
    <a href="/suji-gu/pungdeokcheon-dong/" class="card">
      <h3>풍덕천동</h3>
      <p>수지구청역, 신봉동, 성복동 중심 생활권</p>
    </a>
    <a href="/suji-gu/jukjeon-dong/" class="card">
      <h3>죽전동</h3>
      <p>죽전역, 보정역, 분당 인접 생활권</p>
    </a>
    <a href="/suji-gu/dongcheon-dong/" class="card">
      <h3>동천동</h3>
      <p>동천역, 고기동, 수지 북부 생활권</p>
    </a>
    <a href="/suji-gu/seongbok-dong/" class="card">
      <h3>성복동</h3>
      <p>성복역, 신봉동, 수지구청 인접 생활권</p>
    </a>
    <a href="/suji-gu/sanghyeon-dong/" class="card">
      <h3>상현동</h3>
      <p>상현역, 광교 인접 생활권</p>
    </a>
    <a href="/giheung-gu/singal-dong/" class="card">
      <h3>신갈동</h3>
      <p>신갈역, 기흥역, 강남대역 인접 생활권</p>
    </a>
    <a href="/giheung-gu/gugal-dong/" class="card">
      <h3>구갈동</h3>
      <p>기흥역, 강남대역, 신갈 인접 생활권</p>
    </a>
    <a href="/giheung-gu/dongbaek-dong/" class="card">
      <h3>동백동</h3>
      <p>동백역, 어정역, 초당역 인접 생활권</p>
    </a>
    <a href="/giheung-gu/bojeong-dong/" class="card">
      <h3>보정동</h3>
      <p>보정역, 죽전 인접 생활권</p>
    </a>
    <a href="/cheoin-gu/yeokbuk-dong/" class="card">
      <h3>역북동</h3>
      <p>명지대역, 김량장, 용인 원도심 인접 생활권</p>
    </a>
    <a href="/cheoin-gu/samga-dong/" class="card">
      <h3>삼가동</h3>
      <p>용인시청, 삼가역 생활권</p>
    </a>
    <a href="/cheoin-gu/pogok-eup/" class="card">
      <h3>포곡읍</h3>
      <p>둔전역, 전대·에버랜드역, 에버랜드 인접 생활권</p>
    </a>
  </div>
</section>

<section id="stations">
  <h2>용인 주요 지하철역별 홈타이 안내</h2>
  <p>용인시의 주요 지하철역별로 인접한 지역과 예약 기준을 안내합니다. 각 역을 클릭하여 상세 정보를 확인하세요.</p>
  <div class="card-grid">
    <a href="/station/suji-gu-office-station/" class="card">
      <h3>수지구청역</h3>
      <p>풍덕천동, 신봉동, 성복동 인접 생활권입니다.</p>
    </a>
    <a href="/station/jukjeon-station/" class="card">
      <h3>죽전역</h3>
      <p>죽전동, 보정동, 분당 인접 생활권입니다.</p>
    </a>
    <a href="/station/dongcheon-station/" class="card">
      <h3>동천역</h3>
      <p>동천동, 고기동, 수지 북부 생활권입니다.</p>
    </a>
    <a href="/station/seongbok-station/" class="card">
      <h3>성복역</h3>
      <p>성복동, 신봉동, 풍덕천 인접 생활권입니다.</p>
    </a>
    <a href="/station/sanghyeon-station/" class="card">
      <h3>상현역</h3>
      <p>상현동, 광교 인접 생활권입니다.</p>
    </a>
    <a href="/station/giheung-station/" class="card">
      <h3>기흥역</h3>
      <p>구갈동, 신갈동, 강남대역 인접 생활권입니다.</p>
    </a>
    <a href="/station/dongbaek-station/" class="card">
      <h3>동백역</h3>
      <p>동백동, 어정역, 초당역 인접 생활권입니다.</p>
    </a>
    <a href="/station/guseong-station/" class="card">
      <h3>구성역</h3>
      <p>구성동, 마북동 인접 생활권입니다.</p>
    </a>
  </div>
</section>

<section id="lifestyle">
  <h2>용인 생활권별 예약 기준</h2>
  <p>지역과 역을 연결한 생활권 기준으로 예약하면 더 정확한 방문 주소와 이동 시간을 확인할 수 있습니다.</p>
  <div class="card-grid">
    <a href="/area/suji-gu-office-pungdeokcheon/" class="card">수지구청·풍덕천</a>
    <a href="/area/jukjeon-bojeong/" class="card">죽전·보정</a>
    <a href="/area/dongcheon-gogi/" class="card">동천·고기동</a>
    <a href="/area/giheung-gugal/" class="card">기흥역·구갈</a>
  </div>
</section>

<section id="check">
  <h2>용인 홈타이 예약 전 확인사항</h2>
  <p>예약을 진행하기 전에 다음 항목들을 먼저 확인하면 예약 과정이 훨씬 수월합니다.</p>
  <ul>
    <li><strong>방문 가능 주소 확인</strong> - 자택, 숙소, 오피스텔 등 정확한 방문 주소와 건물 유형 확인</li>
    <li><strong>예약 가능 시간 확인</strong> - 희망 예약 시간이 가능한지 미리 확인</li>
    <li><strong>추가 이동비 여부 확인</strong> - 기본 이동권 외 추가 이동비 발생 여부</li>
    <li><strong>건물 출입 방식 확인</strong> - 공동현관, 자동문, 경비 확인 등</li>
    <li><strong>자택·숙소·오피스텔 이용 기준 확인</strong> - 서비스 제공 장소 기준</li>
    <li><strong>결제 방식 확인</strong> - 현금, 계좌이체, 카드 등 가능한 결제 수단</li>
    <li><strong>예약 변경·취소 기준 확인</strong> - 변경·취소 수수료 및 절차</li>
    <li><strong>개인정보 처리 기준 확인</strong> - 개인정보 수집·이용·보관 방식</li>
    <li><strong>불법·선정적 서비스 불가 안내</strong> - 건전한 관리 서비스만 제공</li>
  </ul>
</section>

<section id="pricing">
  <h2>기본 요금 안내</h2>
  <p>관리 시간(60·90·120분)을 기준으로 정리한 기본 금액입니다. 표시되지 않은 별도 비용은 두지 않는 것을 원칙으로 안내합니다.</p>
  <div class="card-grid">
    <div class="card">
      <h3>60분 코스</h3>
      <p class="price-amount">90,000원</p>
      <p>핵심 부위 위주 가벼운 이완</p>
      <a href="tel:0508-202-4719" class="btn btn-secondary">예약 문의</a>
    </div>
    <div class="card card-featured">
      <span class="badge">추천</span>
      <h3>90분 코스</h3>
      <p class="price-amount">150,000원</p>
      <p>전신 균형 표준 구성·아로마 포함</p>
      <a href="tel:0508-202-4719" class="btn btn-primary">예약 문의</a>
    </div>
    <div class="card">
      <h3>120분 코스</h3>
      <p class="price-amount">180,000원</p>
      <p>구석구석 집중하는 프리미엄 구성</p>
      <a href="tel:0508-202-4719" class="btn btn-secondary">예약 문의</a>
    </div>
  </div>
  <p>방문 지역과 시간대, 이동 거리에 따라 최종 금액은 통화 시 확정됩니다. <a href="/reservation/">요금·예약 기준 자세히 보기 →</a></p>
</section>

<section id="faq">
  <h2>용인 출장마사지 자주 묻는 질문</h2>
  <dl class="faq-list">
    <dt id="faq-1">용인 출장마사지는 어떤 서비스인가요?</dt>
    <dd>방문형 마사지 서비스로, 고객의 자택, 숙소, 오피스텔 등으로 전문가가 방문하여 관리하는 서비스입니다. 처인구, 기흥구, 수지구 전지역으로 방문 가능합니다.</dd>

    <dt id="faq-2">처인구, 기흥구, 수지구의 생활권 차이가 뭔가요?</dt>
    <dd>수지구는 신분당선 중심의 신주거 생활권, 기흥구는 수인분당선·에버라인 중심의 역세권 생활권, 처인구는 에버라인과 차량 이동 중심의 광역 생활권입니다.</dd>

    <dt id="faq-3">예약 전 꼭 확인해야 할 사항은?</dt>
    <dd>방문 가능 주소, 예약 가능 시간, 추가 이동비 여부, 건물 출입 방식, 결제 방식을 먼저 확인하고 예약하는 방식이 좋습니다.</dd>

    <dt id="faq-4">수지구 죽전동과 죽전역은 어떻게 다른가요?</dt>
    <dd>죽전동은 수지구 중심 주거지를 중심으로, 죽전역은 분당선 환승역 중심의 이동 기준으로 구성됩니다.</dd>

    <dt id="faq-5">추가 이동비는 어떻게 계산되나요?</dt>
    <dd>지역별로 기본 이동권이 정해져 있으며, 그 외 먼 거리는 추가 이동비가 발생할 수 있습니다. 예약 시 정확히 확인하세요.</dd>
  </dl>
</section>
"""
}
