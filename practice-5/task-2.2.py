import math
import datetime

radius = float(input("Введіть радіус (у сантиметрах): "))

circle_area = math.pi * radius ** 2

sphere_volume = (4 / 3) * math.pi * radius ** 3

print("Площа кругу з радіусом {:.2f} см: {:.2f} кв. см".format(radius, circle_area))
print("Об'єм кулі з радіусом {:.2f} см: {:.2f} куб. см".format(radius, sphere_volume))


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
