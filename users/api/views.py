from django.utils import timezone

from django.contrib.auth import login, authenticate

from rest_framework import status, authentication, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from achievements.models import Playgroup

from ..models import User

from .serializers import UserSerializer


class loginUser(APIView):
    def post(self, request, format=None):

        user = authenticate(
            request,
            email=request.data['email'],
            password=request.data['password'])

        if user is None:
            return Response({
                'error': 'invalid_data'
            }, status=status.HTTP_404_NOT_FOUND)

        login(request, user)

        token = Token.objects.get(user=user)

        return Response({
            'token': token.key,
            'userId': user.id,
        }, status=status.HTTP_200_OK)


class registerUser(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = User.objects.create_user(
                serializer.data['email'],
                request.data['password'],
                date_validated=timezone.now(),
            )

            token = Token.objects.get(user=user)

            # Create a default playgroup for this player
            playground = Playgroup(
                name=user.email + "'s playgroup",
                author=user,
            )

            return Response({
                'token': token.key,
                'userId': user.id,
            })
        else:
            error_message = ""
            for error_field in serializer.errors:
                error_message = serializer.errors[error_field][0].code

            return Response({
                'error': error_message,
            }, status=status.HTTP_404_NOT_FOUND)
