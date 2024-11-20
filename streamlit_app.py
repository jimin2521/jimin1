import streamlit as st

# CSS를 사용하여 배경색을 하얀색으로 설정
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: white;
    }
    .main {
        background-color: white;
    }
    </style>
    """, unsafe_allow_html=True
)

# 나머지 Streamlit 코드
st.title("배경이 하얀색인 Streamlit 앱")
st.write("배경색을 하얀색으로 설정한 예시입니다.")
