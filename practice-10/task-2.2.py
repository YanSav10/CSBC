import datetime

def find_empty_cell(occupied_cells):
    """Знаходження вільної комірки з мінімальним номером"""
    for i in range(1, 13):
        if i not in occupied_cells:
            return i
    return None

passengers_count = int(input("Введіть кількість пасажирів: "))
passengers_data = []

# Зберігання даних про пасажирів
for i in range(passengers_count):
    data = input(f"Введіть дані пасажира {i + 1} (прізвище здача_багажу видача_багажу): ")
    passenger_info = data.split()
    passengers_data.append(passenger_info)

occupied_cells = set()
for passenger in passengers_data:
    surname, time_deposit, time_withdrawal = passenger
    empty_cell = find_empty_cell(occupied_cells)
    if empty_cell:
        occupied_cells.add(empty_cell)
        print(f"{surname}: {empty_cell}")
    else:
        print(f"Немає вільних комірок для {surname}")


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
