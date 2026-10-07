from dataclasses import dataclass

@dataclass
class Expense:
    amount: float
    category: str
    date: str
    comment: str = ""

def add_expense(expenses, expense):
    expenses.append(expense)

expenses = []
add_expense(expenses, Expense(250, "еда", "2026-10-07", "обед"))
print(expenses)