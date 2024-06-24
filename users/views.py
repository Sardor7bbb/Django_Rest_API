from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import UserModel
from users.serializers import UserSerializer


class UserListAPIView(APIView):
    def get(self, request):
        user = UserModel.objects.all()
        serializer = UserSerializer(user, many=True)
        response = {
            'success': True,
            'total': user.count(),
            'author': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)


class UserDetailAPIView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(UserModel, pk=pk)
        serializer = UserSerializer(user)
        response = {
            'success': True,
            'user': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)


class UserUpdateAPIView(APIView):
    def put(self, request, pk):
        user = get_object_or_404(UserModel, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'message': 'Book update',
                'user': serializer.data
            }
            return Response(response, status=status.HTTP_202_ACCEPTED)
        else:
            response = {
                'success': False,
                'message': 'Invalid request',
                'user': serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UserCreateAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'message': 'Book is created',
                'user': serializer.data
            }
            return Response(response)
        else:
            response = {
                'success': False,
                'message': 'Invalid request',
                'user': serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteAPIView(APIView):
    def delete(self, request, pk):
        user = get_object_or_404(UserModel, pk=pk)
        user.delete()
        response = {
            'success': True,
            'message': 'Book is deleted'
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
