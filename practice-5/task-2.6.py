import datetime
import math

egg_mass_grams = 67.2
egg_specific_heat = 3.7
egg_density = 1.038
egg_thermal_conductivity = 5.4e-10
boiling_water_temperature = 100

small_egg_mass_grams = 47

initial_temperatures_Celsius = [-4, 20]

for initial_temperature_Celsius in initial_temperatures_Celsius:
    t_large_egg = (egg_mass_grams ** (2 / 3) * egg_specific_heat * (egg_density ** (1 / 3))) / (
                egg_thermal_conductivity * math.pi ** 2 * (4 * math.pi / 3) ** (2 / 3) * (
                    boiling_water_temperature - initial_temperature_Celsius))
    t_small_egg = (small_egg_mass_grams ** (2 / 3) * egg_specific_heat * (egg_density ** (1 / 3))) / (
                egg_thermal_conductivity * math.pi ** 2 * (4 * math.pi / 3) ** (2 / 3) * (
                    boiling_water_temperature - initial_temperature_Celsius))

    print(f"Initial temperature: {initial_temperature_Celsius}°C")
    print(f"Time to reach temperature for large egg: {t_large_egg:.2f} seconds")
    print(f"Time to reach temperature for small egg: {t_small_egg:.2f} seconds")


    def printTimeStamp(name):
        print('Автор програми: ' + name)
        print('Час компіляції: ' + str(datetime.datetime.now()))


    printTimeStamp("Yan Savinov")
