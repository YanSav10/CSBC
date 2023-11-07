import datetime

isbn = input("Введіть 13-цифровий ISBN: ")


if len(isbn) != 13 or not isbn.isdigit():
    print("ISBN повинен містити рівно 13 цифр.")
else:
    total = 0
    for i in range(12):
        digit = int(isbn[i])
        if i % 2 == 0:
            total += digit
        else:
            total += digit * 3

    check_digit = (10 - (total % 10)) % 10

    if check_digit == int(isbn[12]):
        print("ISBN валідний.")
    else:
        print("ISBN недійсний. Перевірочна цифра не відповідає обчисленій.")


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
