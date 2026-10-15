from logic import is_valid_date

def ask_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Неверные данные")

def ask_positive_float(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount >0:
                return amount
            print("сумма должна быть больше нуля")
        except ValueError:
            print("Неверные данные")
            
def ask_date(prompt1,prompt2):
    while True:
        start = input(prompt1)
        end = input(prompt2)
        if is_valid_date(start) and is_valid_date(end):
            if start <= end:
                return start, end
            else:
                print("Начальная дата должна быть меньше конечной")
        else:
            print("Неверные данные")