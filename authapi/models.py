from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    uid=models.CharField(max_length=1000,primary_key=True)
    photourl=models.ImageField(null=True,blank=True,upload_to="profile",default="/media/profile/blog9.jpg")
    cover_photo=models.ImageField(upload_to="coverphotos",null=True,blank=True)
    about=models.TextField(null=True,blank=True)
    facebook_id=models.CharField(max_length=1000,null=True,blank=True)
    twitter_id=models.CharField(max_length=1000,null=True,blank=True)
    instagram_id=models.CharField(max_length=1000,null=True,blank=True)
    followers=models.ManyToManyField('self',related_name="followers")
