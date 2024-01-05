import datetime
import numpy as np

today = np.datetime64('today')
print("Сьогоднішня дата:", today)

yesterday = np.datetime64('today') - np.timedelta64(1, 'D')
print("Вчорашня дата:", yesterday)

tomorrow = np.datetime64('today') + np.timedelta64(1, 'D')
print("Завтрашня дата:", tomorrow)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
