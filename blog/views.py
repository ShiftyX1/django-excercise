from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render

def index(request):
    return HttpResponse("<h2>Главная</h2>")


def about(request, name, age):
    return HttpResponse(f"""
    <h2>О пользователе</h2>
    <p>Имя: {name}</p>
    <p>Возраст: {age}</p>
    """)


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")


def forbidden_page(request):
    return HttpResponseForbidden("")


def user(request, name="Undefined", age=0):
    return HttpResponse(f"""
    <h2 align="center">Пользователь</h2>
    <ul>
    <li>Имя: {name}</li>
    <li>Возраст: {age}</li>
    </ul>""")
