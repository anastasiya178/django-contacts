1. Download the project from github:
 https://github.com/anastasiya178/django-contacts.git

2. Add a database
 - create a new schema
 - create a user
 - make sure the user and the db match Database connection strings in settings.py

3. Create and activate Python virtualenv, for ex.:
source /venv/bin/activate

4. Install all the dependencies
pip install -r requirements.txt

5. Apply all required django migrations:

         cd django
         python manage.py makemigrations
         python manage.py migrate
         python manage.py createsuperuser

6. Load initial data using fixtures:

        python manage.py loaddata contacts/fixtures/contacts.json
        python manage.py loaddata contacts/fixtures/groups.json
        python manage.py loaddata contacts/fixtures/users.json

7. Role management is handled the following way:
    - group Admin (can view, create, delete Contact model)
    - group Editor (can view, delete Contact model)
    - group Viewer (can view Contact model)

    One of these groups needs to be assigned to a user in order to meet the project requirements:
    •	Enforces that actions can only be performed by authenticated users with a certain roles:
        o	One role that has read-only access (Viewer group permissions)
        o	Another role that can read/add (Editor group permissions)
        o	Another role that can read/add/delete (Admin group permissions, superuser permissions)


8. Run tests:

        python manage.py test
