from rest_framework import serializers
from .models import *
from authapi.models import User
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

class userModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['uid','username','email','photourl','is_superuser','last_login','date_joined']





class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model=TopicModel
        fields="__all__"
        


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlaceModel
        fields="__all__"


class SubCommentSerializer(serializers.ModelSerializer):
    scname=serializers.SerializerMethodField()
    scphoto=serializers.SerializerMethodField()
    class Meta:
        model=SubCommentModel
        fields=['id','subComment','comment','scUser','scname','scphoto']
    
    def get_scname(self,obj):
        return obj.scUser.username
    
    def get_scphoto(self,obj):
        return obj.scUser.photourl.url

class CommentsSerializer(serializers.ModelSerializer):
    replies=serializers.SerializerMethodField()
    c_name=serializers.SerializerMethodField()
    c_photourl=serializers.SerializerMethodField()
    class Meta:
        model=CommentsModel
        fields=['id','comment','postname','c_userid','c_name','c_photourl','date','likes','replies']

    def get_replies(self,obj):
        return SubCommentSerializer(obj.subcomments,many=True).data

    def get_c_name(self,obj):
        return obj.c_userid.username

    def get_c_photourl(self,obj):
        return obj.c_userid.photourl.url

class ThumbnailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Thumbnails
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):
    url=serializers.HyperlinkedIdentityField(
        view_name="post-detail",
        # lookup_field="title_slug"
    )
    userphoto=serializers.SerializerMethodField()
    comment=serializers.SerializerMethodField()
    topic_name=serializers.SerializerMethodField()
    place_name=serializers.SerializerMethodField()
    likes=userModelSerializer(many=True)
    likes_count=serializers.SerializerMethodField()
    thumbnailimage=serializers.ImageField(max_length=None, use_url=True)
    is_liked=serializers.SerializerMethodField()
    class Meta:
        model=PostModel
        fields=['id','title','overview','content','likes','likes_count','thumbnailimage','topic_name','topic','place_name','place','author','authorname','title_slug','url','userphoto','date','updated_date','comment','is_liked']
        ordering=['-date','-updated_date']
    def get_userphoto(self,obj):
        try:
           userphoto=obj.author.photourl.url
        except:
            userphoto=None
        return userphoto
    def get_topic_name(self,obj):
        return obj.topic.tpname

    def get_place_name(self,obj):
        return obj.place.Pname
    def get_comment(self,obj):
        return CommentsSerializer(obj.comments,many=True).data
    def get_is_liked(self,instance):
        request=self.context.get('request');
        return PostModel.objects.filter(likes=request.user).exists()
    def get_likes_count(self,obj):
        return obj.likes.count()