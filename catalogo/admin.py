from django.contrib import admin
from catalogo.models import bicicleta

@admin.register(bicicleta)
class bicicletaAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'marca', 'modelo', 'categoria', 'stock',)
