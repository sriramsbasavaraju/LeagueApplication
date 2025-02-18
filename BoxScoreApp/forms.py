from django import forms
from .models import Player, Team, Game, PlayerGameStats

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['date']

class PlayerGameStatsForm(forms.ModelForm):
    class Meta:
        model = PlayerGameStats
        exclude = ['game']
        # fields = '__all__'