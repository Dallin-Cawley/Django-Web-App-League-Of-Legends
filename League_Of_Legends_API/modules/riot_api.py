import requests
import json


def riot_API_summoner_info(name):
    url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name
    args = {'api_key': 'RGAPI-d4965f87-1b14-418c-b4b7-a7fa5efdee95'}
    riot_api_summoner_GET = requests.get(url, params=args)

    return json.loads(riot_api_summoner_GET.content)


def riot_API_live_game(summoner_id):
    url = "https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + str(summoner_id)
    args = {'api_key': 'RGAPI-d4965f87-1b14-418c-b4b7-a7fa5efdee95'}
    riot_api_live_game_GET = requests.get(url, params=args)

    return json.loads(riot_api_live_game_GET.content)


def get_profile_icon_url(icon_id):
    return 'http://ddragon.leagueoflegends.com/cdn/10.7.1/img/profileicon/' + str(icon_id) + '.png'


def get_champion_url(participants):
    champion_url_list = {}
    i = 0
    base_url = 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/'

    champion_file = open('League_Of_Legends_API/id_champion.txt', 'r')
    champion_dict = json.loads(champion_file.read())

    for participant in participants:
        url = base_url + champion_dict.get(str(participant.get('championId'))) + '_0.jpg'
        champion_url_list.update({i: url})
        i += 1

    return champion_url_list


def get_champion_name_from_id(champion_id):
    champion_file = open('League_Of_Legends_API/id_champion.txt', 'r')
    champion_dict = json.loads(champion_file.read())

    return champion_dict.get(str(champion_id))


def from_json(json_string):
    return json.loads(json_string)
