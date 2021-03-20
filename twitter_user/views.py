from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View

from twitter_tweets.forms import TweetForm
from twitter_tweets.models import Tweet
from twitter_user.models import TwitterUser
from twitter_notifications.models import Notification


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            self_tweets = Tweet.objects.filter(author=request.user)
            f = TwitterUser.objects.get(id=request.user.id).following.all()
            f_t = Tweet.objects.filter(author__username__in=[x.username for x in f])

            tweets = list(self_tweets) + list(f_t)
            tweets.sort(key=lambda x: x.tweet_date, reverse=True)
            
            form = TweetForm()
            return render(request, "index.html", {"form": form, "tweets": tweets})
        return redirect(reverse("splash"))


@login_required(redirect_field_name="homepage")
def follow_view(request, username):
    follow_user = TwitterUser.objects.get(username=username)
    follow_from = TwitterUser.objects.get(username=request.user.username)
    
    follow_user.followers.add(follow_from)
    follow_from.following.add(follow_user)

    follow_user.save()
    follow_from.save()
    return redirect(reverse("user", args=(username,)))


@login_required(redirect_field_name="homepage")
def unfollow_view(request, username):
    unfollow_user = TwitterUser.objects.get(username=username)
    unfollow_from = TwitterUser.objects.get(username=request.user.username)

    unfollow_user.followers.remove(unfollow_from)
    unfollow_from.following.remove(unfollow_user)

    unfollow_user.save()
    unfollow_from.save()
    return redirect(reverse("user", args=(username,)))


def user_view(request, username):
    user = TwitterUser.objects.get(username=username)
    tweets = Tweet.objects.filter(author=user)
    follow_count = TwitterUser.objects.get(id=user.id).followers.all()
    if request.user.is_authenticated:
        is_following = (
            TwitterUser.objects.get(id=user.id).followers.filter(
                id=request.user.id))
    else:
        is_following = False
    return render(request,
                  "user.html",
                  {"tweets": tweets,
                   "username": username,
                   "is_following": is_following,
                   "follow_count": follow_count})


def notif_view(request):
    unread = Notification.objects.filter(to=request.user, unread=True)
    for x in unread:
        x.unread = False
        x.save()
    return render(request, "notification.html", {"unread": unread})
