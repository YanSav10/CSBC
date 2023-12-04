import datetime
import time

# Реалізація функції map
def my_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

# Реалізація функції filter
def my_filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result

# Реалізація функції reduce
def my_reduce(func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = func(value, element)
    return value

# Декоратор для вимірювання часу роботи функцій
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper

@calculate_time
def my_long_running_function():
    result = my_map(lambda x: x * 2, range(1000000))
    result = my_filter(lambda x: x % 2 == 0, result)
    result = my_reduce(lambda x, y: x + y, result)
    return result

@calculate_time
def python_builtin_long_running_function():
    result = list(map(lambda x: x * 2, range(1000000)))
    result = list(filter(lambda x: x % 2 == 0, result))
    result = sum(result)
    return result

# Виклик функцій для порівняння часу їх виконання
my_long_running_function()
python_builtin_long_running_function()

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")