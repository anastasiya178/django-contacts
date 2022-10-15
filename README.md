1. Clone the project from github:
 https://github.com/anastasiya178/django-contacts.git

2. Build docker compose by executing this command: 

`~ django-contacts % docker-compose build
`

3. Run docker-compose by executing this command:

`~ django-contacts % docker-compose up`

If the services are up and running, you would see the following 
message: 

`Django version 4.1.2, using settings 'contacts_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.`

4. Follow http://0.0.0.0:8000/

5. If you can see the table with contacts - the app is successfully installed!

6. In order to use edit mode without any restrictions, you would need to create a superuser: 

`django-contacts % docker-compose run web /bin/bash`

In the opened shell: 

`root@9dbfa2f99657:/django-contacts# 
`

execute the following command:

`python manage.py createsuperuser
`

Insert username, email(optional), password of your choice. 

6. Role management is handled the following way:
    - group Admin (can view, create, delete Contact model)
    - group Editor (can view, delete Contact model)
    - group Viewer (can view Contact model)

One of these groups needs to be assigned to a user in order to meet the following project requirements:
    > Enforces that actions can only be performed by authenticated users with a certain roles:
        o	One role that has read-only access (Viewer group permissions)
        o	Another role that can read/add (Editor group permissions)
        o	Another role that can read/add/delete (Admin group permissions, superuser permissions)

8. Run tests:

`python manage.py test`
