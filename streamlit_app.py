import streamlit as st

# '메뉴 열기' 버튼을 누르면 새 창을 띄우는 방식
if st.button("메뉴 열기"):
    st.markdown(
        """
        <script type="text/javascript">
            window.open("data:text/html,<html><head><title>메뉴</title></head>
            <body>
                 if menu == "메뉴 1":
        st.write("메뉴 1이 선택되었습니다.")
    elif menu == "메뉴 2":
        st.write("메뉴 2가 선택되었습니다.")
    elif menu == "메뉴 3":
        st.write("메뉴 3이 선택되었습니다.")
    elif menu == "메뉴 4":
        st.write("메뉴 4가 선택되었습니다.")
else:
    st.write("왼쪽 상단의 버튼을 클릭하여 메뉴를 열 수 있습니다.")
