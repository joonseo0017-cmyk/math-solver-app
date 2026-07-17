import streamlit as st

# 디자인 설정: 배경은 검정, 글자는 회색/흰색
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #e0e0e0; }
    /* 버튼을 화면 전체 크기로 확장하여 보이지 않게 만듭니다 */
    div.stButton > button {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        opacity: 0;
        cursor: pointer;
    }
    .main-text {
        text-align: center;
        margin-top: 300px;
        font-size: 24px;
        pointer-events: none; /* 텍스트는 클릭 방해 안 함 */
    }
    </style>
""", unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 0

# 화면 구성
if st.session_state.step == 0:
    st.markdown('<div class="main-text">서준아, 어서와.<br>화면 아무 곳이나 클릭해.</div>', unsafe_allow_html=True)
    # 화면 전체를 덮는 투명 버튼
    if st.button(" ", key="start"):
        st.session_state.step = 1
        st.rerun()

elif st.session_state.step == 1:
    st.subheader("문제 설정")
    # 이후 로직... (사진 업로드 등)
