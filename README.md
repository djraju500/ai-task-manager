# AI Task Manager

A privacy-focused, AI-powered Task Management System that classifies, prioritizes, and assigns tasks intelligently using NLP and ML models. Designed with features like admin-only task assignment, deadline validations, task timelines, and more.
---
Project 1: AI-Powered Task Management System

Problem Statement: Design and develop an intelligent task management system that leverages NLP and ML techniques to
automatically classify, prioritize, and assign tasks to users based on their behavior, deadlines, and
workloads.

---

## 🚀 Features

- ✅ Task Classification (Naive Bayes, SVM)
- 🔢 Priority Prediction (Random Forest/XGBoost)
- 👥 Admin-only Task Assignment with Role-based Login
- 🕒 Deadline Validation (No Past Dates)
- 🔄 Task Status Tracking (In Progress, Completed)
- 📊 Visual Timelines using Plotly
- 🔐 Login & Password
- 📁 Auto Save/Append to `task_data.csv`

---

## 🧠 Models Used
- TfidfVectorizer for NLP
- Naive Bayes / SVM for task classification
- Random Forest / XGBoost for priority prediction

---

## 🗂️ Project Structure

```bash
ai_task_manager/
├── data/
│   ├── assigned_tasks.csv
│   ├── task_data.csv
│   └── cleaned_task_data.csv
├── fonts/DejaVuSans
├── models/
│   ├── priority_label_encoder.pkl
│   ├── priority_predictor_nb.pkl
│   ├── priority_predictor_rf.pkl
│   ├── priority_predictor_svm.pkl
│   ├── priority_predictor_xgb.pkl
│   ├── task_classifier_nb.pkl
│   ├── task_classifier_svm.pkl
│   └── tfidf_vectorizer.pkl
|
├── notebooks/
│        ├──data/
│        |   ├── task_data.csv
│        |   └── users.csv
│        ├── 01_data_preprocessing.ipynb
|        ├── 02_task_classification.ipynb
│        ├── 03_priority_prediction.ipynb
│        ├── 04_task_assignment.ipynb
|        ├── 05_generate_report.ipynb
|        ├── 06_user_report.ipynb
|        ├── 07_user_task_assign_check_app.py
│        └── 08_task_assignment_app.py
├── reports/
│      ├── figures/
│      |      ├── priority_pie.png
│      |      └── tasks_per_user.png
│      ├── users/
│      |     ├── alice_report.pdf
│      |     ├── bob_report.pdf
│      |     ├── Charlie_report.pdf
│      |     └── Diana_report.pdf
│      └── final_report.pdf
├── requirements.txt
└── README.md
```

---

## 📦 Installation

```bash
# 1. Clone your repository
git clone https://github.com/djraju500/ai-task-manager.git

# 2. Navigate into the project directory
cd ai-task-manager

# 3. Create and activate a virtual environment (optional but recommended)
py -m venv venv
venv\Scripts\activate      # On Windows
# source venv/bin/activate # On macOS/Linux

# 4. Install all required packages
pip install -r requirements.txt

# 5. Run the Streamlit app
streamlit run notebooks/08_task_assignment_app.py
```

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Contribution Guide

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Added new feature"`
4. Push to the branch: `git push origin feature-name`
5. Open a Pull Request

---

## 🌐 GitHub Pages Documentation

GitHub Pages deployed from the `/docs` folder.

To update:
1. Add markdown notebooks or docs to `/docs`
2. Commit & push changes
3. GitHub will auto-deploy at:

```
https://github.com/djraju500/ai-task-manager
```

---

## 🤝 Contact

Developed by [Rajesh Ghorpade](https://github.com/djraju500)

📧 Email: rajesh.ghorpade500@gmail.com
