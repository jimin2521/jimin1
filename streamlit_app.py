import streamlit as st

# HTML과 CSS를 사용하여 소주제 클릭 시 새 창 열리게 하기
st.markdown("""
    <style>
        .subtopic {
            font-size: 20px;
            color: #007bff;
            cursor: pointer;
            text-decoration: underline;
        }

        .subtopic:hover {
            color: #0056b3;
        }
    </style>
    
    <div class="subtopic"><a href="https://www.example.com" target="_blank">소주제 1</a></div>
    <div class="subtopic"><a href="https://www.example.com" target="_blank">소주제 2</a></div>
    <div class="subtopic"><a href="https://www.example.com" target="_blank">소주제 3</a></div>
    <div class="subtopic"><a href="https://www.example.com" target="_blank">소주제 4</a></div>
    <div class="subtopic"><a href="https://www.example.com" target="_blank">소주제 5</a></div>
import streamlit as st

# HTML과 CSS를 사용하여 소주제 클릭 시 새 창 열리게 하기
st.markdown("""
    <style>
        .subtopic {
            font-size: 20px;
            color: #007bff;
            cursor: pointer;
            text-decoration: underline;
        }

        .subtopic:hover {
            color: #0056b3;
        }
    </style>
    
    <div class="subtopic"><a href="http://localhost:8501/hello.html" target="_blank">소주제 1</a></div>
    <div class="subtopic"><a href="http://localhost:8501/hello.html" target="_blank">소주제 2</a></div>
    <div class="subtopic"><a href="http://localhost:8501/hello.html" target="_blank">소주제 3</a></div>
    <div class="subtopic"><a href="http://localhost:8501/hello.html" target="_blank">소주제 4</a></div>
    <div class="subtopic"><a href="http://localhost:8501/hello.html" target="_blank">소주제 5</a></div>
""", unsafe_allow_html=True)

