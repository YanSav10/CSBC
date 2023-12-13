import datetime

def remove_leading_zeros(ip):
    parts = ip.split('.')

    # Видалення незначущих нулів з кожного числа та складання знову
    new_ip = ".".join(str(int(part)) for part in parts)

    return new_ip

input_ip = input("Введіть IP-адресу: ")

print("IP-адреса після видалення незначущих нулів:", remove_leading_zeros(input_ip))


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
