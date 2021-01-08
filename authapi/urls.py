from django.urls import include,path
from .views import *
urlpatterns=[
    path('user/me/profile/<slug:pk>',Usereditapi.as_view()),
    path('', include('djoser.urls.base')),
    path('', include('djoser.urls.authtoken')),
    path('',include('djoser.urls.jwt')),
    path("user/<slug:uid>/follow",AddFollowToUser.as_view()),
    path("user/<slug:pk>",AboutUserApi.as_view()),


    # path('',include('social_django.urls'))
]