import streamlit as st
import google.generativeai as genai
from PIL import Image
import json

# 스타일 설정: 시작 화면에서만 투명 버튼이 작동하게 수정
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #e0e0e0; }
    /* 시작 화면용 전체 투명 버튼 */
    .start-overlay { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 1000; }
    .main-text { text-align: center; margin-top: 300px; font-size: 24px; }
    </style>
""", unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 0
if 'problems' not in st.session_state: st.session_state.problems = []
if 'idx' not in st.session_state: st.session_state.idx = 0

# 0단계: 시작 화면 (전체 클릭 시 다음으로)
if st.session_state.step == 0:
    st.markdown('<div class="main-text">서준아, 어서와.<br>화면 아무 곳이나 클릭해.</div>', unsafe_allow_html=True)
    # 시작 버튼을 투명하게 배치
    if st.button(" ", key="start_btn", type="primary", use_container_width=True):
        st.session_state.step = 1
        st.rerun()

# 1단계: 사진 업로드 (여기선 버튼이 보여야 함)
elif st.session_state.step == 1:
    st.subheader("문제 설정")
    uploaded_file = st.file_uploader("문제 사진을 업로드하세요.")
    api_key = st.text_input("Google API Key 입력", type="password")
    
    if uploaded_file and api_key:
        st.image(uploaded_file, caption="업로드된 문제", use_column_width=True)
        if st.button("분석 시작"):
            with st.spinner('AI가 분석 중...'):
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                img = Image.open(uploaded_file)
                prompt = "수학 문제를 JSON으로 추출해줘: [{'q': '문제', 'a': '정답'}, ...]"
                response = model.generate_content([prompt, img])
                try:
                    clean_text = response.text.replace('```json', '').replace('```', '').strip()
                    st.session_state.problems = json.loads(clean_text)
                    st.session_state.step = 2
                    st.rerun()
                except:
                    st.error("분석 실패. 다시 시도해주세요.")

# 2단계: 문제 풀이 (다음 버튼을 눌러야 이동)
elif st.session_state.step == 2:
    if st.session_state.idx < len(st.session_state.problems):
        st.write(f"### 문제 {st.session_state.idx + 1}")
        st.latex(st.session_state.problems[st.session_state.idx]["q"])
        if st.button("다음 문제로 (클릭)"):
            st.session_state.idx += 1
            st.rerun()
    else:
        st.session_state.step = 3
        st.rerun()

# 3단계: 정답 확인
elif st.session_state.step == 3:
    st.subheader("정답지")
    for i, item in enumerate(st.session_state.problems):
        st.write(f"문제 {i+1}:")
        st.latex(item["a"])
    if st.button("처음으로 돌아가기"):
        for key in st.session_state.keys(): del st.session_state[key]
        st.rerun()
