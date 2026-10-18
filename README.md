[![Tests](https://github.com/moestro249/expense-tracker-cli/actions/workflows/tests.yml/badge.svg)](https://github.com/moestro249/expense-tracker-cli/actions/workflows/tests.yml)

# expense-tracker-cli

A console app for tracking personal expenses, written in Python.

## Features
- Add an expense (amount, category, comment; the date is set automatically)
- Show all expenses
- Show totals by category and the overall total
- Delete an expense by its number
- Filter expenses by category
- Show expenses for a date period
- Expenses are saved to a JSON file and loaded on the next start

## Requirements
- Python 3.11 (the version it was developed with)

## Usage
```
git clone https://github.com/moestro249/expense-tracker-cli
cd expense-tracker-cli
python main.py
```

Choose an action by typing its number in the menu.

## Tests
```
pip install pytest
python -m pytest
```

## Project structure
- `models.py` - the `Expense` dataclass
- `logic.py` - functions for totals, filters, deleting and date validation
- `storage.py` - saving and loading expenses as JSON
- `ui.py` - helpers for validated user input
- `main.py` - the menu and the program entry point

## Data
Expenses are stored in `expenses.json` in the folder where the program is run. Each record has `amount`, `category`, `date` (format `YYYY-MM-DD`) and `comment`. The file is listed in `.gitignore`, so personal data is not committed.