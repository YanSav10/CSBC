import datetime

initial_balance = float(input("Введіть початковий баланс рахунку: "))

annual_interest_rate = 9 / 100
tax_rate = 20 / 100
years = 3

for year in range(1, years + 1):
    interest = initial_balance * annual_interest_rate

    tax = interest * tax_rate

    initial_balance += (interest - tax)

    print(f"Рік {year}: {initial_balance:.2f}")

print(f"Сума на рахунку після {years} років: {initial_balance:.2f}")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
