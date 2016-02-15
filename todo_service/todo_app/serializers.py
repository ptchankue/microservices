from rest_framework import serializers
from todo_app.models import Todo

class TodoSerializer(serializers.ModelSerializer):

    class meta:
        model = Todo
