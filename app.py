import streamlit as st
import random


# 페이지 설정
st.set_page_config(
    page_title="여가 활동 추천 서비스",
    page_icon="🎭"
)


# 제목
st.title("🎭 여가 활동 추천 서비스")

st.write("""
나이, 비용, 선호하는 여가 카테고리를 기반으로  
맞춤형 문화·예술·여가 활동을 추천해드립니다.
""")


# 연령대 분류 함수
def classify_age(age):

    if 3 <= age <= 11:
        return "아동"

    elif 12 <= age <= 18:
        return "청소년"

    elif 19 <= age <= 34:
        return "청년"

    elif 35 <= age <= 64:
        return "성인"

    else:
        return "노인"


# 활동 데이터
activities = [

    {
        "name": "경기도 어린이박물관",

        "age_group": ["아동","청소년","청년","성인","노인"],

        "recommended_age": ["아동","성인","노인"],

        "income_by_age": {
            "default": "비용 부담 없이 즐기고 싶어요"
        },

        "category": ["전시 문화유산 관람"],

        "link": "https://gmuseum.kr/reg/regView?category=all&id=60",

        "description": """
어린이와 가족이 함께 즐길 수 있는 체험형 박물관으로,
놀이와 전시를 통해 다양한 문화·예술·과학 활동을 경험할 수 있습니다.

체험 중심 전시가 많아 아동에게 특히 적합하며,
보호자와 함께하는 가족 단위 관람객에게도 추천됩니다.
비교적 부담 없는 비용으로 문화 체험을 즐길 수 있습니다.
"""
    },

    {
        "name": "DDP 전시 관람",

        "age_group": ["아동","청소년","청년","성인","노인"],

        "recommended_age": [],

        "income_by_age": {
            "default": "비용은 크게 상관 없어요"
        },

        "category": ["전시 문화유산 관람"],

        "link": "https://ddp.or.kr/index.html?menuno=240",

        "description": """
동대문디자인플라자(DDP)는 디자인, 예술, 패션 분야의
다양한 전시와 문화행사가 열리는 복합문화공간입니다.

현대적인 전시와 트렌디한 문화 콘텐츠를 경험할 수 있어
청소년과 청년층에게 특히 인기가 많으며,
다양한 특별 전시와 야간 프로그램도 운영됩니다.
"""
    },

    {
        "name": "대학로 연극 공연 관람",

        "age_group": ["아동","청소년","청년","성인","노인"],

        "recommended_age": ["청소년","청년","성인"],

        "income_by_age": {
            "default": "비용은 크게 상관 없어요"
        },

        "category": ["공연 연극 관람"],

        "link": "https://timeticket.co.kr/",

        "description": """
대학로는 다양한 연극과 소극장 공연이 활발하게 운영되는
서울 대표 공연예술 거리입니다.

코미디, 드라마, 창작극 등 다양한 장르를 즐길 수 있으며,
청소년·청년·성인 관람객에게 특히 적합합니다.
학생 할인이나 조기 예매 할인 등이 제공되는 공연도 많습니다.
"""
    },

    {
        "name": "아르코예술극장 연극",

        "age_group": ["아동","청소년","청년","성인","노인"],

        "recommended_age": ["청소년","청년","성인"],

        "income_by_age": {
            "default": "비용은 크게 상관 없어요"
        },

        "category": ["공연 연극 관람"],

        "link": "https://theater.arko.or.kr/home/ko/main",

        "description": """
아르코예술극장은 창작 연극과 실험적인 공연예술 작품을
관람할 수 있는 대표적인 문화예술 공연장입니다.

다양한 현대 연극과 예술 공연을 경험할 수 있어
문화예술에 관심 있는 청소년과 청년층에게 특히 추천됩니다.
일부 공연은 청년 및 학생 할인 혜택도 제공됩니다.
"""
    },

    {
        "name": "서울 생활문화센터 체부",

        "age_group": ["아동","청소년","청년","성인","노인"],

        "recommended_age": ["청소년","청년","성인"],

        "income_by_age": {
            "default": "비용 부담 없이 즐기고 싶어요"
        },

        "category": ["문화센터"],

        "link": "https://ccasc.or.kr/",

        "description": """
시민 누구나 자유롭게 참여할 수 있는 생활문화 공간으로,
예술·공예·음악 등 다양한 문화 활동 프로그램을 운영합니다.

청소년과 성인을 위한 체험형 활동이 많으며,
지역 주민들이 취미와 문화생활을 부담 없이 즐길 수 있습니다.
대부분의 프로그램은 무료 또는 저렴한 비용으로 이용 가능합니다.
"""
    },

    {
        "name": "서울문화예술교육센터",

        "age_group": ["아동","청소년","청년","성인","노인"],

        "recommended_age": ["아동","성인","노인"],

        "income_by_age": {
            "default": "비용 부담 없이 즐기고 싶어요"
        },

        "category": ["문화센터"],

        "link": "https://www.sfac.or.kr/",

        "description": """
어린이를 포함한 가족과 시민이 함께 참여할 수 있는
시각·공연예술 중심의 다양한 예술교육 프로그램을 운영합니다.

사진 교육, 미술작품 해설 강연, 여행 드로잉 등
다양한 문화예술 체험 활동이 마련되어 있으며,
예술을 쉽고 친근하게 접하고 싶은 시민들에게 적합합니다.
"""
    },

    {
        "name": "서울형 키즈카페",

        "age_group": ["아동"],

        "recommended_age": ["아동"],

        "income_by_age": {
            "default": "비용 부담 없이 즐기고 싶어요"
        },

        "category": ["문화센터"],

        "link": "https://umppa.seoul.go.kr/icare/dolbomMENU5/dolbomMENU5_4/dolbomMENU5_4_1.jsp",

        "description": """
서울시가 운영하는 공공형 키즈카페로,
아이들이 안전하게 놀이와 체험 활동을 즐길 수 있는 실내 놀이공간입니다.

3~7세 아동에게 특히 적합하며,
미끄럼틀·블록놀이·신체활동 공간 등 다양한 놀이시설이 마련되어 있습니다.
일반 키즈카페보다 저렴한 비용으로 이용 가능해 보호자 부담도 적습니다.
"""
    },

    {
        "name": "청소년문화의집",

        "age_group": ["청소년","청년"],

        "recommended_age": ["청소년"],

        "income_by_age": {
            "default": "비용 부담 없이 즐기고 싶어요"
        },

        "category": ["문화센터"],

        "link": "https://sbyc.or.kr/",

        "description": """
청소년 중심의 문화·예술·체험 활동을 운영하는
지역 기반 청소년 수련시설입니다.

동아리 활동, 진로 체험, 문화 프로그램 등
다양한 청소년 활동에 참여할 수 있으며,
또래와의 교류와 문화 체험을 원하는 청소년에게 적합합니다.
"""
    },

    {
        "name": "서울노인복지센터",

        "age_group": ["노인"],

        "recommended_age": ["노인"],

        "income_by_age": {
            "default": "비용은 크게 상관 없어요"
        },

        "category": ["문화센터"],

        "link": "https://seoulnoin.or.kr/senior/culture4.asp",

        "description": """
노년층을 위한 문화·여가·복지 프로그램을 운영하는
대표적인 노인 복지 문화시설입니다.

문화 강좌, 건강 프로그램, 취미 활동 등
다양한 활동을 통해 활기찬 여가생활을 지원하며,
노인층이 사회적 교류를 넓히기에 적합한 공간입니다.
"""
    },

    {
        "name": "예술의전당 공연/영화 관람",

        "age_group": ["아동","청소년","청년","성인","노인"],

        "recommended_age": [],

        "income_by_age": {
            "아동": "비용 부담 없이 즐기고 싶어요",
            "청소년": "비용 부담 없이 즐기고 싶어요",
            "청년": "비용 부담 없이 즐기고 싶어요",
            "성인": "비용은 크게 상관 없어요",
            "노인": "비용 부담 없이 즐기고 싶어요"
        },

        "category": ["공연 연극 관람"],

        "link": "https://www.sac.or.kr/site/main/membership/member_step",

        "description": """
예술의전당은 공연, 연극, 영화, 클래식 등
다양한 문화예술 콘텐츠를 즐길 수 있는 대표 문화공간입니다.

수준 높은 공연과 전시를 관람할 수 있어
청년과 성인층에게 특히 추천되며,
7~24세 청소년 및 청년, 69세 이상 관람객에게는 할인 혜택이 제공됩니다.
"""
    },

    {
        "name": "서울청년문화패스",

        "age_group": ["청년"],

        "recommended_age": ["청년"],

        "income_by_age": {
            "default": "비용 부담 없이 즐기고 싶어요"
        },

        "category": ["공연 연극 관람", "전시 문화유산 관람"],

        "link": "https://www.youthcultureseoul.kr/",

        "description": """
서울에 거주하는 20~23세 청년에게
연극, 뮤지컬, 클래식, 전시 등 공연·전시 관람비를
연간 최대 20만 원까지 지원합니다.

문화생활 비용 부담을 줄이고 싶은 청년층에게 특히 적합하며,
다양한 문화예술 활동을 경험할 수 있는 대표적인 청년 지원 프로그램입니다.
"""
    },

    {
        "name": "영화관 할인",

        "age_group": ["아동","청소년","청년","성인","노인"],

        "recommended_age": [],

        "income_by_age": {
            "아동": "비용은 크게 상관 없어요",
            "청소년": "비용은 크게 상관 없어요",
            "청년": "비용은 크게 상관 없어요",
            "성인": "비용은 크게 상관 없어요",
            "노인": "비용 부담 없이 즐기고 싶어요"
        },

        "category": ["공연 연극 관람"],

        "link": "https://www.cgv.co.kr/",

        "description": """
다양한 최신 영화와 문화 콘텐츠를 관람할 수 있는
대표적인 대중 문화 여가 활동입니다.

청소년과 청년층에게 특히 인기가 많으며,
노인 관람객에게는 경로 우대 할인 혜택이 제공됩니다.
조조 할인, 학생 할인 등 다양한 할인 제도도 운영됩니다.
"""
    },

    {
        "name": "국립현대미술관",

        "age_group": ["아동","청소년","청년","성인","노인"],

        "recommended_age": [],

        "income_by_age": {
            "default": "비용 부담 없이 즐기고 싶어요"
        },

        "category": ["전시 문화유산 관람"],

        "link": "https://www.mmca.go.kr/visitingInfo/seoulInfo.do",

        "description": """
현대미술 작품과 다양한 기획 전시를 관람할 수 있는
국내 대표 현대미술 전시 공간입니다.

예술과 디자인에 관심 있는 청소년·청년층에게 특히 추천되며,
무료 전시 및 청년 대상 할인 프로그램도 운영됩니다.
다양한 교육 프로그램과 전시 해설도 함께 제공됩니다.
"""
    },

    {
        "name": "리움미술관",

        "age_group": ["아동","청소년","청년","성인","노인"],

        "recommended_age": [],

        "income_by_age": {
            "아동": "비용 부담 없이 즐기고 싶어요",
            "청소년": "비용 부담 없이 즐기고 싶어요",
            "청년": "비용은 크게 상관 없어요",
            "성인": "비용은 크게 상관 없어요",
            "노인": "비용 부담 없이 즐기고 싶어요"
        },

        "category": ["전시 문화유산 관람"],

        "link": "https://www.leeumhoam.org/",

        "description": """
전통미술과 현대미술 작품을 함께 감상할 수 있는
국내 대표 사립 미술관입니다.

다양한 국내외 예술 작품과 특별 전시를 경험할 수 있으며,
문화예술에 관심 있는 청년과 성인층에게 특히 추천됩니다.
아동·청소년·노인 대상 무료 또는 할인 혜택이 제공되는 전시도 있습니다.
"""
    },

    {
        "name": "4대궁 관람",

        "age_group": ["아동","청소년","청년","성인","노인"],

        "recommended_age": [],

        "income_by_age": {
            "default": "비용 부담 없이 즐기고 싶어요"
        },

        "category": ["전시 문화유산 관람"],

        "link": "https://royal.khs.go.kr/ROYAL/contents/R703000000.do",

        "description": """
경복궁, 창덕궁, 덕수궁, 창경궁 등
서울의 대표 궁궐과 문화유산을 관람할 수 있는 역사 문화 활동입니다.

전통 건축과 역사 문화를 직접 체험할 수 있어
전 연령층에게 추천되며,
한복 착용 시 무료 입장 등 다양한 할인 혜택도 운영됩니다.
"""
    }
]

