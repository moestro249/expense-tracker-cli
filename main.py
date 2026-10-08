from dataclasses import dataclass, asdict
from datetime import date
import json

@dataclass
class Expense:
    amount: float
    category: str
    date: str
    comment: str = ""

def add_expense(expenses, expense):
    expenses.append(expense)

def total(expenses):
    return sum(i.amount for i in expenses)

def total_by_category(expenses):
    result = {}
    for i in expenses:
        result[i.category]=result.get(i.category, 0) + i.amount
        
    return result
              
def save_expenses(expenses):
    exp= [asdict(i) for i in expenses]
    with open('expenses.json','w', encoding='utf-8') as file:
       json.dump(exp, file, ensure_ascii=False)

def load_expenses():
    try:
        with open('expenses.json', 'r', encoding='utf-8') as file:
            exp=json.load(file)   
    except FileNotFoundError:
        return []
    return [Expense(**i) for i in exp]

expenses = load_expenses()

while True:
    while True:
        print("1. Добавить трату", "2. Показать все","3. Итог по категориям","4. Выход")
        try:
            answer=int(input())
            break
        except ValueError:
            print("Введите число из списка ")
    
    if answer==1:
        while True:
            try:
                amount=int(input("amount:"))
                if amount>=0:
                    break
            except ValueError:
                print("Неверные данные")
        category=input("category:")
        camment=input("comment:")
        add_expense(expenses,Expense(amount,category,str(date.today()),camment))
        save_expenses(expenses)
        
    elif answer==2:
        for i in expenses:
            print(i)
        save_expenses(expenses)
        
    elif answer==3:
        totals=total_by_category(expenses)
        if not totals:
            print("Трат нет")
        else:
            for x,y in totals.items():
                print(f"{x}:{y}")
        save_expenses(expenses)
        
    elif answer==4:
        save_expenses(expenses)
        break
    else:
        print("неверная команда")
            
            
            
        
        
        
# add_expense(expenses, Expense(250, "еда", "2026-10-07", "обед"))
# add_expense(expenses, Expense(120, "еда", "2026-10-07", "кофе"))
# add_expense(expenses, Expense(80, "транспорт", "2026-10-07", "метро"))


            
    