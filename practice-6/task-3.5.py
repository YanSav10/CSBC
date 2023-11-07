import datetime

total_cost = 0.0
total_visitors = 0

while True:
    age_input = input("Введіть вік відвідувача (або порожній рядок для завершення): ")

    if age_input == "":
        break

    age = int(age_input)

    if age < 3:
        cost = 0.0
    elif age < 12:
        cost = 48.0
    elif age > 60:
        cost = 50.0
    else:
        cost = 85.0

    total_cost += cost
    total_visitors += 1

discount = 0.0
if total_visitors > 10:
    discount = total_cost * 0.1

print(f"Загальна вартість квитків для групи {total_visitors} відвідувачів: ₴{total_cost:.2f}")
if discount > 0:
    print(f"Знижка 10% за групу: -₴{discount:.2f}")


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
