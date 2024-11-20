import streamlit as st
import time

# 제목
st.title("스크롤하면 점진적으로 나타나는 소주제들")

# 텍스트를 점진적으로 표시하는 함수
def gradually_reveal_text_on_scroll(text_list):
    # 세션 상태에서 카운터를 설정하여 스크롤할 때마다 카운터를 증가시킴
    if 'counter' not in st.session_state:
        st.session_state.counter = 0

    # 페이지에 소주제 하나씩 추가
    num_displayed = st.session_state.counter
    for i in range(num_displayed):
        st.subheader(text_list[i])

    # 스크롤해서 카운터를 증가시키는 기능
    if num_displayed < len(text_list):
        st.session_state.counter += 1
        st.text('스크롤하여 계속 보기')

# 10개의 소주제 리스트
subtopics = [
    "소주제 1: 데이터 분석의 기초",
    "소주제 2: Python 프로그래밍",
    "소주제 3: 머신 러닝 기초",
    "소주제 4: 딥러닝의 원리",
    "소주제 5: 자연어 처리",
    "소주제 6: 데이터 시각화",
    "소주제 7: 웹 개발 기초",
    "소주제 8: 클라우드 컴퓨팅",
    "소주제 9: 인공지능 윤리",
    "소주제 10: AI의 미래"
]

gradually_reveal_text_on_scroll(subtopics)
