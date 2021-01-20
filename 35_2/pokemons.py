# reading a json file

import json

with open("pokemons.json") as file:
    content = file.read()
    pokemons = json.loads(content)["results"]
    # "load" will load a JSON from file while "loads" will from "text"

print(pokemons[0])
