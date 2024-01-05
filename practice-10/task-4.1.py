import datetime
import numpy as np
import matplotlib.pyplot as plt

# Розмір зображення
width, height = 400, 300

# Створення матриці для зображення з градієнтом
image = np.zeros((height, width, 4), dtype=np.uint8)

# Створення градієнту
for y in range(height):
    for x in range(width):
        image[y, x, 0] = int(255 * x / width)  # Червоний канал (R)
        image[y, x, 1] = int(255 * y / height)  # Зелений канал (G)
        image[y, x, 2] = 0  # Синій канал (B)
        image[y, x, 3] = 255  # Альфа-канал (A)

# Відображення зображення
plt.imshow(image)
plt.axis('off')  # Вимкнення координатних вісей
plt.show()

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
