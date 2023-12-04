import datetime

def encrypt(text, height):
    result = ""
    for i in range(height):
        for j in range(i, len(text), height):
            result += text[j]
    return result

def decrypt(text, height):
    result = ""
    width = int(len(text) / height)
    for i in range(width):
        for j in range(height):
            index = i + j * width
            if index < len(text):
                result += text[index]
    return result

text = input("Введіть текст: ")
height = int(input("Введіть висоту частоколу (секретний ключ): "))
encrypted_text = encrypt(text, height)
print("Зашифрований текст: ", encrypted_text)
decrypted_text = decrypt(encrypted_text, height)
print("Розшифрований текст: ", decrypted_text)


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
