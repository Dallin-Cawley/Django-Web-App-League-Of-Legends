from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='league-home'),
    path('results/', views.results, name='results'),

]