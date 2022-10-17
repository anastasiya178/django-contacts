"""Models for Contact app"""


from django.db import models
from django.urls import reverse


# Create your models here.


class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    email = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.first_name, self.last_name

    def get_absolute_url(self):
        return reverse('contacts:index')
