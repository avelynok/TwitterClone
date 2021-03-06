from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    displayname = models.CharField(max_length=50, unique=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True)
    
    def __str__(self):
        return self.username
