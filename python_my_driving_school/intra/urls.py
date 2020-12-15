from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
]

