import datetime
import numpy as np

N = 5

p = 6

arr = np.zeros((N, N), dtype=int)

indices = np.random.choice(N * N, p, replace=False)

np.put(arr, indices, 1)

print("Випадковий 2D-масив:")
print(arr)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
