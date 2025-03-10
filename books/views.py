from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models


def books_detail(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Books, id=id)
        return render(
            request,
            template_name='book_detail.html',
            context={
                'book_id': book_id,
            }
        )

def books_list(request):
    if request.method == "GET":
        query = models.Books.objects.all()
        return render (
            request,
            template_name="book.html",
            context = {
                "query": query,
            }
        )

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