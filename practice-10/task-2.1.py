import datetime

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def next_day(year, month, day):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_in_month[2] = 29

    day += 1

    if day > days_in_month[month]:
        day = 1
        month += 1

        if month > 12:
            month = 1
            year += 1

    return year, month, day

year = int(input("Введіть рік: "))
month = int(input("Введіть місяць: "))
day = int(input("Введіть день: "))

next_year, next_month, next_day = next_day(year, month, day)

print(f"Наступний день: {next_year}-{next_month:02d}-{next_day:02d}")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
