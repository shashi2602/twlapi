from django.contrib import admin
from .models import *

admin.site.register(Usermodel)
admin.site.register(PlaceModel)
admin.site.register(TopicModel)
admin.site.register(PostModel)
admin.site.register(CommentsModel)
admin.site.register(SubCommentModel)
admin.site.register(Thumbnails)