# 사용자 입력
age = st.number_input(
    "나이를 입력하세요",
    min_value=3,
    max_value=100,
    step=1
)

age_group = classify_age(age)

st.success(f"분류된 연령대: {age_group}")

st.write("""
연령대 기준
- 아동: 3~11세
- 청소년: 12~18세
- 청년: 19~34세
- 성인: 35~64세
- 노인: 65세 이상
""")


# 연령 기준 활동 리스트
st.markdown("<br><br>", unsafe_allow_html=True)

st.subheader("👶 연령대 기준 활동 리스트")

for act in activities:

    if age_group in act["age_group"]:
        st.write(f"• {act['name']}")


# 비용 선택
st.markdown("<br><br>", unsafe_allow_html=True)

income = st.radio(
    "비용 조건을 선택하세요",
    [
        "비용 부담 없이 즐기고 싶어요",
        "비용은 크게 상관 없어요"
    ]
)


# 비용 기준 활동 리스트
st.markdown("<br><br>", unsafe_allow_html=True)

st.subheader("💰 비용 기준 활동 리스트")

for act in activities:

    if age_group in act["income_by_age"]:
        act_income = act["income_by_age"][age_group]

    else:
        act_income = act["income_by_age"]["default"]

    if income == act_income:
        st.write(f"• {act['name']}")


