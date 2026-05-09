import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정 및 디자인
st.set_page_config(page_title="Vibe Travel AI", page_icon="✈️")

st.markdown("""
    <style>
    .stTitle { font-weight: 800; color: #0ea5e9; }
    .travel-card { background-color: #f0f9ff; padding: 20px; border-radius: 15px; border: 1px solid #bae1ff; }
    </style>
    """, unsafe_allow_html=True)

# 2. AI 설정 (복사한 API 키를 아래 '여기에_키를_넣으세요' 자리에 따옴표와 함께 넣어주세요)
API_KEY = "여기에_키를_넣으세요" 

if API_KEY != "여기에_키를_넣으세요":
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')
else:
    st.warning("⚠️ 먼저 Google AI Studio에서 발급받은 API 키를 코드에 입력해주세요!")

st.title("✈️ 어디가 유명해? AI 가이드")
st.write("궁금한 도시나 나라를 입력하세요. AI가 숨은 맛집까지 상세히 알려드립니다.")

# 3. 사용자 입력
location = st.text_input("", placeholder="예: 오스트레일리아 시드니, 제주도 서귀포...")

if location and API_KEY != "여기에_키를_넣으세요":
    with st.spinner(f"🔍 AI가 {location}의 구석구석을 살펴보고 있어요..."):
        try:
            # AI에게 구체적인 페르소나와 질문 던지기
            prompt = f"""
            너는 베테랑 여행 가이드야. '{location}'에 대해 다음 정보를 아주 구체적이고 세세하게 알려줘.
            1. 꼭 가봐야 할 유명 관광지 3곳 (설명 포함)
            2. 현지인들만 아는 진짜 맛집 2곳 (대표 메뉴 포함)
            3. 그 지역의 현재 여행 바이브와 꿀팁
            가독성 좋게 불렛포인트와 이모지를 섞어서 대답해줘.
            """
            response = model.generate_content(prompt)
            
            st.divider()
            st.subheader(f"📍 {location} 여행 리포트")
            
            # AI의 답변 출력
            st.markdown(response.text)
            st.balloons()
            
        except Exception as e:
            st.error(f"정보를 가져오는 중에 문제가 생겼어요: {e}")

st.caption("Real-time AI Travel Guide powered by Vibe Coding")
