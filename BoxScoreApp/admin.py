from django.contrib import admin
from .models import Player, Team, Game, PlayerGameStats

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(PlayerGameStats)

#username sbasavaraju