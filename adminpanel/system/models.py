from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Clients(AbstractUser):
    username=models.CharField(max_length=255, blank=False, null=False,unique=True)
    password=models.CharField(max_length=255, blank=False, null=False)
    Age=models.IntegerField(null=True)
    
    def __str__(self):
        return self.username
    