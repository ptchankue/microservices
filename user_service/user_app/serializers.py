from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    """
        Defining the User serializer for User creation and manipulation
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')

class UserUpdateSerializer(serializers.Serializer):
    """
        Defining the User serializer for User creation and manipulation
    """
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

class LoginSerializer(serializers.Serializer):
    """
        Defining the Login serializer for user input
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
