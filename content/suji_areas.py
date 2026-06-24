# 용인시 수지구 6개 지역별 페이지 콘텐츠

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

# ===== 수지구 6개 지역 =====

# 수지구: 풍덕천동 (수지구청역, 신봉동 인접)
pungdeokcheon_dong = create_area_page(
    path="suji-gu/pungdeokcheon-dong/",
    title="풍덕천동 출장마사지｜수지구청역 신봉동인접 생활권 홈타이 안내",
    desc="용인시 수지구 풍덕천동 출장마사지·홈타이 예약 전 수지구청역, 신봉동 인접 생활권을 확인하세요.",
    h1="수지구 풍덕천동 출장마사지",
    breadcrumb=[("용인", "/"), ("수지구", "/suji-gu/"), ("풍덕천동", "")],
    body_content="""<section>
<h2>풍덕천동 소개</h2>
<p>용인시 수지구 풍덕천동은 <a href="/station/suji-gu-office-station/">수지구청역</a>을 중심으로 한 수지구의 중심 생활권입니다. 신분당선 수지구청역은 광역 접근성이 뛰어나며(강남역까지 약 30분), 수지구청, 관공서 등 행정 시설이 밀집했습니다. 신봉동과 인접하여 신봉동의 신분당선 상현역도 접근 가능합니다. 중규모 아파트 단지, 오피스텔, 상업시설이 있습니다.</p>
<p>풍덕천동은 수지구의 북쪽 교통 거점으로, 행정·상업 중심 기능이 있습니다.</p>
</section>

<section>
<h2>풍덕천동의 지리적 특성</h2>
<p>신분당선 수지구청역을 중심으로 발달한 지역입니다. 수지구청, 관공서, 은행, 병원 등 공공·상업 시설이 집중되어 있으며, 수지구의 행정 거점입니다. 신분당선으로 강남역(약 30분), 강남대역(약 10분) 접근이 가능합니다. 신봉동의 상현역도 버스로 10분 거리입니다.</p>
<ul>
<li><strong>주요 역</strong>: <a href="/station/suji-gu-office-station/">신분당선 수지구청역</a></li>
<li><strong>광역 접근</strong>: 강남역(약 30분), 강남대역(약 10분)</li>
<li><strong>행정 시설</strong>: 수지구청, 관공서</li>
<li><strong>인접 지역</strong>: <a href="/suji-gu/shinbong-dong/">신봉동</a>(남쪽), <a href="/suji-gu/dongcheon-dong/">동천동</a>(동쪽)</li>
<li><strong>특징</strong>: 신분당선 역세권, 행정 중심</li>
</ul>
</section>

<section>
<h2>생활권 특성</h2>
<p>풍덕천동은 행정 거점 + 주거 혼합 생활권입니다. 공무원, 관련 업체 근무자, 지역 주민이 함께합니다. 30~50대 가족층이 주거하며, 평일 낮 공무원 출퇴근 피크, 저녁 직장인 퇴근, 주말 가족 활동이 특징입니다. 출장마사지는 평일 저녁, 주말 오후가 중심입니다.</p>
</section>

<section>
<h2>예약 전 확인사항</h2>
<ul>
<li><strong>건물 유형</strong>: 중규모 아파트, 오피스텔, 상업용 건물</li>
<li><strong>아파트 단지</strong>: 정확한 단지명, 동호수 필수</li>
<li><strong>행정 시설 근처</strong>: 공공 시설 인근으로 정확한 주소 중요</li>
<li><strong>신분당선 역세권</strong>: 광역 접근성 우수</li>
<li><strong>시간대</strong>: 평일 저녁(퇴근 후), 주말 오후</li>
<li><strong>주차</strong>: 아파트·상업시설 주차 여건 다름</li>
<li><strong>교통</strong>: 신분당선으로 광역 접근 가능</li>
</ul>
</section>

<section>
<h2>인접 지역·역 안내</h2>
<ul>
<li><a href="/suji-gu/shinbong-dong/">신봉동</a> — 상현역, 신분당선 기반</li>
<li><a href="/suji-gu/dongcheon-dong/">동천동</a> — 동천역, 수지 북부</li>
<li><a href="/station/suji-gu-office-station/">수지구청역</a> — 신분당선 중심</li>
<li><a href="/station/sangbuk-station/">상현역</a> — 신봉동 경계, 버스 10분</li>
</ul>
</section>

<section class="pricing">
<h2>기본 요금 안내</h2>
<p>관리 시간(60·90·120분)을 기준으로 정리한 기본 금액입니다. 표시되지 않은 별도 비용은 두지 않는 것을 원칙으로 안내합니다.</p>
<ul>
<li><strong>60분 코스</strong>: 90,000원 — 핵심 부위 위주 가벼운 이완</li>
<li><strong>90분 코스 (추천)</strong>: 150,000원 — 전신 균형 표준 구성·아로마 포함</li>
<li><strong>120분 코스</strong>: 180,000원 — 구석구석 집중하는 프리미엄 구성</li>
</ul>
<p>방문 지역과 시간대, 이동 거리에 따라 최종 금액은 통화 시 확정됩니다. <a href="/reservation/">요금·예약 기준 자세히 보기 →</a></p>
<p>예약 문의: <a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>"""
)

