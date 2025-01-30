from django import template
from BoxScoreApp.models import Game, PlayerGameStats

register = template.Library()

@register.filter
def divide(value, divisor):
    try:
        return round(value/divisor, 1)
    except(TypeError, ZeroDivisionError):
        return 0
    
@register.filter
def game_str(game: Game):
    return game.__str__()

@register.filter
def total_points(stats: PlayerGameStats):
    return sum(p.points for p in stats)