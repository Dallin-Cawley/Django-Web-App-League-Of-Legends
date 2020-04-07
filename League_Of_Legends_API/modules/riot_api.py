import requests
import json


def riot_API_summoner_info(name):
    url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name
    args = {'api_key': 'RGAPI-b456c718-cd63-468a-8206-5ad4e8faa6d3'}
    riot_api_summoner_GET = requests.get(url, params=args)

    return from_json(riot_api_summoner_GET.content)


def get_profile_icon_url(icon_id):
    return 'http://ddragon.leagueoflegends.com/cdn/10.7.1/img/profileicon/' + str(icon_id) + '.png'


def from_json(json_string):
    return json.loads(json_string)
