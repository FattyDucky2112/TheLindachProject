from django.shortcuts import render
from django.views.generic import View,TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class what_i_learned(TemplateView):
    template_name = "what_i_learned.html"

class urlinfo(TemplateView):
    template_name = "urlinfo.html"
