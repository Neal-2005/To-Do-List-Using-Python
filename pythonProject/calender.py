import streamlit as st
import functions
from streamlit_calendar import calendar
from datetime import datetime

# Load Tasks
todos = functions.get_todo()

# Prepare Data for Calendar
events = []
for todo in todos:
    try:
        task, deadline = todo.strip().split(" | ")
        events.append({
            "title": task,
            "start": deadline,
            "end": deadline,
            "color": "#FF5733" if datetime.strptime(deadline, "%Y-%m-%d") < datetime.today() else "#4CAF50"
        })
    except ValueError:
        st.error(f"Invalid task format: {todo}")

# Calendar Display
st.title("📅 Calendar View")
calendar(events=events, options={"initialView": "dayGridMonth"})

# Navigation Back to Main
st.page_link("app.py", label="⬅️ Back to To-Do List")