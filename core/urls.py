from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name = "login"),
    path('index/', views.index, name = "index"),
    path('register/', views.register, name = "register"),
    path('catalogo/', views.catalogo, name = "catalogo"),
    path('reserva/', views.reserva, name = "reserva"),
]