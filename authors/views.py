from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from authors.models import AuthorModel
from authors.serializers import AuthorSerializer


class AuthorListAPIView(APIView):
    def get(self, request):
        author = AuthorModel.objects.all()
        serializer = AuthorSerializer(author, many=True)
        response = {
            'success': True,
            'total': author.count(),
            'author': serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)

