from django.db import models
from django.utils import timezone
from django.contrib import admin
# import pytz
from twitter_user.models import TwitterUser
# Create your models here.


class Tweet(models.Model):
    author = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name="author",
        null=True,
        blank=True)
    content = models.TextField(max_length=140)
    likes = models.IntegerField(default=0)
    tweet_date = models.DateTimeField(default=timezone.now)


class TweetAdmin(admin.ModelAdmin):
    fields = ("content",)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
