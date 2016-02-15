from django.shortcuts import render, HttpResponse

from rest_framework import (
	authentication,
	permissions,
	viewsets,
	status
)
from rest_framework.response import Response


from todo_app.models import Todo

from todo_app.serializers import TodoSerializer
import logging, datetime

# Create your views here.


def home(request):
    msg = "You have landed on the Todo service :)"
    return HttpResponse(msg)

class TodoViewSet(viewsets.ModelViewSet):

    """API endpoing to manage todo lists"""

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def create(self, request):

        print ">>> User", request.user
        print ">>> Token", request.auth
        serializer = TodoSerializer(data = request.data)

        if serializer.is_valid():
            post = Todo()

            post.description = serializer.data["description"]
            post.author = serializer.data["author"]

            if "due_at" in serializer.data and serializer.data["due_at"]:
                post.due_at = serializer.data["due_at"]
            else:
                post.due_at = datetime.datetime.now() + datetime.timedelta(days=1)

            post.save()

            serializer = TodoSerializer(post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            msg = {
                "error": 400,
                "message": serializer.errors
            }
            return Response(msg, status.HTTP_400_BAD_REQUEST)

    def update(self, request):
        pass

    def retrieve(self, request):
        pass

    def destroy(self, request):
        pass
