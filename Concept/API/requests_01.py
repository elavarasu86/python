import json
import requests

# this is the base url to be used.
base_url = "https://pokeapi.co/api/v2/"
pokemon_name = "pikachu"


# This function is used to get pokemon information.
def get_pokemon_info(name):
    # below format string gives complete url. Based on name we can get specific pokemon details.
    url = f"{base_url}/pokemon/{name}"
    # below requests.get method will hit API and gives response.
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")


pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"]}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")