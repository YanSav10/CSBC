import datetime
import numpy as np

original_vector = np.array([1, 2, 3, 4, 5])

zeros_to_insert = 3

zero_array = np.zeros(len(original_vector) + (len(original_vector) - 1) * zeros_to_insert, dtype=original_vector.dtype)

zero_array[::zeros_to_insert + 1] = original_vector

print("Початковий вектор:", original_vector)
print("Новий вектор з нулями між елементами:", zero_array)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
