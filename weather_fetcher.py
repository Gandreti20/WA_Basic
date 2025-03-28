import requests
import geocoder  # New import for geolocation

def fetch_weather(city, api_key):
    # Construct the API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={api_key}&units=metric"
    print(f"Fetching weather data from: {url}")  # Debugging line
    
    # Fetch the weather data
    response = requests.get(url)
    
    # Check if the request was successful
    print("Response Status Code:", response.status_code)  # Debugging line
    if response.status_code == 200:
        data = response.json()
        # Extract relevant information
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity' ]  # Extract humidity
        location_name = data['name']  # Extract location name
        print(f"Weather in {location_name}: {weather}, Temperature: {temperature}°C, Humidity: {humidity}%")  # Updated line
    else:
        print("Error fetching weather data:", response.json())  # Print the error message

def fetch_weather_by_location(api_key):
    # Get current location
    g = geocoder.ip('me')  # Get location based on IP
    if g.ok:
        city = g.city  # Extract city from location
        print(f"Fetching weather data for your current location: {city}")
        fetch_weather(city, api_key)  # Call existing function
    else:
        print("Could not determine your location.")

if __name__ == "__main__":
    api_key = "9613dd1e193de674cec4d2bf5d0b72cf"  # Your OpenWeatherMap API key
    while True:
        choice = input("Type '1' for current location weather or '2' to enter city name (or type 'exit' to quit): ")
        if choice == '1':
            fetch_weather_by_location(api_key)  # Fetch weather by location
        elif choice == '2':
            city = input("Enter city name: ")
            fetch_weather(city, api_key)  # Fetch weather by city
        elif choice.lower() == 'exit':
            break
