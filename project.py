import streamlit as st

pages = {
    "가입" : [
        st.Page("login.py", title="로그인"),
        st.Page("b.py", title="회원가입")
    ],
    "카테고리명2" : [
        st.Page("c.py", title="C페이지"),
        st.Page("d.py", title="D페이지")
    ]
}
pg = st.navigation(pages)
pg.run()