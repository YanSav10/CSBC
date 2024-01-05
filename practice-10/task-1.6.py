import datetime

my_dict = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

sum_by_key = {key: sum(values) for key, values in my_dict.items()}

sum_by_column = {f'Column_{i+1}': sum(my_dict[key][i] for key in my_dict) for i in range(len(list(my_dict.values())[0]))}

total_sum = sum(sum(values) for values in my_dict.values())

print("Суми елементів у списках за їх ключем:")
print(sum_by_key)
print("\nСуми елементів у списках по стовпчику:")
print(sum_by_column)
print("\nЗагальна сума всіх елементів усіх списків:")
print(total_sum)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
