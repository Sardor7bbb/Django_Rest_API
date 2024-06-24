from rest_framework import serializers

from authors.models import AuthorModel
from books.models import BookModel


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = '__all__'
