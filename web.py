import streamlit as st
from functions import *

todos = get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos)
    st.session_state["new_todo"] = ""

st.title("Gimu")
st.subheader("Basic to-do web app")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{index}.{todo}")
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[f"{index}.{todo}"]
        st.rerun()

st.text_input("Add new to-do", placeholder="Add new to-do",
              label_visibility="hidden", on_change=add_todo, key="new_todo")