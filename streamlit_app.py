import streamlit as st

# HTML, CSS, JavaScript 코드 작성
st.markdown("""
    <style>
        .text {
            font-size: 100pt;
            transition: font-size 0.2s ease;
            display: inline-block;
            opacity: 1;
        }
        
        .text:hover {
            font-size: 200pt;
        }
        
        .text.hidden {
            opacity: 0;
        }
    </style>

    <div id="text1" class="text">텍스트 1</div>
    <div id="text2" class="text">텍스트 2</div>
    <div id="text3" class="text">텍스트 3</div>
    <div id="text4" class="text">텍스트 4</div>
    <div id="text5" class="text">텍스트 5</div>

    <script>
        // 텍스트가 200pt 이상으로 커지면 숨기기
        const texts = document.querySelectorAll('.text');
        
        texts.forEach(text => {
            text.addEventListener('transitionend', () => {
                if (parseFloat(getComputedStyle(text).fontSize) >= 200) {
                    text.classList.add('hidden');
                }
            });
        });
    </script>
""", unsafe_allow_html=True)
