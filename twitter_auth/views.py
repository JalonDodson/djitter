from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from twitter_auth.forms import SignUpForm, LogInForm


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("homepage"))
    form = SignUpForm()
    return render(request, "generic_form.html",
                  {"form": form, "input_value": "Sign Up"})


def login_view(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data
            user = authenticate(
                request, username=d["username"], password=d["password"])
            if user:
                login(request, user)
                return redirect(reverse("homepage"))
    form = LogInForm()
    return render(request, "generic_form.html",
                  {"form": form, "input_value": "Log In", "signup_flag": True})


def logout_view(request):
    logout(request)
    return redirect(reverse("homepage"))
