from django.conf.urls import url
from django.urls import path
from catalogo import views

urlpatterns=[
	path('', views.catalogo, name='catalogo'),
	path('', views.buscar, name='buscar'),
]