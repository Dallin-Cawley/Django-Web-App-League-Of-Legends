from django.shortcuts import render
from django.http import HttpResponse

player = [
    {
        'summoner_name': 'TheFlyingBannana',
        'summoner_level': 142,
        'summoner_icon_id': 192,
        'games_won': 1000
    },
    {
        'summoner_name': 'Taegondy',
        'summoner_level': 200,
        'summoner_icon_id': 36,
        'games_won': 2000
    }
]


def home(request):
    summoners = {
        'player': player
    }
    return render(request, 'League_Of_Legends_API/home.html', summoners)


def results(request):
    return render(request, 'League_Of_Legends_API/results.html')
