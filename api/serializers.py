from rest_framework import serializers
from .models import *
from authapi.models import User
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

class userModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['uid','username','email','photourl','is_superuser']

# class tagsmodelserializer(serializers.ModelSerializer):
#     class Meta:
#         model=tagsmodel
#         fields="__all__"

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
        return obj.scUser.photourl

class CommentsSerializer(serializers.ModelSerializer):
    replies=serializers.SerializerMethodField()
    c_name=serializers.SerializerMethodField()
    c_photourl=serializers.SerializerMethodField()
    class Meta:
        model=CommentsModel
        fields=['id','comment','postname','c_userid','c_name','c_photourl','replies']

    def get_replies(self,obj):
        return SubCommentSerializer(obj.subcomments,many=True).data

    def get_c_name(self,obj):
        return obj.c_userid.username

    def get_c_photourl(self,obj):
        return obj.c_userid.photourl

class PostSerializer(TaggitSerializer,serializers.ModelSerializer):
    url=serializers.HyperlinkedIdentityField(
        view_name="post-detail",
        # lookup_field="title_slug"
    )
    userphoto=serializers.SerializerMethodField()
    comment=serializers.SerializerMethodField()
    topic_name=serializers.SerializerMethodField()
    place_name=serializers.SerializerMethodField()
    tags=TagListSerializerField()
    likes=serializers.SerializerMethodField()
    class Meta:
        model=PostModel
        fields=['id','title','overview','content','thumbnail','likes','tags','topic_name','topic','place_name','place','author','authorname','title_slug','url','userphoto','date','comment']
    
    def get_userphoto(self,obj):
        try:
           userphoto=obj.author.photourl
        except:
            userphoto=None
        return userphoto
    def get_topic_name(self,obj):
        return obj.topic.tpname

    def get_place_name(self,obj):
        return obj.place.Pname
    def get_likes(self,obj):
        return obj.likes.count()
    def get_comment(self,obj):
        return CommentsSerializer(obj.comments,many=True).data