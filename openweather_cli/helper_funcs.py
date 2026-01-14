# Ensures data is always in a capitalized format for searching
def format_input(user_input):
    formatted = user_input.capitalize()
    return formatted

# Builds a dictionary for given location for later use:
def build_dict(loc):
    parts = { 
        "name": loc.get("name"),
        "state": loc.get("state"),
        "country": loc.get("country"),
        "lat": loc.get('lat'),
        "lon": loc.get('lon'),
    }
    return parts

# Join location data together for display
def format_location(loc_dict):   
    fields = ("name", "state", "country", "lat", "lon")
    parts = []

    for field in fields:
        value = loc_dict.get(field)
        if value:
            parts.append(str(value))

    return ", ".join(parts)

# Displays cities found and then prompts for which to use
def display_cities(city_list, search_limit):
    print("\n============ CITIES FOUND ============\n") 
    for i in range(0, len(city_list)):
        print(f"{i+1}) {city_list[i]}")
    print("\n======================================\n")
   
    # Ensure choice submitted by the user is valid 
    user_choice = 0
    while True:
        try:
            user_choice = int(input("Please input the number corresponding to the city you want to use: "))
            pass
        except ValueError:
            print("That is not an integer. Please try again.")
            continue

        if user_choice < 1 or user_choice > int(search_limit):
            print("Choice is outside of range")
            continue
        else: 
            print("City number chosen: ", user_choice)
            break

    return user_choice

# Displays weather for chosen city in great detail
def display_weather(data):
    report = f"""
============ WEATHER REPORT ============
Location: {data['name']}, {data.get('sys', {}).get('country', 'N/A')}

Coordinates:
  Latitude:  {data['coord']['lat']}
  Longitude: {data['coord']['lon']}

Weather:
{chr(10).join(f"  {w['main']} ({w['description']})" for w in data['weather'])}

Temperature:
  Current:    {data['main']['temp']}°F
  Feels like: {data['main']['feels_like']}°F
  Min:        {data['main']['temp_min']}°F
  Max:        {data['main']['temp_max']}°F

Conditions:
  Humidity: {data['main']['humidity']}%
  Pressure: {data['main']['pressure']} hPa
  Clouds:   {data['clouds']['all']}%

Wind:
  Speed:     {data['wind']['speed']} mph
  Direction: {data['wind']['deg']}°
========================================
"""
    print(report.strip())

# Ensures that user selects a valid city to search
def prompt_search(favorites):
    display_favorites(favorites)
    user_choice = 0
    while True:
        try:
            user_choice = int(input("Please input the number corresponding to the city you want to search: "))
            pass
        except ValueError:
            print("That is not an integer. Please try again.")
            continue

        if user_choice > len(favorites) or user_choice < 1:
            print("Choice is outside of range")
            continue
        else: 
            print("Favorite city to search: ", user_choice)
            break

    return user_choice

# Loops through favorites, makes them displayable, and prints
def display_favorites(favorites):
    displayable_list = []
    for i in range(0, len(favorites)):
        displayable_list.append(format_location(favorites[i]))

    print("\n============ FAVORITE CITIES ============\n") 
    for i in range(0, len(displayable_list)):
        print(f"{i+1}) {displayable_list[i]}")
    print("\n======================================\n")

# Ensures that user selects a valid city to delete
def prompt_delete(favorites):
    display_favorites(favorites)
    user_choice = 0
    while True:
        try:
            user_choice = int(input("Please input the number corresponding to the city you want to delete: "))
            pass
        except ValueError:
            print("That is not an integer. Please try again.")
            continue

        if user_choice > len(favorites) or user_choice < 1:
            print("Choice is outside of range")
            continue
        else: 
            print("Favorite city to delete: ", user_choice)
            break

    return user_choice


