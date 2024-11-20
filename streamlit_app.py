import streamlit as st

# 타이틀
st.title('스크롤 내릴 때 소주제가 하나씩 뜨는 예시')

# 소주제 목록 (예시)
subtopics = [
    "소주제 1", "소주제 2", "소주제 3", "소주제 4", "소주제 5", 
    "소주제 6", "소주제 7", "소주제 8", "소주제 9", "소주제 10", 
    "소주제 11", "소주제 12", "소주제 13", "소주제 14", "소주제 15",
    "소주제 16", "소주제 17", "소주제 18", "소주제 19", "소주제 20"
]

# 세션 상태를 이용하여 표시할 소주제의 인덱스를 추적
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# 10개씩 소주제 보여주기
for i in range(st.session_state.current_index, min(st.session_state.current_index + 10, len(subtopics))):
    st.subheader(subtopics[i])
    st.write(f"{subtopics[i]}에 대한 내용이 여기에 있습니다.")

# 더 보기 버튼
if st.session_state.current_index + 10 < len(subtopics):
    if st.button("더 보기"):
        st.session_state.current_index += 10
