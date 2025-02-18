from django.shortcuts import render, get_object_or_404, redirect
from .models import Team, Player, Game, PlayerGameStats
from .forms import PlayerForm, TeamForm, GameForm, PlayerGameStatsForm

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

def edit_game(request, slug=None):
    if slug:
        game = get_object_or_404(Game, slug=slug)
        team1_players = game.team1.players.all()
        team2_players = game.team2.players.all()
    else:
        game = None
    if request.method == 'POST':
        game_form = GameForm(request.POST, instance=game)
        team1_forms = [PlayerGameStatsForm(request.POST, prefix=str(player.id), instance=PlayerGameStats.objects.get(game=game, player=player)) for player in team1_players]
        team2_forms = [PlayerGameStatsForm(request.POST, prefix=str(player.id), instance=PlayerGameStats.objects.get(game=game, player=player)) for player in team2_players]
        if game_form.is_valid():
            game_form.save()
            for form in team1_forms + team2_forms:
                if form.is_valid():
                    form.save()
            return redirect('game_display', slug=game.slug)
    else:
        game_form = GameForm(instance=game)
        team1_forms = [PlayerGameStatsForm(prefix=str(player.id), instance=PlayerGameStats.objects.get(game=game, player=player)) for player in team1_players]
        team2_forms = [PlayerGameStatsForm(prefix=str(player.id), instance=PlayerGameStats.objects.get(game=game, player=player)) for player in team2_players]
    return render(request, 'BoxScoreApp/edit_game.html', {'game_form': game_form, 'game': game, 'team1_forms': team1_forms, 'team2_forms': team2_forms})

def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm()
    return render(request, 'BoxScoreApp/add_player.html', {'form': form})
# Create your views here.
