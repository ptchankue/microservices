"""
    Implementing the views for the user service
    - login
    - signup
    - verify/validate token

"""
import logging

from django.shortcuts import render, HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import IntegrityError

from rest_framework import (
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

logger = logging.getLogger(__name__)

def home(request):
    """
        Home page to reach this service
    """

    msg = "You landed safely on the UserService API:\n"%request.META
    return HttpResponse(msg)



class SignUpViewSet(viewsets.ModelViewSet):
    """Signing up a user"""
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request):
        logger.debug("Creating a new user")

        serializer = UserSerializer(data=request.data)

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
        print ">>> User", request.user
        print ">>> Token", request.auth

        serializer = LoginSerializer(data=request.data)
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
                    if token is None:
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

def create_auth_token(user):
    """
        Creating a token
        Arg: user, an instance of User
        Result: a token
    """
    print ">>> creating a token"
    token = get_auth_token(user)
    if token is None:
        print ">>> actual token creation"
        token = Token.objects.create(user=user)
    return token.key

class VerifyViewSet(viewsets.ModelViewSet):
    """ API endpoint to verify a user token """
    serializer_class = UserSerializer

    def create(self, request):
        print request.data
        if "token" in request.data and request.data["token"]:

            token = get_user_by_token(request.data["token"])

            if token:
                #User.objects.get(id=3)
                print "the user id", token
                user = User.objects.get(id=token).__dict__
                response = {
                    "username": user["username"],
                    "firstname": user["first_name"],
                    "lastname": user["last_name"],
                    "email": user["email"],
                    "token": request.data["token"],
                }
                return Response(response)
            else:
                msg = {
                    "error": 404,
                    "message": "token %s was not found"%(request.data["token"])
                }
                return Response(msg, status=status.HTTP_404_NOT_FOUND)

        else:
            msg = {
                "error": 400,
                "message": "<token> needs to be provided"
            }
            return Response(msg, status.HTTP_400_BAD_REQUEST)

def get_auth_token(user):
    """
        Getting an authentification token
        Args: an instance of User
        Result: a token (string)
    """
    print ">>> getting a token for", user
    try:
        token = Token.objects.get(user_id=user.id)
        if token:
            return token.key
        else:
            return None
    except Exception, exp:
        logger.log(exp)
        return None

def create_user(payload):
    """
        Creating a user
        Args: a dictionary containing the user data
            the keys are (username, password, email, first_name, last_name)
        Result: an instance of the newly created user
    """
    print ">>> creating a user"
    try:
        user = User.objects.create_user(**payload)
    except IntegrityError, exp:
        print exp
        user = User.objects.get(username=payload["username"])
    return user

def get_user_by_token(token):
    """
        Getting a user id from User knowing its token
        Arg: token
        Result: user id (django.contrib.auth.models.User)
    """
    try:
        i = Token.objects.get(key=token).user_id
    except Exception, exp:
        print exp
        i = None
    return i
