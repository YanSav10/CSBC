import datetime

def caesar_cipher(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            # Визначення верхньої або нижньої межі алфавіту залежно від регістру символу
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')

            # Зсув по алфавіту
            shifted = (ord(char) - start + shift) % 26 + start
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

# Запит на введення повідомлення та зсуву
message = input("Введіть повідомлення для шифрування/дешифрування: ")
shift_value = int(input("Введіть розмір зсуву (ціле число): "))

# Виклик функції для шифрування
encrypted_message = caesar_cipher(message, shift_value)
print(f"Зашифроване/дешифроване повідомлення: {encrypted_message}")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
