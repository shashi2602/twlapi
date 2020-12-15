from django.urls import include,path

urlpatterns=[
    path('', include('djoser.urls.base')),
    path('', include('djoser.urls.authtoken')),
    path('',include('djoser.urls.jwt')),
    # path('',include('social_django.urls'))
]