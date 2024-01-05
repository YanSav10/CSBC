import datetime

my_dict = {
    'id1': {
        'name': 'Bob',
        'area': 'IT'
    },
    'id2': {
        'name': 'Bob',
        'area': 'IT'
    },
    'id3': {
        'name': 'Rob',
        'area': 'Healthcare'
    },
    'id4': {
        'name': 'Julie',
        'area': 'Marketing'
    }
}

unique_values = set()
duplicates = []

for key, value in my_dict.items():
    val_as_tuple = tuple(value.items())
    if val_as_tuple not in unique_values:
        unique_values.add(val_as_tuple)
    else:
        duplicates.append(key)

print("Ключі, які містять дублікати значень:", duplicates)

for key in duplicates:
    del my_dict[key]

print("\nОновлений словник без дублікатів значень:")
print(my_dict)


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
