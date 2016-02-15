from django.shortcuts import render, HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import IntegrityError

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



class SignUpViewSet(viewsets.ModelViewSet):
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

            user = create_user(myuser)

            serializer = UserSerializer(user)
            return Response(serializer.data, status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class LoginViewSet(viewsets.ModelViewSet):
    """ API endpoint for login in """
    serializer_class = LoginSerializer
    def create(self, request):
        logger.debug("Signing in a user")
        print ">>> User",request.user
        print ">>> Token",request.auth

        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.data["username"],
                password=serializer.data["password"])
            if user:
                if user.is_active:
                    # Preparing customised response
                    response = {}
                    response["username"] = user.username
                    response["first_name"] = user.first_name
                    response["last_name"] = user.last_name
                    response["email"] = user.email

                    token = get_auth_token(user)
                    if token == None:
                        token = create_auth_token(user)
                    response["token"] = token

                    return Response(response, status.HTTP_200_OK)
                else:
                    return Response("User is authenticated and not is active", status.HTTP_200_OK)
            else:
                msg = {
                    "error": 404,
                    "message": "Username and Password do not match"
                }
                return Response(msg, status.HTTP_404_NOT_FOUND)

        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

# creating token after login
def create_auth_token(user):
    print ">>> creating a token"
    token = get_auth_token(user)
    if token==None:
        print ">>> actual token creation"
        token = Token.objects.create(user=user)
    return token.key

# getting token
def get_auth_token(user):
    print ">>> getting a token for", user
    try:
        token = Token.objects.get(user_id=user.id)
        if token:
            return token.key
        else:
            return None
    except Exception, e:
        return None

def create_user(payload):
    """
        Create a user
        Input: a dictionary containing the user data
         the keys are (username, password, email, first_name, last_name)
    """
    print ">>> creating a user"
    try:
        user = User.objects.create_user(**payload)
    except IntegrityError, e:
        user= User.objects.get(username=payload["username"])
    return user
