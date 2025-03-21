
from django.urls import path
from . import views

urlpatterns = [
    path("text/", views.TextView.as_view(), name="text"),
    path("animal/", views.AnimalView.as_view(), name="animal"),
    path("time/", views.TimeView.as_view(), name="time"),
    path("", views.BookListView.as_view(), name="books"),
    path("book_list/<int:id>/", views.BookDetailView.as_view(), name="books_detail"),
    path("search/", views.SearchBooksView.as_view(), name="search"),
]