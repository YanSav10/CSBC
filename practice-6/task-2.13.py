import datetime

year = int(input("Введіть рік: "))

animals = ["Дракон", "Змія", "Кінь", "Коза", "Мавпа", "Півень", "Собака", "Свиня", "Щур", "Бик", "Тигр", "Кролик"]

start_year = 2000

animal_index = (year - start_year) % 12
animal = animals[animal_index]

print(f"За китайським гороскопом, рік {year} відповідає тварині: {animal}")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
