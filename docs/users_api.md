# User Service API

[Signing up](#signup)

[Login](#login)

[Verify token](#verify)

[Update user information](#update)

<a id="signup"></a>
### Signing up

username and password are required, the other fields are optional

* Request

		POST /api/v1/signup/
		
* Content-Type

		application/json
		
* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS
		Authorization: client token

* Request Body

		{
			"username": "myownuser",
			"password": "secret",
			"first_name": "Marcello",
			"last_name": "Ahmadou", 
			"email": "armagedon@ymail.com" 
		}

	

* Response Code

		201 CREATED

* Response Body

		{
    		"id": 5,
    		"username": "myownuser",
    		"password": "pbkdf2_sha256$12000$DSDq64QEQtMf$Y7MQkGltQrGqv0fYnePOpvAcVs+LZOaGFPEHPs6VjDw=",
    		"email": "armagedon@ymail.com",
    		"first_name": "Marcello",
    		"last_name": "Ahmadou"
		}

<a id="login"></a>
### Login

username and password are required

* Request

		POST /api/v1/login/
		
* Content-Type

		application/json
		
* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS
		Authorization: client token

* Request Body

		{
			"username": "myownuser",
			"password": "secret"
		}

	

* Response Code

		200 OK

* Response Body

		{
    		"username": "myownuser",
    		"first_name": "Marcello",
    		"last_name": "Ahmadou",
    		"email": "armagedon@ymail.com",
    		"token": "8f108966eb547384382452b23651843e22374173"
		}

<a id="verify"></a>
### Verify token


* Request

		POST /api/v1/verify/
		
* Content-Type

		application/json
		
* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS
		Authorization: client token

* Request Body

		{
  			"token":"f2823f78920bd288b9f84ebb4cf6a90d702335c2"
		}

	

* Response Code

		200 OK

* Response Body

		{
    		"username": "test",
    		"lastname": "",
    		"token": "f2823f78920bd288b9f84ebb4cf6a90d702335c2",
    		"email": "",
    		"firstname": ""
		}

<a id="update"></a>
### Update user information


* Request

		PUT /api/v1/users/{user_id}/
		
* Content-Type

		application/json
		
* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS
		Authorization: client token

* Request Body

		{
  			"first_name":"Alexis",
  			"last_name": "Gomez"
		}

	

* Response Code

		202 ACCEPTED

* Response Body

		{
    		"id": 3,
    		"username": "test",
    		"password": "pbkdf2_sha256$12000$12yT9IrcJ01e$PY4zr/PgQYrK8yfb0PjDblqZYiAMPQ6XGYb/Ik9Ls1c=",
    		"email": "",
    		"first_name": "Alexis",
    		"last_name": "Gomez"
		}

