from django.contrib import admin
from .models import LikePost,Post,FollowersCount,Profile

admin.site.register(LikePost)
admin.site.register(Post)
admin.site.register(FollowersCount)
admin.site.register(Profile)


