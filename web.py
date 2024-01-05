import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.set_todos(todos)


def submit():
    st.session_state.input = st.session_state.new_todo
    st.session_state.new_todo = ''


st.title("Todo")
st.subheader("This is a Todo App.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    state = st.checkbox(todo, key=todo)
    if state:
        todos.pop(index)
        functions.set_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input("New todo",
              placeholder="Add new todo...",
              on_change=add_todo,
              key="new_todo")


