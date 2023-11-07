import datetime

water_usage = float(input("Введіть споживання води в кубометрах: "))

fixed_charge = 20.0

limit1 = 30
limit2 = 20
limit3 = 10
rate1 = 9.86
rate2 = 11.22
rate3 = 13.06
rate4 = 17.89

total_cost = 0.0

if water_usage <= limit1:
    total_cost = fixed_charge + water_usage * rate1
elif water_usage <= limit1 + limit2:
    total_cost = fixed_charge + limit1 * rate1 + (water_usage - limit1) * rate2
elif water_usage <= limit1 + limit2 + limit3:
    total_cost = fixed_charge + limit1 * rate1 + limit2 * rate2 + (water_usage - limit1 - limit2) * rate3
else:
    total_cost = (fixed_charge + limit1 * rate1 + limit2 * rate2 + limit3 * rate3 + (water_usage - limit1 - limit2 - limit3) * rate4)

print(f"Загальна вартість: {total_cost:.2f} грн")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
