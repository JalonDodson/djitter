from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from twitter_tweets.forms import TweetForm
from twitter_tweets.models import Tweet
from twitter_notifications.models import Notification
from twitter_user.models import TwitterUser
# Create your views here.


def tweet_view(request, tweet_id):
    tweet = Tweet.objects.filter(id=tweet_id).first()
    return render(request, "tweet.html", {"tweet": tweet})


@login_required()
def like_view(request):
    return render(request, "index.html", {})


@login_required()
def post_view(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data
            mentions = [x for x in d["content"].split() if "@" in x]
            tweet = Tweet.objects.create(
                                         content=d['content'],
                                         author=request.user)
            if mentions:
                for m in mentions:
                    user_to = m.strip("@")
                    user = request.user
                    x = TwitterUser.objects.filter(username=user_to).first()
                    if x:
                        Notification.objects.create(
                                                    notifier=user,
                                                    to=x, tweet=tweet)
            return redirect(reverse("homepage"))
    form = TweetForm()
    return render(request,
                  "generic_form.html", {"form": form, "input_value": "Submit"})
