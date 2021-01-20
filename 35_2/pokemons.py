# reading a json file

import json

with open("pokemons.json") as file:
    content = file.read()
    pokemons = json.loads(content)["results"]
    # "load" will load a JSON from file while "loads" will from "text"

print(pokemons[0])

# another way of reading JSON

with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]
    # here we're loading the file
    # that's why we're using load instead
print(pokemons[0])


with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

grass_type_pokemons = [
    pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
]
# Abre o arquivo para escrevermos apenas o pokemons do tipo grama

with open("grass_pokemons.json", "w") as file:
    json_to_write = json.dumps(
        grass_type_pokemons
    )  # conversão de Python para o formato json (str)
    file.write(json_to_write)
