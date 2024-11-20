import streamlit as st

# HTML, CSS, JavaScript 코드 작성
st.markdown("""
    <style>
        .text {
            font-size: 100pt;
            opacity: 0;
            transition: opacity 1s ease-in-out;
        }
        .text.show {
            opacity: 1;
        }
    </style>

    <div id="text1" class="text">텍스트 1</div>
    <div id="text2" class="text">텍스트 2</div>
    <div id="text3" class="text">텍스트 3</div>
    <div id="text4" class="text">텍스트 4</div>
    <div id="text5" class="text">텍스트 5</div>

    <script>
        // Intersection Observer API 사용하여 스크롤 시 텍스트 나타나게 하기
        const texts = document.querySelectorAll('.text');
        
        // 텍스트가 화면에 들어오면 show 클래스를 추가하여 opacity를 1로 설정
        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('show');
                    observer.unobserve(entry.target);  // 이미 보였으면 감시 중지
                }
            });
        }, { threshold: 0.5 });  // 50% 이상 보이면 효과 적용
        
        // 각 텍스트에 대해 Intersection Observer 설정
        texts.forEach(text => {
            observer.observe(text);
        });
    </script>
""", unsafe_allow_html=True)
