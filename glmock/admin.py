from django.contrib import admin
from .models import VideoPost, Comment, userdata,Membership, UserMembership, Subscription

admin.site.register(VideoPost)
admin.site.register(Comment)
admin.site.register(userdata)
admin.site.register(Membership)
admin.site.register(UserMembership)
admin.site.register(Subscription)