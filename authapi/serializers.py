from djoser.serializers import UserCreateSerializer,UserSerializer
from rest_framework import serializers
from  .models import *

class usercreateserli(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=User
        fields=('uid','username','email','photourl','password')