# 수지구: 신봉동 (상현역, 신분당선 기반)
shinbong_dong = create_area_page(
    path="suji-gu/shinbong-dong/",
    title="신봉동 출장마사지｜상현역 신분당선 생활권 홈타이 안내",
    desc="용인시 수지구 신봉동 출장마사지·홈타이 예약 전 상현역, 신분당선 생활권을 확인하세요.",
    h1="수지구 신봉동 출장마사지",
    breadcrumb=[("용인", "/"), ("수지구", "/suji-gu/"), ("신봉동", "")],
    body_content="""<section>
<h2>신봉동 소개</h2>
<p>용인시 수지구 신봉동은 <a href="/station/sangbuk-station/">신분당선 상현역</a>을 중심으로 발전한 신흥 생활권입니다. 신분당선으로 강남역(약 25분), 판교역(약 15분) 등 광역 접근성이 뛰어나며, 수원 광교 신도시와도 인접합니다. 신규 아파트 단지, 오피스텔, 상업시설이 조성되고 있으며, 젊은 가족층(30~40대) 입주가 활발합니다.</p>
<p>신봉동은 신분당선 개통으로 급속히 발전하는 수지구의 신흥 생활권입니다.</p>
</section>

<section>
<h2>신봉동의 지리적 특성</h2>
<p>신분당선 상현역을 중심으로 발달하는 신규 개발 지역입니다. 상현역은 강남역(약 25분), 판교역(약 15분) 직통 접근이 가능하며, 수원 광교 방향 접근도 용이합니다. 새로운 아파트 단지, 도로 정비, 상업시설 건설이 진행 중입니다.</p>
<ul>
<li><strong>주요 역</strong>: <a href="/station/sangbuk-station/">신분당선 상현역</a></li>
<li><strong>광역 접근</strong>: 강남역(약 25분), 판교역(약 15분), 광교역(약 20분)</li>
<li><strong>신도시 연결</strong>: 수원 광교 신도시 인접</li>
<li><strong>인접 지역</strong>: <a href="/suji-gu/pungdeokcheon-dong/">풍덕천동</a>(북쪽), <a href="/suji-gu/jukjeon-dong/">죽전동</a>(서쪽)</li>
<li><strong>특징</strong>: 신분당선 역세권, 신도시 개발</li>
</ul>
</section>

<section>
<h2>생활권 특성</h2>
<p>신봉동은 신규 입주자 중심의 신흥 생활권입니다. 30대 신혼부부, 자녀 있는 4~5인 가족이 주거하며, 신축 시설로 인한 건설 활동과 정착이 진행 중입니다. 신분당선 개통으로 강남, 판교 직장 출퇴근자 수요가 증가하고 있으며, 저녁~야간 직장인 중심 예약과 주말 가족 단위 예약이 있습니다.</p>
</section>

<section>
<h2>예약 전 확인사항</h2>
<ul>
<li><strong>건물 유형</strong>: 신축 아파트(대단지), 신축 오피스텔</li>
<li><strong>신축 단지 게이트</strong>: 최신 보안 시스템, 사전 안내 필수</li>
<li><strong>아파트 단지명</strong>: 정확한 단지명, 동호수 필수</li>
<li><strong>개발 진행</strong>: 지속적인 공사로 교통 변화 가능</li>
<li><strong>시간대</strong>: 저녁 퇴근 후(오후 6시~), 주말 예약 많음</li>
<li><strong>주차</strong>: 신축 단지이나 초기 주차 부족 가능</li>
<li><strong>광역 수요</strong>: 신분당선으로 인한 광역 예약 증가</li>
<li><strong>엘리베이터</strong>: 신축이라 최신 시설</li>
</ul>
</section>

<section>
<h2>인접 지역·역 안내</h2>
<ul>
<li><a href="/suji-gu/pungdeokcheon-dong/">풍덕천동</a> — 수지구청역</li>
<li><a href="/suji-gu/jukjeon-dong/">죽전동</a> — 죽전역, 분당 인접</li>
<li><a href="/station/sangbuk-station/">상현역</a> — 신분당선 중심</li>
</ul>
</section>

<section class="pricing">
<h2>기본 요금 안내</h2>
<p>관리 시간(60·90·120분)을 기준으로 정리한 기본 금액입니다. 표시되지 않은 별도 비용은 두지 않는 것을 원칙으로 안내합니다.</p>
<ul>
<li><strong>60분 코스</strong>: 90,000원 — 핵심 부위 위주 가벼운 이완</li>
<li><strong>90분 코스 (추천)</strong>: 150,000원 — 전신 균형 표준 구성·아로마 포함</li>
<li><strong>120분 코스</strong>: 180,000원 — 구석구석 집중하는 프리미엄 구성</li>
</ul>
<p>방문 지역과 시간대, 이동 거리에 따라 최종 금액은 통화 시 확정됩니다. <a href="/reservation/">요금·예약 기준 자세히 보기 →</a></p>
<p>예약 문의: <a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>"""
)

