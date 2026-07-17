import streamlit as st

# 젠틀한 다크 모드 스타일 설정
st.markdown("""
    <style>
    .stApp {
        background-color: #1e1e1e;
        color: #e0e0e0;
    }
    .welcome-text {
        color: #ffffff;
        font-size: 32px;
        font-weight: 300;
        text-align: center;
        padding-top: 150px;
    }
    .instruction {
        color: #888888;
        text-align: center;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

if 'show_main' not in st.session_state: st.session_state.show_main = False

if not st.session_state.show_main:
    st.markdown('<div class="welcome-text">서준아, 어서와.</div>', unsafe_allow_html=True)
    st.markdown('<div class="instruction">화면을 클릭하면 시작합니다.</div>', unsafe_allow_html=True)
    if st.button(" ", key="overlay", use_container_width=True):
        st.session_state.show_main = True
        st.rerun()
else:
    st.subheader("문제 설정")
    
    col1, col2 = st.columns(2)
    with col1:
        uploaded_file = st.file_uploader("문제 사진을 올려주세요.")
    with col2:
        num_questions = st.slider("문제 개수", 1, 30, 5)
        api_key = st.text_input("API Key 입력", type="password")
        
    if uploaded_file:
        st.image(uploaded_file, use_column_width=True)
        if st.button("분석 시작"):
            st.info("AI가 사진에서 문제를 추출 중입니다. 잠시만 기다려주세요.")
            # 분석 속도 최적화를 위해 모델을 'gemini-1.5-flash'로 설정해야 합니다.
