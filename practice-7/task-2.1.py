import datetime
# Анонімна функція для видалення голосних букв з тексту
remove_vowels = lambda text: ''.join(filter(lambda x: x.lower() not in 'aeiouаеиоуєії', text))

# Введення тексту від користувача
input_text = input("Введіть текст: ")

# Виведення тексту без голосних букв
result = remove_vowels(input_text)
print("Текст без голосних букв:", result)


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
