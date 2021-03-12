from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class TwitterUser(AbstractUser):
    display = models.CharField(max_length=48)
    number = models.IntegerField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    followers = models.ManyToManyField(
        "self", symmetrical=False, related_name="user_followers", blank=True)
    following = models.ManyToManyField(
        "self", symmetrical=False, related_name="user_following", blank=True)

    def __str__(self):
        return f"{self.display} | {self.username}"
