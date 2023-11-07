import random
import datetime

result = random.randint(0, 36)


def get_color(number):
    if number in [0, 00]:
        return "Green"
    elif number in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
        return "Red"
    else:
        return "Black"


result_message = f"На рулетці випало {result}..."
payout_message = f"Виплатити {result}"
color_message = f"Виплатити {get_color(result)}"
odd_even_message = "Виплатити Odd" if result % 2 != 0 and result not in [0, 00] else "Виплатити Even"
range_message = "Виплатити 1 to 18" if 1 <= result <= 18 else "Виплатити 19 to 36"

print(result_message)
print(payout_message)
print(color_message)
print(odd_even_message)
print(range_message)


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
