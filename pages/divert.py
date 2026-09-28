import streamlit as st
import time
from pathlib import Path

path = Path(__file__).resolve().parent

st.success("Operation completed successfully!")
st.snow()
time.sleep(10)
st.toast("Diverted to another page!", icon="🎉")
st.switch_page(path / "login.py")