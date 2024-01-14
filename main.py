import requests

api_url = "https://api.weather.gov/forecast"


def do_research(latitude, longitude):
    try:
        r = requests.get(f"{api_url}/{latitude},{longitude}")
        r.raise_for_status()

        forecast_data = r.json()

        if 'properties' in forecast_data and 'periods' in forecast_data['properties']:
            first_period = forecast_data['properties']['periods'][0]
            temperature_celsius = (first_period['temperature'] - 32) * 5/9
            wind_direction = first_period['windDirection']
            wind_speed = first_period['windSpeed']

            print(f"Temperature: {temperature_celsius:.2f} °C")
            print(f"Wind Direction: {wind_direction}")
            print(f"Wind Speed: {wind_speed}")
        else:
            print("No forecast information available for the given coordinates.")

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")


def get_input():
    latitude = 0.0
    longitude = 0.0

    while True:

        latitude_input = input("Enter latitude: ")
        longitude_input = input("Enter longitude: ")

        try:
            latitude = float(latitude_input)
        except ValueError:
            print("Latitude is invalid")

        try:
            longitude = float(longitude_input)
            break
        except ValueError:
            print("Longitude is invalid")
            continue

    do_research(latitude, longitude)


if __name__ == '__main__':
    get_input()
