from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def text(request):
    if request.method == "GET":
        return HttpResponse("About Me <br>"
                            "Имя: Мигель <br>"
                            "Прозвище: Василек <br>"
                            "Дата рождения: 22.11.2005 <br>"
                            "Образование: КНУ, 2-ой курс <br>")

def animal(request):
    if request.method == "GET":
        return HttpResponse('Jennifer <br> <img src="/static/images/photo_5357577784995735657_y.jpg" alt="Jennifer">')

def time(request):
    if request.method == "GET":
        return HttpResponse(f"{datetime.now()}")