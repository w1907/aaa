from django.contrib import admin
from catalogo.models import bicicleta, catalogo, equipamiento

@admin.register(bicicleta)
class bicicletaAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'marca', 'modelo', 'categoria', 'stock',)

@admin.register(catalogo)
class catalogoAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'categorias',)

@admin.register(equipamiento)
class catalogoAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'nombre', 'precio',)