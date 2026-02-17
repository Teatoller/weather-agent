# weather.py
# A simple version of the weather program that just prints the current weather for a given location.


def get_current_weather(location):
    # This is a placeholder for the actual weather fetching logic.
    # In a real implementation, you would use an API to get the weather data.
    return f"The current weather in {location} is sunny with a temperature of 25°C."


def main():
    location = input("Enter a location to get the current weather: ")
    weather = get_current_weather(location)
    print(weather)
if __name__ == "__main__":    
    main()