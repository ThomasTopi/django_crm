from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("clean/", views.cleaning_groups, name="cleaning_groups"),
    path("money-collect/", views.money_collect, name="money_collect"),
]
