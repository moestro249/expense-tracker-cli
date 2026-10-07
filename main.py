from dataclasses import dataclass, asdict
import json

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
add_expense(expenses, Expense(120, "еда", "2026-10-07", "кофе"))
add_expense(expenses, Expense(80, "транспорт", "2026-10-07", "метро"))
print(expenses)

def total(expenses):
    return sum(i.amount for i in expenses)

def total_by_category(expenses):
    result = {}
    for i in expenses:
        result[i.category]=result.get(i.category, 0) + i.amount
        
    return result

print(total_by_category(expenses))
        
        
def save_expenses(expenses):
    exp= [asdict(i) for i in expenses]
    with open('expenses.json','w', encoding='utf-8') as file:
       json.dump(exp, file, ensure_ascii=False)
       
save_expenses(expenses)


def load_expenses():
    try:
        with open('expenses.json', 'r', encoding='utf-8') as file:
            exp=json.load(file)   
    except FileNotFoundError:
        return []
    return [Expense(**i) for i in exp]
            
print(load_expenses())
            
    