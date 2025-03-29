from django.urls import path
from . import views

urlpatterns = [
    path('recipe_list/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipe_list/<int:id>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('create_recipe/', views.RecipeCreateView.as_view(), name='create_recipe'),
    path('delete_recipe/<int:id>/', views.RecipeDeleteView.as_view(), name='delete_recipe'),
    path('create_ingredient/<int:recipe_id>/', views.IngredientCreateView.as_view(), name='create_ingredient'),
]
