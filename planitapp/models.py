from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class planner(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    data = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'PLANNERS'
    
    def __str__(self):
        return '{}'.format(self.account)
