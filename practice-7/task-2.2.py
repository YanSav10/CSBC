import datetime

def text_decorator(decorator):
    def decorator_function(func):
        def wrapper(text):
            print(decorator * len(text))
            print(decorator + ' ' + text + ' ' + decorator)
            print(decorator * len(text))
        return wrapper
    return decorator_function

# Декоратор, який обрамляє текст символами, переданими в декоратор
@text_decorator('=')
def display_text(text):
    print(text)

# Введення тексту від користувача
input_text = input("Введіть текст: ")

# Виклик функції, оберненої декоратором
display_text(input_text)


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")