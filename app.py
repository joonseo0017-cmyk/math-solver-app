import streamlit as st
import json
from PIL import Image

# 디자인 설정
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #e0e0e0; }
    .main-text { text-align: center; margin-top: 200px; font-size: 24px; }
    </style>
""", unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 0
if 'problems' not in st.session_state: st.session_state.problems = []

# 0단계: 시작
if st.session_state.step == 0:
    st.markdown('<div class="main-text">서준아, 어서와.<br>화면 아무 곳이나 클릭해.</div>', unsafe_allow_html=True)
    if st.button("시작하기", use_container_width=True):
        st.session_state.step = 1
        st.rerun()

# 1단계: 테스트용 문제 로딩 (API 키 오류 회피)
elif st.session_state.step == 1:
    st.subheader("문제 설정")
    uploaded_file = st.file_uploader("문제 사진을 업로드하세요.", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file:
        st.image(uploaded_file, caption="업로드 완료", use_container_width=True)
        if st.button("분석 없이 바로 시작하기"):
            # 예시 데이터로 강제 설정 (분석 기능 대기 중)
            st.session_state.problems = [
                {"q": "x^2 + 2x + 1", "a": "x = -1"},
                {"q": "x^2 + 6x + 9", "a": "x = -3"}
            ]
            st.session_state.idx = 0
            st.session_state.step = 2
            st.rerun()

# 2단계: 문제 풀이
elif st.session_state.step == 2:
    prob = st.session_state.problems[st.session_state.idx]
    st.write(f"### 문제 {st.session_state.idx + 1}")
    st.latex(prob['q'])
    
    if st.button("다음 문제"):
        if st.session_state.idx < len(st.session_state.problems) - 1:
            st.session_state.idx += 1
            st.rerun()
        else:
            st.session_state.step = 3
            st.rerun()

# 3단계: 정답 확인
elif st.session_state.step == 3:
    st.subheader("정답 확인")
    for i, p in enumerate(st.session_state.problems):
        st.write(f"{i+1}번 답:")
        st.latex(p['a'])
    if st.button("처음으로"):
        for key in st.session_state.keys(): del st.session_state[key]
        st.rerun()
