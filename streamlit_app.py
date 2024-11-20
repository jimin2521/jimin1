import streamlit as st
import time

# 타이틀
st.title('스크롤에 따라 소주제들이 나타나는 예시')

# 소주제 목록
subtopics = [
    "소주제 1", "소주제 2", "소주제 3", "소주제 4", "소주제 5", 
    "소주제 6", "소주제 7", "소주제 8", "소주제 9", "소주제 10", 
    "소주제 11", "소주제 12", "소주제 13", "소주제 14", "소주제 15",
    "소주제 16", "소주제 17", "소주제 18", "소주제 19", "소주제 20"
]

# 소주제를 10개씩 표시하도록 설정
for i in range(0, len(subtopics), 10):
    for j in range(i, min(i + 10, len(subtopics))):
        with st.expander(subtopics[j]):
            st.write(f"{subtopics[j]}에 대한 내용이 여기에 있습니다.")
            time.sleep(0.1)  # 애니메이션 효과를 위해 잠시 대기
