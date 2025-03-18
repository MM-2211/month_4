from django.urls import path
from . import views

urlpatterns = [
    path('create_basket/', views.create_basket, name='create_basket'),
    path('basket_list/', views.basket_list, name='basket_list'),
    path('basket_list/<int:id>/', views.basket_detail, name='basket_detail'),
    path('basket_list/<int:id>/update/', views.basket_update, name='basket_update'),
    path('basket_list/<int:id>/delete/', views.basket_delete, name='basket_delete'),
]