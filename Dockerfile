# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /django-contacts
COPY requirements.txt /django-contacts/
RUN pip install -r requirements.txt
COPY . /django-contacts/
RUN python manage.py collectstatic --noinput &&\
    python manage.py migrate &&\
    python manage.py loaddata contacts/fixtures/contacts.json &&\
    python manage.py loaddata contacts/fixtures/auth_groups.json
EXPOSE 8000
# running server
CMD python manage.py runserver 0.0.0.0:8000
