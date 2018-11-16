from catalogo.models import catalogo, bicicleta
import django_filters

class bicicletaFilter(django_filters.FilterSet):
	class Meta:
		model = bicicleta
		fields = ['categoria', 'aro',]

class catalogoFilter(django_filters.FilterSet):
	class Meta:
		model = catalogo
		fields = ['tipo',]