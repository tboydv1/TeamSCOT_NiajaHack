from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.
# Here, we created a model class with its attributes
class HouseOwner(models.Model):

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.title








