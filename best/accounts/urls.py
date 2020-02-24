from django.urls import path
from . import views


urlpatterns = [

    path('', views.account, name="Register"),
    path('register', views.register, name="Account"),
    path('login', views.login, name="Login")
]