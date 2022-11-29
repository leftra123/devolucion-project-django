from django import forms
from .models import Cliente, Producto, Devolucion


# class DevolucionesForm(forms.ModelForm):
#     class Meta:
#         model = Devoluciones
#         fields = "__all__"
#         widgets = {
#             'nombre_del_cliente': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Ingresa el nombre del cliente"},),
#             'cantidad_devuelta': forms.NumberInput(attrs={'class': 'form-control',"placeholder":"Ingresa la cantidad devuelta", 'min':1},),
#             'vendedor': forms.Select(attrs={'class': 'form-control'},
#              choices=[
#                 ('vendedor uno', 'vendedor uno'),
#                 ('vendedor dos', 'vendedor dos'),
#                 ('vendedor tres', 'vendedor tres'),
#                 ('vendedor cuatro', 'vendedor cuatro'),
#                 ('vendedor cinco', 'vendedor cinco'),
#                 ('vendedor seis', 'vendedor seis'),
#                 ('vendedor siete', 'vendedor siete'),
#                 ('vendedor ocho', 'vendedor ocho'),
#             ]
#             ),
#             'distribuidor_a_cargo': forms.Select(attrs={'class': 'form-control'},
#              choices=[
#                 ('distribuidor uno', 'distribuidor uno'),
#                 ('distribuidor dos', 'distribuidor dos'),
#                 ('distribuidor tres', 'distribuidor tres'),
#                 ('distribuidor cuatro', 'distribuidor cuatro'),
#                 ('distribuidor cinco', 'distribuidor cinco'),
#              ]),
#             'producto_devuelto': forms.TextInput(attrs={'class': 'form-control', "placeholder":"Ingresa el nombre del producto"},),
#             'fecha_de_creacion': forms.DateInput(attrs={'class': 'form-control', "placeholder":"Ingresa la fecha de creacion", 'type':'date'},),
#         }
