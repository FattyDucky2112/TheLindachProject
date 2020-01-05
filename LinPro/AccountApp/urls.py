from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from accountapp import views

app_name = "accountapp"

urlpatterns =  [
    url(r'^login/$',views.register, name = "register"),

]
