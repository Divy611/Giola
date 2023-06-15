from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

MEMBERSHIP_CHOICES = (('Premium', 'Premium'),('Free', 'Free'))

class Membership(models.Model):
    slug = models.SlugField(null=True, blank=True)
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, default='Free',max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True)
    def __str__(self):
        return self.membership_type

class UserMembership(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='user_membership', on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, related_name='user_membership', on_delete=models.SET_NULL, null=True)
    def __str__(self):
       return self.user.username

class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, related_name='subscription', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.user_membership.user.username
class VideoPost(models.Model):
    id=models.UUIDField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='videos/thumbnail/', default='none')
    category = models.CharField(max_length=50, default='none')
    pub_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes')
    video_views = models.ManyToManyField(User, related_name='video_views')
    def __str__(self):
        return self.title

class userdata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    profile_pic = models.ImageField(upload_to='pic/', default='pic/default.jpg')
    subscribers = models.ManyToManyField(User, related_name='subscribers')

class Comment(models.Model):
    post = models.ForeignKey(VideoPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    def __str__(self):
        return self.user.username