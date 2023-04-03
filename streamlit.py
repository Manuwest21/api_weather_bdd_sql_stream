import requests
import streamlit as st

# API key
API_KEY = "41a65c4b3f220173fa1f518a942388bc"

# Base URL for weather API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Function to get weather data
def get_weather_data(city: str, country: str) -> dict:
    # API endpoint for weather data
    endpoint = f"{BASE_URL}?q={city},{country}&appid={API_KEY}"

    # Send request to API endpoint
    response = requests.get(endpoint)

    # Return weather data as dictionary
    return response.json()

# Streamlit app
st.title("Weather App")

# User input for city and country
city = st.text_input("Enter city name")
country = st.text_input("Enter country code")

# Check if city and country are provided
if city and country:
    # Get weather data for given city and country
    weather_data = get_weather_data(city, country)

    # Display weather data
    # st.write(f"Weather in {city.title()}, {country.upper()}")
    st.write(f"Temperature: {weather_data['main']['temp']} K")
    st.write(f"Feels like: {weather_data['main']['feels_like']} K")
    st.write(f"Humidity: {weather_data['main']['humidity']} %")
    st.write(f"Pressure: {weather_data['main']['pressure']} hPa")
    st.write(f"Wind speed: {weather_data['wind']['speed']} m/s")
    st.write(f"Wind direction: {weather_data['wind']['deg']} deg")