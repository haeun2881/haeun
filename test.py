import streamlit as st

st.set_page_config(
    page_title = "BMI 계산기",
    page_icon = "🎂",
)

st.title("BMI 계산기")
st.write("키, 체중을 입력해 BMI를 계산해봅시다.")

키 = st.number_input("키를 입력하세요", step=1, value=170)
체중 = st.number_input("체중을 입력하세요.")
키 = 키/100
bmi = 체중/(키*키)
st.write(f"당신의 BMI지수는 {bmi}")

if bmi<18.5:
    st.write("저체중입니다.")
elif bmi<22.9:
    st.write("정상입니다.")
elif bmi<24.9:
    st.write("과체중입니다.")
elif bmi<29.9:
    st.write("경도비만입니다.")
else:
    st.write("고도비만입니다.")