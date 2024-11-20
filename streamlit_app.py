import streamlit as st

# '메뉴 열기' 버튼을 누르면 새 창을 띄우는 방식
if st.button("메뉴 열기"):
    st.markdown(
        """
        <script type="text/javascript">
            window.open("data:text/html,<html><head><title>메뉴</title></head>
            <body>
                <h2>메뉴 선택</h2>
                <ul>
                    <li><a href="#">메뉴 1</a></li>
                    <li><a href="#">메뉴 2</a></li>
                    <li><a href="#">메뉴 3</a></li>
                    <li><a href="#">메뉴 4</a></li>
                </ul>
            </body></html>", "_blank");
        </script>
        """, unsafe_allow_html=True
    )
