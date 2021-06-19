from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class planit(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=100)

class planner(models.Model):
    inf = 10**10000
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    data = models.CharField(max_length=inf, blank=True)
    time = models.CharField(max_length=inf, blank=True)

    class Meta:
        verbose_name_plural = 'PLANNERS'
    
    def __str__(self):
        return '{}'.format(self.account)

'''    
class planit(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=100)

class User(models.Model):
    class planit(models.Model):
        added_date = models.DateTimeField()
        text = models.CharField(max_length=100)'''
