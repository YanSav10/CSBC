import datetime

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set1.difference_update(set2)

print("Оновлена перша множина після виключення спільних елементів:")
print(set1)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
