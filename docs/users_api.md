# Users API

### Signing up



* Request

		POST /api/v1/posts/
		
* Content-Type

		application/json
		
* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS

* Request Body

		{
			"author": "test_user",
			"target_id": "f5ca33a1-2193-11e5-b0fa-685b35b7fe48",
			"target_type": "group", 
			"body": "Je ne sais pas ce qui ne va pas " 
		}

ALLOWED_CONTAINER_TYPES     = ['person', 'group', 'page']

In the case of posting to someone wall, the target type will be *person* and the target id will be the *username* of the person
	

* Response Code

		201 CREATED

* Response Body

		{
    		"id": "ed928368-47fb-11e5-ae48-9acf71d9784e",
    		"author": "test_user",
    		"created_at": "2015-08-21T13:58:25.281965",
    		"updated_at": "2015-08-21T13:58:25.281992",
    		"view_count": 0,
    		"like_count": 0,
    		"comment_count": 0,
    		"target_id": "f5ca33a1-2193-11e5-b0fa-685b35b7fe48",
    		"target_type": "group",
    		"body": "Je ne sais pas ce qui ne va pas",
    		"location": null,
    		"at_mention": [],
    		"link": null,
    		"tags": [],
    		"photo": {
        		"url_thumbnail": null,
        		"url_original": null
    		},
    		"image_url": null,
    		"actions": {
        		"comment": "/api/v1/comments/ed928368-47fb-11e5-ae48-9acf71d9784e/",
        		"like": "/api/v1/likes/ed928368-47fb-11e5-ae48-9acf71d9784e/"
    		}
		} 
