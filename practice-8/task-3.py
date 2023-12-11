import datetime
def time_conversion(time):
    try:
        # Розділяємо час на години, хвилини, секунди та AM/PM
        hours, minutes, seconds_ampm = time.split(':')
        seconds = seconds_ampm[:2]
        am_pm = seconds_ampm[2:]

        # Перевірка часу на коректність
        if len(hours) != 2 or len(minutes) != 2 or len(seconds) != 2 or (am_pm != 'AM' and am_pm != 'PM'):
            raise ValueError("Некоректний формат часу")

        # Перевірка на коректність годин
        if int(hours) < 1 or int(hours) > 12:
            raise ValueError("Некоректне значення годин")

        # Перевірка на коректність хвилин і секунд
        if int(minutes) < 0 or int(minutes) > 59 or int(seconds) < 0 or int(seconds) > 59:
            raise ValueError("Некоректне значення хвилин або секунд")

        # Якщо PM та години не 12, додаємо 12 годин
        if am_pm == 'PM' and hours != '12':
            hours = str(int(hours) + 12)

        # Якщо AM та години 12, переводимо години у 00
        if am_pm == 'AM' and hours == '12':
            hours = '00'

        # Формуємо рядок у форматі 24-годинного часу
        military_time = f"{hours}:{minutes}:{seconds}"
        return military_time
    except ValueError as e:
        return str(e)


input_time = input("Введіть час у форматі 'hh:mm:ssAM' або 'hh:mm:ssPM': ")

result = time_conversion(input_time)
print(result)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
