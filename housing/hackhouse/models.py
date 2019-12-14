from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.
# Here, we created a model class with its attributes
class HouseOwner(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)






