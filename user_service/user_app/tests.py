"""
    Tests for the user service

"""
from django.test import TestCase
import mock

from user_app.views import (
    get_auth_token, create_auth_token,
    create_user,
)

# Create your tests here.


class TokenTest(TestCase):
    """>>> Test case related to tokens"""

    def test_generate_token(self):
        """>>>Testing create_auth_token and get_auth_token"""
        util = UserUtil()
        user = util.test_create_user()
        # creating a token for the new user
        token1 = create_auth_token(user)
        # getting the token of the same user
        token2 = get_auth_token(user)

        # the 2 tokens should be equql
        self.assertEqual(token1, token2)

    def test_get_token(self):
        """>>> Test for retrieving a token """
        pass

class LoginTest(TestCase):
    """Test case for login in"""

    def setUp(self):
        self.util = UserUtil()

    def test_login(self):
        """should pass"""

        user = self.util.test_create_user()

        payload = {
            "username": "test",
            "password": "test"
        }
        url = "/api/v1/login/"
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 200)

    def test_login_fail(self):
        """should fail"""
        payload = {
            "username": "test",
            "password": "test@@"
        }
        url = "/api/v1/login/"
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 404)

class SignupTest(TestCase):
    """Test case for signing up"""
    def test_signup(self):
        """>>> Testing sign up"""
        payload = {
            "username": "alphabet",
            "password": "test@@"
        }
        url = "/api/v1/signup/"
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 201)

class UserUtil(object):
    """
        Util class used to create users for testing
    """
    def __init__(self, **attrs):
        self.payload = {}

    def test_create_user(self):
        """>>>Testing user creation"""
        self.payload["username"] = "test"
        self.payload["password"] = "test"
        try:
            user = create_user(self.payload)
        except Exception, exp:
            print exp
            user = None
        return user
