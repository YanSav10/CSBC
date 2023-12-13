import datetime

def get_key():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = 'dypriajuhtqwesfovcnblxmkzg'
    return {alphabet[i]: key[i] for i in range(len(alphabet))}

def encrypt(message, key):
    return ''.join(key[letter] if letter in key else letter for letter in message)

def decrypt(encrypted_message, key):
    key = {value: key for key, value in key.items()}
    return ''.join(key[letter] if letter in key else letter for letter in encrypted_message)

key = get_key()

# Читаємо текст для шифрування
message = input("Введіть текст для шифрування: ")

# Шифруємо текст
encrypted_message = encrypt(message, key)
print("Шифрований текст: ", encrypted_message)

# Дешифруємо текст
decrypted_message = decrypt(encrypted_message, key)
print("Дешифрований текст: ", decrypted_message)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
