from datetime import date
from models import Expense
from logic import (
    filter_by_category,
    add_expense,
    filter_by_period,
    delete_expense,
    total,
    total_by_category,
)
from ui import ask_positive_float, ask_int, ask_date
from storage import save_expenses, load_expenses


def main():
    expenses = load_expenses()

    while True:
        print(
            "1. Добавить трату",
            "2. Показать все",
            "3. Итог по категориям",
            "4. удалить",
            "5. фильтр по категориям",
            "6. показать траты за период",
            "7. Выход",
            sep="\n",
        )
        answer = ask_int("")

        if answer == 1:
            amount = ask_positive_float(prompt="amount:")
            category = input("category:")
            comment = input("comment:")
            add_expense(expenses, Expense(amount, category, str(date.today()), comment))
            save_expenses(expenses)

        elif answer == 2:
            if not expenses:
                print("Трат пока нет")
            else:
                for i in expenses:
                    print(i)

        elif answer == 3:
            totals = total_by_category(expenses)
            if not totals:
                print("Трат нет")
            else:
                for x, y in totals.items():
                    print(f"{x}:{y}")
                print(f"Всего потрачено: {total(expenses)}")

        elif answer == 4:
            if not expenses:
                print("Трат нет")
            else:
                for n, e in enumerate(expenses, start=1):
                    print(n, e)
                ans = ask_int(prompt="Выберите номер который хотите удалить:")
                if delete_expense(expenses, (ans - 1)):
                    print("Удалено")
                    save_expenses(expenses)
                else:
                    print("Нет такого номера")
        elif answer == 5:
            totals = total_by_category(expenses)
            if not totals:
                print("Трат нет")
            else:
                for n, c in enumerate(totals, start=1):
                    print(n, c)
                ans = ask_int(prompt="Выберите номер категории:")
                categories = list(totals)

                if 1 <= ans <= len(categories):
                    result = filter_by_category(expenses, categories[ans - 1])
                    if result:
                        print(categories[ans - 1])
                        for n, i in enumerate(result, start=1):
                            print(n, i.amount)
                        print("Всего потрачено:", total(result))
                    else:
                        print("Трат нет")
                else:
                    print("Нет такого номера")
        elif answer == 6:
            print(sorted({i.date for i in expenses}))
            start, end = ask_date(
                prompt1="Выберите с какой даты вести отсчет:",
                prompt2="Выберите с какой даты закончить:",
            )
            result = filter_by_period(expenses, start, end)
            if not result:
                print("Трат нет")
            else:
                for i in result:
                    print(i)
                print("итог:", total(result))

        elif answer == 7:
            break
        else:
            print("неверная команда")


if __name__ == "__main__":
    main()
