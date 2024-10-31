import streamlit as st

st.write("다음 중 프로그래밍에 대한 설명으로 가장 적절한 것은?")
결과 = st.radio("보기",["python을 배운다.",
               '10주동안 수업을 한다.',
               '3번 결석해도 괜찮다.',
               '재미없다.'])


btn = st.button("정답확인")
if btn:
    if 결과 == "python을 배운다.":
        st.success("정답!!")
        st.balloons()
    else:
        st.error("오답!!")



slider = st.select_slider("반을 선택하세요",
                          ['1반','2반','3반','4반'])



st.metric("Wind","2m/s",'-2%')

과학 = st.multiselect("과학탐구 과목을 선택하세요.",
                    ['물리','화학','생명','지구과학'], max_selections=2)

과목 = st.selectbox("과목을 선택하세요",
                  ["확률과 통계",'미분과 적분','기하와 백터'])
st.write("당신이 선택한 과목은 "+과목+"입니다.")



색상 = st.radio("당신이 좋아하는 색상은?",
              ["빨강","노랑","파랑"])

st.write(색상+"을 좋아하시네요?")



짜장면 = st.checkbox("짜장면 5000원")
짬뽕 = st.checkbox("짬뽕 6000원")
탕수육 = st.checkbox("탕수육 12000원")

가격 = 0
if 짜장면:
    가격+=5000
if 짬뽕:
    가격+=6000
if 탕수육:
    가격+=12000

if 가격 !=0:
    st.write(str(가격)+"원 입니다.")



st.title("😎 title")
st.header("header")
st.subheader("subheader")
st.write("**서하은**님 안녕하세요")
st.write(":red[함지고등학교]")

st.title("로그인")
id = st.text_input("아이디")
pw = st.text_input("비밀번호",
                   type='password')
btn = st.button("확인")

if btn:
    if id == 'abc' and pw == '123':
        st.success("로그인 성공!!")
    else:
        st.error("로그인 실패!!")