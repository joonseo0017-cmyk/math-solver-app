import streamlit as st
import google.generativeai as genai
import time

st.set_page_config(page_title="수학 퀴즈 앱", layout="centered")

# 세션 상태 초기화 (앱이 새로고침되어도 데이터 유지)
if 'step' not in st.session_state: st.session_state.step = 1
if 'problems' not in st.session_state: st.session_state.problems = []
if 'current_idx' not in st.session_state: st.session_state.current_idx = 0

st.title("🧮 수학 퀴즈 챌린지")

# 단계별 로직
if st.session_state.step == 1:
    st.write("### 서준님, 오늘 풀 문제의 주제를 입력해주세요.")
    st.session_state.user_input = st.text_area("문제 주제:")
    if st.button("다음"):
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.write(f"주제: {st.session_state.user_input}")
    st.session_state.num = st.slider("문제 개수를 선택하세요", 1, 30, 5)
    api_key = st.text_input("Google API Key 입력", type="password")
    
    if st.button("준비 완료!"):
        with st.spinner('문제를 만드는 중...'):
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"주제 '{st.session_state.user_input}'에 대해 {st.session_state.num}개의 문제를 각 문제와 정답을 분리하여 JSON 리스트 형식(질문, 정답)으로만 응답해."
            # (실제 구현 시 JSON 파싱 로직 추가 권장, 여기선 간략화)
            st.session_state.problems = ["문제1 내용", "문제2 내용", "문제3 내용"] # 예시 데이터
            st.session_state.step = 3
            st.rerun()

elif st.session_state.step == 3:
    # 3초 카운트다운
    placeholder = st.empty()
    for i in range(3, 0, -1):
        placeholder.write(f"### {i}초 후 시작합니다!")
        time.sleep(1)
    placeholder.empty()
    st.session_state.step = 4
    st.rerun()

elif st.session_state.step == 4:
    idx = st.session_state.current_idx
    if idx < len(st.session_state.problems):
        st.subheader(f"문제 {idx + 1}")
        st.write(st.session_state.problems[idx])
        if st.button("다음 문제"):
            st.session_state.current_idx += 1
            st.rerun()
    else:
        st.success("모든 문제를 푸셨습니다! 정답을 공개합니다.")
        st.write("--- 정답지 ---")
        # 정답 출력 로직
