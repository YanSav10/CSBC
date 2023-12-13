import datetime
import random

# Список слів
word_list = ['apple', 'orange', 'banana', 'grape', 'pineapple', 'watermelon', 'strawberry', 'blueberry']

def generate_password(words):

    word1 = random.choice(words).capitalize()
    word2 = random.choice(words).capitalize()

    while len(word1 + word2) < 8 or len(word1 + word2) > 10 or len(word1) < 3 or len(word2) < 3:
        word1 = random.choice(words).capitalize()
        word2 = random.choice(words).capitalize()

    password = word1 + word2

    return password

generated_password = generate_password(word_list)
print(f"Згенерований пароль: {generated_password}")


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")