import streamlit as st

# 스타일 설정: 배경 검정, 글자 회색, 투명 버튼
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #e0e0e0; }
    div.stButton > button {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background-color: transparent !important; border: none !important; color: transparent !important;
    }
    .main-text { text-align: center; margin-top: 300px; font-size: 24px; pointer-events: none; }
    </style>
""", unsafe_allow_html=True)

# 세션 초기화
if 'step' not in st.session_state: st.session_state.step = 0
if 'problems' not in st.session_state: 
    st.session_state.problems = [
        {"q": "x^2 + 2x + 1 = 0", "a": "x = -1"},
        {"q": "3x + 5 = 11", "a": "x = 2"}
    ]
if 'idx' not in st.session_state: st.session_state.idx = 0

# 0단계: 시작
if st.session_state.step == 0:
    st.markdown('<div class="main-text">서준아, 어서와.<br>화면 아무 곳이나 클릭해.</div>', unsafe_allow_html=True)
    if st.button("start"):
        st.session_state.step = 1
        st.rerun()

# 1단계: 설정 및 업로드
elif st.session_state.step == 1:
    st.subheader("문제 설정")
    uploaded_file = st.file_uploader("사진을 올리면 분석 준비가 됩니다.")
    num = st.slider("문제 개수", 1, 30, 5)
    
    # 파일을 올렸을 때만 분석 시작 버튼이 활성화되도록 로직 추가
    if uploaded_file:
        st.image(uploaded_file, caption="업로드된 문제지", use_column_width=True)
        if st.button("분석 시작"):
            st.session_state.step = 2
            st.rerun()

# 2단계: 문제 풀이
elif st.session_state.step == 2:
    if st.session_state.idx < len(st.session_state.problems):
        st.write(f"### 문제 {st.session_state.idx + 1}")
        st.latex(st.session_state.problems[st.session_state.idx]["q"])
        st.write("---")
        st.write("화면 클릭 시 다음 문제")
        if st.button("next"):
            st.session_state.idx += 1
            st.rerun()
    else:
        st.session_state.step = 3
        st.rerun()

# 3단계: 정답지 및 처음으로 가기
elif st.session_state.step == 3:
    st.subheader("정답 확인")
    for i, item in enumerate(st.session_state.problems):
        st.write(f"문제 {i+1} 정답:")
        st.latex(item["a"])
    
    st.write("---")
    st.write("화면을 클릭하면 처음부터 다시 시작합니다.")
    if st.button("restart"):
        # 모든 데이터 초기화
        st.session_state.step = 0
        st.session_state.idx = 0
        st.rerun()
