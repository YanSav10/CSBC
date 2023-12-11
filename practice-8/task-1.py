from datetime import datetime


def days_until_new_year():
    while True:
        try:
            # Запитати користувача про поточну дату
            input_date_str = input("Введіть поточну дату (у форматі dd.mm.yyyy): ")

            # Перетворити рядок у об'єкт datetime
            input_date = datetime.strptime(input_date_str, "%d.%m.%Y")

            # Перевірка чи введена дата не є майбутньою
            if input_date > datetime.now():
                print("Введена дата майбутня. Будь ласка, введіть поточну дату.")
                continue

            # Визначити дату Нового року для наступного року
            new_year_date = datetime(input_date.year + 1, 1, 1)

            # Визначити різницю між поточною датою та Новим роком
            delta = new_year_date - input_date

            # Повернути кількість днів до Нового року
            return delta.days
        except ValueError:
            print("Некоректний формат дати. Будь ласка, введіть дату у форматі dd.mm.yyyy.")


# Виклик функції та виведення результату
days_left = days_until_new_year()
print(f"До Нового року залишилося {days_left} днів")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.now()))


printTimeStamp("Yan Savinov")
