import calendar
import datetime

def display_calendar(year, month):
    try:
        cal = calendar.month(year, month)
        print(f"Календар на {calendar.month_name[month]}, {year}:")
        print(cal)
    except IndexError:
        print("Некоректно введений рік або місяць.")


# Введення року та місяця з консолі
try:
    input_year = int(input("Введіть рік: "))
    input_month = int(input("Введіть місяць (від 1 до 12): "))
    if not 1 <= input_month <= 12:
        raise ValueError("Некоректно введений місяць.")

    display_calendar(input_year, input_month)
except ValueError as e:
    print(e)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
