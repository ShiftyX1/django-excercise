from django.urls import path, re_path, include
from blog import views

urlpatterns = [
    path("", views.index),
    path("user/", views.user)
]