# 수지구: 죽전동 (죽전역 중심, 분당 인접)
jukjeon_dong = create_area_page(
    path="suji-gu/jukjeon-dong/",
    title="죽전동 출장마사지｜죽전역 분당인접 생활권 홈타이 안내",
    desc="용인시 수지구 죽전동 출장마사지·홈타이 예약 전 죽전역, 분당 인접 생활권을 확인하세요.",
    h1="수지구 죽전동 출장마사지",
    breadcrumb=[("용인", "/"), ("수지구", "/suji-gu/"), ("죽전동", "")],
    body_content="""<section>
<h2>죽전동 소개</h2>
<p>용인시 수지구 죽전동은 <a href="/station/jukjeon-station/">죽전역</a>을 중심으로 한 분당 인접 생활권입니다. 수인분당선 죽전역으로 분당 신도시(판교역, 강남역 방향) 광역 접근성이 뛰어나며, 분당의 현대식 도시 문화가 영향을 미칩니다. 중규모 아파트 단지, 신축 오피스텔, 상업시설이 있으며, 분당의 쾌적한 생활 환경을 유지하고 있습니다.</p>
<p>죽전동은 분당과 용인을 연결하는 광역 생활권으로, 분당의 영향을 받는 수지구 최남부 지역입니다.</p>
</section>

<section>
<h2>죽전동의 지리적 특성</h2>
<p>수인분당선 죽전역을 중심으로 발달한 분당 인접 지역입니다. 죽전역은 분당 신도시의 중심 역들(판교역, 강남역 방향)로 직통 접근이 가능하며, 분당의 모든 편의시설(백화점, 쇼핑몰, 문화시설) 접근성이 뛰어납니다. 용인(기흥 보정동)과도 인접하여 광역 환승 거점입니다.</p>
<ul>
<li><strong>주요 역</strong>: <a href="/station/jukjeon-station/">수인분당선 죽전역</a></li>
<li><strong>광역 접근</strong>: 판교역(약 15분), 강남역(약 35분), 광교역(약 20분)</li>
<li><strong>분당 인접</strong>: 분당 신도시 바로 옆(도보 거리도 일부 가능)</li>
<li><strong>인접 지역</strong>: <a href="/suji-gu/sanghyun-dong/">상현동</a>(북쪽), <a href="/giheung-gu/bojeong-dong/">기흥구 보정동</a>(북쪽)</li>
<li><strong>특징</strong>: 분당 인접, 광역 역세권</li>
</ul>
</section>

<section>
<h2>생활권 특성</h2>
<p>죽전동은 분당과 용인을 연결하는 광역 생활권입니다. 분당의 영향으로 비교적 젊은 가족층(30~40대), 신혼부부가 거주합니다. 판교, 강남 직장 출퇴근자 수요가 높으며, 분당의 쾌적한 생활 환경과 문화 시설 이용이 특징입니다. 저녁~야간 직장인 중심 예약과 주중·주말 수요가 균형적입니다.</p>
</section>

<section>
<h2>예약 전 확인사항</h2>
<ul>
<li><strong>건물 유형</strong>: 중규모 아파트, 신축 오피스텔, 주택</li>
<li><strong>아파트 단지</strong>: 정확한 단지명, 동호수 필수</li>
<li><strong>분당 인접</strong>: 분당의 현대식 시설·문화 영향</li>
<li><strong>역세권 특성</strong>: 죽전역 근처, 수인분당선 광역 접근성 좋음</li>
<li><strong>광역 직장인</strong>: 판교·강남 직장 출퇴근자 많음</li>
<li><strong>시간대</strong>: 평일 저녁 퇴근 후(오후 6시~) 집중, 주중·주말 균형</li>
<li><strong>주차</strong>: 아파트·오피스텔 주차 여건 다름</li>
<li><strong>교통</strong>: 수인분당선으로 광역 접근 우수</li>
</ul>
</section>

<section>
<h2>인접 지역·역 안내</h2>
<ul>
<li><a href="/suji-gu/sanghyun-dong/">상현동</a> — 상현역, 광교 인접</li>
<li><a href="/suji-gu/shinbong-dong/">신봉동</a> — 상현역, 신분당선</li>
<li><a href="/giheung-gu/bojeong-dong/">기흥구 보정동</a> — 기흥 생활권</li>
<li><a href="/station/jukjeon-station/">죽전역</a> — 수인분당선 중심</li>
</ul>
</section>

<section class="pricing">
<h2>기본 요금 안내</h2>
<p>관리 시간(60·90·120분)을 기준으로 정리한 기본 금액입니다. 표시되지 않은 별도 비용은 두지 않는 것을 원칙으로 안내합니다.</p>
<ul>
<li><strong>60분 코스</strong>: 90,000원 — 핵심 부위 위주 가벼운 이완</li>
<li><strong>90분 코스 (추천)</strong>: 150,000원 — 전신 균형 표준 구성·아로마 포함</li>
<li><strong>120분 코스</strong>: 180,000원 — 구석구석 집중하는 프리미엄 구성</li>
</ul>
<p>방문 지역과 시간대, 이동 거리에 따라 최종 금액은 통화 시 확정됩니다. <a href="/reservation/">요금·예약 기준 자세히 보기 →</a></p>
<p>예약 문의: <a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>"""
)

