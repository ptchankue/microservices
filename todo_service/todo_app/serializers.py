from rest_framework import serializers
from todo_app.models import Todo

class TodoSerializer1(serializers.ModelSerializer):

    class Meta:
        model = Todo

class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    description = serializers.CharField(min_length=5)
    due_at = serializers.DateTimeField(allow_null=True, required=False)
    completed = serializers.BooleanField(required=False)
