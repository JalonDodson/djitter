from django import forms
from django.contrib.auth.forms import UserCreationForm
from twitter_user.models import TwitterUser


class SignUpForm(UserCreationForm):
    # username = forms.CharField(max_length=64)
    # display = forms.CharField(max_length=48)
    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = TwitterUser
        fields = ("username", "display")


class LogInForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
