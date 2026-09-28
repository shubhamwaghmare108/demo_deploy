import streamlit as st
import pandas as pd
from datetime import date
from pathlib import Path

path = Path(__file__).resolve().parent

st.title("Welcome to My Streamlit App")
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
})

st.metric("Accuracy", "92%")
name = st.text_input("Enter your name:",max_chars=5)
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1,value = 100)
#dob = st.date_input("Enter your date of birth:",)
dob = st.date_input(
    "Date of Birth:",
    min_value=date(1990, 1, 1),
    max_value=date(2100, 12, 31),
    value=date(2026, 1, 1)
)
gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
interests = st.multiselect("Select your interests:", ["Technology", "Sports", "Music", "Travel"])
terms_agreed = st.checkbox("I agree to the terms and conditions")
selected_option = st.radio("Select an option:", ["Option 1", "Option 2", "Option 3"])
terms_toggle = st.toggle("I agree to the terms and conditions")
additional_info = st.text_area("Additional Information:", height=100)
file_upload = st.file_uploader("Upload a file:")
color = st.color_picker("Pick a color:")
value = st.slider("Select a value:", min_value=0, max_value=100, value=50)
submit_button = st.button("Upload Folder")

if st.button("Submit"):
    st.switch_page(path / "pages" / "divert.py")
    

"""st.text(f"Hello, {name}! Welcome to my Streamlit app!")
st.text(f"You are {age} years old.")
st.text(f"Your date of birth is {dob}.")
st.text(f"Your gender is {gender}.")
st.text(f"Your interests are: {', '.join(interests)}.")
st.text(f"Selected value is {value}.")

st.text("This is a simple example of a Streamlit application.")
st.write(additional_info)
st.write("Here is a sample DataFrame:")
st.write(df)
st.dataframe(df)

data = {
    "name": "Shubham",
    "role": "Data Scientist",
    "experience": 3
}

st.write(data)

models = ["YOLO", "OSNet", "ByteTrack"]

st.write(models)"""