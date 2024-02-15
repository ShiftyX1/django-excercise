from django.urls import path, re_path, include
from blog import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="blog/index.html")),
    path("user/", views.user)
]
