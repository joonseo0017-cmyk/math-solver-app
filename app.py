import streamlit as st
import google.generativeai as genai
from PIL import Image
import json

# 디자인 설정
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #e0e0e0; }
    div.stButton > button {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background-color: transparent !important; border: none !important; color: transparent !important;
        z-index: 999;
    }
    .main-text { text-align: center; margin-top: 300px; font-size: 24px; pointer-events: none; }
    </style>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if 'step' not in st.session_state: st.session_state.step = 0
if 'problems' not in st.session_state: st.session_state.problems = []
if 'idx' not in st.session_state: st.session_state.idx = 0

# 0단계: 시작
if st.session_state.step == 0:
    st.markdown('<div class="main-text">서준아, 어서와.<br>화면 아무 곳이나 클릭해.</div>', unsafe_allow_html=True)
    if st.button("start"):
        st.session_state.step = 1
        st.rerun()

# 1단계: 사진 업로드 및 분석
elif st.session_state.step == 1:
    st.subheader("문제 설정")
    uploaded_file = st.file_uploader("문제 사진을 업로드하세요.")
    api_key = st.text_input("Google API Key 입력", type="password")
    
    if uploaded_file and api_key:
        st.image(uploaded_file, caption="업로드된 문제", use_column_width=True)
        if st.button("분석 시작"):
            with st.spinner('AI가 문제를 분석 중입니다...'):
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                img = Image.open(uploaded_file)
                
                # 프롬프트로 JSON 형식을 강제하여 오류 방지
                prompt = "사진 속 수학 문제를 추출해줘. 반드시 아래 JSON 형식으로만 답해줘: [{'q': '문제 수식', 'a': '정답'}, ...]"
                response = model.generate_content([prompt, img])
                
                try:
                    # 응답에서 JSON 부분만 추출
                    clean_text = response.text.replace('```json', '').replace('
