from django.shortcuts import render
from django.http import HttpResponse
from catalogo.models import bicicleta, catalogo
from catalogo.filters import bicicletaFilter, catalogoFilter

# Create your views here.
def buscar(request):
	data = {}
	template_name = 'aa.html'
	bicicletas = bicicleta.objects.all()
	print(request.GET.get("categoria"))
	bicicleta_filtro = bicicletaFilter(request.GET, queryset=bicicletas)
	data['filter'] = bicicleta_filtro
	return render(request, template_name, data)