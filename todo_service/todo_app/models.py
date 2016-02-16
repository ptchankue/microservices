"""
    Defining models: Todo
"""
from django.db import models

# Create your models here.

class Todo(models.Model):
    # username of the author of the Todo's task
    author = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_at = models.DateTimeField()
    completed = models.BooleanField(default=False)
