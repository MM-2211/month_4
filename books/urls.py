
from django.urls import path
from . import views

urlpatterns = [
    path("text/", views.text),
    path("animal/", views.animal),
    path("time/", views.time),
    path("book_list/", views.books_list),
    path("book_list/<int:id>/", views.books_detail),
]