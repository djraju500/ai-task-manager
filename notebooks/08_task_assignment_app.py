#!/usr/bin/env python
# coding: utf-8

# In[19]:


import streamlit as st
import pandas as pd
import os
from datetime import datetime, date

# Paths
USERS_FILE = "data/users.csv"
TASKS_FILE = "data/task_data.csv"

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

# ------------------------- Helper Functions -------------------------

def load_users():
    if os.path.exists(USERS_FILE):
        return pd.read_csv(USERS_FILE)
    else:
        return pd.DataFrame(columns=["username", "password", "role"])

def save_users(users):
    users.to_csv(USERS_FILE, index=False)

def load_tasks():
    if os.path.exists(TASKS_FILE):
        return pd.read_csv(TASKS_FILE)
    else:
        return pd.DataFrame(columns=["task_id", "description", "deadline", "assigned_to", "status", "priority", "category"])

def save_tasks(tasks):
    tasks.to_csv(TASKS_FILE, index=False)

def register_user(username, password, role):
    users = load_users()
    if username in users['username'].values:
        return False
    users = pd.concat([users, pd.DataFrame([[username, password, role]], columns=users.columns)], ignore_index=True)
    save_users(users)
    return True

def authenticate_user(username, password):
    users = load_users()
    user = users[(users['username'] == username) & (users['password'] == password)]
    if not user.empty:
        return user.iloc[0].to_dict()
    return None

def generate_task_id(tasks_df):
    if tasks_df.empty:
        return "T000"
    else:
        last_id = str(tasks_df["task_id"].iloc[-1])  # Convert to string safely
        if last_id.startswith("T") and last_id[1:].isdigit():
            num = int(last_id[1:])
        else:
            num = 0  # fallback if ID format is unexpected
        return f"T{num+1:03d}"


# ------------------------- UI Components -------------------------

def show_registration():
    st.subheader("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["admin", "member"])
    if st.button("Register"):
        if register_user(username, password, role):
            st.success("User registered successfully.")
        else:
            st.error("Username already exists.")

def show_login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = authenticate_user(username, password)
        if user:
            st.session_state.logged_in = True
            st.session_state.user = user
            st.success(f"Welcome, {user['username']} ({user['role']})")
        else:
            st.error("Invalid credentials")

def show_task_assignment(user):
    st.subheader("Assign Task (Admin Only)")
    tasks_df = load_tasks()
    users_df = load_users()

    if user["role"] != "admin":
        st.warning("Only admin can assign tasks.")
        return

    task_id = generate_task_id(tasks_df)
    description = st.text_area("Task Description")
    deadline = st.date_input("Deadline", min_value=date.today())

    members = users_df[users_df["role"] == "member"]["username"].tolist()
    if not members:
        st.warning("No members available to assign tasks.")
        return

    assigned_to = st.selectbox("Assign To", members)
    status = st.selectbox("Status", ["Not Started", "In Progress", "Completed"])
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])
    category = st.selectbox("Category", ["Bug", "Feature", "Improvement", "Research", "Other"])

    if st.button("Assign Task"):
        new_task = pd.DataFrame([[task_id, description, deadline.strftime("%Y-%m-%d"), assigned_to, status, priority, category]],
                                columns=tasks_df.columns)
        tasks_df = pd.concat([tasks_df, new_task], ignore_index=True)
        save_tasks(tasks_df)
        st.success(f"Task {task_id} assigned to {assigned_to}.")

def show_user_tasks(user):
    st.subheader("My Tasks")
    tasks_df = load_tasks()
    user_tasks = tasks_df[tasks_df["assigned_to"] == user["username"]]
    if not user_tasks.empty:
        st.dataframe(user_tasks)
    else:
        st.info("No tasks assigned to you yet.")

# ------------------------- Main App -------------------------

def main():
    st.title("🧠 AI Task Management System")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.user = None

    menu = st.sidebar.selectbox("Menu", ["Login", "Register"])

    if not st.session_state.logged_in:
        if menu == "Login":
            show_login()
        elif menu == "Register":
            show_registration()
    else:
        st.sidebar.success(f"Logged in as: {st.session_state.user['username']}")
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.experimental_rerun()

        if st.session_state.user["role"] == "admin":
            show_task_assignment(st.session_state.user)
        show_user_tasks(st.session_state.user)

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




