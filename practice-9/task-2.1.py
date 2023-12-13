import datetime
import re

text = input("Введіть текст: ")

pattern = r'\b\w{6}\b'

matches = re.findall(pattern, text)

print("6-символьні слова з введеного тексту:")
for match in matches:
    print(match)


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")