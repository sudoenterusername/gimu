import streamlit as st
from functions import *

todos = get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    write_todos(todos)

st.title("Gimu")
st.subheader("Basic to-do web app")

for todo in todos:
    st.checkbox(todo)

st.text_input("Add new to-do", placeholder="Add new to-do",
              label_visibility="hidden", on_change=add_todo, key="new_todo")

st.session_state
