from django.db import models
from django.db.models.fields.related import ForeignKey

from core.models import TimeStampedModel, UUIDModel
from users.models import User


class Achievement(TimeStampedModel, UUIDModel, models.Model):
    name = models.CharField(max_length=150, default="")
    description = models.TextField(blank=True, default="")
    points = models.IntegerField(blank=True, default=0)
    author = ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)


class Game(TimeStampedModel, UUIDModel, models.Model):
    name = models.CharField(max_length=150, default="")
    external_url = models.CharField(max_length=150, default="", null=True, blank=True)
    author = ForeignKey(User, on_delete=models.CASCADE)


class GameAchievement(TimeStampedModel, UUIDModel, models.Model):
    game = ForeignKey(Game, on_delete=models.CASCADE)
    achievement = ForeignKey(Achievement, on_delete=models.CASCADE)
    points = models.IntegerField(blank=True, default=0)
    author = ForeignKey(User, on_delete=models.CASCADE)


class PlayerRole(UUIDModel, models.Model):
    name = models.CharField(max_length=150, default="")


class GamePlayer(TimeStampedModel, UUIDModel, models.Model):
    game = ForeignKey(Game, on_delete=models.CASCADE)
    player = ForeignKey(User, on_delete=models.CASCADE)
    player_role = ForeignKey(PlayerRole, on_delete=models.CASCADE)


class PlayerAchievement(TimeStampedModel, UUIDModel, models.Model):
    player = ForeignKey(User, on_delete=models.CASCADE)
    game_achievement = ForeignKey(GameAchievement, on_delete=models.CASCADE)
