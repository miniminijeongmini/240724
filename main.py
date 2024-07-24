import streamlit as st
st.title('나의 첫 번째 웹 시비스')
name=st.text_input('이름을 입력해주세요:')
menu=st.selectbox('좋아하는 음식을 선택하세요!', ['우유 빙수' , '슈립프 버거' , '치킨너겟'])
if st.button('인사말 생성'):
  st.write(f'안녕하세요!(name)님! 당신이 좋아하는 음식은 (menu)이군요! 너무 맛있겠군요! 반갑습니다!:)')
