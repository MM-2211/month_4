from django.urls import path
from . import views

urlpatterns = [
    path('create_basket/', views.CreateBasket.as_view(), name='create_basket'),
    path('basket_list/', views.BasketListView.as_view(), name='basket_list'),
    path('basket_list/<int:id>/', views.BasketDetailView.as_view(), name='basket_detail'),
    path('basket_list/<int:id>/update/', views.BasketUpdateView.as_view(), name='basket_update'),
    path('basket_list/<int:id>/delete/', views.BasketDeleteView.as_view(), name='basket_delete'),
    path('search_basket/', views.SearchBasketView.as_view(), name='search_basket'),
]