from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from appone import views

app_name = 'appone'

urlpatterns = [
    url(r'^what_i_learned/$',views.what_i_learned.as_view(), name = "what_i_learned"),
    url(r'^cookbook/$',views.cookbook.as_view(), name = "cookbook"),
    url(r'^urlinfo/$',views.urlinfo.as_view(), name = "urlinfo"),
    url(r'^flexboxes/$',views.flexboxes.as_view(), name = "flexboxes"),
    url(r'^javascript/$',views.javascript.as_view(), name = "javascript"),
]
