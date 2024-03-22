from os import name
from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.query_view, name = 'query'),
]