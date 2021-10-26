import requests
from pprint import pprint

token = "2619421814940190"
hero_name_list = ["Hulk", "Captain America", "Thanos"]


def get_id_hero(hero_name):
    url = f'https://superheroapi.com/api/{token}/search/{hero_name}'
    resp = requests.get(url).json()
    return resp['results'][0]["id"]


def max_intelligence_hero(hero_list):
    max_intelligence = -1
    for hero_name in hero_list:
        id = get_id_hero(hero_name)
        url = f'https://superheroapi.com/api/{token}/{id}/powerstats'
        resp = requests.get(url).json()
        intelligence = int(resp["intelligence"])
        if intelligence > max_intelligence:
            max_intelligence = intelligence
            buf = hero_name
    return buf


print(max_intelligence_hero(hero_name_list))
