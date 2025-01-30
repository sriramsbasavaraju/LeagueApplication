from django.shortcuts import render, get_object_or_404, redirect
from .models import Team, Player, Game, PlayerGameStats
from .forms import PlayerForm, TeamForm, GameForm

def home(request):
    return render(request, 'BoxScoreApp/index.html')

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'BoxScoreApp/team_list.html', {'teams': teams})

def team_details(request, team_name):
    team = get_object_or_404(Team, name=team_name)
    players = team.players.all()
    return render(request, 'BoxScoreApp/team_detail.html', {'team': team, 'players': players})

def player_details(request, player_name):
    player = get_object_or_404(Player, name=player_name)
    return render(request, 'BoxScoreApp/player_detail.html', {'player': player})

def games_list(request):
    games = Game.objects.all()
    return render(request, 'BoxScoreApp/games_list.html', {'games': games})
def player_list(request):
    players = Player.objects.all().order_by('name')
    return render(request, 'BoxScoreApp/player_list.html', {'players': players})

def game_display(request, slug):
    game = get_object_or_404(Game, slug=slug)
    team1_players = game.team1.players.all()
    team2_players = game.team2.players.all()

    team1_stats = PlayerGameStats.objects.filter(game=game, player__team=game.team1)
    team2_stats = PlayerGameStats.objects.filter(game=game, player__team=game.team2)
    return render(request, 'BoxScoreApp/game_display.html', {
        'game': game,
        'team1_players': team1_players, 
        'team2_players': team2_players, 
        'team1_stats': team1_stats, 
        'team2_stats': team2_stats,
    })
def editor(request):
    return render(request, 'BoxScoreApp/editor.html')

def edit_player(request, player_name=None):
    if player_name:
        player = get_object_or_404(Player, name=player_name)
    else:
        player = None
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_detail', player_name=form.cleaned_data['name'])
    else:
        form = PlayerForm(instance=player)
    return render(request, 'BoxScoreApp/edit_player.html', {'form': form, 'player': player})

def edit_team(request, team_name=None):
    if team_name:
        team = get_object_or_404(Team, name=team_name)
    else:
        team = None
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_detail', team_name=form.cleaned_data['name'])
    else:
        form = TeamForm(instance=team)
    return render(request, 'BoxScoreApp/edit_team.html', {'form': form, 'team': team})

# Create your views here.
