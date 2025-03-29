from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from . import models
from . import forms

class RecipeListView(generic.ListView):
    model = models.Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return models.Recipe.objects.all().order_by('-id')

class RecipeDetailView(generic.DetailView):
    model = models.Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'

class RecipeCreateView(generic.CreateView):
    model = models.Recipe
    template_name = 'recipes/create_recipe.html'
    form_class = forms.RecipeForm
    success_url = reverse_lazy('recipe_list')

    def form_valid(self, form):
        return super().form_valid(form)

class RecipeDeleteView(generic.DeleteView):
    model = models.Recipe
    template_name = 'recipes/confirm_delete.html'
    success_url = reverse_lazy('recipe_list')

    def get_object(self, *args, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.Recipe, id=recipe_id)

class IngredientCreateView(generic.CreateView):
    model = models.Ingredient
    template_name = 'recipes/create_ingredient.html'
    form_class = forms.IngredientForm
    success_url = reverse_lazy('recipe_list')

    def form_valid(self, form):
        form.instance.recipe = get_object_or_404(models.Recipe, id=self.kwargs['recipe_id'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = get_object_or_404(models.Recipe, id=self.kwargs['recipe_id'])
        return context
