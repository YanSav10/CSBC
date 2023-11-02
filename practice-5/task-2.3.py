import math
import datetime

side_length = float(input("Введіть довжину сторони многокутника: "))
num_sides = int(input("Введіть кількість сторін многокутника: "))

area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))

print("Площа регулярного многокутника зі стороною довжиною {} і {} сторонами: {:.2f}".format(side_length, num_sides, area))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
