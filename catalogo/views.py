from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from catalogo.models import bicicleta, catalogo
from catalogo.filters import bicicletaFilter, catalogoFilter

# Create your views here.

def catalogo(request):
	data = {}
	template_name = 'catalogo.html'
	bicicleta_filtro = bicicletaFilter(request.GET or None)
	catalogo_filtro = catalogoFilter(request.GET or None)
	data['filter'] = bicicleta_filtro
	data['filter2'] = catalogo_filtro
	return render(request, template_name, data)

def buscar(request):
	data = {}
	template_name = 'catalogo.html'
	bicicletas = bicicleta.objects.all()
	print(request.GET)
	print(request.GET.get("categoria"))
	bicicleta_filtro = bicicletaFilter(request.GET or None)
	return render(request, template_name, data)