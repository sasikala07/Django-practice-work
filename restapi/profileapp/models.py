from django.db import models


# Create your models here.

class Profile(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
