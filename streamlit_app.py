import streamlit as st

# '메뉴 열기' 버튼을 누르면 새 창을 띄우는 방식
if st.button("메뉴 열기"):
    st.markdown(
        """
        <script type="text/javascript">
            window.open("data:text/html,<html><head><title>하얀 화면</title></head>
            <body style='background-color: white;'>
                <h2>하얀 화면입니다!</h2>
            </body></html>", "_blank");
        </script>
        """, unsafe_allow_html=True
    )

