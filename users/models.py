from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=13,default='')
    CHOICES = (
        (1,'admin'),
        (2,'adib'),
        (3,'user'),
    )
    roles = models.PositiveIntegerField(default=1,choices=CHOICES)