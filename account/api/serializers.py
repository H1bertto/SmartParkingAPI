from rest_framework.serializers import ModelSerializer, ReadOnlyField
from account.models import User


class UserSerializer(ModelSerializer):
    full_name = ReadOnlyField()

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'phone']


class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'email', 'password']


class LogoutUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = []
