from django import forms
from appone.models import Ingredient, Recipes

class IngredientForm(forms.ModelForm):
    class Meta():
        model = Ingredient
        fields = ('name','cathegory')

class RecipesForm(forms.ModelForm):
    class Meta():
        model = Recipes
        fields = ('name','ingredients')
