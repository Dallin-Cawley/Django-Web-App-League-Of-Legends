import requests
import json


def riot_API_summoner_info(name):
    url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name
    args = {'api_key': 'RGAPI-d4965f87-1b14-418c-b4b7-a7fa5efdee95'}
    riot_api_summoner_GET = requests.get(url, params=args)

    return from_json(riot_api_summoner_GET.content)


def get_profile_icon_url(icon_id):
    return 'http://ddragon.leagueoflegends.com/cdn/10.7.1/img/profileicon/' + str(icon_id) + '.png'


def from_json(json_string):
    return json.loads(json_string)
