import datetime

my_words_list1 = ['hello', 'world', 'Python', 'C', 'Java', 'C', 'Python']
my_words_list2 = ['Python', 'Java', 'PHP', 'HTML', 'Java', 'PHP']

set1 = set(my_words_list1)
set2 = set(my_words_list2)

result = list(set1 - set2)

print("Слова, що присутні в списку 1, але відсутні в списку 2:")
print(result)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
