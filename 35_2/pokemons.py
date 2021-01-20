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
