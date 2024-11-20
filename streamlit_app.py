import streamlit as st

# 5개의 열을 생성
columns = st.columns(5)

# 각 열에 텍스트를 삽입
for i in range(5):
    columns[i].write(f"열 {i+1}")

# 각 열에 버튼 추가 예시
for i in range(5):
    if columns[i].button(f"버튼 {i+1}"):
        st.write(f"버튼 {i+1}이 클릭되었습니다!")
