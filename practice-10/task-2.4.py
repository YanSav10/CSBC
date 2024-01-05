import datetime

def calculate_sum():
    total_sum = 0

    while True:
        user_input = input("Введіть число (або Enter для завершення): ")

        if not user_input:
            break

        try:
            number = float(user_input)
            total_sum += number
            print(f"Поточна сума: {total_sum}")
        except ValueError:
            print("Помилка! Введено некоректне число. Спробуйте ще раз.")

    print(f"Загальна сума: {total_sum}")
    print("Програма завершила роботу.")

calculate_sum()

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
