from django.urls import path
from .views import *

urlpatterns = [
    #comments operation urls
    path("comments",commentscreateapi.as_view()),
    path("comments/<int:postname>",commentsretrive.as_view()),
    path("subcomments/<int:pk>",subcommentretrive.as_view()),
    path("subcomments",subcommentcreateapi.as_view()),
    path("comments/<int:pk>/ud",commentsupdatedeleteapi.as_view()),
    path("subcomments/<int:pk>/ud",subcommentupdatedeleteapi.as_view()),
    #posts operation urls
    path("user/post/create",postcreateapi.as_view()),#right
    path("post",GetAllPosts.as_view()),#right
    path("post/thumbnail",thumbnailcreateapi.as_view()),#right
    path("post/<int:pk>",GetSinglePost.as_view(),name="post-detail"),
    path("post/<int:pid>/like",AddLikeToPost.as_view(),name="post-like"),
    path("post/thumbnail/<int:pk>",GetThumbnailOfPost.as_view()),
    path("post/<int:pid>/fav",ArticlesFavoriteAPIView.as_view()),
    #place operation urls
    path("place",placecreateapi.as_view()),#right
    path("place/all",getplacesapi.as_view()),#right
    path('place/<slug:place>',GetAllPlacesposts.as_view()),
    #topic operation urls
    path("topic/<slug:topic>",GetAllTopicPosts.as_view()),
    path("topic",topiccreateapi.as_view()),#right
    #user operation urls
    path("users/",getusers.as_view(),name="createusers"),
    path("users/<int:pk>",updatedeleteuser.as_view(),name="updatedeleteuser"),
    path("users/<slug:pk>",getuserbyid.as_view()),
    path("user/place/<int:pk>",placeupdatedeleteapi.as_view()),
    path("user/topic/<int:pk>",topicupdatedeleteapi.as_view()),
    path("user/post/<int:pk>",postupdatedeleteapi.as_view()),
    path('user/post',GetUserPosts.as_view()),
    path("author/posts/<slug:userid>",GetAuthorPosts.as_view()),

]