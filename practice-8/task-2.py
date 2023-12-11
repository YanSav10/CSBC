import pytz
from datetime import datetime
from geopy.geocoders import Nominatim


def get_current_time(latitude, longitude):
    geolocator = Nominatim(user_agent="geo_locator")
    location = geolocator.reverse((latitude, longitude), language='en')

    if 'timezone' not in location.raw:
        return "Timezone information is not available for the provided coordinates."

    timezone = pytz.timezone(location.raw['timezone'])
    current_time = datetime.now(timezone)
    return current_time.strftime("%Y-%m-%d %H:%M:%S %Z")


def main():
    print("Enter the coordinates (latitude, longitude):")
    latitude = float(input("Latitude: "))
    longitude = float(input("Longitude: "))

    current_time = get_current_time(latitude, longitude)
    print(f"The current time at the provided coordinates is: {current_time}")


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.now()))


printTimeStamp("Yan Savinov")
