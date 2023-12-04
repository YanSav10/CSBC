import datetime


def generate_pascal_triangle(height):
    triangle = []
    for i in range(height):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle


def print_pascal_triangle(triangle):
    max_width = len(' '.join(map(str, triangle[-1])))
    for row in triangle:
        print(' '.join(map(str, row)).center(max_width))


# Запит на введення висоти трикутника Паскаля
height = int(input("Введіть висоту трикутника Паскаля: "))

pascal_triangle = generate_pascal_triangle(height)
print("Трикутник Паскаля:")
print_pascal_triangle(pascal_triangle)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
