# Generated by Django 5.1.2 on 2025-01-31 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BoxScoreApp', '0005_game_team1_score_game_team2_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='team1_score',
        ),
        migrations.RemoveField(
            model_name='game',
            name='team2_score',
        ),
    ]
