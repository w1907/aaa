from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def catalogo(request):
	data = {}
	template_name = 'catalogo.html'
	return render(request, template_name, data)