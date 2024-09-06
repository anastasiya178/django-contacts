"""Models for Contact app"""
from django.db import models
from django.urls import reverse

from datetime import datetime


# Create your models here.
class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    email = models.CharField(max_length=255, default=None)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('contacts:index')


class Pet(models.Model):
    MALE_OR_FEMALE = [
        ("M", "Male"),
        ("F", "Female"),
        ("U", "Unknown"),
    ]

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(choices=MALE_OR_FEMALE, default="Unknown")
    dob = models.DateField()
    color = models.CharField(max_length=255, default=None)
    owner = models.ForeignKey("Contact", on_delete=models.CASCADE)
    animal = models.ForeignKey("Animal", on_delete=models.CASCADE)
    breed = models.ForeignKey("Breed", on_delete=models.CASCADE)

    @property
    def age(self):
        age = datetime.now().date() - self.dob
        return int(age.days / 365.25)

    def __str__(self):
        return f"{self.name}, {self.animal}"


class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Breed(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    animal = models.ForeignKey("Animal", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
