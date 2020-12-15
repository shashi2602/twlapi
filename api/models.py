from django.db import models
import uuid
from authapi.models import User
from django.utils.text import slugify
from taggit.managers import TaggableManager

class Usermodel(models.Model):
    id=models.CharField(max_length=500,primary_key=True)
    email=models.CharField(max_length=500)
    photoURL=models.CharField(max_length=100)
    displayName=models.CharField(max_length=500)
    def __str__(self):
        return self.displayName



class TopicModel(models.Model):
    tpname=models.CharField(max_length=500)
    tpdecs=models.CharField(max_length=500,null=True)
    tpname_slug=models.SlugField(null=True,blank=True)

    def save(self, *args, **kwargs):
        if self.tpname_slug==None:
            slug1 = slugify(self.tpname)
            has_slug = TopicModel.objects.filter(tpname_slug=slug1).exists()
            count = 1
            while has_slug:
                count += 1
                slug1 = slugify(self.tpname) + '-' + str(count)
                has_slug =  TopicModel.objects.filter(tpname_slug=slug1).exists()
            self.tpname_slug = slug1
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.tpname

    @property
    def topicpost(self):
        return PostModel.objects.filter(topic=self)

class PlaceModel(models.Model):
    Pname=models.CharField(max_length=500)
    Pdecs=models.CharField(max_length=500,null=True)
    pname_slug=models.SlugField(null=True,blank=True)
    def save(self, *args, **kwargs):
        if self.pname_slug==None:
            slug1 = slugify(self.Pname)
            has_slug =PlaceModel.objects.filter(pname_slug=slug1).exists()
            count = 1
            while has_slug:
                count += 1
                slug1 = slugify(self.Pname) + '-' + str(count)
                has_slug =  PlaceModel.objects.filter(pname_slug=slug1).exists()
            self.pname_slug = slug1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Pname
    
    @property
    def placepost(self):
        return PostModel.objects.filter(place=self)

class PostModel(models.Model):
    title=models.TextField(null=False,default="")
    content=models.TextField(null=False)
    overview=models.TextField(null=False)
    thumbnail=models.ImageField(upload_to="thumbnail/",blank=True)
    topic=models.ForeignKey(TopicModel,null=True,on_delete=models.PROTECT)
    tags=TaggableManager()
    place=models.ForeignKey(PlaceModel,null=True,on_delete=models.PROTECT)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    authorname=models.CharField(null=False,max_length=1000,default="")
    likes=models.ManyToManyField(User,blank=True,related_name="post_like")
    title_slug=models.SlugField(null=True,blank=True)
    date=models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.title_slug==None:
            slug1 = slugify(self.title)
            has_slug = PostModel.objects.filter(title_slug=slug1).exists()
            count = 1
            while has_slug:
                count += 1
                slug1 = slugify(self.title) + '-' + str(count)
                has_slug =  PostModel.objects.filter(title_slug=slug1).exists()
            self.title_slug = slug1
        super().save(*args, **kwargs)

    @property
    def comments(self):
        instance=self
        qs=CommentsModel.objects.filter(postname=self)
        return qs
    
    @property
    def topics(self):
        return TopicModel
    def __str__(self):
        return self.title

class CommentsModel(models.Model):
    comment=models.TextField()
    postname=models.ForeignKey(PostModel,on_delete=models.CASCADE)
    c_userid=models.ForeignKey(User,on_delete=models.CASCADE)

    @property
    def subcomments(self):
        instance=self
        qs=SubCommentModel.objects.filter(comment=self)
        return qs

    

class SubCommentModel(models.Model):
    subComment=models.TextField()
    comment=models.ForeignKey(CommentsModel,on_delete=models.CASCADE)
    scUser=models.ForeignKey(User,on_delete=models.CASCADE)