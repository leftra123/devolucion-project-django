from datetime import datetime
from django.db import models

from . import choices

# import requests

# response = requests.request("GET", "https://mindicador.cl/api/dolar/28-11-2022", headers={}, data={})

# print(response.text)
    
class Cliente(models.Model):
    nombre = models.CharField(unique=True, max_length=100, null=False, verbose_name='Nombre')
    tipo = models.CharField(max_length=100, choices=choices.TIPO_DE_CLIENTE, default='Araucania', verbose_name='Tipo de cliente')
    
    class Meta:
        ordering = ['tipo']
    
    def __str__(self):
        return self.nombre.upper()
    

class Producto(models.Model):
    nombre = models.CharField(unique=True, max_length=100, null=False, verbose_name='Nombre')
    linea = models.CharField(max_length=50, null=False, verbose_name='Linea de producto')
    precio_unitario = models.PositiveIntegerField()
    
    class Meta:
        ordering = ['linea']
        
    def __str__(self):
        return self.nombre.upper()
    
    
class Devolucion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    vendedor = models.CharField(max_length=100, null=False, verbose_name="Vendedor")
    distribuidora = models.CharField(max_length=100, choices=choices.DISTRIBUIDORA, verbose_name="Distribuidora")
    fecha = models.DateField(default=datetime.now, verbose_name='Fecha de creacion')

    class Meta:
        ordering = ['distribuidora']
        
    def __str__(self):
        return self.distribuidora.upper()