from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator

from api_yamdb.settings import (MESSAGE_FOR_RESERVED_NAME,
                                MESSAGE_FOR_USER_NOT_FOUND,
                                RESERVED_NAME)
from users.models import User


class ForUserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователей со статусом user.
    Зарезервированное имя "me" использовать нельзя"""
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )
        read_only_fields = ('role', )

    def validate_username(self, value):
        if value == RESERVED_NAME:
            raise serializers.ValidationError(MESSAGE_FOR_RESERVED_NAME)
        return value


class ForAdminSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователей со статусом admin.
    Зарезервированное имя "me" использовать нельзя"""
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role')

    def validate_username(self, value):
        if value == RESERVED_NAME:
            raise serializers.ValidationError(MESSAGE_FOR_RESERVED_NAME)
        return value


class TokenSerializer(serializers.Serializer):
    """Получение токена.
    Зарезервированное имя "me" использовать нельзя."""
    username = serializers.CharField(max_length=200, required=True)
    confirmation_code = serializers.CharField(max_length=200, required=False)

    def validate_username(self, value):
        if value == RESERVED_NAME:
            raise serializers.ValidationError(MESSAGE_FOR_RESERVED_NAME)
        if not User.objects.filter(username=value).exists():
            raise exceptions.NotFound(MESSAGE_FOR_USER_NOT_FOUND)
        return value