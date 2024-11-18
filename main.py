import requests

URL = 'https://api.pokemonbattle.ru/'
header = {'trainer_token' : '6442ca1e9d6c1005367ea1a6f8a01e4a', 'Content-Type' : 'application/json'}

body_creation = {
    "name": "generate",         #Тут прописываем имя для нового покемона
    "photo_id": -1              #Тут вставляем id фотографии нового покемона
}

body_change = {
    "pokemon_id": "137832",     #Id покемона, имя которого надо изменить
    "name": "Pythonika",        #Тут меняем имя покемона
    "photo_id": 78              #Если надо изменить фото
}

body_in_pokeball = {
    "pokemon_id": "137832"      #Id покемона, которого надо добавить в покебол
}

# Создание покемона (**POST /pokemons**)
response_creation = requests.post(url = f'{URL}v2/pokemons', headers = header, json = body_creation)
print(response_creation.text)


#Смена имени покемона (**PUT /pokemons**)
response_change = requests.put(f'{URL}/v2/pokemons', headers = header, json = body_change)
print(response_change.text)


#Поймать покемона в покебол (**POST /trainers/add_pokeball** )
response_in_pokeball = requests.post(url = f'{URL}v2/trainers/add_pokeball', headers = header, json = body_in_pokeball)
print(response_in_pokeball.text)