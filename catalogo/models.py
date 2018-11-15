from django.db import models
from catalogo.defines import CATEGORIA_BICI_CHOICES, CATEGORIA_CATALOGO_CHOICES

class catalogo(models.Model):
	codigo = models.CharField(max_length=45, blank=False)
	categorias = models.CharField(max_length=45, blank=False, choices=CATEGORIA_CATALOGO_CHOICES)

	def __str__(self):
		return self.categorias

class bicicleta(models.Model):
	codigo = models.CharField(max_length=45, blank=False)
	catalogo = models.ForeignKey(catalogo, null=True, on_delete=models.CASCADE)
	marca = models.CharField(max_length=45, blank=False)
	modelo = models.CharField(max_length=45, blank=False)
	categoria = models.CharField(max_length=45, blank=False, choices=CATEGORIA_BICI_CHOICES)
	imagen = models.ImageField(upload_to='imagenes_bicicletas', blank=True)
	aro = models.FloatField()
	talla = models.FloatField()
	color = models.CharField(max_length=45, blank=False)
	stock = models.IntegerField()
	precio = models.IntegerField()

	def __str__(self):
		return self.modelo

class equipamiento(models.Model):
	codigo = models.CharField(max_length=45, blank=False)
	nombre = models.CharField(max_length=45, blank=False)
	precio = models.IntegerField()
	catalogo = models.ForeignKey(catalogo, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre