from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from auth_user.models import AuthUser


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    telegram_id = serializers.CharField()
    username_field = 'telegram_id'

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['telegram_id'] = user.telegram_id
        token['password'] = user.password

        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = (
            'id', 'telegram_id', 'username',
            'first_name', 'last_name',
            'date_joined',
        )


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = (
            'id', 'telegram_id', 'username',
            'first_name', 'last_name', 'password',
            'date_joined',
        )

    def create(self, validated_data):
        validated_data['is_active'] = True
        return AuthUser.objects.create_user(**validated_data)