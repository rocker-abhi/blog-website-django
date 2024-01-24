from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("login/", views.login_account),
    path("signup/", views.signup),
    path("home/", views.home),
    path("new-post/", views.new_post),
]