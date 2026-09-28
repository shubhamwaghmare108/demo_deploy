import streamlit as st
username = st.text_input("Username:")

password = st.text_input("Password:", type="password")

if st.button("Login"):
    if username == "admin" and password == "123":
        st.success("Login successful!")
        st.switch_page("app.py")
    else:
        st.error("Invalid username or password.")