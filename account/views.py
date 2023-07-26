from django.shortcuts import render
from rest_framework import generics, serializers, status, permissions
from rest_framework.response import Response
from .serializer import RegisterSerializer, LoginSerializer
from .models import Account


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'data': 'Account successfully created'}, status=status.HTTP_201_CREATED)


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'tokens': serializer.data['tokens']}, status=status.HTTP_200_OK)

