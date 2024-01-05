import datetime
import numpy as np

print("Версія NumPy:", np.__version__)

np.show_config()

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
