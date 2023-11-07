import datetime

temperature = float(input("Введіть температуру повітря в градусах Цельсія: "))
wind_speed = float(input("Введіть швидкість вітру в км/год: "))

if temperature <= 10 and wind_speed > 4.8:
    wci = round(13.12 + 0.6215 * temperature - 11.37 * wind_speed ** 0.16 + 0.3965 * temperature * wind_speed ** 0.16)
    print(f"Індекс прохолодності вітру: {wci}")
else:
    print("Умови для обчислення індексу прохолодності вітру не виконані.")


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
