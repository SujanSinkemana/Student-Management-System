from django.db import models
from django.forms import CharField, EmailField
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password =models.CharField(max_length=9)