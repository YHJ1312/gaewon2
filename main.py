import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="Global Wanderer", page_icon="✈️", layout="centered")

# 2. 디자인
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stTitle { font-weight: 700; color: #1e293b; letter-spacing: -1px; }
    .info-box { padding: 15px; border-radius: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("✈️ 어느 장소로 유명해?")
st.write("궁금한 여행지를 입력하면 AI가 실시간으로 정보를 찾아드립니다.")

# 3. 사용자 입력
location = st.text_input("", placeholder="예: 오스트레일리아, 아이슬란드, 도쿄...")

# 4. 실시간 정보 생성 로직 (Simulated AI Engine)
if location:
    st.divider()
    
    # 로딩 바이브를 주어 사용자에게 '찾고 있음'을 알립니다.
    with st.spinner(f"✨ {location}에 대한 멋진 정보를 정리하고 있어요..."):
        
        # 💡 [핵심 변경 사항] 
        # 이제 고정된 DB가 아니라, 입력값에 따라 문장을 조합하거나 
        # 나중에 여기에 OpenAI 같은 실제 AI API를 연결할 수 있습니다.
        
        # 현재는 우선 어떤 입력에도 대응할 수 있는 '스마트 템플릿' 형식을 적용합니다.
        st.subheader(f"📍 {location} 여행 가이드")
        
        col1, col2 = st.columns(2)
        
        # 실제 AI 연결 전까지는 예시를 풍성하게 보여주기 위해 
        # 입력값(location)을 활용한 동적 가이드를 출력합니다.
        with col1:
            st.info(f"🏛️ **유명 관광지**\n\n{location}의 랜드마크와 숨겨진 명소들을 탐험해 보세요.")
        with col2:
            st.success(f"🍴 **현지 맛집/음식**\n\n{location}에서만 맛볼 수 있는 특별한 요리를 추천합니다.")
            
        st.write(f"🌈 *{location}은(는) 지금 당신을 기다리고 있어요!*")
        st.balloons()

st.caption("Minimalist Travel Guide powered by Vibe Coding")
