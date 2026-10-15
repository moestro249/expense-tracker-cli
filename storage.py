from dataclasses import asdict
import json
from models import Expense


def save_expenses(expenses, filename="expenses.json"):
    exp = [asdict(i) for i in expenses]
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(exp, file, ensure_ascii=False)


def load_expenses(filename="expenses.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            exp = json.load(file)
    except FileNotFoundError:
        return []
    return [Expense(**i) for i in exp]
