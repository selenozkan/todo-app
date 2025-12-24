# To-Do List App (CLI · Desktop GUI · Web)

A simple desktop To-Do List application. It allows users to manage their tasks through a user-friendly graphical interface. Users can add, edit, complete, and remove tasks — all saved locally in a `.txt` file. This project is developed as a part of Udemy course.

This repository contains **three versions of the same To-Do List application**, all sharing the same core logic:

1. **Command-line version** (CLI)
2. **Desktop GUI version** (FreeSimpleGUI)
3. **Web version** (Streamlit – deployed)

All three versions reuse the same backend logic (`functions.py`) and persist tasks in `todos.txt`.


---

## 📂 Project Structure

```
todo-app/
├── functions.py     # Shared todo logic
├── todos.txt        # Persistent storage for tasks
├── cli.py           # Command-line interface version
├── gui.py           # Desktop GUI version (FreeSimpleGUI)
├── web.py           # Web version (Streamlit)
├── requirements.txt # Dependencies for GUI + Web
└── README.md
```
---
## 🧰 Setup
### 0) **Python 3.10+** (required)

### 1) Get the project
```bash
git clone https://github.com/selenozkan/todo-app.git
cd todo-app
```
### 2) Create & activate a virtual environment (recommended)

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3) Install dependencies
```bash
pip install -r requirements.txt
```
---

## ▶️ Run the three versions

## 🔹 Version 1: Command-Line Interface (CLI)
```bash
python cli.py
```

---

## 🔹 Version 2: Desktop GUI Application
```bash
python gui.py
```

---

## 🔹 Version 3: Web Application (Streamlit)
```bash
streamlit run web.py
```

Live Streamlit version:
https://selenozkan-my-todo-app-web-hakaad.streamlit.app

---
