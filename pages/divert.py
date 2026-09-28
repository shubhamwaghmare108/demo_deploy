import streamlit as st
import time
st.success("Operation completed successfully!")
st.snow()
time.sleep(10)
st.toast("Diverted to another page!", icon="🎉")
st.switch_page("pages/login.py")