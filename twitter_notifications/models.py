from django.db import models
from twitter_user.models import TwitterUser
from twitter_tweets.models import Tweet
# Create your models here.


class Notification(models.Model):
    notifier = models.ForeignKey(
                                 TwitterUser,
                                 on_delete=models.CASCADE,
                                 related_name="sender", blank=True, null=True)
    to = models.ForeignKey(TwitterUser,
                           on_delete=models.CASCADE,
                           related_name="recip",
                           blank=True, null=True)
    tweet = models.ForeignKey(Tweet,
                              on_delete=models.CASCADE,
                              related_name="mentioned_in",
                              blank=True, null=True)
    unread = models.BooleanField(default=True)
