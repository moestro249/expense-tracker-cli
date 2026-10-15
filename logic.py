from datetime import datetime


def add_expense(expenses, expense):
    expenses.append(expense)


def total(expenses):
    return sum(i.amount for i in expenses)


def total_by_category(expenses):
    result = {}
    for i in expenses:
        result[i.category] = result.get(i.category, 0) + i.amount
    return result


def delete_expense(expenses, index):
    if 0 <= index < len(expenses):
        del expenses[index]
        return True
    return False


def filter_by_category(expenses, category):
    return [e for e in expenses if e.category == category]


def filter_by_period(expenses, start, end):
    return [i for i in expenses if start <= i.date <= end]


def is_valid_date(s):
    try:
        parsed = datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        return False
    return parsed.strftime("%Y-%m-%d") == s
