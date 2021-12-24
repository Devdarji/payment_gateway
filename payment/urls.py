from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import home, success

urlpatterns = [
    path('', home, name="home"),
    path('success', success, name="success"),
]
