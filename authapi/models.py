from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    uid=models.CharField(max_length=1000,primary_key=True)
    photourl=models.CharField(max_length=1000,default="")
    