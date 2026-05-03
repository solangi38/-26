import streamlit as st

st.title("청년 여가 추천 서비스")
st.write("간단한 정보를 입력하면 맞춤 여가 활동을 추천해드립니다.")

# -----------------------------
# 1. 사용자 입력
# -----------------------------
age = st.selectbox("나이를 선택하세요", list(range(20, 36)))

districts = [
    "강남구","강동구","강북구","강서구","관악구","광진구","구로구","금천구",
    "노원구","도봉구","동대문구","동작구","마포구","서대문구","서초구",
    "성동구","성북구","송파구","양천구","영등포구","용산구","은평구",
    "종로구","중구","중랑구"
]

district = st.selectbox("거주 구를 선택하세요", districts)

income = st.radio(
    "여가 활동 비용에 대해 어떻게 생각하시나요?",
    ["비용 부담 없이 즐기고 싶어요", "적당한 비용은 괜찮아요", "비용은 크게 상관 없어요"]
)

category = st.selectbox(
    "선호하는 여가 카테고리를 선택하세요",
    ["야외", "문화/예술", "힐링/휴식"]
)

# -----------------------------
# 2. 활동 데이터
# -----------------------------
activities = [
    {"name":"한강 공원 산책","category":["야외","힐링/휴식"],
     "district":["강남구","송파구","영등포구","마포구"],
     "income":["비용 부담 없이 즐기고 싶어요"],"age_range":(20,35)},

    {"name":"자전거 타기 (한강)","category":["야외"],
     "district":["강서구","영등포구","송파구"],
     "income":["적당한 비용은 괜찮아요"],"age_range":(20,35)},

    {"name":"서울숲 산책","category":["야외","힐링/휴식"],
     "district":["성동구"],
     "income":["비용 부담 없이 즐기고 싶어요"],"age_range":(20,35)},

    {"name":"북한산 등산","category":["야외"],
     "district":["강북구","은평구"],
     "income":["적당한 비용은 괜찮아요","비용은 크게 상관 없어요"],"age_range":(20,35)},

    {"name":"남산 타워 주변 걷기","category":["야외"],
     "district":["중구","용산구"],
     "income":["비용 부담 없이 즐기고 싶어요"],"age_range":(20,35)},

    {"name":"피크닉","category":["야외"],
     "district":["광진구","마포구","송파구","영등포구"],
     "income":["적당한 비용은 괜찮아요"],"age_range":(20,35)},

    {"name":"미술관 방문","category":["문화/예술"],
     "district":["종로구","중구"],
     "income":["적당한 비용은 괜찮아요"],"age_range":(20,35)},

    {"name":"전시회 관람","category":["문화/예술"],
     "district":["종로구","마포구"],
     "income":["적당한 비용은 괜찮아요"],"age_range":(20,35)},

    {"name":"독립 영화 관람","category":["문화/예술"],
     "district":["마포구"],
     "income":["적당한 비용은 괜찮아요"],"age_range":(20,35)},

    {"name":"연극 공연 관람","category":["문화/예술"],
     "district":["종로구"],
     "income":["적당한 비용은 괜찮아요"],"age_range":(20,35)},

    {"name":"한복 체험 + 궁궐 방문","category":["문화/예술"],
     "district":["종로구"],
     "income":["적당한 비용은 괜찮아요"],"age_range":(20,35)},

    {"name":"전통 공예 체험","category":["문화/예술"],
     "district":["종로구","은평구"],
     "income":["적당한 비용은 괜찮아요"],"age_range":(20,35)},

    {"name":"카페에서 휴식","category":["힐링/휴식"],
     "district":["마포구","강남구","성동구"],
     "income":["적당한 비용은 괜찮아요"],"age_range":(20,35)},

    {"name":"명상","category":["힐링/휴식"],
     "district":districts,
     "income":["비용 부담 없이 즐기고 싶어요","적당한 비용은 괜찮아요"],"age_range":(20,35)},

    {"name":"드라이브","category":["힐링/휴식","야외"],
     "district":districts,
     "income":["비용은 크게 상관 없어요"],"age_range":(20,35)},

    {"name":"책 읽으며 쉬기","category":["힐링/휴식","문화/예술"],
     "district":districts,
     "income":["비용 부담 없이 즐기고 싶어요"],"age_range":(20,35)}
]

# -----------------------------
# 3. 추천 이유 생성
# -----------------------------
def generate_reason(user, act, score):
    parts = []

    if score >= 6:
        parts.append("매우 잘 맞는 활동이에요.")
    elif score >= 4:
        parts.append("잘 맞는 활동이에요.")
    else:
        parts.append("가볍게 추천드려요.")

    if user["category"] in act["category"]:
        parts.append(f"{user['category']} 활동을 선호하시고")

    if user["income"] in act["income"]:
        parts.append("비용 조건도 잘 맞아서")

    if user["district"] in act["district"]:
        parts.append("가까운 위치에서 즐길 수 있어")

    parts.append("추천드려요.")

    return " ".join(parts)

# -----------------------------
# 4. 추천 실행
# -----------------------------
if st.button("추천 받기"):

    user = {
        "age": age,
        "district": district,
        "income": income,
        "category": category
    }

    results = []

    for act in activities:
        score = 0

        if category in act["category"]:
            score += 3
        elif category == "야외" and "힐링/휴식" in act["category"]:
            score += 1

        if district in act["district"]:
            score += 2
        else:
            score -= 1

        if income in act["income"]:
            score += 2
        elif income == "적당한 비용은 괜찮아요":
            score += 1

        if act["age_range"][0] <= age <= act["age_range"][1]:
            score += 1

        results.append((act, score))

    results.sort(key=lambda x: x[1], reverse=True)

    selected = []
    used = set()

    for act, score in results:
        main_category = act["category"][0]

        if main_category not in used:
            selected.append((act, score))
            used.add(main_category)

        if len(selected) == 3:
            break

    st.subheader("추천 결과")

    for act, score in selected:
        reason = generate_reason(user, act, score)

        st.write(f"👉 {act['name']}")
        st.write(reason)
        st.write(f"(적합도 점수: {score})")
        st.write("---")
