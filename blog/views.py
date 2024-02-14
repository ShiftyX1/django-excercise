from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.template.response import TemplateResponse

def index(request):
    return TemplateResponse(request, 'blog/index.html')


def user(request):
    age = request.GET.get("age")
    name = request.GET.get("name")
    return HttpResponse(f"<h2>Имя: {name}, Возраст: {age}</h2>")
