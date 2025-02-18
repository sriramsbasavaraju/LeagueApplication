from django.db import models
from django.utils.text import slugify
import random

# Player model
class Player(models.Model):
    POSITIONS = [
        (1, "Point Guard"),
        (2, "Shooting Guard"),
        (3, "Small Forward"),
        (4, "Power Forward"),
        (5, "Center"),
    ]
    name = models.CharField(max_length=100)
    # slug = models.SlugField(unique=True, blank=True)
    number = models.IntegerField()
    height = models.IntegerField()  # Height in cm or inches
    weight = models.FloatField()    # Weight in kg or lbs
    position = models.IntegerField(choices=POSITIONS)
    team = models.ForeignKey("Team", related_name="players", on_delete=models.SET_NULL, null=True)
    # Season stats
    season_points = models.IntegerField(default=0)
    season_assists = models.IntegerField(default=0)
    season_off_rebounds = models.IntegerField(default=0)
    season_def_rebounds = models.IntegerField(default=0)
    season_fouls = models.IntegerField(default=0)
    season_steals = models.IntegerField(default=0)
    season_blocks = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    # def save(self, *args, **kwargs):
    #     if not self.slug:  # Generate a random 6-digit number if slug is missing
    #         while True:
    #             random_slug = str(random.randint(100000, 999999))  # Generate a 6-digit random number
    #             if not Player.objects.filter(slug=random_slug).exists():  # Ensure uniqueness
    #                 self.slug = random_slug
    #                 break
    #     super().save(*args, **kwargs)

# Team model
class Team(models.Model):
    name = models.CharField(max_length=100)
    head_coach = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# Game model
class Game(models.Model):
    slug = models.SlugField(unique=True, blank=True)
    team1 = models.ForeignKey(Team, related_name="games_as_team1", on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name="games_as_team2", on_delete=models.CASCADE)
    date = models.DateField()
    def __str__(self):
        return self.team1.name + " vs " + self.team2.name + " " + str(self.date)
    def save(self, *args, **kwargs):
        if not self.slug:  # Generate a random 6-digit number if slug is missing
            while True:
                random_slug = str(random.randint(100000, 999999))  # Generate a 6-digit random number
                if not Game.objects.filter(slug=random_slug).exists():  # Ensure uniqueness
                    self.slug = random_slug
                    break
        super().save(*args, **kwargs)

# BoxScore model
class PlayerGameStats(models.Model):
    game = models.ForeignKey(Game, related_name="player_stats", on_delete=models.CASCADE)
    player = models.ForeignKey(Player, related_name="game_stats", on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    off_rebounds = models.IntegerField(default=0)
    def_rebounds = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    fouls = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    blocks = models.IntegerField(default=0)
    def __str__(self):
        return self.player.name