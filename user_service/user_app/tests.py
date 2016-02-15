from django.test import TestCase

from user_app.views import (
    get_auth_token, create_auth_token,
    create_user,
)
import mock

# Create your tests here.


class TokenTest(TestCase):

    def test_generate_token(self):
        """>>>Testing create_auth_token and get_auth_token"""
        util = UserUtil()
        user = util.test_create_user()
        # creating a token for the new user
        t1 = create_auth_token(user)
        # getting the token of the same user
        t2 = get_auth_token(user)

        # the 2 tokens should be equql
        self.assertEqual(t1, t2)

    def test_get_token(self):
        pass

class LoginTest(TestCase):
    pass

class SignupTest(TestCase):
    pass

class UserUtil(object):

    def __init__(self, **attrs):
        self.payload = {}
    def test_create_user(self):
        self.payload["username"] = "test"
        self.payload["password"] = "test"
        try:
            user = create_user(self.payload)
        except Exception, e:
            print e
            user = None
            pass
        return user
