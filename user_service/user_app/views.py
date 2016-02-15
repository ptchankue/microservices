from django.shortcuts import render, HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import (
    authentication,
    permissions,
    viewsets,
    status
)
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from user_app.serializers import (
    UserSerializer,
    LoginSerializer,
)
# Create your views here.
import logging

logger = logging.getLogger(__name__)

def home(request):

    msg="You landed safely on the UserService API"
    return HttpResponse(msg)



class SignUpView(viewsets.ModelViewSet):
    """"""
    serializer_class= UserSerializer
    queryset= User.objects.all()

    def create(self, request):
        logger.debug("Creating a new user")

        serializer = UserSerializer(data = request.data)

        if serializer.is_valid():
            myuser = {}
            myuser["username"] = serializer.data["username"]
            myuser["password"] = serializer.data["password"]
            # optional fields
            if "first_name" in serializer.data and serializer.data["first_name"]:
                myuser["first_name"] = serializer.data["first_name"]
            if "last_name" in serializer.data and serializer.data["last_name"]:
                myuser["last_name"] = serializer.data["last_name"]
            if "email" in serializer.data and serializer.data["email"]:
                myuser["email"] = serializer.data["email"]

            user = User.objects.create_user(**myuser)

            serializer = UserSerializer(user)
            return Response(serializer.data, status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



# creating token after login
def create_auth_token(user):
    Token.objects.create(user=instance)

# getting token
def get_user_token(user):
    return Token.objects.get(user_id=user.id).key
