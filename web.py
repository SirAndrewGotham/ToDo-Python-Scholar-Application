import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    session_todo = st.session_state["new_todo"] + "\n"
    todos.append(session_todo)
    functions.write_todos(todos)



st.title("Andrew Gotham's ToDo App")
# st.subheader("Never stop learnin'!")
# st.write("<p>This is just a text.</p>", unsafe_allow_html=True)
st.text_input(label = "", placeholder = "Enter a todo", on_change=add_todo, key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

# for debugging
# st.session_state