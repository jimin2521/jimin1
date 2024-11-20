import streamlit as st

# 왼쪽 상단에 버튼을 만들어 메뉴를 트는 기능 구현
if st.button("#"):
    # 버튼 클릭 시 4개의 메뉴가 표시됨
    menu = st.radio("메뉴 선택", ["메뉴 1", "메뉴 2", "메뉴 3", "메뉴 4"])
    
    # 선택된 메뉴에 대한 콘텐츠 표시
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
