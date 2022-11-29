from django.contrib import admin
from .models import Devolucion, Cliente, Producto

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Devolucion)