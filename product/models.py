from django.db import models

# Create your models here.

class Product (models.Model):
    pid = models.CharField(max_length=10, primary_key=True)
    pname = models.CharField(max_length=100)
    pdesc = models.TextField(max_length=1000)
    price = models.BigIntegerField()
    brand=models.CharField(max_length=50,default="M")
