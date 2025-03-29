from django import forms
from . import models

class RecipeForm(forms.ModelForm):
    class Meta:
        model = models.Recipe
        fields = ['title', 'description']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = models.Ingredient
        fields = ['name', 'quantity', 'recipe']
