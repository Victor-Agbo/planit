from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class planner(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    data = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'PLANNERS'
    
    def __str__(self):
<<<<<<< HEAD
        return '{}'.format(self.account)
=======
        return '{}'.format(self.account)
>>>>>>> f7c889b979494f71528ffeedfbab88403f31b838
