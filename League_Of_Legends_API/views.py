from django.shortcuts import render
from League_Of_Legends_API.modules.riot_api import *

from League_Of_Legends_API.summoner_form import SearchedSummonerNameForm


def home(request):
    summoner_info = riot_API_summoner_info('TheFlyingBannana')
    summoners = {
        'summoner': summoner_info,
        'icon_url': get_profile_icon_url(summoner_info.get('profileIconId'))
    }
    return render(request, 'League_Of_Legends_API/home.html', summoners)


def results(request):
    if request.method == 'GET':
        summoner_name_form = SearchedSummonerNameForm(request.GET)

        if summoner_name_form.is_valid():
            summoner_name = summoner_name_form.cleaned_data['summoner_name']
            summoner_info = riot_API_summoner_info(summoner_name)
            summoner_live_game_request = riot_API_live_game(summoner_info.get('id'))
            summoner_ranked_info = riot_API_ranked_info(summoner_info.get('id'))

            if summoner_live_game_request == "Not In Game":
                summoners = {
                    'summoner': summoner_info,
                    'icon_url': get_profile_icon_url(summoner_info.get('profileIconId')),
                    'is_in_game': False,
                    'ranked_info': summoner_ranked_info,
                    'ranked_tier_url': get_emblem_url(summoner_ranked_info)
                }
            else:
                summoner_live_game_info = summoner_live_game_request.get('participants')
                summoners = {
                    'summoner': summoner_info,
                    'icon_url': get_profile_icon_url(summoner_info.get('profileIconId')),
                    'is_in_game': True,
                    'champions': get_champion_url(summoner_live_game_info),
                    'live_game': summoner_live_game_info,
                    'ranked_info': summoner_ranked_info,
                    'ranked_tier_url': get_emblem_url(summoner_ranked_info)
                }

            return render(request, 'League_Of_Legends_API/results.html', summoners)
        else:
            print("form is not valid")
            summoners = {
                'form': summoner_name_form,
            }
            return render(request, 'League_Of_Legends_API/results.html', summoners)

    return render(request, 'League_Of_Legends_API/results.html')
