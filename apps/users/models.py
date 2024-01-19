# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    points=models.IntegerField(default=0)
    nickname=models.CharField(max_length=24, null=False, unique=True)

    def __str__(self):
        return self.nickname