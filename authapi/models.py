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
    following=models.ManyToManyField('self',related_name="followed_by",symmetrical=False)
    favorites=models.ManyToManyField('api.PostModel',related_name="favorited_by")
    
    def follow(self, profile):
        """Follow `profile` if we're not already following `profile`."""
        return  self.followers.add(profile)

    def unfollow(self, profile):
        """Unfollow `profile` if we're already following `profile`."""
        return self.followers.remove(profile)

    def is_following(self, profile):
        """Returns True if we're following `profile`; False otherwise."""
        return self.following.filter(uid=profile.uid).exists()

    def is_followed_by(self, profile):
        """Returns True if `profile` is following us; False otherwise."""
        return self.followed_by.filter(pk=profile.pk).exists()

    def addfavorite(self, article):
        """Favorite `article` if we haven't already favorited it."""
        return self.favorites.add(article)

    def unfavorite(self, article):
        """Unfavorite `article` if we've already favorited it."""
        return self.favorites.remove(article)

    def has_favorited(self, article):
        """Returns True if we have favorited `article`; else False."""
        return self.favorites.filter(pk=article.pk).exists()