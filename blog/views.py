from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.template.response import TemplateResponse


def index(request):
    cat = ["Python", "Java", "JS", "Go", "C#", "Kotlin", "C++"]
    empty_list = []
    return render(request, "blog/index.html", context={"cat": cat})


def user(request):
    age = request.GET.get("age")
    name = request.GET.get("name")
    return HttpResponse(f"<h2>Имя: {name}, Возраст: {age}</h2>")
