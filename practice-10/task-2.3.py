import datetime

text = input("Введіть текст: ")

word_count = len(text.split())
letter_count = sum(c.isalpha() for c in text)
digit_count = sum(c.isdigit() for c in text)
lowercase_count = sum(c.islower() for c in text)
uppercase_count = sum(c.isupper() for c in text)
space_count = sum(c.isspace() for c in text)

print(f"Кількість слів: {word_count}")
print(f"Кількість букв: {letter_count}")
print(f"Кількість цифр: {digit_count}")
print(f"Кількість малих літер: {lowercase_count}")
print(f"Кількість великих літер: {uppercase_count}")
print(f"Кількість пробілів: {space_count}")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
