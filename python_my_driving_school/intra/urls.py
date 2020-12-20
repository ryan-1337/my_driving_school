from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('edit_profil/', views.editProfil, name="edit_profil"),
    path('setrdv/', views.setRdv, name="setrdv"),
    path('updaterdv/<str:pk>/', views.updateRdv, name="updaterdv"),
    path('delete/<str:pk>/', views.deleteRdv, name="delete"),
]

