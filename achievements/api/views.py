from django.core.exceptions import ValidationError

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Playgroup, PlayerRole, PlaygroupPlayer

from .serializers import PlaygroupPlayerSerializer


class playgroup_players(APIView):
    def get(self, request, playgroup_id, format=None):
        try:
            playgroup = Playgroup.objects.filter(
                id=playgroup_id,
                playgroupplayer__player=request.user,
            ).first()
        except ValidationError:
            return Response({
                'error': 'validation_error',
            }, status=status.HTTP_400_BAD_REQUEST)

        if playgroup is None:
            return Response({
                'error': 'no_playgroup',
            }, status=status.HTTP_400_BAD_REQUEST)

        players = PlaygroupPlayer.objects.filter(playgroup=playgroup)
        serializer = PlaygroupPlayerSerializer(instance=players, many=True)

        return Response({
            'playgroupId': playgroup.id,
            'players': serializer.data,
        }, status=status.HTTP_200_OK)
