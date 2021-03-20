from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import View

import datetime
from twitter_auth.forms import SignupForm, LoginForm
from twitter_user.models import TwitterUser
import phonenumbers

class SignupView(View):
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("homepage"))
    

    def get(self, request):
        form = SignupForm()
        return render(request, "auth/signup.html", {"form": form})


class LoginView(View):
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data
            user = authenticate(
                request, username=d["username"], password=d["password"])
            if user:
                login(request, user)
                return redirect(reverse("homepage"))
    

    def get(self, request):
        form = LoginForm()
        return render(request, "auth/login.html", {"form": form})


class SplashView(View):
    def post(self, request):
        if not request.user.is_authenticated:
            form = SignupForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                
                number = data["number"].replace('-','').replace('(','').replace(')','')
                ph = phonenumbers.parse(number, "US")
                valid_num = phonenumbers.is_valid_number(ph)
                if not valid_num:
                    messages.error(request, "Invalid phone number, use format: 123-456-7890")
                    form = SignupForm()
                    return render(request, "auth/splash.html", {"form": form, "reg_error": "invalid_num"})
                dob = datetime.date(int(data["year"]), int(data["month"]), int(data["day"]))
                user = TwitterUser.objects.create_user(
                                                username=data["username"],
                                                password=data["password"],
                                                dob=dob,
                                                number=ph.national_number)
                x = authenticate(request, username=data["username"], password=data["password"])
                if x:
                    login(request, user)
                    return redirect(reverse("homepage"))
        
            

    def get(self, request):
        if not request.user.is_authenticated:
            form = SignupForm()
            return render(request, "auth/splash.html", {"form": form})
        return render(request, "index.html", {})


def logout_view(request):
    logout(request)
    return redirect(reverse("homepage"))
