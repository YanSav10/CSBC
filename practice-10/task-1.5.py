import datetime

my_set = {3, 4, 5, 1, 2, 7, 8, 9}

elements_to_remove = {2, 9, 5}

if len(elements_to_remove) == 3:
    my_set.difference_update(elements_to_remove)
    print("Оновлена множина після видалення трьох елементів:")
    print(my_set)
else:
    print("Будь ласка, вкажіть рівно три елементи для видалення.")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
