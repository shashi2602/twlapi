from django.urls import path
from .views import *

urlpatterns = [
    path("users/",getusers.as_view(),name="createusers"),
    path("users/<int:pk>",updatedeleteuser.as_view(),name="updatedeleteuser"),
    path("users/<slug:pk>",getuserbyid.as_view()),
    path("place",placecreateapi.as_view()),#right
    path("topic",topiccreateapi.as_view()),#right
    path("post",GetAllPosts.as_view()),#right
    path("user/post/create",postcreateapi.as_view()),#right
    path("comments",commentscreateapi.as_view()),
    path("subcomments",subcommentcreateapi.as_view()),
    path("user/place/<int:pk>",placeupdatedeleteapi.as_view()),
    path("user/topic/<int:pk>",topicupdatedeleteapi.as_view()),
    path("user/post/<int:pk>",postupdatedeleteapi.as_view()),
    path("comments/<int:pk>",commentsupdatedeleteapi.as_view()),
    path("subcomments/<int:pk>",subcommentupdatedeleteapi.as_view()),
    path('user/post',GetUserPosts.as_view()),
    path("post/<int:pk>",GetSinglePost.as_view(),name="post-detail"),
    path('place/<slug:place>',GetAllPlacesposts.as_view()),
    path("topic/<slug:topic>",GetAllTopicPosts.as_view()),
    path("post/<int:pid>/like",AddLikeToPost.as_view(),name="post-like")
    
]