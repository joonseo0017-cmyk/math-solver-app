import streamlit as st
import google.generativeai as genai
from PIL import Image
import json

# 스타일 설정
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #e0e0e0; }
    .main-text { text-align: center; margin-top: 200px; font-size: 24px; }
    </style>
""", unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 0

# 0단계: 시작
if st.session_state.step == 0:
    st.markdown('<div class="main-text">서준아, 어서와.<br>화면 아무 곳이나 클릭해.</div>', unsafe_allow_html=True)
    if st.button("시작하기", use_container_width=True):
        st.session_state.step = 1
        st.rerun()

# 1단계: 사진 분석
elif st.session_state.step == 1:
    st.subheader("문제 설정")
    uploaded_file = st.file_uploader("문제 사진을 업로드하세요.", type=['jpg', 'jpeg', 'png'])
    api_key = st.text_input("Google API Key", type="password")
    
    if uploaded_file and api_key:
        st.image(uploaded_file, use_column_width=True)
        if st.button("분석 시작"):
            try:
                with st.spinner('AI가 문제를 읽는 중...'):
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    
                    # 이미지를 PIL 객체로 변환
                    img = Image.open(uploaded_file)
                    
                    prompt = "이 사진에서 수학 문제들을 추출해. 반드시 다음 JSON 형식으로만 응답해: [{'q': '문제수식', 'a': '정답'}, ...]"
                    response = model.generate_content([prompt, img])
                    
                    # 응답 정리
                    text = response.text.replace('```json', '').replace('```', '').strip()
                    st.session_state.problems = json.loads(text)
                    st.session_state.idx = 0
                    st.session_state.step = 2
                    st.rerun()
            except Exception as e:
                st.error(f"분석 중 오류 발생: {e}")

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

# 3단계: 정답지
elif st.session_state.step == 3:
    st.subheader("정답 확인")
    for i, p in enumerate(st.session_state.problems):
        st.write(f"{i+1}번 답:")
        st.latex(p['a'])
    if st.button("처음으로"):
        st.session_state.step = 0
        st.rerun()
        
