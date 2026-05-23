import streamlit as st
import random

# -----------------------------
# 제목
# -----------------------------
st.title("🎭 여가 활동 추천 서비스")
st.write("나이, 비용, 선호 카테고리를 기반으로 맞춤 여가 활동을 추천해드립니다.")

# -----------------------------
# 연령대 분류 함수
# -----------------------------
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

# -----------------------------
# 활동 데이터
# -----------------------------
activities = [

    {
        "name": "경기도 어린이박물관",
        "age_group": ["아동","청소년","청년","성인","노인"],
        "recommended_age": ["아동","성인","노인"],
        "income_by_age": {
            "default": "비용 부담 없이 즐기고 싶어요"
        },
        "category": ["전시 문화유산 관람"],
        "link": "https://gmuseum.kr/reg/regView?category=all&id=60"
    },

    {
        "name": "DDP 전시 관람",
        "age_group": ["아동","청소년","청년","성인","노인"],
        "recommended_age": [],
        "income_by_age": {
            "default": "비용은 크게 상관 없어요"
        },
        "category": ["전시 문화유산 관람"],
        "link": "https://ddp.or.kr/index.html?menuno=240"
    },

    {
        "name": "대학로 연극 공연 관람",
        "age_group": ["아동","청소년","청년","성인","노인"],
        "recommended_age": ["청소년","청년","성인"],
        "income_by_age": {
            "default": "비용은 크게 상관 없어요"
        },
        "category": ["공연 연극 관람"],
        "link": "https://timeticket.co.kr/"
    },

    {
        "name": "아르코예술극장 연극",
        "age_group": ["아동","청소년","청년","성인","노인"],
        "recommended_age": ["청소년","청년","성인"],
        "income_by_age": {
            "default": "비용은 크게 상관 없어요"
        },
        "category": ["공연 연극 관람"],
        "link": "https://theater.arko.or.kr/home/ko/main"
    },

    {
        "name": "서울 생활문화센터 체부",
        "age_group": ["아동","청소년","청년","성인","노인"],
        "recommended_age": ["청소년","청년","성인"],
        "income_by_age": {
            "default": "비용 부담 없이 즐기고 싶어요"
        },
        "category": ["문화센터"],
        "link": "https://ccasc.or.kr/"
    },

    {
        "name": "서울문화예술교육센터",
        "age_group": ["아동","청소년","청년","성인","노인"],
        "recommended_age": ["아동","성인","노인"],
        "income_by_age": {
            "default": "비용 부담 없이 즐기고 싶어요"
        },
        "category": ["문화센터"],
        "link": "https://www.sfac.or.kr/"
    },

    {
        "name": "청소년문화의집",
        "age_group": ["청소년","청년"],
        "recommended_age": ["청소년"],
        "income_by_age": {
            "default": "비용 부담 없이 즐기고 싶어요"
        },
        "category": ["문화센터"],
        "link": "https://sbyc.or.kr/"
    },

    {
        "name": "서울노인복지센터",
        "age_group": ["노인"],
        "recommended_age": ["노인"],
        "income_by_age": {
            "default": "비용은 크게 상관 없어요"
        },
        "category": ["문화센터"],
        "link": "https://seoulnoin.or.kr/senior/culture4.asp"
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
        "link": "https://www.sac.or.kr/site/main/membership/member_step"
    },

    {
        "name": "서울청년문화패스",
        "age_group": ["청년"],
        "recommended_age": ["청년"],
        "income_by_age": {
            "default": "비용 부담 없이 즐기고 싶어요"
        },
        "category": ["공연 연극 관람", "전시 문화유산 관람"],
        "link": "https://www.youthcultureseoul.kr/"
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
        "link": "https://www.cgv.co.kr/"
    },

    {
        "name": "국립현대미술관",
        "age_group": ["아동","청소년","청년","성인","노인"],
        "recommended_age": [],
        "income_by_age": {
            "default": "비용 부담 없이 즐기고 싶어요"
        },
        "category": ["전시 문화유산 관람"],
        "link": "https://www.mmca.go.kr/visitingInfo/seoulInfo.do"
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
        "link": "https://www.leeumhoam.org/"
    },

    {
        "name": "4대궁 관람",
        "age_group": ["아동","청소년","청년","성인","노인"],
        "recommended_age": [],
        "income_by_age": {
            "default": "비용 부담 없이 즐기고 싶어요"
        },
        "category": ["전시 문화유산 관람"],
        "link": "https://royal.khs.go.kr/ROYAL/contents/R703000000.do"
    }

]

# -----------------------------
# 사용자 입력
# -----------------------------
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

# -----------------------------
# 1차 활동 리스트
# -----------------------------
st.subheader("👶 연령대 기준 활동 리스트")

age_filtered = []

for act in activities:
    if age_group in act["age_group"]:
        age_filtered.append(act)

for act in age_filtered:
    st.write(f"• {act['name']}")

# -----------------------------
# 비용 선택
# -----------------------------
income = st.radio(
    "비용 조건을 선택하세요",
    [
        "비용 부담 없이 즐기고 싶어요",
        "비용은 크게 상관 없어요"
    ]
)

# -----------------------------
# 2차 활동 리스트
# -----------------------------
st.subheader("💰 비용 기준 활동 리스트")

income_filtered = []

for act in age_filtered:

    if age_group in act["income_by_age"]:
        act_income = act["income_by_age"][age_group]
    else:
        act_income = act["income_by_age"]["default"]

    if income == act_income:
        income_filtered.append(act)

for act in income_filtered:
    st.write(f"• {act['name']}")

# -----------------------------
# 카테고리 선택
# -----------------------------
category = st.selectbox(
    "선호하는 여가 카테고리를 선택하세요",
    [
        "공연 연극 관람",
        "전시 문화유산 관람",
        "문화센터"
    ]
)

# -----------------------------
# 3차 활동 리스트
# -----------------------------
st.subheader("🎨 카테고리 기준 활동 리스트")

category_filtered = []

for act in income_filtered:
    if category in act["category"]:
        category_filtered.append(act)

for act in category_filtered:
    st.write(f"• {act['name']}")

# -----------------------------
# 최종 추천
# -----------------------------
if st.button("최종 추천 받기"):

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

    # -----------------------------
    # 결과 출력
    # -----------------------------
    st.subheader("🏆 최종 추천 활동")

    for act, score in final_recommendations:

        st.success(act["name"])

        st.write(f"적합도 점수: {score}")

        if age_group in act["recommended_age"]:
            st.write("✔ 추천 연령대에 적합한 활동입니다.")

        st.write(f"✔ 선택한 카테고리: {category}")

        st.markdown(
            f"[공식 사이트 바로가기]({act['link']})"
        )

        st.write("---")
