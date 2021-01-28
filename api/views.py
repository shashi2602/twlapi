from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import generics,mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from authapi.models import User
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic import DetailView
from rest_framework.parsers import FormParser,MultiPartParser


class getusers(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=userModelSerializer
    permission_classes=[IsAuthenticated]

class getuserbyid(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=userModelSerializer
    permission_classes=[IsAuthenticated]

class updatedeleteuser(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=userModelSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Usermodel.objects.filter(uid=self.request.uid)

class topiccreateapi(generics.ListCreateAPIView):
    queryset=TopicModel.objects.all()
    serializer_class=TopicSerializer
    permission_classes=[IsAuthenticated]

class topicupdatedeleteapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=TopicModel.objects.all()
    serializer_class=TopicSerializer
    permission_classes=[IsAuthenticated]

class postcreateapi(generics.ListCreateAPIView):
    queryset=PostModel.objects.all()
    serializer_class=PostSerializer
    # authentication_classes=(TokenAuthentication)
    permission_classes=[IsAuthenticated]
    parser_classes=[MultiPartParser,FormParser]

class postupdatedeleteapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=PostModel.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
      data= queryset=PostModel.objects.filter(author=self.request.user.uid)
      return data
class thumbnailcreateapi(generics.ListCreateAPIView):
    queryset=Thumbnails.objects.all()
    serializer_class=ThumbnailsSerializer
    # permission_classes=[IsAuthenticated]
class placecreateapi(generics.ListCreateAPIView):
    queryset=PlaceModel.objects.all()
    serializer_class=PlaceSerializer
    permission_classes=[IsAuthenticated]
class getplacesapi(generics.ListAPIView):
    queryset=PlaceModel.objects.all()
    serializer_class=PlaceSerializer
    # permission_classes=[IsAuthenticated]

class placeupdatedeleteapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=PlaceModel.objects.all()
    serializer_class=PlaceSerializer
    permission_classes=[IsAuthenticated]

class commentscreateapi(generics.ListCreateAPIView):
    queryset=CommentsModel.objects.all().order_by('-date')
    serializer_class=CommentsSerializer
    permission_classes=[IsAuthenticated]
class commentsretrive(generics.ListAPIView):
    queryset=CommentsModel.objects.all().order_by('-date')
    serializer_class=CommentsSerializer
    # permission_classes=[IsAuthenticated]
    lookup_field='postname'

class commentsupdatedeleteapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=CommentsModel.objects.all()
    serializer_class=CommentsSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return CommentsModel.objects.filter(c_userid=self.request.user.uid)

class subcommentcreateapi(generics.ListCreateAPIView):
    queryset=SubCommentModel.objects.all()
    serializer_class=SubCommentSerializer
    permission_classes=[IsAuthenticated]

class subcommentretrive(generics.RetrieveAPIView):
    queryset=SubCommentModel.objects.all()
    serializer_class=SubCommentSerializer
    permission_classes=[IsAuthenticated]


class subcommentupdatedeleteapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=SubCommentModel.objects.all()
    serializer_class=SubCommentSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return SubCommentModel.objects.filter(scUser=self.request.user.uid)

class GetAllPosts(generics.ListAPIView):
    queryset=PostModel.objects.all().order_by('-date')
    serializer_class=PostSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['title','author','place__Pname','topic__tpname']

class GetUserPosts(generics.ListAPIView):
    queryset=PostModel
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
      data=  queryset=PostModel.objects.filter(author=self.request.user.uid)
      return data
class GetAuthorPosts(generics.ListAPIView):
    queryset=PostModel
    serializer_class=PostSerializer
    def get_queryset(self):
        data=  queryset=PostModel.objects.filter(author=self.kwargs['userid'])
        return data
class GetSinglePost(generics.RetrieveAPIView):
    queryset=PostModel.objects.all()
    serializer_class=PostSerializer

class GetThumbnailOfPost(generics.RetrieveAPIView):
    queryset=Thumbnails.objects.all()
    serializer_class=ThumbnailsSerializer
    # def get_queryset(self):
    #     return Thumbnails.objects.filter(postid__id=self.kwargs['postid'])
class GetAllPlacesposts(generics.ListAPIView):
    queryset=PostModel.objects.all()
    serializer_class=PostSerializer
    def get_queryset(self):
        return PostModel.objects.filter(place__pname_slug=self.kwargs['place'])

class GetAllTopicPosts(generics.ListAPIView):
    queryset=PostModel.objects.all()
    serializer_class=PostSerializer
    def get_queryset(self):
        return PostModel.objects.filter(topic__tpname_slug=self.kwargs['topic'])


class AddLikeToPost(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,pid=None,format=None):
        obj=get_object_or_404(PostModel,id=pid)
        user_=self.request.user
        updated=False
        liked=False
        if user_:
            if user_ in obj.likes.all():
                liked=False
                obj.likes.remove(user_)
            else:
                liked=True
                obj.likes.add(user_)
            updated=True
        data={
            'updated':updated,
            'liked':liked
        }
        return Response(data)


class ArticlesFavoriteAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def delete(self, request, pid=None):
        profile = self.request.user
        serializer_context = {'request': request}

        try:
            article = PostModel.objects.get(id=pid)
        except PostModel.DoesNotExist:
            raise NotFound('An article with this slug was not found.')

        profile.unfavorite(article)

        serializer = self.serializer_class(article, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pid=None):
        profile = self.request.user
        serializer_context = {'request': request}

        try:
            article = PostModel.objects.get(id=pid)
        except PostModel.DoesNotExist:
            raise NotFound('An article with this slug was not found.')

        profile.addfavorite(article)

        serializer = self.serializer_class(article, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_201_CREATED)