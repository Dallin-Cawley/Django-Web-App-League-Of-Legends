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

    if riot_API_isInGame(riot_api_live_game_GET):
        return json.loads(riot_api_live_game_GET.content)
    else:
        return "Not In Game"


def riot_API_ranked_info(summoner_id):
    url = 'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + str(summoner_id)
    args = {'api_key': 'RGAPI-d4965f87-1b14-418c-b4b7-a7fa5efdee95'}
    riot_api_ranked_info_GET = requests.get(url, params=args)

    return format_ranked_info(json.loads(riot_api_ranked_info_GET.content))


def format_ranked_info(ranked_info):
    queue_types = {}

    for rank in ranked_info:

        if rank.get('queueType') == 'RANKED_FLEX_SR':
            queue_types.update({'is_flex_rank': True})
            queue_types.update({'flex_tier': format_tier_name(rank.get('tier'))})
            queue_types.update({'flex_rank': rank.get('rank')})

        elif rank.get('queueType') == 'RANKED_SOLO_5x5':
            queue_types.update({'is_solo_rank': True})
            queue_types.update({'solo_tier': format_tier_name(rank.get('tier'))})
            queue_types.update({'solo_rank': rank.get('rank')})
        else:
            queue_types.update({'is_solo_rank': False})
            queue_types.update({'is_flex_rank': False})

    return queue_types


def format_tier_name(tier):
    switch = {
        'IRON': 'Iron',
        'BRONZE': 'Bronze',
        'SILVER': 'Silver',
        'GOLD': 'Gold',
        'PLATINUM': 'Platinum',
        'DIAMOND': 'Diamond',
        'MASTER': 'Master',
        'CHALLENGER': 'Challenger'
    }

    return switch.get(tier, 'Not Ranked')


def get_emblem_url(queue_types):
    base_url = '/images/Emblem_'
    ranked_emblem_urls = {}

    if queue_types.get('is_flex_rank'):
        full_url = base_url + queue_types.get('flex_tier') + '.png'
        ranked_emblem_urls.update({'flex': full_url})
    else:
        ranked_emblem_urls.update({'flex': ''})

    if queue_types.get('is_solo_rank'):
        full_url = base_url + queue_types.get('solo_tier') + '.png'
        ranked_emblem_urls.update({'solo': full_url})
    else:
        ranked_emblem_urls.update({'solo': ''})

    return ranked_emblem_urls


def riot_API_isInGame(request):
    if request.status_code == 200:
        return True
    else:
        return False


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
