import streamlit as st

# 웹페이지 타이틀
st.title('Streamlit 웹페이지 예제')

# 텍스트
st.header('여기는 헤더입니다')
st.subheader('여기는 서브헤더입니다')
st.write('Streamlit을 이용하여 빠르게 웹 애플리케이션을 만들 수 있습니다.')

# 버튼 추가
if st.button('버튼을 클릭해보세요'):
    st.write('버튼이 클릭되었습니다!')

# 입력 폼
name = st.text_input('이름을 입력하세요')
if name:
    st.write(f'안녕하세요, {name}님!')

# 슬라이더
age = st.slider('나이를 선택하세요', 0, 100, 25)
st.write(f'당신의 나이는 {age}세입니다.')

# 차트 (간단한 데이터 예시)
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'x': np.arange(1, 11),
    'y': np.random.randn(10)
})
st.line_chart(df)