# 수지구: 동천동 (동천역, 수지 북부)
dongcheon_dong = create_area_page(
    path="suji-gu/dongcheon-dong/",
    title="동천동 출장마사지｜동천역 수지북부 생활권 홈타이 안내",
    desc="용인시 수지구 동천동 출장마사지·홈타이 예약 전 동천역, 수지 북부 생활권을 확인하세요.",
    h1="수지구 동천동 출장마사지",
    breadcrumb=[("용인", "/"), ("수지구", "/suji-gu/"), ("동천동", "")],
    body_content="""<section>
<h2>동천동 소개</h2>
<p>용인시 수지구 동천동은 <a href="/station/dongcheon-station/">동천역</a>을 중심으로 한 수지구의 북부 생활권입니다. 신분당선 동천역으로 강남역(약 40분) 접근이 가능하며, 수지구 북부 주거 지역의 중심입니다. 중규모 아파트 단지, 주택가, 지역 상업시설이 있으며, 가족 단위 거주자가 많습니다.</p>
<p>동천동은 수지구 북부 조용한 주거 생활권입니다.</p>
</section>

<section>
<h2>동천동의 지리적 특성</h2>
<p>신분당선 동천역을 중심으로 발달한 주거 지역입니다. 동천역은 강남역 직통 접근(약 40분)으로 광역 역세권이지만, 상대적으로 조용한 주거 환경을 유지하고 있습니다. 풍덕천동, 신봉동 같은 번화한 지역과 달리 주거 중심입니다.</p>
<ul>
<li><strong>주요 역</strong>: <a href="/station/dongcheon-station/">신분당선 동천역</a></li>
<li><strong>광역 접근</strong>: 강남역(약 40분)</li>
<li><strong>인접 지역</strong>: <a href="/suji-gu/pungdeokcheon-dong/">풍덕천동</a>(서쪽), <a href="/suji-gu/sanghyun-dong/">상현동</a>(남쪽)</li>
<li><strong>특징</strong>: 주거 중심, 신분당선 역세권</li>
</ul>
</section>

<section>
<h2>생활권 특성</h2>
<p>동천동은 조용한 주거 생활권입니다. 30~50대 가족층이 주거하며, 아이 있는 가정이 많습니다. 평일 낮 주부·유아동, 저녁 직장인 퇴근, 주말 가족 활동이 특징입니다. 출장마사지는 평일 낮, 저녁, 주말 오후가 중심입니다.</p>
</section>

<section>
<h2>예약 전 확인사항</h2>
<ul>
<li><strong>건물 유형</strong>: 중규모 아파트, 주택, 소규모 상가</li>
<li><strong>아파트 단지</strong>: 정확한 단지명, 동호수 필수</li>
<li><strong>주거지역 특성</strong>: 조용한 환경, 소음 관리 중요</li>
<li><strong>신분당선 역세권</strong>: 광역 접근성 있으나 주거 중심</li>
<li><strong>시간대</strong>: 평일 낮, 저녁, 주말 오후</li>
<li><strong>주차</strong>: 아파트·주택 주차 여건 다름</li>
<li><strong>교통</strong>: 신분당선으로 광역 접근 가능</li>
</ul>
</section>

<section>
<h2>인접 지역·역 안내</h2>
<ul>
<li><a href="/suji-gu/pungdeokcheon-dong/">풍덕천동</a> — 수지구청역</li>
<li><a href="/suji-gu/sanghyun-dong/">상현동</a> — 상현역, 광교 인접</li>
<li><a href="/station/dongcheon-station/">동천역</a> — 신분당선 중심</li>
</ul>
</section>

<section class="pricing">
<h2>기본 요금 안내</h2>
<p>관리 시간(60·90·120분)을 기준으로 정리한 기본 금액입니다. 표시되지 않은 별도 비용은 두지 않는 것을 원칙으로 안내합니다.</p>
<ul>
<li><strong>60분 코스</strong>: 90,000원 — 핵심 부위 위주 가벼운 이완</li>
<li><strong>90분 코스 (추천)</strong>: 150,000원 — 전신 균형 표준 구성·아로마 포함</li>
<li><strong>120분 코스</strong>: 180,000원 — 구석구석 집중하는 프리미엄 구성</li>
</ul>
<p>방문 지역과 시간대, 이동 거리에 따라 최종 금액은 통화 시 확정됩니다. <a href="/reservation/">요금·예약 기준 자세히 보기 →</a></p>
<p>예약 문의: <a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>"""
)

