"""Models for Contact app"""


from django.db import models
from django.urls import reverse


# Create your models here.


class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, default=None)
    email = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contacts:index')


class Product(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=255)
    ordered_by = models.ForeignKey(Contact, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
