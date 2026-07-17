import streamlit as st
import google.generativeai as genai

# 스타일 설정: 버튼의 배경색과 테두리를 완전히 투명으로 만듦
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #e0e0e0; }
    
    /* 버튼 스타일을 완전히 투명하게 설정 */
    div.stButton > button {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-color: transparent !important;
        border: none !important;
        color: transparent !important;
        box-shadow: none !important;
    }
    
    .main-text { 
        text-align: center; 
        margin-top: 300px; 
        font-size: 24px; 
        pointer-events: none; /* 텍스트는 클릭을 방해하지 않음 */
    }
    </style>
""", unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 0

# 0단계: 시작 화면
if st.session_state.step == 0:
    st.markdown('<div class="main-text">서준아, 어서와.<br>화면 아무 곳이나 클릭해.</div>', unsafe_allow_html=True)
    if st.button("start"):
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
    
    if uploaded_file and st.button("분석 시작"):
        # 이후 로직은 동일
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.write("문제 풀이 화면입니다.")
