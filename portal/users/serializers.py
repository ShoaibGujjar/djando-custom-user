from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=[
            "name"
        ]


class UserAuthSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=[
            'name',
            'id',
            'email'
        ]

class UserSerializer(serializers.ModelSerializer):
    isAdmin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'lastName', 'email', 'name', 'isAdmin','is_author','sex']


    def get_isAdmin(self, obj):
        return obj.is_staff



class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'isAdmin','is_author', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

    def get_isAdmin(self, obj):
        return obj.is_staff


