"""
URL configuration for BoxScore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BoxScoreApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'home'),    
    path('teams/', views.team_list, name= 'team_list'),
    path('teams/add_team/', views.add_team, name='add_team'),
    path('teams/<str:team_name>/', views.team_details, name= 'team_detail'),
    path('teams/<str:team_name>/edit/', views.edit_team, name='edit_team'),  
    path('games/', views.games_list, name = 'games_list'),
    path('players/', views.player_list, name = 'player_list'),
    path('players/add_player/', views.add_player, name='add_player'),
    path('players/<str:player_name>/', views.player_details, name = 'player_detail'),
    path('players/<str:player_name>/edit/', views.edit_player, name='edit_player'),
    path('games/<slug:slug>', views.game_display, name = 'game_display'), 
    path('games/<slug:slug>/edit/', views.edit_game, name='edit_game'),
    
    
]
