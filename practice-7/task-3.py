import datetime
def power(base, exponent):
    # Базовий випадок: якщо показник степені рівний 0, повертаємо 1
    if exponent == 0:
        return 1
    # Рекурсивний випадок: підносимо base до степеня (exponent - 1)
    else:
        return base * power(base, exponent - 1)

# Приклад використання:
num = int(input("Введіть число: "))
exp = int(input("Введіть показник степені: "))

result = power(num, exp)
print(f"{num} в піднесенні до степені {exp} дорівнює {result}")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
