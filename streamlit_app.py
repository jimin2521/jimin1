import streamlit as st
import time

# 제목
st.title("스크롤하면 글이 점점 나타나는 예제")

# 텍스트를 점진적으로 표시하는 함수
def gradually_reveal_text(text, interval=0.1):
    # 글자를 한글자씩 표시
    for i in range(len(text) + 1):
        st.write(text[:i])
        time.sleep(interval)

# 예시 텍스트
sample_text = "이 텍스트는 스크롤하면서 점차적으로 나타납니다. 스크롤을 계속 해보세요!"

gradually_reveal_text(sample_text)
