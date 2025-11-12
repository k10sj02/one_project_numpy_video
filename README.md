# 🧾 Employee Output Tracker

A Python project that analyzes and visualizes employee productivity using NumPy and Matplotlib.

## 🚀 Features
- Reads employee performance data from `company.txt`
- Calculates total, average, and highest output
- Visualizes results with clear bar charts
- Uses OOP structure via `operationclass.py` for modularity

## 🧰 Tech Stack
- **Python 3.8+**
- **NumPy**
- **Matplotlib**

## 📂 Project Structure

employee-output-tracker/
│
├── main.py             # Main script (runs analysis & plots)
├── operationclass.py   # Defines operations for data processing
├── company.txt         # Input data file
├── pyproject.toml      # Project dependencies
├── uv.lock             # Dependency lock file
└── .gitignore          # Ignores **pycache**, etc.

## ⚙️ Run the Project
```bash
git clone https://github.com/k10sj02/employee-output-tracker.git
cd employee-output-tracker
uv run main.py
````

## 📊 Example Output

* Total Output: 950 units
* Average per Employee: 79 units
* Highest Performer: “Employee 6”