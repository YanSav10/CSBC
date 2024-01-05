import datetime

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

        print(f"Iteration {i + 1}: {arr}")

    return arr

my_list = [15, 30, 8, 22, 11, 4]

print("Початковий список:", my_list)
sorted_list = bubble_sort(my_list.copy())
print("Відсортований список:", sorted_list)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
