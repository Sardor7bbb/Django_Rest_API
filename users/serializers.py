from rest_framework import serializers

from authors.models import AuthorModel
from books.models import BookModel
from users.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
