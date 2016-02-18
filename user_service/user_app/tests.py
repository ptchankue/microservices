"""
    Tests for the user service

"""
import json

from django.test import TestCase

from user_app.views import (
    get_auth_token, create_auth_token,
    create_user, get_user_by_token
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
    def setUp(self):
        """Setting up the SignupTest"""
        self.client.defaults['HTTP_AUTHORIZATION'] = "f2823f78920bd288b9f84ebb4cf6a90d702335c2"

        payload = {
            "username": "albert",
            "password": "albertsecret"
        }
        url = "/api/v1/signup/"
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 201)
        self.resp = json.loads(response.content)

    def test_signup(self):
        """>>> Testing sign up"""
        payload = {
            "username": "alphabet",
            "password": "test@@"
        }
        url = "/api/v1/signup/"
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 201)

    def test_update_user(self):
        """Updating some user information"""

        payload = {
            "first_name": "alphabet",
        }
        url = "/api/v1/users/" +str(self.resp["id"])+"/"
        response = self.client.put(url, json.dumps(payload), content_type="application/json")
        self.assertEqual(response.status_code, 202)


class VerifyTest(TestCase):
    """Test case for verify in"""

    def setUp(self):
        """Setting up VerifyTest """
        self.token = "f2823f78920bd288b9f84ebb4cf6a90d702335c2"

    def test_verify(self):
        """verify a token with UserService"""
        payload = {
            "token": self.token
        }
        url = "/api/v1/verify/"
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 404)

class UserUtil(object):
    """
        Util class used to create users for testing
    """
    def __init__(self, **attrs):
        self.payload = {}
        self.token = "f2823f78920bd288b9f84ebb4cf6a90d702335c2"

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
    def test_get_user_by_token(self):
        """Test the function get_user_by_token"""
        user_id = get_user_by_token(self.token)

        self.assertEqual(user_id, 3)

    def test_home(self):
        """testing home landing page"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
