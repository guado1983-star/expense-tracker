# Expense Tracker CLI

A command-line expense tracking application built in Python. Allows users to add, view, edit, delete, search, and export personal expenses stored in a flat file database.

Built as a foundational Python project covering file I/O, data validation, CRUD operations, and CSV export.

---

## Features

- Add expenses with name, amount, category, and date
- View all expenses in a formatted list
- View total spending across all expenses
- View total spending broken down by category
- View total spending broken down by month
- Edit any existing expense field by field
- Delete expenses by selection number
- Search expenses by name, category, or date
- Export all expenses to a CSV file compatible with Excel and Numbers
- Duplicate detection before saving
- Full input validation with error handling

---

## Requirements

- Python 3.8 or higher
- No third party libraries required — uses Python standard library only
  - `os`
  - `csv`
  - `datetime`

---

## Installation

1. Clone or download this repository
2. Navigate to the project folder in your terminal
3. No pip installs required

---

## How to Run

```bash
python app.py
```

> **Important:** Always run from the VS Code integrated terminal, not the Run button.
> Open terminal with Ctrl + ` (Windows/Linux) or Cmd + ` (Mac)

---

## Menu Options

| Option | Function |
|--------|----------|
| 1 | Add Expense |
| 2 | Show All Expenses |
| 3 | Show Total |
| 4 | Show Total by Category |
| 5 | Delete Expense |
| 6 | Search Expenses |
| 7 | Show by Month |
| 8 | Edit Expense |
| 9 | Export to CSV |
| 10 | Exit |

---

## Data Storage

Expenses are stored in `expenses.txt` in the same folder as the script.

Format — 4 fields, comma separated:
```
name,amount,category,date
Coffee,4.50,Food,2025-01-15
```

CSV exports are saved as `expenses_export.csv` with UTF-8 BOM encoding for clean Excel and Numbers compatibility.

---

## Project Structure

```
project/
├── app.py                  # Main application
├── expenses.txt            # Live data file (auto-generated)
├── expenses_export.csv     # CSV export (auto-generated on demand)
├── context.txt             # Developer setup and rules
└── README.md               # This file
```

---

## Key Concepts Covered

- **CRUD operations** — Create, Read, Update, Delete
- **File I/O** — Reading and writing flat file databases
- **Data validation** — Input sanitization, date format enforcement, negative amount rejection
- **Defensive parsing** — Bounded split to handle commas in expense names
- **Float formatting** — Fixed point notation to prevent IEEE 754 rounding artifacts
- **Duplicate detection** — Pre-insert uniqueness check across all fields
- **Path resolution** — `os.path.abspath(__file__)` for environment-independent file access
- **CSV export** — UTF-8 BOM encoding for cross-platform spreadsheet compatibility
- **Error handling** — try/except on all file operations and user input

---

## Known Behavior

Display-only functions use `input()` instead of `print()` for output due to VS Code terminal output buffering. This forces stdout to flush and display results correctly.

