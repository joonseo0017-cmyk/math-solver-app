import streamlit as st
import google.generativeai as genai

# 스타일 설정: 전체 화면 클릭 가능하게
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #e0e0e0; }
    /* 투명 버튼을 화면 전체에 배치 */
    div.stButton > button {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background-color: transparent !important; border: none !important; color: transparent !important;
    }
    .main-text { text-align: center; margin-top: 300px; font-size: 24px; pointer-events: none; }
    </style>
""", unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 0
if 'problems' not in st.session_state: st.session_state.problems = ["x^2 + 2x + 1 = 0", "3x + 5 = 11", "2x - 4 = 0"]
if 'idx' not in st.session_state: st.session_state.idx = 0

# 0단계: 시작
if st.session_state.step == 0:
    st.markdown('<div class="main-text">서준아, 어서와.<br>화면 아무 곳이나 클릭해.</div>', unsafe_allow_html=True)
    if st.button("start"):
        st.session_state.step = 1
        st.rerun()

# 1단계: 설정
elif st.session_state.step == 1:
    st.subheader("문제 설정")
    uploaded_file = st.file_uploader("사진 업로드")
    num = st.slider("문제 개수", 1, 30, 5)
    if st.button("분석 시작"):
        st.session_state.step = 2
        st.rerun()

# 2단계: 문제 풀이 (클릭 시 다음 이동)
elif st.session_state.step == 2:
    if st.session_state.idx < len(st.session_state.problems):
        st.write(f"### 문제 {st.session_state.idx + 1}")
        st.latex(st.session_state.problems[st.session_state.idx])
        st.write("---")
        st.write("화면을 클릭하면 다음 문제로 넘어갑니다.")
        if st.button("next"):
            st.session_state.idx += 1
            st.rerun()
    else:
        st.session_state.step = 3
        st.rerun()

# 3단계: 결과
elif st.session_state.step == 3:
    st.write("### 정답지")
    st.write("모든 문제를 완료했습니다.")
