from dotenv import load_dotenv
import os
import requests
from helper_funcs import *

# Load and access environment variables from .env file, fail and exit program if not set
load_dotenv()
api_key = os.getenv("API_KEY")
if not api_key:
    raise RuntimeError("API_KEY is not set")

# Set default for number of responses
search_limit = "5"

# Set empty list for favorites for later use
favorites = []

# Set default for units; options include: standard(Kelvin), metric(Celsius), and imperial(Fahrenheit)
units = "imperial"

# Sets urls for later querying in functions      
city_url = "https://api.openweathermap.org/geo/1.0/direct?q="
weather_url = "https://api.openweathermap.org/data/2.5/weather?"

# Logic used by all searches; fetches desired city with lat/lon for later use
# This step is necessary as searching directly by name is considered deprecated!
def get_city(user_input):
    # Ensure consistent formatting
    city = format_input(user_input)

    # Combine data and make a request
    request_url = city_url+city+"&limit="+search_limit+"&appid="+api_key
    response = requests.get(request_url)
    data = response.json()

    # Makes a dictionary for return value while creating a displayable list for gathering user input
    city_dict_list = []
    displayable_list = []
    for loc in data:
        parts = build_dict(loc)
        city_dict_list.append(parts)
        displayable_list.append(format_location(parts))
    user_choice = display_cities(displayable_list, search_limit)

    return city_dict_list[user_choice-1]

# Based off of the lattitude and longitude; fetches weather in desired city
def get_weather(lon, lat):
    # Combine data and make a request
    request_url = weather_url+"lat="+str(lat)+"&lon="+str(lon)+"&appid="+api_key+"&units="+units
    response = requests.get(request_url)
    data = response.json()
    display_weather(data)

# Attempts to search for the weather of a city when given a valid name
def search_name(user_input):
    city = get_city(user_input)
    get_weather(city.get("lon"), city.get("lat"))

# Attempts to search for the weather of a favorite city
def search_favorites():
    if len(favorites) == 0:
        print("Cannot search for a favorite city as there are none in the list!")
    user_choice = prompt_search(favorites)
    get_weather(favorites[user_choice-1].get("lon"), favorites[user_choice-1].get("lat"))
    
# Adds city to favorites
def add_favorites(user_input):
    if len(favorites) == 3:
        print("Cannot add a favorite city as the list is full!")
        return
    city = get_city(user_input)
    favorites.append(city)

# Lists favorite cities
def list_favorites():
    if len(favorites) == 0:
        print("You have no favorites currently!")
    else:
        display_favorites(favorites)
    for i in range(0, len(favorites)):
        get_weather(favorites[i].get("lon"), favorites[i].get("lat"))

# Deletes a favorite city to delete based on user choice
def delete_favorites():
    if len(favorites) == 0:
        print("Cannot delete a favorite city as there are none in the list!")
    user_choice = prompt_delete(favorites)
    del favorites[user_choice-1]

