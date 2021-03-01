from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from twitter_tweets.forms import TweetForm
from twitter_tweets.models import Tweet
from twitter_user.models import TwitterUser
from twitter_notifications.models import Notification


@login_required()
def home_view(request):
    self_tweets = Tweet.objects.filter(author=request.user)
    f = TwitterUser.objects.get(id=request.user.id).following.all()
    f_t = Tweet.objects.filter(author__username__in=[x.username for x in f])
    tweets = list(self_tweets) + list(f_t)
    tweets.sort(key=lambda x: x.tweet_date, reverse=True)
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data
            Tweet.objects.create(author=request.user, content=d["content"])
            return redirect(reverse("homepage"))
    form = TweetForm()
    return render(request,
                  "index.html",
                  {"form": form,
                   "tweets": tweets})


@login_required()
def follow_view(request, username):
    to_follow = TwitterUser.objects.get(username=username)
    follow_from = TwitterUser.objects.get(username=request.user.username)

    to_follow.followers.add(follow_from)
    follow_from.following.add(to_follow)
    return redirect(reverse("user", args=(username,)))


@login_required()
def unfollow_view(request, username):
    to_unfollow = TwitterUser.objects.get(username=username)
    unfollow_from = TwitterUser.objects.get(username=request.user.username)

    to_unfollow.followers.remove(unfollow_from)
    unfollow_from.following.remove(to_unfollow)
    return redirect(reverse("user", args=(username,)))


def user_view(request, username):
    user = TwitterUser.objects.get(username=username)
    tweets = Tweet.objects.filter(author=user)
    follow_count = TwitterUser.objects.get(id=user.id).following.all()
    if request.user.is_authenticated:
        c = TwitterUser.objects.get(id=user.id)
        is_following = (TwitterUser.objects.get(id=c.id).following.filter(id=user.id))
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
