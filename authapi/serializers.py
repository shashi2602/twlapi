from djoser.serializers import UserCreateSerializer,UserSerializer
from rest_framework import serializers
from  .models import *


class usercreateserli(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=User
        fields=('uid','username','email','password')

class userserliz(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['uid','username','email','photourl','is_superuser','last_login','date_joined']
class AboutUserserilz(serializers.ModelSerializer):
        class Meta:
            model=User
            fields=['uid','username','email','photourl','is_superuser','last_login','date_joined','cover_photo','about','facebook_id','twitter_id',"instagram_id","followers"]


class Userrestapiserilizer(serializers.ModelSerializer):
    followers=userserliz(many=True)
    class Meta:
        model=User
        fields=['username','photourl','cover_photo','about','facebook_id','twitter_id',"instagram_id","followers"]
