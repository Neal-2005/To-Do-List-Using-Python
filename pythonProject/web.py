import streamlit as st
import functions
import smtplib
from email.message import EmailMessage
from streamlit_calendar import calendar
from datetime import datetime, timedelta

todos = functions.get_todo()

# Initialize session state for calendar visibility
if 'show_calendar' not in st.session_state:
    st.session_state['show_calendar'] = False

# Initialize session state for user email
if 'user_email' not in st.session_state:
    st.session_state['user_email'] = ""

# Email sending function
def send_email(task, deadline):
    email = st.session_state['user_email']
    msg = EmailMessage()
    msg['Subject'] = f'Reminder: {task} is Due Soon!'
    msg['From'] = 'mhatreneal@gmail.com'
    msg['To'] = email
    msg.set_content(f"Reminder: Your task '{task}' is due on {deadline}. Please take action accordingly.")

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login('mhatreneal@gmail.com', 'rbfm voky gtdb vnke')
            smtp.send_message(msg)
            st.success(f"Email reminder successfully sent to {email}")
    except Exception as e:
        st.error(f"Error: {e}")

# Function to add a task with a deadline

def add_todo():
    task = st.session_state["new_todo"]
    deadline = st.session_state["deadline"].strftime("%Y-%m-%d")
    formatted_task = f"{task} | {deadline}\n"
    todos.append(formatted_task)
    functions.write_todo(todos)
    st.rerun()


def complete_task(index):
    del todos[index]
    functions.write_todo(todos)
    st.rerun()

def toggle_calendar():
    st.session_state['show_calendar'] = not st.session_state['show_calendar']


def get_status(deadline):
    today = datetime.today().date()
    deadline_date = datetime.strptime(deadline, "%Y-%m-%d").date()

    if deadline_date < today:
        return "❗ Overdue"
    elif deadline_date == today:
        return "⚠️ Due Today"
    elif (deadline_date - today).days <= 3:
        return "⏳ Due Soon"
    else:
        return "🟢 Upcoming"

# Prepare events for the calendar
events = []
color_map = {
    "❗ Overdue": "#FF5733",
    "⚠️ Due Today": "#FFC300",
    "⏳ Due Soon": "#FFA500",
    "🟢 Upcoming": "#4CAF50"
}

for todo in todos:
    parts = todo.strip().split(" | ")
    if len(parts) == 2:  # Ensure proper format
        task, deadline = parts
        status = get_status(deadline)
        if status in ["⚠️ Due Today", "❗ Overdue"]:
            send_email(task, deadline)
        events.append({
            "title": f"{task} ({status})",
            "start": deadline,
            "end": deadline,
            "color": color_map[status]
        })
    else:
        st.warning(f"Skipping invalid task format: {todo.strip()}")

# To-Do List
st.title("📝 My Todo-App")

# User email input at the start
st.session_state['user_email'] = st.text_input("Enter your Email for Reminders", value=st.session_state['user_email'])

st.text_input("Enter To-Do...", key="new_todo")
st.date_input("Set Deadline", key="deadline")
st.button("Add Task", on_click=add_todo)

# Filter Selection
filter_option = st.selectbox("Filter by Deadline Status", ["All", "Upcoming", "Past", "Today"])

# Display Task List
st.subheader("Task List")
for index, todo in enumerate(todos):
    parts = todo.strip().split(" | ")
    if len(parts) == 2:
        task, deadline = parts
        status = get_status(deadline)

        if filter_option == "All" or \
           (filter_option == "Upcoming" and status == "🟢 Upcoming") or \
           (filter_option == "Past" and status == "❗ Overdue") or \
           (filter_option == "Today" and status == "⚠️ Due Today"):

            col1, col2 = st.columns([0.8, 0.2])
            with col1:
                st.markdown(f"- {status} **{task}** | 📅 {deadline}")
            with col2:
                if st.button("✅", key=f"done_{index}"):
                    complete_task(index)

# Calendar Section
if st.button("📅 Show/Hide Calendar View", on_click=toggle_calendar):
    pass

if st.session_state['show_calendar']:
    st.title("📅 Calendar View")
    if events:
        calendar(events=events, options={"initialView": "dayGridMonth"})
    else:
        st.info("No tasks available for the calendar.")
