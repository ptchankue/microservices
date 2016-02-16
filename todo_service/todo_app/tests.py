"""
    TodoTestCase
"""
import json
from datetime import datetime

from django.test import TestCase

#from todo_app.views import create_task
# Create your tests here.


class TodoTestCase(TestCase):

    """>>> testing todo app"""
    def setUp(self):
        """>>> Setting up"""

        data = {
            "author": "test-user",
            "description": "Sprint planning meeting",
            "created_at":datetime.now()
        }
        url = "/api/v1/todos/"
        self.response = self.client.post(url, data)
        self.assertEqual(self.response.status_code, 201)

    def test_add(self):
        """>>> Creating a todo task"""
        data = {
            "author": "myuser",
            "description": "Sprint planning meeting",
            "created_at":datetime.now()
        }
        url = "/api/v1/todos/"
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_retrieve(self):
        """>>> Retrieving a todo task"""

        resp = json.loads(self.response.content)
        print resp
        url = "/api/v1/todos/" + str(resp["id"]) + "/"
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        resp = json.loads(response.content)

        self.assertEqual(resp["author"], "test-user")

    def test_edit(self):
        """>>> Editing a todo task"""
        pass
    def test_delete(self):
        """>>> Deleting a todo task"""
        pass

    def test_listing(self):
        """>>> Listing a todo tasks"""
        url = "/api/v1/todos/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
