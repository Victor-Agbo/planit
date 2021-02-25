from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class planit(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=100)

class User(models.Model):
    class planit(models.Model):
        added_date = models.DateTimeField()
        text = models.CharField(max_length=100)