# 수지구: 상현동 (상현역, 광교 인접)
sanghyun_dong = create_area_page(
    path="suji-gu/sanghyun-dong/",
    title="상현동 출장마사지｜상현역 광교인접 생활권 홈타이 안내",
    desc="용인시 수지구 상현동 출장마사지·홈타이 예약 전 상현역, 광교 인접 생활권을 확인하세요.",
    h1="수지구 상현동 출장마사지",
    breadcrumb=[("용인", "/"), ("수지구", "/suji-gu/"), ("상현동", "")],
    body_content="""<section>
<h2>상현동 소개</h2>
<p>용인시 수지구 상현동은 <a href="/station/sangbuk-station/">상현역</a>을 중심으로 한 신분당선 역세권 생활권입니다. 신분당선으로 강남역(약 25분), 판교역(약 15분) 광역 접근성이 뛰어나며, 수원 광교 신도시와도 인접합니다. 신규 아파트 단지, 오피스텔, 신분당선 기반 상업시설이 있으며, 신봉동과 함께 수지구의 신흥 생활권입니다.</p>
<p>상현동은 광교와 용인을 연결하는 신분당선 역세권 생활권입니다.</p>
</section>

<section>
<h2>상현동의 지리적 특성</h2>
<p>신분당선 상현역을 중심으로 발달한 광역 역세권 지역입니다. 상현역에서 강남역(약 25분), 판교역(약 15분) 직통 접근이 가능하며, 수원 광교 신도시(도보 거리)와도 인접합니다. 신분당선과 광교-용인 간 버스 연결로 광역 이동이 활발합니다.</p>
<ul>
<li><strong>주요 역</strong>: <a href="/station/sangbuk-station/">신분당선 상현역</a></li>
<li><strong>광역 접근</strong>: 강남역(약 25분), 판교역(약 15분), 광교역(약 5분 버스)</li>
<li><strong>광교 신도시 인접</strong>: 도보 거리, 광교 문화·상업시설 이용</li>
<li><strong>인접 지역</strong>: <a href="/suji-gu/shinbong-dong/">신봉동</a>(북쪽), <a href="/suji-gu/jukjeon-dong/">죽전동</a>(남쪽), <a href="/suji-gu/seongbok-dong/">성복동</a>(동쪽)</li>
<li><strong>특징</strong>: 신분당선 역세권, 광교 신도시 인접</li>
</ul>
</section>

<section>
<h2>생활권 특성</h2>
<p>상현동은 광역 역세권 + 광교 신도시 영향의 신흥 생활권입니다. 30~40대 젊은 가족층, 신혼부부가 거주하며, 강남, 판교, 광교 직장 출퇴근자 수요가 높습니다. 광교 신도시의 쾌적한 생활 환경 영향으로 비교적 높은 생활수준을 유지합니다. 저녁~야간 직장인 중심 예약과 주말 가족 단위 예약이 있습니다.</p>
</section>

<section>
<h2>예약 전 확인사항</h2>
<ul>
<li><strong>건물 유형</strong>: 신규 아파트, 신축 오피스텔, 주택</li>
<li><strong>아파트 단지</strong>: 정확한 단지명, 동호수 필수</li>
<li><strong>신분당선 역세권</strong>: 광역 접근성 우수, 개발 진행 중</li>
<li><strong>광교 인접</strong>: 광교 시설 영향, 광교 거주자도 이용 가능</li>
<li><strong>광역 직장인</strong>: 강남·판교·광교 직장 출퇴근자 많음</li>
<li><strong>시간대</strong>: 평일 저녁 퇴근 후(오후 6시~) 집중</li>
<li><strong>주차</strong>: 아파트·오피스텔 주차 여건 다름</li>
<li><strong>교통</strong>: 신분당선, 광교 버스 모두 이용 가능</li>
</ul>
</section>

<section>
<h2>인접 지역·역 안내</h2>
<ul>
<li><a href="/suji-gu/shinbong-dong/">신봉동</a> — 상현역, 신분당선</li>
<li><a href="/suji-gu/jukjeon-dong/">죽전동</a> — 죽전역, 분당 인접</li>
<li><a href="/suji-gu/seongbok-dong/">성복동</a> — 성복역, 신분당선</li>
<li><a href="/station/sangbuk-station/">상현역</a> — 신분당선 중심</li>
</ul>
</section>

<section class="pricing">
<h2>기본 요금 안내</h2>
<p>관리 시간(60·90·120분)을 기준으로 정리한 기본 금액입니다. 표시되지 않은 별도 비용은 두지 않는 것을 원칙으로 안내합니다.</p>
<ul>
<li><strong>60분 코스</strong>: 90,000원 — 핵심 부위 위주 가벼운 이완</li>
<li><strong>90분 코스 (추천)</strong>: 150,000원 — 전신 균형 표준 구성·아로마 포함</li>
<li><strong>120분 코스</strong>: 180,000원 — 구석구석 집중하는 프리미엄 구성</li>
</ul>
<p>방문 지역과 시간대, 이동 거리에 따라 최종 금액은 통화 시 확정됩니다. <a href="/reservation/">요금·예약 기준 자세히 보기 →</a></p>
<p>예약 문의: <a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>"""
)

