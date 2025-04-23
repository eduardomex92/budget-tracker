# 💸 Budget Tracker App

**Developer:** Heiner Alcala-Salas  
**Language:** Python  
**UI:** GUI (tkinter + BreezyPythonGUI) and CLI support

---

## 📋 Overview

The Budget Tracker is a Python application that allows users to manage their personal finances with a clean graphical interface and an optional command-line interface. Users can log income, create expense categories, visualize financial summaries, and generate comparison charts — all with data persistently stored in a JSON file.

This project demonstrates object-oriented design with real-world file handling, modularity, and interactive GUI/CLI dual access.

---

## 🧩 Features

- Add income with validation
- Track categorized expenses with manual or dropdown category entry
- Add/remove budget categories dynamically
- View financial summaries: income, expenses, remaining balance
- Visualize data with a bar chart (matplotlib)
- Save/load data automatically via a local JSON file
- Includes both a GUI version (`main.py`) and CLI version (`budgetApp.py`)

---

## 🛠️ Tech Stack

- **Language:** Python
- **GUI Libraries:** tkinter, BreezyPythonGUI
- **Data Storage:** JSON (file-based persistence)
- **Visualization:** matplotlib
- **Design:** Object-Oriented Programming (`BudgetTracker`, `Category` classes)

---

## 📁 Folder Structure
<pre>budget-tracker/ ├── main.py # GUI version using EasyFrame (BreezyPythonGUI) ├── budgetApp.py # CLI-based version of the app ├── BudgetTracker.py # Core logic for managing categories and tracking ├── Category.py # Defines a single category and its expenses ├── budget_data.json # Persistent storage file for income and expenses ├── dollar_icon.gif # Header icon image used in the GUI
</pre>

