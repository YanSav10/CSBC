import datetime
import re

def check_sequences(text):
    pattern = r'\b[a-z]+(?:_[a-z]+)+\b'  # Регулярний вираз для пошуку послідовностей
    sequences = re.findall(pattern, text)

    if sequences:
        print("Знайдені послідовності з малих латинських літер, розділених символом '_':")
        for sequence in sequences:
            print(sequence)
    else:
        print("У тексті відсутні послідовності з малих латинських літер, розділених символом '_'.")

user_text = input("Введіть текст: ")

check_sequences(user_text)


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")