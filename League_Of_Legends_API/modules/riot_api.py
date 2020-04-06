import requests
import json


def riot_API_summoner_info(name):
    url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name
    args = {'api_key': 'RGAPI-72e44e7e-5527-4b1a-89f6-7d011b02dff6'}
    riot_api_summoner_GET = requests.get(url, params=args)

    return from_json(riot_api_summoner_GET.content)


def get_profile_icon_url(icon_id):
    return 'http://ddragon.leagueoflegends.com/cdn/10.7.1/img/profileicon/' + str(icon_id) + '.png'


def from_json(json_string):
    return json.loads(json_string)
