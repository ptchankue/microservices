# Todo Service API

[Creating a task](#new)

[Listing tasks](#list)

[Viewing a task](#view)

[Updating a task](#update)

[Deleting a task](#delete)

<a id="new"></a>
### Creating a task

the **description** field is required

* Request

		POST /api/v1/todos/
		
* Content-Type

		application/json
		
* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS
		Authorization: client token

* Request Body

		{
  			"description":"Cleaning the carpet"
		}

	

* Response Code

		201 CREATED

* Response Body

		{
    		"id": 7,
    		"author": "test",
    		"description": "Cleaning the carpet",
    		"due_at": "2016-02-16T21:22:58.679948Z",
    		"created_at": "2016-02-17T21:22:58.751899Z",
    		"completed": false
		}

<a id="list"></a>
### Listing tasks

username and password are required

* Request

		GET /api/v1/todos/
		
* Content-Type

		application/json
		
* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS
		Authorization: client token

* Request Body

		None

	

* Response Code

		200 OK

* Response Body

		[
    		{
        		"id": 5,
        		"author": "test",
        		"description": "Going to the farm",
        		"due_at": "2016-02-15T19:36:30.730406Z",
        		"created_at": "2016-02-16T19:36:30.761263Z",
        		"completed": false
    		},
    		{
        		"id": 6,
        		"author": "test",
        		"description": "Laver la voiture v2",
        		"due_at": "2016-02-15T20:15:04.152730Z",
        		"created_at": "2016-02-16T20:15:04.153900Z",
        		"completed": false
    		},
    		{
        		"id": 7,
        		"author": "test",
        		"description": "Cleaning the carpet",
        		"due_at": "2016-02-16T21:22:58.679948Z",
        		"created_at": "2016-02-17T21:22:58.751899Z",
        		"completed": false
    		}
		]

<a id="view"></a>
### Viewing a task


* Request

		GET /api/v1/todos/{task_id}/
		
* Content-Type

		application/json
		
* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS
		Authorization: client token

* Request Body

		None

	

* Response Code

		200 OK

* Response Body

		{
    		"id": 7,
    		"author": "test",
    		"description": "Cleaning the carpet",
    		"due_at": "2016-02-16T21:22:58.679948Z",
    		"created_at": "2016-02-17T21:22:58.751899Z",
    		"completed": false
		}

<a id="update"></a>
### Updating a task


* Request

		PUT /api/v1/todos/{task_id}/
		
* Content-Type

		application/json
		
* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS
		Authorization: client token

* Request Body

		{
  			"completed":true
		}

	

* Response Code

		202 ACCEPTED

* Response Body

		{
    		"id": 7,
    		"author": "test",
    		"description": "Cleaning the carpet",
    		"due_at": "2016-02-16T21:22:58.679948Z",
    		"created_at": "2016-02-17T21:22:58.751899Z",
    		"completed": true
		}
<a id="delete"></a>
### Deleting a task


* Request

		DELETE /api/v1/todos/{task_id}/
		
* Content-Type

		application/json
		
* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS
		Authorization: client token

* Request Body

		None

* Response Code

		204 NO CONTENT

* Response Body

		None