import datetime
import numpy as np

def number_generator():
    for i in range(10):
        yield i

gen = number_generator()

arr = np.fromiter(gen, dtype=int)

print("Масив згенерованих чисел:", arr)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
