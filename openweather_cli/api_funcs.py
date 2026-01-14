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

    return city_dict_list[user_choice-1], displayable_list[user_choice-1]

# Based off of the lattitude and longitude; fetches weather in desired city
def get_weather(lat, lon):
    # Combine data and make a request
    request_url = weather_url+"lat="+str(lat)+"&lon="+str(lon)+"&appid="+api_key+"&units="+units
    response = requests.get(request_url)
    data = response.json()
    


def search_name(user_input):
    city = get_city(user_input) 
    get_weather(city[0].get("lon"), city[0].get("lat"))
