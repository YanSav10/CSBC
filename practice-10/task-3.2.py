import datetime
import numpy as np

matrix = np.ones((4, 4))

matrix[1:3, 1:3] = 0

print(matrix)


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
