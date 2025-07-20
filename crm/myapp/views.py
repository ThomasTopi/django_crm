from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


def home(request):
    if request.user.is_authenticated:
        return render(request, "home_user.html", {})
    else:
        return render(request, "home.html", {})


def login_view(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("home")
        else:
            error = "Nesprávné uživatelské jméno nebo heslo."
    return render(request, "login.html", {"error": error})


def logout_view(request):
    auth_logout(request)
    return redirect("home")
