import requests

URL = "https://pokeapi.co/api/v2/pokemon/15"

response = requests.get(URL)
data = response.json()
print(data.keys())

data_types = data["types"]

types_list = []

for type in data_types:
    types_list.append(type["type"]["name"])

types = f"{data["name"]} " + ', '.join(types_list)
print(types)