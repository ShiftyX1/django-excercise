from django.urls import path, re_path
from blog import views

urlpatterns = [path('', views.index, name='index'),
               re_path(r'^about/', views.about, name='about', kwargs={'name': 'Tom', 'age': 30}),
               path('contact/', views.contact, name='contact'),
               path('forbidden/', views.forbidden_page, name='forbidden_test'),
               path('user/<str:name>/<int:age>/', views.user),
               path("user/<str:name>/", views.user),
               path("user/", views.user),
               ]
