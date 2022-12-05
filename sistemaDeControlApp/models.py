from django.db import models
from django.contrib.auth.models import User

from . import choices

# import requests

# response = requests.request("GET", "https://mindicador.cl/api/dolar/02-12-2022", headers={}, data={})

# print(response.text)
class Dolar(models.Model):
    valor = models.FloatField()

    def __str__(self):
        return str(self.valor)
    


class Cliente(models.Model):
    nombre = models.CharField(unique=True, max_length=100, null=False, verbose_name='Nombre')
    tipo = models.CharField(max_length=100, choices=choices.TIPO_DE_CLIENTE, default='Araucania', verbose_name='Tipo de cliente')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        ordering = ['tipo']
    
    def __str__(self):
        return self.nombre.upper()
    

class Producto(models.Model):
    nombre = models.CharField(unique=True, max_length=100, null=False, verbose_name='Nombre')
    linea = models.CharField(max_length=50, null=False, verbose_name='Linea de producto')
    precio_unitario = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
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
    fecha = models.DateTimeField(auto_now_add=True)
    #fecha = models.DateField(default=datetime.now, verbose_name='Fecha de creacion')
    monto_devolucion_clp = models.PositiveIntegerField(verbose_name='Monto de devolucion en CLP')
    monto_devolucion_usd = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Monto de devolucion en USD')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    class Meta:
        ordering = ['distribuidora']
        
    def __str__(self):
        return self.distribuidora.upper()