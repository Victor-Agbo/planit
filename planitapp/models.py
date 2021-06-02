from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class planner(models.Model):
    person = models.OneToOneField(User, on_delete = models.CASCADE)
    data = models.CharField(maxlength = inf)
    
    class Meta:
        verbose_name_plural = 'PLANNERS'
        
    def __str__(self):
        return '{}'.format(self.person)
'''    
class planit(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=100)

class User(models.Model):
    class planit(models.Model):
        added_date = models.DateTimeField()
        text = models.CharField(max_length=100)'''
