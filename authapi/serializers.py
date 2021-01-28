from djoser.serializers import UserCreateSerializer,UserSerializer
from rest_framework import serializers
from  .models import *
from api.serializers import PostSerializer


class usercreateserli(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=User
        fields=('uid','username','email','password','photourl')

class userserliz(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['uid','username','email','photourl','is_superuser','last_login','date_joined']
class AboutUserserilz(serializers.ModelSerializer):
    following=userserliz(many=True)
    is_user_following=serializers.SerializerMethodField()
    favorites=PostSerializer(many=True)
    class Meta:
        model=User
        fields=['uid','username','email','photourl','is_superuser','last_login','date_joined','cover_photo','about','facebook_id','twitter_id',"instagram_id","following",'is_user_following','favorites']
    def get_is_user_following(self,instance):
        request=self.context.get('request',None);
        if request is None:
            return False
        if not request.user.is_authenticated:
            return False
        return User.objects.filter(following=request.user).exists()
class Userrestapiserilizer(serializers.ModelSerializer):
    followers=userserliz(many=True)
    class Meta:
        model=User
        fields=['username','photourl','cover_photo','about','facebook_id','twitter_id',"instagram_id","followers"]