# 카테고리 선택
st.markdown("<br><br>", unsafe_allow_html=True)

category = st.selectbox(
    "선호하는 여가 카테고리를 선택하세요",
    [
        "공연 연극 관람",
        "전시 문화유산 관람",
        "문화센터"
    ]
)


# 카테고리 기준 활동 리스트
st.markdown("<br><br>", unsafe_allow_html=True)

st.subheader("🎨 카테고리 기준 활동 리스트")

for act in activities:

    if category in act["category"]:
        st.write(f"• {act['name']}")


# 최종 추천
st.markdown("<br><br>", unsafe_allow_html=True)

if st.button("🏆 최종 추천 받기"):

    results = []

    for act in activities:

        score = 0

        # 연령 점수
        if age_group in act["recommended_age"]:
            score += 5

        elif age_group in act["age_group"]:
            score += 2

        # 비용 점수
        if age_group in act["income_by_age"]:
            act_income = act["income_by_age"][age_group]

        else:
            act_income = act["income_by_age"]["default"]

        if income == act_income:
            score += 3

        # 카테고리 점수
        if category in act["category"]:
            score += 4

        results.append((act, score))

    # 최고 점수 계산
    max_score = max(score for act, score in results)

    # 최고 점수 활동만 추출
    top_activities = [
        (act, score)
        for act, score in results
        if score == max_score
    ]

    # 동점 처리
    if len(top_activities) >= 3:
        final_recommendations = random.sample(top_activities, 2)

    else:
        final_recommendations = top_activities[:2]


    # 최종 결과 출력
    st.subheader("🏆 최종 추천 활동")

    for act, score in final_recommendations:

        st.success(act["name"])

        st.write(act["description"])

        st.markdown(
            f"[관련 사이트 바로가기]({act['link']})"
        )

        st.write("---")
#끝! ㅇㄴㄹㄴㅇ
