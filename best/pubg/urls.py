from django.contrib import admin
from django.urls import path
from . import views
# define your paths here
urlpatterns = [
    path('', views.index, name="Home"),
    path('mdview/<int:myid>', views.mdview, name="MatchDetail"),
    path('termsandconditions/', views.tandc, name="Terms"),
    path('mdview/sub', views.joinnow, name="Submit"),
    path('asd/', views.asd, name="profile")
]