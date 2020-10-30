# Chatroom backend

Chatroom-backend is a backend server stack for the chatroom project using Django REST Framework.


## Usage

	cd into root chatroom backend
	$ pip install django
	$ pip install djangorestframework
	$ pip install django-cors-headers
	$ python3 manage.py runserver
	To authenticate, POST to /auth/ then put the token in the header as such {'Authorization': 'Token <token>'}

## Available Command
	
	admin console
		BROWSER	/admin/
	login
		POST	/auth/
	get all posts
		GET	/api/posts/
	create a post
		POST	/api/posts/
	create a comment
		POST	/api/posts/<id>/comment/
	edit a post
		POST	/api/posts/<id>/edit/
	edit a comment
		POST	/api/comments/<id>/edit/


## Credentials

	status | username | password | token
	admin | azurediamond | hunter2 | 311067c9572651952f190bd870aa2bc2cd55864c
	user | testboi | hunter02 | 2ffb59d6778925d6fb55fdae6de88387557c76f8
