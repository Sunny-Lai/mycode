

import requests

result = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
name = result.json()
print(result['teamName'
