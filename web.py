import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    session_todo = st.session_state["new_todo"]
    todos.append(session_todo+"\n")
    functions.write_todos(todos)



st.title("Andrew Gotham's ToDo App")
# st.subheader("Never stop learnin'!")
# st.write("This is just the text.")
st.text_input(label = "", placeholder = "Enter a todo", on_change=add_todo, key="new_todo")

for todo in todos:
    st.checkbox(todo)

# for debugging
st.session_state