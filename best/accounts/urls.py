from django.urls import path
from . import views


urlpatterns = [

    # path('', views.account, name="Register"),
    path('register', views.register, name="Register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="Logout"),
    path('asd/<str:user>', views.aj, name="aj"),
    path('asd/aj', views.aj, name="aj")
]