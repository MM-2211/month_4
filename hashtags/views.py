from django.shortcuts import render
from . import models


def all_category_books(request):
    if request.method == 'GET':
        query = models.Product.objects.all()
        return render(request,
                      template_name='tags/all_category_books.html',
                      context={'query': query}
                      )
def teenagers_category_books(request):
    if request.method == 'GET':
        query = models.Product.objects.all().filter(tags__name='Для подростков')
        return render(request,
                      template_name='tags/teenagers_category_books.html',
                      context={'query': query}
                      )
def kids_category_books(request):
    if request.method == 'GET':
        query = models.Product.objects.all().filter(tags__name='Для детей')
        return render(request,
                      template_name='tags/kids_category_books.html',
                      context={'query': query})