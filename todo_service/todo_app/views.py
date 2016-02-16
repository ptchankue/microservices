"""
    Implementation of all views for CRUD operations: Todo
"""
import logging
import datetime
import json

from django.shortcuts import HttpResponse
from django.conf import settings

from rest_framework import (
    viewsets,
    status,
)
from rest_framework.response import Response


from todo_app.models import Todo

from todo_app.serializers import TodoSerializer, TodoUpdateSerializer

# Create your views here.

logger = logging.getLogger(__name__)

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

        print ">>> User:", request.user
        print ">>> Token:", request.auth, request.current_user
        serializer = TodoSerializer(data=request.data)

        serializer.initial_data["author"] = request.user
        if serializer.is_valid():
            post = Todo()

            post.description = serializer.data["description"]
            post.author = serializer.data["author"]

            if "due_at" in serializer.data and serializer.data["due_at"]:
                _date = datetime.datetime.strptime(str(serializer.data['due_at']),
                    "%Y-%m-%dT%H:%M:%S.%fZ")
                post.due_at = _date
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
        print ">>> User:", request.user
        print ">>> Token:", request.auth

        serializer = TodoUpdateSerializer(data=request.data)
        if serializer.is_valid():

            post = Todo.objects.get(id=pk)

            if post:

                if "due_at" in serializer.data and serializer.data["due_at"]:
                    _date = datetime.datetime.strptime(str(serializer.data['due_at']),
                        "%Y-%m-%dT%H:%M:%S.%fZ")
                    post.due_at = _date

                if "description" in serializer.data and serializer.data["description"]:
                    post.description = serializer.data["description"]

                if "completed" in serializer.data and serializer.data["completed"]:
                    post.completed = serializer.data["completed"]

                post.save()


                print post.due_at, type(post.due_at), post.created_at




                serializer = TodoSerializer(post)

                print '\nPUT ===>' + str(serializer.data)

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
        print ">>> User", request.user
        print ">>> Token", request.auth

        author = request.current_user["username"]
        print "current user:", author
        post = Todo.objects.get(id=pk)

        if post:

            if author==post.author:
                serializer = TodoSerializer(post)
                return Response(serializer.data)
            else:
                # Throw an error if the user doesn't have permission to view this content
                msg = {
                    "error": 403,
                    "message": "You are not permitted to view this content"
                }
                return Response(msg, status=403)
        else:
            msg = {
                "error": 404,
                "message": "Todo task could not be found"
            }
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        """Deleting a task"""
        print ">>> User", request.user
        print ">>> Token", request.auth

        post = Todo.objects.get(id=pk)

        if post:
            post.delete()
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
