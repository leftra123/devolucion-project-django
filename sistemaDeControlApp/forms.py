from django import forms
from .models import Cliente, Producto, Devolucion
from . import choices


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Ingresa el nombre del cliente"},),
            'tipo': forms.Select(attrs={'class': 'form-control'}, choices=choices.TIPO_DE_CLIENTE),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
        widgets = {
            'nombre': forms.Select(attrs={'class': 'form-control'}, choices=choices.NOMBRE_DE_PRODUCTO),
            'linea': forms.Select(attrs={'class': 'form-control'}, choices=choices.LINEA_DE_PRODUCTO),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Ingresa el precio unitario del producto", 'min': 1},),
        }


class DevolucionForm(forms.ModelForm):
    class Meta:
        model = Devolucion
        fields = "__all__"
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}, choices=choices.TIPO_DE_CLIENTE),
            'producto': forms.Select(attrs={'class': 'form-control'}, choices=choices.LINEA_DE_PRODUCTO),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Ingresa la cantidad devuelta", 'min': 1},),
            'vendedor': forms.Select(attrs={'class': 'form-control'}, choices=choices.VENDEDOR),
            'distribuidor': forms.SelectMultiple(attrs={'class': 'form-control'}, choices=choices.DISTRIBUIDORA),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'},),
            'monto_devolucion_clp': forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Ingresa el monto de devolucion en CLP", 'min': 1},),
            'monto_devolucion_usd': forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Ingresa el monto de devolucion en USD", 'min': 1},),
        }
