"""
    Serializers to manage user inputs
"""
from rest_framework import serializers
from todo_app.models import Todo

class TodoSerializer(serializers.Serializer):
    """Defining TodoSerializer"""
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    description = serializers.CharField(min_length=5)
    due_at = serializers.DateTimeField(allow_null=True, required=False)
    created_at = serializers.DateTimeField(read_only=True)
    completed = serializers.BooleanField(required=False)

class TodoUpdateSerializer(serializers.Serializer):
    """Defining TodoUpdateSerializer"""
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(min_length=5)
    due_at = serializers.DateTimeField(allow_null=True, required=False)
    completed = serializers.BooleanField(required=False)
