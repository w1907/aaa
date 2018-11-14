from django.db import models
from catalogo.defines import CATEGORIA_BICI_CHOICES

class bicicleta(models.Model):
	codigo = models.IntegerField()
	marca = models.CharField(max_length=45, blank=True)
	modelo = models.CharField(max_length=45, blank=True)
	categoria = models.CharField(max_length=45, choices=CATEGORIA_BICI_CHOICES)
	imagen = models.ImageField(upload_to='imagenes_bicicletas')
	aro = models.IntegerField()
	talla = models.FloatField()
	color = models.CharField(max_length=45, blank=True)
	stock = models.IntegerField()
	precio = models.IntegerField()

class catalogo(models.Model):
	codigo = models.IntegerField()
	bicicleta = models.ForeignKey(bicicleta, null=True, blank=True, on_delete=models.CASCADE)