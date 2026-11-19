
import argparse
import requests


def get_coordinates(city):
    # Get the latitude and longitude for the city

    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": city,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "MWCC"
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    if len(data) == 0:
        print("City not found.")
        return None, None

    latitude = data[0]["lat"]
    longitude = data[0]["lon"]

    return latitude, longitude


def get_noaa_endpoint(lat, lon):
    # Get the NOAA forecast URL

    url = "https://api.weather.gov/points/" + lat + "," + lon

    response = requests.get(url)
    data = response.json()

    forecast_url = data["properties"]["forecast"]

    return forecast_url


def get_noaa_forecast(url):
    # Get the weather forecast

    response = requests.get(url)
    data = response.json()

    periods = data["properties"]["periods"]

    return periods


def main():
    # Set up the command line options

    parser = argparse.ArgumentParser(
        description="Weather Forecast Program"
    )

    parser.add_argument(
        "-l", "--location",
        required=True,
        help="Enter a city and state"
    )

    parser.add_argument(
        "-d", "--detailed",
        action="store_true",
        help="Show the detailed forecast"
    )

    parser.add_argument(
        "-w", "--week",
        action="store_true",
        help="Show the weekly forecast"
    )

    parser.add_argument(
        "-a", "--average",
        action="store_true",
        help="Show the average temperature"
    )

    args = parser.parse_args()

    print("\nGetting weather for", args.location)

    latitude, longitude = get_coordinates(args.location)

    if latitude is None:
        return

    forecast_url = get_noaa_endpoint(latitude, longitude)

    periods = get_noaa_forecast(forecast_url)

    if len(periods) == 0:
        print("No weather information available.")
        return

    # Display the weekly forecast

    if args.week:

        print("\nWEEKLY WEATHER FORECAST")
        print("----------------------------")

        for period in periods[:14]:
            print(
                period["name"],
                "-",
                str(period["temperature"]) + "°" +
                period["temperatureUnit"],
                "-",
                period["shortForecast"]
            )

    # Calculate the average temperature

    elif args.average:

        temperatures = []

        for period in periods:
            temperatures.append(period["temperature"])

        average = sum(temperatures) / len(temperatures)

        print("\nAVERAGE TEMPERATURE")
        print("----------------------------")
        print("Average temperature:", round(average, 1), "degrees")

    # Display the current forecast

    else:

        current = periods[0]

        print("\nWEATHER FORECAST")
        print("----------------------------")

        print("Forecast:", current["name"])
        print(
            "Temperature:",
            current["temperature"],
            current["temperatureUnit"]
        )
        print("Conditions:", current["shortForecast"])

        if args.detailed:
            print("\nDetailed Forecast:")
            print(current["detailedForecast"])


if __name__ == "__main__":
    main()
