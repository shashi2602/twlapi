from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response




class Usereditapi(generics.RetrieveUpdateAPIView):
    queryset=User.objects.all()
    serializer_class=Userrestapiserilizer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(uid=self.request.user.uid)

class AboutUserApi(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=AboutUserserilz
class AddFollowToUser(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,uid=None,format=None):
        obj=get_object_or_404(User,uid=uid)
        user_=self.request.user
        updated=False
        followed=False
        if user_:
            if user_ in obj.followers.all():
                followed=False
                obj.followers.remove(user_)
            else:
                followed=True
                obj.followers.add(user_)
            updated=True
        data={
            'updated':updated,
            'followed':followed
        }
        return Response(data)

