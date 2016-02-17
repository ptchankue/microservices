# Micro services

This open source project 

The two services will not be sharing any data hence have to commnuicate through API endpoints. For example when getting the list of tasks for a user, the **Todo service** can verify the user requesting the information via the **User service**.


[Django Rest Framework] (http://www.django-rest-framework.org/) will intensively be used in this project for :

*	Views implementation (Class Based Views),
*	Authentification: Generating and managing tokens
*	Serializers design

## Table of content

[Architecture](#architecture)

[User Service](#userservice)

[Todo Service](#todoservice)


<a id="architecture"></a>
## Architecture:

![Architecture of teh microservice](docs/microservice_architecture.png)

-> **Fig.1: Architecture of the microservice system** <-

Figure 1 depicts the architecture of the micro service system allowing users to manipulate their todo lists. Users interacts wiuth the syste using any fornt-end application (mobile, desktop). 




<a id="userservice"></a>
## User service:

[Documentation](docs/users_api.md)

The user service allows users to signup (very simple user model) and login to the system. When a user login a token is generated and stored for her/him, that token will then be used by other microservices to identify each user.


<a id="todoservice"></a>
## Todo Service:

[Documentation](docs/todo_api.md)

Steps to set up the project:

Creating the virtual anvironment

		source bin/activitate my_micro_env

Installing the dependencies

		pip install -r requirements.txt

Creating the database

		./manage.py syncdb

