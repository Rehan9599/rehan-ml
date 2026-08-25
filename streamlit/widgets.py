import streamlit as st

st.title("Streamlit app")

name=st.text_input("enetr your name")
age=st.slider("select age",0,100,25)
options=['a','b','s']
choice=st.selectbox("choose your otion:", options)
st.write(f"ypur selected {choice}")
if name and age:
    st.write(f"heloo {name} your age is {age}")