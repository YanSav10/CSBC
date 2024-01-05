import datetime
import numpy as np

vector = np.array([3, 7, 11, 15, 19])

scalar = 12

index = np.argmin(np.abs(vector - scalar))

nearest_value = vector[index]

print(f"Заданий вектор: {vector}")
print(f"Заданий скаляр: {scalar}")
print(f"Найближче значення: {nearest_value} (індекс {index})")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
