import streamlit as st
import time

# 1. 페이지 설정 및 디자인
st.set_page_config(page_title="무한 여행 백과사전", page_icon="🌍", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    .stTitle { color: #0284c7 !important; font-weight: 800 !important; }
    .info-card { 
        background-color: white; 
        padding: 25px; 
        border-radius: 15px; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border-left: 5px solid #0ea5e9;
    }
    .tag { color: #38bdf8; font-weight: bold; font-size: 0.9rem; }
    </style>
    """, unsafe_allow_html=True)

# 2. 방대한 여행 데이터베이스 (직접 내용을 더 추가할 수 있습니다!)
travel_data = {
    "오스트레일리아": {
        "land": "📍 시드니 오페라 하우스, 그레이트 배리어 리프, 울루루",
        "food": "🍴 미트 파이, 피시 앤 칩스, 캥거루 스테이크",
        "tip": "💡 자외선이 매우 강하니 선크림 필수! 운전석이 한국과 반대예요."
    },
    "일본": {
        "land": "📍 도쿄 타워, 교토 기요미즈데라, 오사카 도톤보리",
        "food": "🍴 이치란 라멘, 규카츠, 신선한 스시",
        "tip": "💡 110V 어댑터가 필요해요. 식당 안에서 조용히 대화하는 것이 예의입니다."
    },
    "프랑스": {
        "land": "📍 파리 에펠탑, 루브르 박물관, 몽생미셸 수도원",
        "food": "🍴 바게트와 치즈, 달팽이 요리(에스카르고), 마카롱",
        "tip": "💡 식당에서 계산서를 요청할 때 서두르지 마세요. 느긋한 식사 문화를 즐기세요."
    },
    "미국": {
        "land": "📍 뉴욕 타임스퀘어, 그랜드 캐니언, 자유의 여신상",
        "food": "🍴 오리지널 치즈버거, 딥디쉬 피자, 텍사스 바비큐",
        "tip": "💡 팁 문화가 중요해요(보통 15~20%). 주마다 세금이 다를 수 있습니다."
    },
    "제주도": {
        "land": "📍 성산일출봉, 협재 해수욕장, 사려니 숲길",
        "food": "🍴 흑돼지 구이, 고기국수, 오메기떡",
        "tip": "💡 렌터카 예약은 필수! 날씨 변화가 심하니 얇은 겉옷을 챙기세요."
    }
}

# 3. 앱 화면 구성
st.title("🌍 어디든 알려주는 여행 백과")
st.write("궁금한 국가나 도시 이름을 입력해 보세요. (예: 오스트레일리아, 일본, 프랑스...)")

# 사용자 입력창
user_input = st.text_input("", placeholder="어디로 떠나고 싶으신가요?").strip()

if user_input:
    # 4. "따르르" 느낌을 주기 위한 가짜 로딩 효과
    with st.spinner(f"🔍 '{user_input}'의 기록을 서재에서 꺼내오는 중..."):
        time.sleep(0.7) # 로딩 바이브를 위한 아주 짧은 멈춤
        
        if user_input in travel_data:
            data = travel_data[user_input]
            st.divider()
            st.markdown(f"## 📍 {user_input} 여행 리포트")
            
            # 깔끔한 카드 형식으로 출력
            st.markdown(f"""
            <div class="info-card">
                <p class="tag">TOP LANDMARKS</p>
                <p>{data['land']}</p>
                <hr>
                <p class="tag">MUST-EAT FOOD</p>
                <p>{data['food']}</p>
                <hr>
                <p class="tag">TRAVEL TIPS</p>
                <p>{data['tip']}</p>
            </div>
            """, unsafe_allow_html=True)
            st.balloons()
        else:
            # 데이터가 없을 때의 위트 있는 피드백
            st.warning(f"😭 아쉽게도 '{user_input}'에 대한 기록이 아직 백과사전에 없어요!")
            st.write("다른 유명한 국가(일본, 프랑스, 미국 등)를 먼저 검색해 보시겠어요?")
            st.snow() # 아쉬움을 달래는 눈송이 효과

st.caption("Simplified Travel Encyclopedia v1.0 (No API Required)")
