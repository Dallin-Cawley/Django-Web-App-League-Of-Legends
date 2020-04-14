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
    print(request.GET)
    if request.method == 'GET':
        summoner_name_form = SearchedSummonerNameForm(request.GET)

        if summoner_name_form.is_valid():
            print("form is valid")
            summoner_name = summoner_name_form.cleaned_data['summoner_name']
            summoner_info = riot_API_summoner_info(summoner_name)
            summoner_live_game_request = riot_API_live_game(summoner_info.get('id'))

            if not summoner_live_game_request:
                summoners = {
                    'summoner': summoner_info,
                    'icon_url': get_profile_icon_url(summoner_info.get('profileIconId')),
                    'is_in_game': False
                }
            else:
                summoner_live_game_info = summoner_live_game_request.get('participants')
                summoners = {
                    'summoner': summoner_info,
                    'icon_url': get_profile_icon_url(summoner_info.get('profileIconId')),
                    'is_in_game': True,
                    'champions': get_champion_url(summoner_live_game_info),
                    'live_game': summoner_live_game_info
                }

            return render(request, 'League_Of_Legends_API/results.html', summoners)
        else:
            print("form is not valid")
            summoners = {
                'form': summoner_name_form,
            }
            return render(request, 'League_Of_Legends_API/results.html', summoners)

    return render(request, 'League_Of_Legends_API/results.html')
