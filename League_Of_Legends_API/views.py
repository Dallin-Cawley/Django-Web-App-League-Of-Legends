from django.shortcuts import render
from League_Of_Legends_API.modules.riot_api import riot_API_summoner_info


def home(request):
    summoners = {
        'url': riot_API_summoner_info('TheFlyingBannana')
    }
    return render(request, 'League_Of_Legends_API/home.html', summoners)


def results(request):
    return render(request, 'League_Of_Legends_API/results.html')
