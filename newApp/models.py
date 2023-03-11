from django.db import models

# Create your models here.
class Users(models.Model):
    userId = models.CharField(max_length=100)
    userName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    gender = models.CharField(max_length=100)
