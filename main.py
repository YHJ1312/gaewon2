import streamlit as st
import google.generativeai as genai

# 1. 페이지 테마 및 제목 설정
st.set_page_config(page_title="어디든 알려주는 여행 AI", page_icon="🌍", layout="centered")

# 2. 감각적인 바이브 디자인 (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .stTitle { font-size: 2.5rem !important; color: #0ea5e9 !important; font-weight: 800 !important; }
    .stTextInput input { border-radius: 20px !important; border: 2px solid #e2e8f0 !important; padding: 15px !important; }
    .stMarkdown h3 { color: #1e293b; border-bottom: 2px solid #f1f5f9; padding-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. AI 두뇌 연결 (여기에 복사한 키를 넣으세요!)
API_KEY = "여기에_발급받은_API_키를_넣으세요"

def get_ai_response(location):
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    
    # AI가 '어디든' 상세하게 답변하도록 만드는 마법의 주문(프롬프트)
    query = f"""
    너는 전 세계를 구석구석 다녀본 전문 여행 가이드야. 
    사용자가 입력한 '{location}'에 대해 다음 내용을 아주 구체적으로 알려줘.
    
    1. 🏛️ **꼭 방문해야 할 명소 3곳**: 단순히 이름만 나열하지 말고, 왜 가야 하는지 구체적인 이유와 팁을 포함해줘.
    2. 🍴 **현지 맛집과 추천 메뉴**: 유명한 체인점 말고, 현지인들이 사랑하는 진짜 맛집 2곳과 꼭 먹어야 할 메뉴.
    3. 💡 **여행자를 위한 실무 꿀팁**: 그곳의 교통편, 날씨 대비법, 혹은 그 지역만의 특별한 예절 등.
    
    답변은 가독성 좋게 이모지와 불렛포인트를 써서 풍성하게 작성해줘.
    """
    response = model.generate_content(query)
    return response.text

# 4. 앱 화면 구성
st.title("🌍 어디로 떠나고 싶나요?")
st.write("도시, 국가, 혹은 작은 동네 이름을 입력하고 엔터를 치세요. AI가 상세 가이드를 즉석에서 작성합니다.")

# 사용자 입력창
user_input = st.text_input("", placeholder="예: 아이슬란드, 뉴욕 브루클린, 양양 서피비치, 파리 마레지구...")

if user_input:
    if API_KEY == "여기에_발급받은_API_키를_넣으세요":
        st.warning("⚠️ 코딩 파트너의 조언: 코드의 API_KEY 부분에 실제 키를 입력해야 작동합니다!")
    else:
        with st.spinner(f"✨ AI가 '{user_input}'의 모든 정보를 모으고 있어요..."):
            try:
                result = get_ai_response(user_input)
                st.divider()
                st.markdown(f"## 📍 {user_input} 여행 리포트")
                st.markdown(result)
                st.balloons()
            except Exception as e:
                st.error(f"정보를 가져오지 못했습니다. API 키가 정확한지 확인해 주세요. (에러: {e})")

st.caption("어디든 자판만 치면 정보가 쏟아지는 무한 여행 가이드 v1.0")
