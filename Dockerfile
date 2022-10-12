# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /django-contacts
COPY requirements.txt /django-contacts/
RUN pip install -r requirements.txt
COPY . /django-contacts/
