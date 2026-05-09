import streamlit as st
import google.generativeai as genai

# 페이지 설정
st.set_page_config(page_title="어디든 알려주는 여행 AI", page_icon="🌍")

# 디자인 (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .stTitle { color: #0ea5e9 !important; font-weight: 800 !important; }
    </style>
    """, unsafe_allow_html=True)

# 🔑 API 키 설정 (본인의 키를 꼭 따옴표 안에 넣으세요)
API_KEY = "여기에_발급받은_API_키를_넣으세요"

# AI 로직 함수
def get_ai_response(location):
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    query = f"전문 여행 가이드로서 '{location}'의 명소 3곳, 현지 맛집 2곳, 여행 꿀팁을 아주 상세하게 이모지를 섞어 알려줘."
    response = model.generate_content(query)
    return response.text

# 화면 구성
st.title("🌍 어디가 유명해? AI 가이드")
st.write("도시나 국가 이름을 입력하면 AI가 상세 정보를 '따르르' 생성합니다.")

user_input = st.text_input("장소를 입력하세요", placeholder="예: 아이슬란드, 뉴욕, 제주도...")

if user_input:
    if API_KEY == "여기에_발급받은_API_키를_넣으세요":
        st.error("잠깐! 코드의 API_KEY 부분에 실제 키를 입력해야 작동합니다.")
    else:
        with st.spinner(f"✨ AI가 '{user_input}' 정보를 실시간으로 작성 중..."):
            try:
                result = get_ai_response(user_input)
                st.divider()
                st.markdown(result)
                st.balloons()
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
