FROM python:3.8-alpine

MAINTAINER Robley Gori <ro6ley.github.io>

EXPOSE 8000

ADD . /django-contacts

WORKDIR /django-contacts

RUN apk add --no-cache gcc python3-dev musl-dev

RUN apk add --no-cache musl-dev gcc libffi-dev g++

RUN apk add --no-cache mariadb-dev build-base

RUN pip install -r requirements.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD [ "python", "django-contacts/manage.py", "runserver", "0.0.0.0:8000" ]