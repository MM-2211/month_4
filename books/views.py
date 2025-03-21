from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from django.views import generic, View
from . import models




class SearchBooksView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'query'

    def get_queryset(self):
        return models.Books.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, *args, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Books, id=book_id)

# def books_detail(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(models.Books, id=id)
#         return render(
#             request,
#             template_name='book_detail.html',
#             context={
#                 'book_id': book_id,
#             }
#         )


class BookListView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'query'
    model = models.Books

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.all()

# def books_list(request):
#     if request.method == "GET":
#         query = models.Books.objects.all()
#         return render (
#             request,
#             template_name="book.html",
#             context = {
#                 "query": query,
#             }
#         )

class TextView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("About Me <br>"
                            "Имя: Мигель <br>"
                            "Прозвище: Василек <br>"
                            "Дата рождения: 22.11.2005 <br>"
                            "Образование: КНУ, 2-ой курс <br>")


# def text(request):
#     if request.method == "GET":
#         return HttpResponse("About Me <br>"
#                             "Имя: Мигель <br>"
#                             "Прозвище: Василек <br>"
#                             "Дата рождения: 22.11.2005 <br>"
#                             "Образование: КНУ, 2-ой курс <br>")

class AnimalView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Jennifer <br> <img src="/static/images/photo_5357577784995735657_y.jpg" alt="Jennifer">')

# def animal(request):
#     if request.method == "GET":
#         return HttpResponse('Jennifer <br> <img src="/static/images/photo_5357577784995735657_y.jpg" alt="Jennifer">')

class TimeView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(f"{datetime.now()}")

# def time(request):
#     if request.method == "GET":
#         return HttpResponse(f"{datetime.now()}")