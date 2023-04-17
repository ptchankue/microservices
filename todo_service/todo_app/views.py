"""
    Implementation of all views for CRUD operations: Todo
"""
import logging
import datetime

from django.shortcuts import HttpResponse
from django.conf import settings

from rest_framework import (
    viewsets,
    status,
)
from rest_framework.response import Response

from .models import Todo

from .serializers import TodoSerializer, TodoUpdateSerializer

# Create your views here.

LOGGER = logging.getLogger(__name__)


def home(request):
    """Landing page for testing"""

    msg = "You have landed on the Todo service :)"
    return HttpResponse(msg)


class TodoViewSet(viewsets.ModelViewSet):
    """API endpoing to manage todo lists"""

    serializer_class = TodoSerializer

    def list(self, request):
        """>>>Listing all tasks for the logged user"""
        queryset = Todo.objects.filter(author=request.user)

        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Creating a task for a user"""

        print(">>> User:", request.user)
        print(">>> Token:", request.auth, request.current_user)
        serializer = TodoSerializer(data=request.data)

        serializer.initial_data["author"] = request.user
        if serializer.is_valid():

            post = Todo()

            post.description = serializer.data["description"]
            post.author = serializer.data["author"]

            if "due_at" in serializer.data and serializer.data["due_at"]:
                post.due_at = convert_time(serializer.data["due_at"])

            else:
                today = datetime.datetime.now()
                _date = (today - datetime.timedelta(days=settings.DEFAULT_DAYS))

                post.due_at = _date

            post.save()

            serializer = TodoSerializer(post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            msg = {
                "error": 400,
                "message": serializer.errors
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """Updating a task"""
        print(">>> User:", request.user)
        print(">>> Token:", request.auth)

        serializer = TodoUpdateSerializer(data=request.data)
        if serializer.is_valid():

            post = Todo.objects.get(id=pk)

            if post:

                check_permission(request, post, 'update')

                if "due_at" in serializer.data and serializer.data["due_at"]:
                    post.due_at = convert_time(serializer.data["due_at"])

                if "description" in serializer.data and serializer.data["description"]:
                    post.description = serializer.data["description"]

                if "completed" in serializer.data and serializer.data["completed"]:
                    post.completed = serializer.data["completed"]

                post.save()

                print(post.due_at, type(post.due_at), post.created_at)

                serializer = TodoSerializer(post)

                print('\nPUT ===>' + str(serializer.data))

                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                msg = {
                    "error": 404,
                    "message": "Todo task could not be found"
                }
                return Response(msg, status=status.HTTP_404_NOT_FOUND)

        else:
            msg = {
                "error": 400,
                "message": serializer.errors
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
            Retrieving a task
        """
        print(">>> User", request.user)
        print(">>> Token", request.auth)

        author = request.current_user["username"]
        print("current user:", author)
        post = Todo.objects.get(id=pk)

        if post:

            check_permission(request, post, 'view')

            serializer = TodoSerializer(post)
            return Response(serializer.data)

        else:
            msg = {
                "error": 404,
                "message": "Todo task could not be found"
            }
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        """Deleting a task"""
        print(">>> User", request.user)
        print(">>> Token", request.auth)

        task = Todo.objects.get(id=pk)

        if task:
            check_permission(request, task, 'delete')

            task.delete()
            msg = {
                "error": 204,
                "message": "Task was succesfully deleted"
            }

            return Response(msg, status=status.HTTP_204_NO_CONTENT)
        else:
            msg = {
                "error": 404,
                "message": "Todo task could not be found"
            }
            return Response(msg, status=status.HTTP_404_NOT_FOUND)


def check_permission(request, post, action):
    """
        Checks if the current user has the right to perform an action
        Args: request (request object), post (The instance of the task )
              and action (to be performed: view/delete/update)
        Result: None if everythong is fine, 403 error otherwise
    """
    if post.author != request.user:
        msg = {
            "error": 403,
            "message": "You are not permitted to %s this content" % action
        }
        return Response(msg, status=403)


def convert_time(str_time):
    """
        Convert the date to the correct format
        Args: data (string)
        Return: datetime in the right format
    """
    _date = datetime.datetime.strptime(str(str_time),
                                       "%Y-%m-%dT%H:%M:%S.%fZ")
    return _date
