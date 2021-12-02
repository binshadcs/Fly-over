from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('userLogin', views.user_login, name="user_login"),
    path('userLogout', views.logout, name="user_logout"),

]