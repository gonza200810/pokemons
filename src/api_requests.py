'''
vamos a realizar nuestra primera peticion a una Api

'''
import requests

# la api
api_url = 'https://pokeapi.co/api/v2/pokemon/ditto'
# peticion
response = requests.get(api_url, timeout = 10)
#para revisar si hubo errores en la peticicion
response.raise_for_status()

print(response.status_code)
pokemon = response.json()
# vamos a inprimir el tipo de variables de pokemon
print(type(pokemon))
#vamos a imprimir el contenido de pokemons
print(pokemon)

# vamos a imprimir el id 
print(pokemon['id'])
print(pokemon['name'])
print('no recuerdo:', pokemon['is_default'])

print('altura del pokemon:', pokemon['height']/10)
print('peso:',pokemon['weight']/10)