# 수지구: 성복동 (성복역, 신분당선 중심)
seongbok_dong = create_area_page(
    path="suji-gu/seongbok-dong/",
    title="성복동 출장마사지｜성복역 신분당선 생활권 홈타이 안내",
    desc="용인시 수지구 성복동 출장마사지·홈타이 예약 전 성복역, 신분당선 생활권을 확인하세요.",
    h1="수지구 성복동 출장마사지",
    breadcrumb=[("용인", "/"), ("수지구", "/suji-gu/"), ("성복동", "")],
    body_content="""<section>
<h2>성복동 소개</h2>
<p>용인시 수지구 성복동은 <a href="/station/seongbok-station/">성복역</a>을 중심으로 한 신분당선 역세권 생활권입니다. 신분당선으로 강남역(약 20분), 판교역(약 10분) 광역 접근성이 뛰어나며, 광교 신도시(버스 연결)와도 인접합니다. 신규 아파트 단지, 오피스텔, 신분당선 기반 상업시설이 있으며, 수지구의 남부 신흥 생활권입니다.</p>
<p>성복동은 신분당선 개통으로 급속히 발전하는 수지구의 신흥 역세권 생활권입니다.</p>
</section>

<section>
<h2>성복동의 지리적 특성</h2>
<p>신분당선 성복역을 중심으로 발달한 광역 역세권 지역입니다. 성복역에서 강남역(약 20분), 판교역(약 10분) 직통 접근이 가능하며, 신분당선 중에서도 강남 접근성이 가장 뛰어난 역들 중 하나입니다. 광교 신도시(버스 연결)와도 인접하여 광교 문화·상업시설 이용이 가능합니다.</p>
<ul>
<li><strong>주요 역</strong>: <a href="/station/seongbok-station/">신분당선 성복역</a></li>
<li><strong>광역 접근</strong>: 강남역(약 20분), 판교역(약 10분), 광교역(버스 연결)</li>
<li><strong>광교 신도시 인접</strong>: 버스 연결, 광교 시설 이용 가능</li>
<li><strong>인접 지역</strong>: <a href="/suji-gu/sanghyun-dong/">상현동</a>(북쪽), 광교 신도시(남쪽)</li>
<li><strong>특징</strong>: 신분당선 역세권, 광교 인접</li>
</ul>
</section>

<section>
<h2>생활권 특성</h2>
<p>성복동은 신분당선 중심의 신흥 역세권 생활권입니다. 30~40대 젊은 가족층, 신혼부부, 광교 신도시 주민도 이용하는 지역입니다. 강남, 판교 직장 출퇴근자 수요가 높으며, 신분당선의 강남 접근성이 뛰어나 서울 광역 수요도 있습니다. 저녁~야간 직장인 중심 예약과 주중·주말 균형적 수요가 특징입니다.</p>
</section>

<section>
<h2>예약 전 확인사항</h2>
<ul>
<li><strong>건물 유형</strong>: 신규 아파트, 신축 오피스텔, 주택</li>
<li><strong>아파트 단지</strong>: 정확한 단지명, 동호수 필수</li>
<li><strong>신분당선 역세권</strong>: 광역 접근성 우수</li>
<li><strong>광교 인접</strong>: 광교 신도시 주민도 이용</li>
<li><strong>광역 직장인</strong>: 강남·판교 직장 출퇴근자 많음</li>
<li><strong>시간대</strong>: 평일 저녁 퇴근 후(오후 6시~) 집중, 주중·주말 균형</li>
<li><strong>주차</strong>: 아파트·오피스텔 주차 여건 다름</li>
<li><strong>교통</strong>: 신분당선으로 광역 접근 우수</li>
</ul>
</section>

<section>
<h2>인접 지역·역 안내</h2>
<ul>
<li><a href="/suji-gu/sanghyun-dong/">상현동</a> — 상현역, 광교 인접</li>
<li><a href="/suji-gu/jukjeon-dong/">죽전동</a> — 분당 인접</li>
<li><a href="/station/seongbok-station/">성복역</a> — 신분당선 중심</li>
</ul>
</section>

<section class="pricing">
<h2>기본 요금 안내</h2>
<p>관리 시간(60·90·120분)을 기준으로 정리한 기본 금액입니다. 표시되지 않은 별도 비용은 두지 않는 것을 원칙으로 안내합니다.</p>
<ul>
<li><strong>60분 코스</strong>: 90,000원 — 핵심 부위 위주 가벼운 이완</li>
<li><strong>90분 코스 (추천)</strong>: 150,000원 — 전신 균형 표준 구성·아로마 포함</li>
<li><strong>120분 코스</strong>: 180,000원 — 구석구석 집중하는 프리미엄 구성</li>
</ul>
<p>방문 지역과 시간대, 이동 거리에 따라 최종 금액은 통화 시 확정됩니다. <a href="/reservation/">요금·예약 기준 자세히 보기 →</a></p>
<p>예약 문의: <a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>"""
)

PAGES = [
    pungdeokcheon_dong,
    shinbong_dong,
    jukjeon_dong,
    dongcheon_dong,
    sanghyun_dong,
    seongbok_dong,
]
