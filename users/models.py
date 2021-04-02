from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

from core.models import TimeStampedModel, UUIDModel
from achievements.models import PlayerRole, Playgroup, PlaygroupPlayer

from .managers import UserManager


class User(PermissionsMixin, UUIDModel, TimeStampedModel, AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    name = models.CharField(max_length=100, default='', blank=True)

    date_validated = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    def createDefaultPlaygroup(self):
        # Get the ADMIN player role
        player_role = PlayerRole.objects.filter(name='admin').first()

        # Create a default playgroup for this player
        playgroup = Playgroup(
            name=self.email + "'s playgroup",
            author=self,
        )
        playgroup.save()

        playgroup_player = PlaygroupPlayer(
            player=self,
            player_role=player_role,
            playgroup=playgroup,
        )
        playgroup_player.save()

        return playgroup


# Create an API token when an user is created
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
