import streamlit as st
import functions

todos  = functions.get_todo()
def add_todo():
    todo = st.session_state["new_todo"] + '\n' #session state is like a dictionary
    todos.append(todo)
    functions.write_todo(todos)





st.title("My Todo-App")
st.subheader("This is my To-Do project")
st.write("This app is for increasing your productivity")



for todo in todos:
    st.checkbox(todo)


st.text_input(label = "", placeholder="Enter To-Do...",
              on_change = add_todo, key = "new_todo")



