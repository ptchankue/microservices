"""
    auth.py defining the custom Middleware to handle the permissions
"""
import json
import requests

from django.conf import settings
from django.http import HttpResponse

class CustomAuthMiddleware(object):
    """Middleware that handles the permissions"""
    def process_request(self, request):
        """Processing the incoming request"""

        if "HTTP_AUTHORIZATION" in request.META and request.META["HTTP_AUTHORIZATION"]:
            self.token = request.META['HTTP_AUTHORIZATION']
        else:
            response_data = {
                'error': 401,
                'errorMessage': 'A token should be provided to this request',
            }
            return HttpResponse(json.dumps(response_data),
                                content_type="application/json", status=401)

        code = self.verify_token()
        if code == 0:

            request.current_user = self.user
            request.auth = self.user["token"]
            request.user = self.user["username"]
            return None
        else:
            response_data = {
                'error': 401,
                'errorMessage': 'The token provided is invalid',
            }
            return HttpResponse(json.dumps(response_data),
                                content_type="application/json", status=401)


    def verify_token(self):
        """Verify the token with the user service"""
        url = settings.USER_URL + '/verify/'
    	headers = {
		              "Content-Type": "application/json",
		              "Authorization": "f2823f78920bd288b9f84ebb4cf6a90d702335c2"
	          }

        payload = {
            "token": self.token
            }
        response = None

        print url, "\n", headers
        print "payload\n", payload
        response = requests.post(url, data=json.dumps(payload), headers=headers)

        if response.status_code == 200:
            code = 0
            self.user = json.loads(response.content)

        else:
            code = 1

        return code
