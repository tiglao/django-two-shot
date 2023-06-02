from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from accounts.forms import LoginForm, SignUpForm


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password,
            )

            if user is not None:
                auth_login(request)
                return redirect("home")
    else:
        form = LoginForm()

    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]

            if password == password_confirmation:
                user = User.objects.create_user(
                    username,
                    password=password,
                )
                auth_login(request, user)
                return redirect("home")
            else:
                form.add_error("password", "the passwords do not match")
    else:
        form = SignUpForm()

    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def exit(request):
    logout(request)
    return redirect("login")
