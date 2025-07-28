#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import os
from fpdf import FPDF
from io import BytesIO

# Paths
DATA_PATH = "../data/assigned_tasks.csv"
FONT_PATH = r"C:\Users\Admin\ai_task_manager\fonts\DejaVuSans\ttf"

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    return df

df = load_data()
users = df["assigned_to"].dropna().unique()

# Streamlit UI
st.set_page_config(page_title="User Task Report", layout="centered")
st.title("📋 User Task Report Generator")

selected_user = st.selectbox("Select a user:", sorted(users))

if selected_user:
    user_df = df[df["assigned_to"].str.lower() == selected_user.lower()]
    
    if user_df.empty:
        st.warning(f"No tasks found for user: {selected_user}")
    else:
        st.success(f"Found {len(user_df)} tasks for user: {selected_user}")
        st.dataframe(user_df)

        # Generate PDF
        def generate_pdf(data, user):
            pdf = FPDF()
            pdf.add_page()
            pdf.add_font("DejaVu", "", os.path.join(FONT_PATH, "DejaVuSans.ttf"), uni=True)
            pdf.add_font("DejaVu", "B", os.path.join(FONT_PATH, "DejaVuSans-Bold.ttf"), uni=True)
            pdf.set_font("DejaVu", "B", 16)
            pdf.cell(200, 10, f"📋 Task Report for {user}", ln=True, align="C")
            
            pdf.set_font("DejaVu", "", 12)
            pdf.ln(10)
            pdf.cell(200, 10, f"✅ Total Tasks: {len(data)}", ln=True)

            pdf.ln(5)
            pdf.set_font("DejaVu", "B", 11)
            pdf.cell(20, 8, "ID", border=1)
            pdf.cell(80, 8, "📝 Description", border=1)
            pdf.cell(30, 8, "📅 Deadline", border=1)
            pdf.cell(30, 8, "⚡ Priority", border=1)
            pdf.cell(30, 8, "🔮 Predicted", border=1)
            pdf.ln()

            pdf.set_font("DejaVu", "", 10)
            for _, row in data.iterrows():
                pdf.cell(20, 8, str(row["task_id"]), border=1)
                pdf.cell(80, 8, str(row["description"])[:40], border=1)
                pdf.cell(30, 8, str(row["deadline"]), border=1)
                pdf.cell(30, 8, str(row["priority"]), border=1)
                pdf.cell(30, 8, str(row["predicted_priority"]), border=1)
                pdf.ln()

            # Output to BytesIO
            buffer = BytesIO()
            pdf.output(buffer)
            buffer.seek(0)
            return buffer

        if st.button("📄 Generate PDF Report"):
            pdf_bytes = generate_pdf(user_df, selected_user)
            st.success("PDF Report Generated ✅")

            st.download_button(
                label="📥 Download PDF",
                data=pdf_bytes,
                file_name=f"{selected_user}_report.pdf",
                mime="application/pdf"
            )


# In[ ]:




