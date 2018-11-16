from django.contrib import admin
from catalogo.models import bicicleta, catalogo, equipamiento

@admin.register(bicicleta)
class bicicletaAdmin(admin.ModelAdmin):
	list_display = ('catalogo', 'marca', 'modelo', 'categoria',)

@admin.register(catalogo)
class catalogoAdmin(admin.ModelAdmin):
	list_display = ('tipo',)

@admin.register(equipamiento)
class equipamientoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'precio',)