from datetime import datetime

from django.contrib.auth import login, authenticate

from rest_framework import status, authentication, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import User

from .serializers import UserSerializer


class loginUser(APIView):
    def post(self, request, format=None):

        print("LOGIN USER")

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
                firstname=serializer.data['firstname'],
                lastname=serializer.data['lastname'],
                is_children=False
            )

            token = Token.objects.get(user=user)

            return Response({
                'status': status.HTTP_200_OK,
                'token': token.key,
            })
        else:
            return Response({
                "status": status.HTTP_404_NOT_FOUND,
                'message': serializer.errors,
            }, status=status.HTTP_404_NOT_FOUND)
