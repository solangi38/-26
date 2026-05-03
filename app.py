import streamlit as st

st.title("여가 활동 추천 서비스")
st.write("연령대와 지역을 기반으로 맞춤 여가 활동을 추천해드립니다.")

# -----------------------------
# 1. 사용자 입력
# -----------------------------
age_group = st.selectbox(
    "연령대를 선택하세요",
    ["아동", "청소년", "청년", "성인", "노인"]
)

regions = [
    # 서울
    "강남구","강동구","강북구","강서구","관악구","광진구","구로구","금천구",
    "노원구","도봉구","동대문구","동작구","마포구","서대문구","서초구",
    "성동구","성북구","송파구","양천구","영등포구","용산구","은평구",
    "종로구","중구","중랑구",

    # 경기
    "수원시","성남시","고양시","용인시","부천시","안산시","안양시",
    "남양주시","화성시","평택시","의정부시","시흥시","파주시",
    "김포시","광명시","군포시","오산시","이천시","안성시",
    "양주시","구리시","포천시","의왕시","하남시","여주시",
    "동두천시","과천시","가평군","양평군","연천군"
]

region = st.selectbox("거주 지역을 선택하세요", regions)

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

    {"name":"경기도 어린이박물관","category":["문화/예술"],
     "region":["용인시"],
     "income":["비용 부담 없이 즐기고 싶어요","적당한 비용은 괜찮아요"],
     "age_group":["아동","청소년"]},

    {"name":"노인복지관","category":["힐링/휴식","문화/예술"],
     "region":["서울","경기"],
     "income":["비용 부담 없이 즐기고 싶어요","적당한 비용은 괜찮아요","비용은 크게 상관 없어요"],
     "age_group":["노인"]},

    {"name":"청소년문화의집","category":["힐링/휴식","문화/예술"],
     "region":[
        "서대문구","은평구","강서구","구로구","금천구","동작구","마포구",
        "강동구","도봉구","노원구","성동구","성북구","양천구","영등포구","용산구",
        "구리시","평촌","하남시","광주시","성남시","과천시",
        "안양시","수원시","남양주시","양평군","가평군","양주시"
     ],
     "income":["비용 부담 없이 즐기고 싶어요","적당한 비용은 괜찮아요","비용은 크게 상관 없어요"],
     "age_group":["청소년"]},

    # 🔥 구체화된 문화 활동
    {"name":"국립현대미술관 서울관 방문","category":["문화/예술"],
     "region":["서울"],
     "income":["적당한 비용은 괜찮아요"],
     "age_group":["청소년","청년","성인","노인"]},

    {"name":"리움미술관 방문","category":["문화/예술"],
     "region":["서울"],
     "income":["적당한 비용은 괜찮아요"],
     "age_group":["청소년","청년","성인","노인"]},

    {"name":"DDP 전시 관람","category":["문화/예술"],
     "region":["서울"],
     "income":["적당한 비용은 괜찮아요"],
     "age_group":["청소년","청년","성인","노인"]},

    {"name":"예술의전당 전시 관람","category":["문화/예술"],
     "region":["서울"],
     "income":["적당한 비용은 괜찮아요"],
     "age_group":["청소년","청년","성인","노인"]},

    {"name":"대학로 연극 공연 관람","category":["문화/예술"],
     "region":["서울"],
     "income":["적당한 비용은 괜찮아요"],
     "age_group":["청년","성인","노인"]},

    {"name":"아르코예술극장 연극 관람","category":["문화/예술"],
     "region":["서울"],
     "income":["적당한 비용은 괜찮아요"],
     "age_group":["청년","성인","노인"]},

    # 기존 활동
    {"name":"인디 영화관 (인디스페이스)","category":["문화/예술"],
     "region":["서울"],
     "income":["적당한 비용은 괜찮아요"],
     "age_group":["청년"]},

    {"name":"인디 영화관 (에무시네마)","category":["문화/예술"],
     "region":["서울"],
     "income":["적당한 비용은 괜찮아요"],
     "age_group":["청년"]}
]

# -----------------------------
# 3. 추천 이유
# -----------------------------
def generate_reason(user, act, score):
    parts = []

    if score >= 5:
        parts.append("매우 잘 맞는 활동이에요.")
    elif score >= 3:
        parts.append("잘 맞는 활동이에요.")
    else:
        parts.append("가볍게 추천드려요.")

    if user["age_group"] in act["age_group"]:
        parts.append("연령대에 잘 맞고")

    if user["category"] in act["category"]:
        parts.append("선호 카테고리와 일치하며")

    if user["income"] in act["income"]:
        parts.append("비용 조건도 잘 맞아서")

    parts.append("추천드려요.")

    return " ".join(parts)

# -----------------------------
# 4. 추천 실행
# -----------------------------
if st.button("추천 받기"):

    user = {
        "age_group": age_group,
        "region": region,
        "income": income,
        "category": category
    }

    results = []

    for act in activities:
        score = 0

        if age_group in act["age_group"]:
            score += 3

        if category in act["category"]:
            score += 2

        if income in act["income"]:
            score += 2

        if region in act["region"] or "서울" in act["region"] or "경기" in act["region"]:
            score += 2

        results.append((act, score))

    results.sort(key=lambda x: x[1], reverse=True)

    st.subheader("추천 결과")

    for act, score in results[:3]:
        reason = generate_reason(user, act, score)

        st.write(f"👉 {act['name']}")
        st.write(reason)
        st.write(f"(적합도 점수: {score})")
        st.write("---")
