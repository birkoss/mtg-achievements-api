from django.db import models
from django.db.models.fields.related import ForeignKey

from core.models import TimeStampedModel, UUIDModel


class Achievement(TimeStampedModel, UUIDModel, models.Model):
    name = models.CharField(max_length=150, default="")
    description = models.TextField(blank=True, default="")
    points = models.IntegerField(blank=True, default=0)
    author = ForeignKey(
        "users.User", blank=True, null=True, on_delete=models.CASCADE
    )


class Playgroup(TimeStampedModel, UUIDModel, models.Model):
    name = models.CharField(max_length=150, default="")
    external_url = models.CharField(
        max_length=150, default="", null=True, blank=True
    )
    author = ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PlaygroupAchievement(TimeStampedModel, UUIDModel, models.Model):
    playgroup = ForeignKey(Playgroup, on_delete=models.CASCADE)
    achievement = ForeignKey(Achievement, on_delete=models.CASCADE)
    points = models.IntegerField(blank=True, default=0)
    author = ForeignKey("users.User", on_delete=models.CASCADE)


class PlayerRole(UUIDModel, models.Model):
    name = models.CharField(max_length=150, default="")

    def __str__(self):
        return self.name


class PlaygroupPlayer(TimeStampedModel, UUIDModel, models.Model):
    playgroup = ForeignKey(Playgroup, on_delete=models.CASCADE)
    player = ForeignKey("users.User", on_delete=models.CASCADE)
    player_role = ForeignKey(PlayerRole, on_delete=models.CASCADE)
    date_validated = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return (
                self.player_role.name + " of " + self.playgroup.name
                + " : " + self.player.email
            )


class PlayerAchievement(TimeStampedModel, UUIDModel, models.Model):
    player = ForeignKey("users.User", on_delete=models.CASCADE)
    playgroup_achievement = ForeignKey(
        PlaygroupAchievement, on_delete=models.CASCADE
    )
