import requests
import pytest

URL = 'https://api.pokemonbattle.ru/'
trainer_id = 7100

def test_status_code200():
    response = requests.get(url = f'{URL}v2/trainers')
    assert response.status_code == 200

def test_name_trainer():
    response_name = response = requests.get(url = f'{URL}v2/trainers?trainer_id={trainer_id}')
    assert response_name.json()["data"][0]["trainer_name"] == 'Тренер Рик'
