import datetime

decimal_num = int(input("Введіть десяткове число: "))

result = ""
q = decimal_num

while q != 0:
    r = q % 2
    result = str(r) + result
    q = q // 2

print(f"Двійкове представлення числа {decimal_num} - {result}")


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
