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
        except Exception as  exp:
            print( exp)
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
