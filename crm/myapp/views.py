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


def cleaning_groups(request):
    skupina_1 = [1, 5, 6]
    skupina_2 = [4, 2, 3]
    skupina_3 = [5, 8, 9]
    skupina_4 = [10, 22, 12]
    return render(
        request,
        "clean.html",
        {
            "skupina_1": skupina_1,
            "skupina_2": skupina_2,
            "skupina_3": skupina_3,
            "skupina_4": skupina_4,
        },
    )


def money_collect(request):
    users = [
        {"name": "Jan Novák", "amount": 500},
        {"name": "Petr Svoboda", "amount": 300},
        {"name": "Anna Dvořáková", "amount": 200},
    ]
    equipment_votes = [
        {"name": "Bench press", "link": "https://example.com/bench-press"},
        {"name": "Běžecký pás", "link": "https://example.com/bezecky-pas"},
    ]
    return render(
        request,
        "money_collect.html",
        {"users": users, "equipment_votes": equipment_votes},
    )
