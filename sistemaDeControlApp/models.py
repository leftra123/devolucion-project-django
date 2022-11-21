from datetime import datetime
from django.db import models


class Devoluciones(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre_del_cliente = models.CharField(max_length=50, null=False, verbose_name='Cliente')
    cantidad_devuelta = models.IntegerField(null=False, verbose_name='Cantidad')
    vendedor = models.CharField(max_length=50, null=False, verbose_name='Vendedor')
    distribuidor_a_cargo = models.CharField(null=False, max_length=50, verbose_name='Distribuidor')
    producto_devuelto = models.CharField(null=False, max_length=50, verbose_name='Producto')
    fecha_de_creacion = models.DateField(default=datetime.now, verbose_name='Fecha de creacion')

    def __str__(self):
        return self.nombre_del_cliente + ' - ' + str(self.producto_devuelto)
