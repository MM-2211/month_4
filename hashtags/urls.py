from django.urls import path
from . import views

urlpatterns = [
    path('all_hashtags_films/', views.all_category_books, name='all'),
    path('teen_hashtags_films/', views.teenagers_category_books, name='teen'),
    path('kids_hashtags_films/', views.kids_category_books, name='kids'),
]