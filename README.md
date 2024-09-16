# Contacts Django

Table of Contents:
- Description
- Installation Guide
- Linters
- How to login to Docker web container shell


## Description
This project helps to explore various features of Django, DRF, Docker and other tools. 
I gradually add more features based on my current interest and time availability.

Initial idea: Using the app you can add and remove the contacts using the UI, as well the API and the Django 
admin.

Below you can find the tools used and main features within it. 

Django:
- roles and users
- admin customization
- templates

Docker:
- containerize the app
- use Postgres image to run Postgres using docker-compose instead of local installation
- use docker-compose for web and DB containers

Django REST Framework (DRF):
- create CRUD endpoints

## Installation guide

1. Clone the project from github:
 https://github.com/anastasiya178/django-contacts.git

2. Create a .env file (TBD)

3. Build docker compose by executing this command: 

``` 
~ django-contacts % docker-compose build
```

4. Run docker-compose by executing this command:

```
~ django-contacts % docker-compose up
```

If the services are up and running, you would see the following 
message in the terminal: 

```
Django version 4.1.2, using settings 'contacts_project.settings
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```


5. Follow http://0.0.0.0:8000/

6. If you can see the table with contacts - the app is successfully installed!
<img width="1331" alt="image" src="https://github.com/user-attachments/assets/5daafb14-0ba8-4b7f-8212-ba6adc919c85">


7. In order to use edit mode, you would need to create a superuser: 

```
~ django-contacts % docker-compose run web /bin/bash
```

In the opened shell execute the following command:

```
root@9dbfa2f99657:/django-contacts#  python manage.py createsuperuser
```
Insert username, email (optional), password of your choice:

Now you can login to the Django admin: http://0.0.0.0:8000/admin/
and be able to edit the contacts or create additional users (see #* for Role 
management).

8. Role management is handled the following way:
    - group Admin (can view, create, delete Contact model)
    - group Editor (can view, delete Contact model)
    - group Viewer (can view Contact model)

One of these groups needs to be assigned to a newly created user.

9. Run tests:
- login to Docker web container shell

```
~ django-contacts % docker-compose run web /bin/bash
```

```
~ django-contacts % python manage.py test
```

## Linters used: 
See the list of linters used on the project:

1. [Pylint](https://docs.pylint.org/) is a tool that checks for errors in Python code, tries to enforce a coding standard 
and looks for bad code smells. 

2. [flake8](https://flake8.pycqa.org/) is a tool for style guide enforcement.

### How to login to Docker web container shell

`~ django-contacts % docker-compose run web /bin/bash`

May be useful for: 
- running tests
- creating superuser
- doing other things using `python manage.py`


Helpful links: 

https://stackoverflow.com/questions/58547120/django-db-utils-operationalerror-2002-cant-connect-to-mysql-server-on-db

