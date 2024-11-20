import streamlit as st

# HTML 및 CSS 코드 작성
st.markdown("""
    <style>
    .hover-text {
        font-size: 100px;
        transition: font-size 0.3s ease;
    }
    .hover-text:hover {
        font-size: 200px;
    }
    </style>
    <div class="hover-text">텍스트 1</div>
    <div class="hover-text">텍스트 2</div>
    <div class="hover-text">텍스트 3</div>
    <div class="hover-text">텍스트 4</div>
    <div class="hover-text">텍스트 5</div>
""", unsafe_allow_html=True)
