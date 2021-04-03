from rest_framework import serializers

from ..models import Playgroup, PlaygroupPlayer, PlayerRole
from users.models import User


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']


class PlayerRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerRole
        fields = ['name']


class PlaygroupPlayerSerializer(serializers.ModelSerializer):
    player_role = PlayerRoleSerializer(read_only=True)
    player = PlayerSerializer(read_only=True)

    class Meta:
        model = PlaygroupPlayer
        fields = ['player_role', 'player']
