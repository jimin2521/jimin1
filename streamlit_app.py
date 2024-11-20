import streamlit as st

# HTML, CSS 코드 작성
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
    
    <div class="subtopic" onclick="window.open('https://www.example.com', '_blank')">소주제 1</div>
    <div class="subtopic" onclick="window.open('https://www.example.com', '_blank')">소주제 2</div>
    <div class="subtopic" onclick="window.open('https://www.example.com', '_blank')">소주제 3</div>
    <div class="subtopic" onclick="window.open('https://www.example.com', '_blank')">소주제 4</div>
    <div class="subtopic" onclick="window.open('https://www.example.com', '_blank')">소주제 5</div>
""", unsafe_allow_html=True)
