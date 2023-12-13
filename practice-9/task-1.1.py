import datetime

X = int(input("Введіть значення X: "))
Y = int(input("Введіть значення Y: "))
Z = X ** Y

formatted_string = f"{X} у степені {Y} буде дорівнювати {Z}."
print(formatted_string)

substring = f"{X} у степені {Y}"[::-1]
print(substring)


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")