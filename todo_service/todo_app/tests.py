"""
    TodoTestCase
"""
import json
from datetime import datetime

from django.test import TestCase

from todo_app.views import (
    convert_time, check_permission,
)
from todo_app.models import Todo

# Create your tests here.

# coverage run todo_service/manage.py test todo_app

class TodoTestCase(TestCase):

    """>>> testing todo app"""
    def setUp(self):
        """>>> Setting up"""

        self.client.defaults['HTTP_AUTHORIZATION'] = "f2823f78920bd288b9f84ebb4cf6a90d702335c2"
        data = {
            "author": "test",
            "description": "Sprint planning meeting",
            "created_at": datetime.now()
        }
        url = "/api/v1/todos/"
        self.response = self.client.post(url, data)
        self.assertEqual(self.response.status_code, 201)

        self.resp = json.loads(self.response.content)

    def test_add(self):
        """>>> Creating a todo task"""
        data = {
            "author": "test",
            "description": "Sprint planning meeting",
            "created_at":datetime.now()
        }
        url = "/api/v1/todos/"
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)


    def test_retrieve(self):
        """>>> Retrieving a todo task"""

        url = "/api/v1/todos/" + str(self.resp["id"]) + "/"
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        resp = json.loads(response.content)

        self.assertEqual(resp["author"], "test")

    def test_edit(self):
        """>>> Editing a todo task"""
        data = {
            "description": "Sprint planning meeting-Updated",
        }
        url = "/api/v1/todos/" + str(self.resp["id"]) + "/"

        response = self.client.put(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 202)

        resp_ = json.loads(response.content)

        self.assertEqual(resp_["description"], "Sprint planning meeting-Updated")

    def test_delete(self):
        """>>> Deleting a todo task"""
        url = "/api/v1/todos/" + str(self.resp["id"]) + "/"

        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)


    def test_listing(self):
        """>>> Listing a todo tasks"""
        url = "/api/v1/todos/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_(self):
        """>>> Retrieving a todo task"""

        resp = json.loads(self.response.content)
        print resp
        url = "/api/v1/todos/" + str(resp["id"]) + "/"
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        resp = json.loads(response.content)

        self.assertEqual(resp["author"], "test")

class TestTodoFail(TestCase):
    """Checking the failed requests"""

    def setUp(self):
        """>>> Setting up"""

        self.client.defaults['HTTP_AUTHORIZATION'] = "==f2823f78920bd288b9f84ebb4cf6a90d702335c2"
        data = {
            "author": "test",
            "description": "Sprint planning meeting",
            "created_at": datetime.now()
        }
        url = "/api/v1/todos/"
        self.response = self.client.post(url, data)
        self.assertEqual(self.response.status_code, 401)

    def test_f_add(self):
        data = {
            "author": "parliement",
            "description": "Sprint planning meeting",
            "created_at": datetime.now()
        }
        url = "/api/v1/todos/"
        self.response = self.client.post(url, data)
        self.assertEqual(self.response.status_code, 401)

class TestHelpers(TestCase):
    """Test of helper functions"""

    def setUp(self):
        """Setting up"""
        self.date = "2016-02-17T21:22:58.751899Z"

        self.post = Todo(author="test-fail", description="description text")

        self.client.defaults['HTTP_AUTHORIZATION'] = "f2823f78920bd288b9f84ebb4cf6a90d702335c2"


    def test_home(self):
        """testing home landing page"""
        response = self.client.get('/')
        print response.__dict__
        self.assertEqual(response.status_code, 200)

    def test_convert_time(self):
        """testing the date conversion"""
        _date = convert_time(self.date)
        self.assertIs(type(_date), datetime)

    def test_permission(self):
        """testing check permission"""

        #_date = check_permission(self.client.request, self.post, "view")
        #self.assertIs(type(_date), datetime)

def create_task():
    """Creating a task"""
    pass
