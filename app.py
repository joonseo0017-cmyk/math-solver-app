import streamlit as st
import google.generativeai as genai
import time

st.set_page_config(page_title="서준이의 수학 앱", layout="centered")

# 세션 초기화
if 'step' not in st.session_state: st.session_state.step = 1

st.title("🧮 수학 퀴즈 챌린지")

if st.session_state.step == 1:
    st.header("서준아! 어서와! 👋")
    st.write("문제 풀 준비 됐지?")
    uploaded_file = st.file_uploader("문제 사진을 올려줘!", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="업로드한 문제", use_column_width=True)
        st.session_state.num = st.slider("몇 문제 풀거야?", 1, 10, 3)
        api_key = st.text_input("Google API Key", type="password")
        
        if st.button("문제 분석 시작!"):
            with st.spinner('AI가 문제를 분석 중이야...'):
                st.session_state.step = 2
                st.rerun()

elif st.session_state.step == 2:
    st.write("### 3초 뒤에 시작할게!")
    placeholder = st.empty()
    for i in range(3, 0, -1):
        placeholder.write(f"### {i}")
        time.sleep(1)
    st.session_state.step = 3
    st.rerun()

elif st.session_state.step == 3:
    st.subheader("문제 풀이 모드")
    st.latex(r"x^2 - 4x + 4 = 0") # 예시 수식
    if st.button("다음 문제"):
        st.write("다음으로 이동...")
