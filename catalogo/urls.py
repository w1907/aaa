from django.conf.urls import url
from django.urls import path
from catalogo import views

urlpatterns=[
	url('', views.buscar, name="catalogo1"),
]