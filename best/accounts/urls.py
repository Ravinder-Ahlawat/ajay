from django.urls import path
from . import views


urlpatterns = [

    # path('', views.account, name="Register"),
    path('register', views.register, name="Register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="Logout"),
    path('aj/', views.aj, name="aj")
]