"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitter_user.views import home_view, follow_view, unfollow_view, user_view, notif_view
from twitter_tweets.views import tweet_view, like_view, post_view
from twitter_auth.views import signup_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="homepage"),
    path('user/<str:username>/', user_view, name="user"),
    path('follow/<str:username>/', follow_view, name="follow"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('notifications/', notif_view, name="notifs"),
    path('post/', post_view, name='post'),
    path('signup/', signup_view, name="signup"),
    path('status/<int:tweet_id>/', tweet_view, name="tweet"),
    path('status/<int:tweet_id>/like/',
         like_view, name="like_tweet"),
    path('unfollow/<str:username>/', unfollow_view, name="unfollow"),

]
