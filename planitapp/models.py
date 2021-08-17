from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.


class Planner(models.Model):
    paid = [('NP', 'No Payment'), ('PTCA', 'Paid To Clear Ads'), ('PTGS', 'Paid To Get SMS'), ('FP', 'Full Payment')]
    account = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    paid = models.CharField(choices=paid, max_length=1)
    timezone = models.CharField(max_length=5)
    phone_number = models.CharField(blank=True, max_length=5)

    class Meta:
        verbose_name_plural = 'PLANNERS'
    
    def __str__(self):
        return '{}'.format(self.account)
