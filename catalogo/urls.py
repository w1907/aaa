from django.urls import path
from catalogo import views

urlpatterns=[
	path('catalogo', views.catalogo, name="catalogo"),
]