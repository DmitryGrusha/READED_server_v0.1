from rest_framework import serializers
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'country_code', 'phone_number', 'password']


class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
