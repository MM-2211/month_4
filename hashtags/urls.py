from django.urls import path
from . import views

urlpatterns = [
    path('all_hashtags_films/', views.AllCategoryBooksView.as_view(), name='all'),
    path('teen_hashtags_films/', views.TeenagerBooksView.as_view(), name='teen'),
    path('kids_hashtags_films/', views.KidsBooksView.as_view(), name='kids'),
]