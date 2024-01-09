import requests
import time

API_KEY = 'f709362a2d9d4da69b2132534240501'
FAVORITE_CITIES = []  # Initialize an empty list for favorite cities

def get_weather(city):
    url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch weather data for {city}")
        return None

def display_weather(weather_data):
    if weather_data:
        print(f"Weather in {weather_data['location']['name']}, {weather_data['location']['country']}:")
        print(f"Temperature: {weather_data['current']['temp_c']}°C")
        print(f"Condition: {weather_data['current']['condition']['text']}")
    else:
        print("Failed to display weather data.")

def add_to_favorites(city):
    response = input(f"Do you want to add {city} to your favorite cities? (yes/no): ")
    if response.lower() == 'yes':
        FAVORITE_CITIES.append(city)
        print(f"{city} added to favorites.")
    else:
        print(f"{city} not added to favorites.")

def list_favorites():
    if FAVORITE_CITIES:
        print("Your favorite cities:")
        for city in FAVORITE_CITIES:
            print(city)
    else:
        print("No favorite cities yet.")

def remove_from_favorites(city):
    response = input(f"Do you want to remove {city} from your favorite cities? (yes/no): ")
    if response.lower() == 'yes':
        FAVORITE_CITIES.remove(city)
        print(f"{city} removed from favorites.")
    else:
        print(f"{city} not removed from favorites.")

def main():
    try:
        while True:
            city = input("Enter the city name: ")
            weather_data = get_weather(city)
            display_weather(weather_data)

            add_to_favorites(city)

            list_response = input("Do you want to list your favorite cities? (yes/no): ")
            if list_response.lower() == 'yes':
                list_favorites()

            remove_response = input("Do you want to remove this city from your favorites? (yes/no): ")
            if remove_response.lower() == 'yes':
                remove_from_favorites(city)

            time.sleep(15)  # Auto refresh every 15 seconds
    except KeyboardInterrupt:
        print("\nExiting the weather application.")

if __name__ == "__main__":
    main()
