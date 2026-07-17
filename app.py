import streamlit as st
import time

# 핑크색 배경 스타일 적용
st.markdown("""
    <style>
    .stApp {
        background-color: #ffeef2;
    }
    .main-title {
        text-align: center;
        color: #ff6b8b;
        font-size: 50px;
        margin-top: 100px;
    }
    </style>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if 'show_upload' not in st.session_state:
    st.session_state.show_upload = False

# 화면 구성
if not st.session_state.show_upload:
    # 핑크 배경에 환영 인사만 띄우기
    st.markdown('<div class="main-title">서준아! 어서와! 👋</div>', unsafe_allow_html=True)
    st.write("---")
    st.write("### 아무 곳이나 클릭해서 시작해보자!")
    
    # 버튼을 크게 만들어 아무 곳이나 누르는 느낌 구현
    if st.button("시작하기 (여기 클릭!)", use_container_width=True):
        st.session_state.show_upload = True
        st.rerun()

else:
    # 클릭 후 사진 업로드 화면
    st.header("📸 문제 사진을 올려줘!")
    uploaded_file = st.file_uploader("여기에 문제를 올려봐", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="업로드한 문제", use_container_width=True)
        num = st.slider("몇 문제 풀거야?", 1, 10, 3)
        if st.button("문제 분석 시작하기"):
            st.success(f"{num}개의 문제를 분석해서 준비할게!")
