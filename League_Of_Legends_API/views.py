from django.shortcuts import render
from League_Of_Legends_API.modules.riot_api import *


def home(request):
    summoner_info = riot_API_summoner_info('TheFlyingBannana')
    summoners = {
        'summoner': summoner_info,
        'icon_url': get_profile_icon_url(summoner_info.get('profileIconId'))
    }
    return render(request, 'League_Of_Legends_API/home.html', summoners)


def results(request):
    return render(request, 'League_Of_Legends_API/results.html')
