import datetime
import math

points = []

while True:
    x_input = input("Enter the x part of the coordinate: ")

    if x_input == "":
        break

    x = float(x_input)
    y = float(input("Enter the y part of the coordinate: "))

    points.append((x, y))

if len(points) < 2:
    print("Для обчислення периметру потрібно щонайменше дві точки.")
else:
    perimeter = 0.0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        perimeter += distance

    x1, y1 = points[0]
    x2, y2 = points[-1]
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    perimeter += distance

    print(f"The perimeter of that polygon is {perimeter}")


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
