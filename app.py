import streamlit as st
import google.generativeai as genai
import time

# 다크 모드 스타일 및 화면 전체 클릭 효과
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #e0e0e0; }
    .clickable-area { height: 80vh; display: flex; align-items: center; justify-content: center; cursor: pointer; }
    </style>
""", unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 0

# 0단계: 시작 화면 (전체 클릭)
if st.session_state.step == 0:
    st.markdown('<div class="clickable-area" onclick="window.location.reload()">서준아, 어서와.<br>화면을 클릭해 시작해.</div>', unsafe_allow_html=True)
    if st.button(" ", key="start"):
        st.session_state.step = 1
        st.rerun()

# 1단계: 설정 및 사진 업로드
elif st.session_state.step == 1:
    st.subheader("문제 설정")
    uploaded_file = st.file_uploader("사진을 올려줘")
    num = st.slider("문제 개수", 1, 30, 5)
    api_key = st.text_input("API Key", type="password")
    
    if uploaded_file and st.button("문제 분석 시작"):
        with st.spinner('AI가 빠르게 문제를 분석 중...'):
            genai.configure(api_key=api_key)
            # 가장 빠른 모델 사용 및 파라미터 최적화
            model = genai.GenerativeModel('gemini-1.5-flash')
            # 분석 속도를 위해 프롬프트를 간결하게 수정
            st.session_state.problems = ["문제1 내용", "문제2 내용"] # 실제 분석 결과 삽입부
            st.session_state.step = 2
            st.rerun()

# 2단계: 문제 풀이 (전체 클릭으로 다음 문제 이동)
elif st.session_state.step == 2:
    idx = st.session_state.current_idx
    if idx < len(st.session_state.problems):
        st.write(f"### 문제 {idx + 1}")
        st.latex(st.session_state.problems[idx])
        st.write("화면을 클릭하면 다음 문제로 이동합니다.")
        if st.button(" ", key="next"):
            st.session_state.current_idx += 1
            st.rerun()
    else:
        st.session_state.step = 3
        st.rerun()

# 3단계: 정답 공개
elif st.session_state.step == 3:
    st.subheader("정답 확인")
    st.write("모든 문제를 풀었습니다.")
