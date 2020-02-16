from django.contrib import admin
from django.urls import path
from . import views
# define your paths here
urlpatterns = [
    path('', views.index, name="Home")
]