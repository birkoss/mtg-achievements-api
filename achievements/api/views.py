from django.core.exceptions import ValidationError
from django.utils import timezone

from rest_framework import status, authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Playgroup, PlayerRole, PlaygroupPlayer
from users.models import User

from .serializers import PlaygroupPlayerSerializer


class playgroup_players(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # Add a new User (or an existing User) in the current playgroup
    def post(self, request, playgroup_id, format=None):
        playgroup = fetch_playgroup(
            id=playgroup_id,
            playgroupplayer__player=request.user,
            playgroupplayer__player_role__name='admin',
        )
        if playgroup is None:
            return create_error_response('invalid_playgroup')

        if 'email' not in request.data or 'role' not in request.data:
            return create_error_response('missing_email_role')

        if not validate_email(request.data['email']):
            return create_error_response('invalid_email')

        role = PlayerRole.objects.filter(name=request.data['role']).first()
        if role is None:
            return create_error_response('invalid_role')

        # Get the user (and create it if needed)
        user = User.objects.filter(email=request.data['email']).first()
        if user is None:
            user = User(
                email=request.data['email'],
                password=User.objects.make_random_password()
            )
            user.save()

        # Confirm it's not already in this playgroup
        playgroup_player = PlaygroupPlayer.objects.filter(
            player=user, playgroup=playgroup
        ).first()
        if playgroup_player is not None:
            return create_error_response('already_in_playgroup')

        # Add user in playgroup
        playgroup_player = PlaygroupPlayer(
            playgroup=playgroup,
            player_role=role,
            player=user,
            # If the user is a valid user (logged in user, must validate the membership)  # nopep8
            date_validated=(timezone.now() if user.date_validated else None)
        )
        playgroup_player.save()

        return Response({
            'playgroupId': playgroup.id,
            'playerId': user.id,
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


class playgroup_player(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, playgroup_id, player_id, format=None):
        playgroup = fetch_playgroup(
            id=playgroup_id,
            playgroupplayer__player=request.user,
            playgroupplayer__player_role__name='admin',
        )
        if playgroup is None:
            return create_error_response('invalid_playgroup')

        # Confirm it's already in this playgroup
        playgroup_player = PlaygroupPlayer.objects.filter(
            player__id=player_id, playgroup=playgroup
        ).first()
        if playgroup_player is None:
            return create_error_response('invalid_player')

        playgroup_player.delete()

        return Response({
            'playgroupId': playgroup.id,
        }, status=status.HTTP_200_OK)

    def patch(self, request, playgroup_id, player_id, format=None):
        playgroup = fetch_playgroup(
            id=playgroup_id,
            playgroupplayer__player=request.user,
            playgroupplayer__player_role__name='admin',
        )
        if playgroup is None:
            return create_error_response('invalid_playgroup')

        if 'role' not in request.data:
            return create_error_response('missing_role')

        role = PlayerRole.objects.filter(name=request.data['role']).first()
        if role is None:
            return create_error_response('invalid_role')

        # Confirm it's already in this playgroup
        playgroup_player = PlaygroupPlayer.objects.filter(
            player__id=player_id, playgroup=playgroup
        ).first()
        if playgroup_player is None:
            return create_error_response('invalid_player')

        playgroup_player.player_role = role
        playgroup_player.save()

        return Response({
            'playgroupId': playgroup.id,
            'playerId': playgroup_player.player.id,
        }, status=status.HTTP_200_OK)


def fetch_playgroup(**kwargs):
    try:
        return Playgroup.objects.filter(**kwargs).first()
    except ValidationError:
        pass

    return None


def create_error_response(error):
    return Response({
        'error': error,
    }, status=status.HTTP_400_BAD_REQUEST)


def validate_email(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
