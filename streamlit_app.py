import streamlit as st
import time

# 제목
st.title("스크롤하면 점진적으로 나타나는 소주제들")

# 텍스트를 점진적으로 표시하는 함수
def gradually_reveal_text(text_list, interval=0.5):
    for text in text_list:
        st.subheader(text)  # 각 소주제는 subheader로 출력
        time.sleep(interval)

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

gradually_reveal_text(subtopics)
