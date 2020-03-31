from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('<h1>League Home</h1>')


def results(request):
    return HttpResponse('<h1>League Results</h1>')
