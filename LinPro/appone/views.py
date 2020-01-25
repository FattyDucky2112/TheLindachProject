from django.shortcuts import render
from django.views.generic import View,TemplateView
from appone.models import Ingredient, Recipes
from appone.forms import IngredientForm, RecipesForm


class IndexView(TemplateView):
    template_name = "index.html"

class what_i_learned(TemplateView):
    template_name = "what_i_learned.html"

class urlinfo(TemplateView):
    template_name = "urlinfo.html"

class cookbook(TemplateView):
    template_name = "cookbook.html"

class flexboxes(TemplateView):
    template_name = "flexboxes.html"

class javascript(TemplateView):
    template_name = "javascript.html"
