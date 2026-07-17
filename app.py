import streamlit as st
import google.generativeai as genai

# 스타일 설정
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #e0e0e0; }
    /* 첫 화면 전용 투명 버튼 */
    .start-button button { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; opacity: 0; }
    .main-text { text-align: center; margin-top: 300px; font-size: 24px; }
    </style>
""", unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 0

# 0단계: 시작
if st.session_state.step == 0:
    st.markdown('<div class="main-text">서준아, 어서와.<br>화면 아무 곳이나 클릭해.</div>', unsafe_allow_html=True)
    if st.button(" ", key="start", help="시작"):
        st.session_state.step = 1
        st.rerun()

# 1단계: 문제 설정
elif st.session_state.step == 1:
    st.subheader("문제 설정")
    col1, col2 = st.columns(2)
    with col1:
        uploaded_file = st.file_uploader("문제 사진 업로드")
    with col2:
        num = st.slider("문제 개수", 1, 30, 5)
        api_key = st.text_input("API Key", type="password")
    
    if uploaded_file:
        st.image(uploaded_file, use_column_width=True)
        if st.button("분석 시작"):
            with st.spinner('AI 분석 중...'):
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                # 여기에 실제 분석 로직이 들어갑니다.
                st.session_state.problems = ["문제 예시 1", "문제 예시 2"] 
                st.session_state.current_idx = 0
                st.session_state.step = 2
                st.rerun()

# 2단계: 문제 풀이
elif st.session_state.step == 2:
    if st.session_state.current_idx < len(st.session_state.problems):
        st.write(f"### 문제 {st.session_state.current_idx + 1}")
        st.latex(st.session_state.problems[st.session_state.current_idx])
        st.write("화면 클릭 시 다음 문제")
        # 다음 문제 이동용 투명 버튼
        if st.button(" ", key="next"):
            st.session_state.current_idx += 1
            st.rerun()
    else:
        st.session_state.step = 3
        st.rerun()

# 3단계: 정답 확인
elif st.session_state.step == 3:
    st.write("### 정답지")
    st.write("풀이가 완료되었습니다.")
