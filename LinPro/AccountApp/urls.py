from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from accountapp import views

app_name = "accountapp"

urlpatterns =  [
    url(r'^register/$',views.register, name = "register"),
    path('accounts/', include('django.contrib.auth.urls')),
]
