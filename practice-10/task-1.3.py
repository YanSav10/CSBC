import datetime

set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4}

if set1.issubset(set2):
    print("Перша множина є підмножиною другої.")
elif set2.issubset(set1):
    print("Друга множина є підмножиною першої.")
else:
    print("Ці множини не є підмножинами одна одної.")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
