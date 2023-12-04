import datetime

# Словник з абонентами та їх номерами телефонів
subscribers = {
    'Anna': '0931234567',
    'Alice': '0977654321',
    'Vadim': '0951112233',
    'Iryna': '0979876543',
    'Mike': '0935554444',
    'Kate': '0661122334',
    'Alex': '0679998881',
    # Додаткові абоненти з різними кодами операторів
    'Mary': '0981112233',
    'Peter': '0949876543',
    'Eva': '0965554444',
    'Taras': '0681122334',
    'Vitalii': '0919998881'
}

# Функція для фільтрування абонентів за мобільним оператором
def filter_subscribers(operator_code, subscribers_dict):
    filtered_subscribers = filter(lambda subscriber: subscriber[1].startswith(operator_code), subscribers_dict.items())
    return list(map(lambda subscriber: subscriber[0], filtered_subscribers))

# Усі коди мобільних операторів в Україні
operator_codes = ['050', '066', '095', '099', '063', '073', '067', '068', '091', '092', '093', '094', '095', '096', '097', '098']

# Виведення списків абонентів для кожного оператора
for code in operator_codes:
    operator_subscribers = filter_subscribers(code, subscribers)
    print(f"Абоненти оператора з кодом {code}: {operator_subscribers}")


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
