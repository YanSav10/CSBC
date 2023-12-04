import datetime

def add(a):
    def inner(b):
        return a + b
    return inner

add_two = add(2)
print(add_two(5))  # Виведе: 7


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")