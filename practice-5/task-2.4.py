import datetime

balloon_volume_liters = 12
balloon_volume_m3 = balloon_volume_liters / 1000
room_temperature_Celsius = 20
room_temperature_Kelvin = room_temperature_Celsius + 273.15
universal_gas_constant = 8.314
min_pressure_Pa = 18.6e6
max_pressure_Pa = 30e6

min_moles = (min_pressure_Pa * balloon_volume_m3) / (universal_gas_constant * room_temperature_Kelvin)
max_moles = (max_pressure_Pa * balloon_volume_m3) / (universal_gas_constant * room_temperature_Kelvin)

print(f"Кількість молів газу в балоні при мінімальному тиску: {min_moles:.2f} моль")
print(f"Кількість молів газу в балоні при максимальному тиску: {max_moles:.2f} моль")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
