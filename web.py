import streamlit as st
from functions import *

todos = get_todos()

st.title("Gimu")
st.subheader("Basic to-do web app")

for todo in todos:
    st.checkbox(todo)

st.text_input("Add new to-do", placeholder="Add new to-do", label_visibility="hidden")
