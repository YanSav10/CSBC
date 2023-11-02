import datetime
small_containers = int(input("Введіть кількість контейнерів об'ємом до 1 літра: "))
large_containers = int(input("Введіть кількість контейнерів об'ємом понад 1 літр: "))

small_container_deposit = small_containers * 0.10
large_container_deposit = large_containers * 0.25

total_deposit = small_container_deposit + large_container_deposit

print("Доплата за контейнери об'ємом до 1 літра: ${:.2f}".format(small_container_deposit))
print("Доплата за контейнери об'ємом понад 1 літр: ${:.2f}".format(large_container_deposit))
print("Загальна доплата: ${:.2f}".format(total_deposit))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
