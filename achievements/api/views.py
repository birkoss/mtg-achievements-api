from django.core.exceptions import ValidationError

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Playgroup, PlayerRole, PlaygroupPlayer

from .serializers import PlaygroupPlayerSerializer


class playgroup_players(APIView):
    # Add a new User (or an existing User) in the current playgroup
    def post(self, request, playgroup_id, format=None):
        playgroup = fetch_playgroup(
            id=playgroup_id,
            playgroupplayer__player=request.user,
        )
        if playgroup is None:
            return create_error_response('invalid_playgroup')

        # Validate the role

        # Validate the email

        # If User doesn't exists, create user with email

        # Check if user not already in playgroup before adding

        # Add user in playgroup

        # If user is NOT validated, auto validate it's entrie in the playgroup

        return Response({
            'playgroupId': playgroup.id,
            'playerId': 'XXXXXXXXX',
        }, status=status.HTTP_200_OK)

    def get(self, request, playgroup_id, format=None):
        playgroup = fetch_playgroup(
            id=playgroup_id,
            playgroupplayer__player=request.user,
        )
        if playgroup is None:
            return create_error_response('invalid_playgroup')

        players = PlaygroupPlayer.objects.filter(playgroup=playgroup)
        serializer = PlaygroupPlayerSerializer(instance=players, many=True)

        return Response({
            'playgroupId': playgroup.id,
            'players': serializer.data,
        }, status=status.HTTP_200_OK)


def fetch_playgroup(**kwargs):
    try:
        return Playgroup.objects.filter(**kwargs).first()
    except ValidationError:
        pass

    return None


def create_error_response(error):
    return Response({
        'message': error,
    }, status=status.HTTP_400_BAD_REQUEST)
