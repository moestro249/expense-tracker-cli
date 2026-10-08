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


def main():
    expenses = load_expenses()

    while True:
        while True:
            print("1. Добавить трату", "2. Показать все","3. Итог по категориям","4. Выход", sep="\n")
            try:
                answer=int(input())
                break
            except ValueError:
                print("Введите число из списка ")
        
        if answer==1:
            while True:
                try:
                    amount=float(input("amount:"))
                    if amount>0:
                        break
                    else:
                        print("Неверные данные")
                except ValueError:
                    print("Неверные данные")
            category=input("category:")
            comment=input("comment:")
            add_expense(expenses,Expense(amount,category,str(date.today()),comment))
            save_expenses(expenses)
            
        elif answer==2:
            if not expenses:
                print("Трат пока нет")
            else:
                for i in expenses:
                    print(i)
            
        elif answer==3:
            totals=total_by_category(expenses)
            if not totals:
                print("Трат нет")
            else:
                for x,y in totals.items():
                    print(f"{x}:{y}")
                print(f"Всего потрачено: {total(expenses)}")
            
        elif answer==4:
            break
        else:
            print("неверная команда")

if __name__=="__main__":
    main()


            
    