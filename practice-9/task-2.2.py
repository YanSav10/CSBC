import datetime
import re

def reformat_date(date):
    pattern = r'(\d{4})-(\d{2})-(\d{2})'

    reformatted_date = re.sub(pattern, r'\3-\2-\1', date)

    return reformatted_date

input_date = input("Введіть дату у форматі yyyy-mm-dd: ")

date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
if not date_pattern.match(input_date):
    print("Неправильний формат дати. Будь ласка, введіть у форматі yyyy-mm-dd.")
else:
    print("Початкова дата:", input_date)
    print("Переформатована дата:", reformat_date(input_date))


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
