import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="Global Wanderer", page_icon="✈️", layout="centered")

# 2. 디자인 수정 (여기서 에러가 났던 부분을 바로잡았습니다!)
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
    }
    .stTitle {
        font-weight: 700;
        color: #1e293b;
        letter-spacing: -1px;
    }
    </style>
    """, unsafe_allow_html=True) # <- 'index'가 아니라 'html'입니다!

# 3. 헤더 섹션
st.title("✈️ 어느 곳으로 떠나고 싶으신가요?")
st.write("꿈꾸던 여행지를 입력하면 그곳의 정취를 담은 정보를 찾아드립니다.")

# 4. 사용자 입력부
location = st.text_input("", placeholder="예: 파리, 교토, 제주도, 뉴욕...")

# 5. 여행 정보 데이터베이스
travel_db = {
    "파리": {
        "landmark": "에펠탑, 루브르 박물관",
        "food": "크로와상, 에스카르고",
        "vibe": "예술과 낭만이 흐르는 거리"
    },
    "교토": {
        "landmark": "기요미즈데라, 후시미 이나리 신사",
        "food": "가이세키 요리, 말차 디저트",
        "vibe": "전통과 정적이 머무는 시간"
    },
    "제주도": {
        "landmark": "성산일출봉, 비자림",
        "food": "흑돼지 구이, 고기국수",
        "vibe": "에메랄드빛 바다와 현무암의 조화"
    }
}

# 6. 결과 출력
if location:
    st.divider()
    if location in travel_db:
        info = travel_db[location]
        st.subheader(f"📍 {location}의 여행 조각들")
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"🏛️ **추천 관광지**\n\n{info['landmark']}")
        with col2:
            st.success(f"🍴 **놓칠 수 없는 맛**\n\n{info['food']}")
        
        st.write(f"✨ *{info['vibe']}*")
    else:
        st.warning(f"'{location}'에 대한 정보를 수집 중입니다! 대신 그곳의 날씨나 항공권을 먼저 확인해보시는 건 어떨까요?")
        st.balloons()

st.caption("Minimalist Travel Guide powered by Vibe Coding")
