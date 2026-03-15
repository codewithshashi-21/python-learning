# Day 26 – Fetching data from a public API

import requests


def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print("Could not get weather data.")
            return

        data = response.json()

        current = data["current_condition"][0]
        temp = current["temp_C"]
        desc = current["weatherDesc"][0]["value"]

        print(f"\nWeather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {desc}")

    except requests.exceptions.RequestException:
        print("Network error. Try again.")


if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)