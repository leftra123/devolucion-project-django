from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# form y models
from . models import Producto, Cliente, Devolucion, User, Dolar
from . forms import ProductoForm, ClienteForm, DevolucionForm
# para api
import requests

'''
 consultar dolar
'''
@login_required
def dolar(request):
    #fecha = datetime.date.today()
    response = requests.request("GET", "https://mindicador.cl/api/dolar", headers={}, data={})
    valor = response.json().get('serie')[0].get('valor')
    dolar = Dolar(valor=valor)
    dolar.save()
    return render(request, "API/consulta_api.html", {
        "dolar": dolar
    })


'''
vista principal
'''


def home(request):
    return render(request, "index.html")


'''
crear un nuevo usuario y:
- redireccionar a la pagina de registro_creado
- si el usuario ya existe, avisar el error
- si las contraseñas no coinciden, avisar el error
- si el usuario no existe, crearlo y redireccionar a la pagina de registro_creado
'''


def signup(request):
    if request.method == 'GET':
        return render(request, 'auth/signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # registrar usuario
                user = User.objects.create_user(
                    # 
                    username=request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                # este redirect hay que modificarlo
                return redirect('registro_creado')
            except IntegrityError:
                return render(request, 'auth/signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'auth/signup.html', {
            'form': UserCreationForm,
            'error': 'Contraseñas no coinciden'
        })

@login_required
def registro_creado(request):
    return render(request, 'registro/registro_creado.html')


@ login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'auth/signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password'])
        if user is None:
            return render(request, 'auth/signin.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o contraseña es incorrecto'
            })
        else:
            login(request, user)
            # este redirect hay que modificarlo
            return redirect('home')


''' fin de vistas de autenticacion'''
#
#
'''
Cliente
atrr:
- nombre
- tipo de cliente
el cliente lo puede agregar solo el administrador del sistema
'''
# registro de cliente
@login_required
def registro_de_cliente(request):
    cliente = Cliente.objects.filter(user=request.user)
    return render(request, "cliente/registro_de_cliente.html", {
        "cliente": cliente
    })


@login_required
def crear_nuevo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            # mostrar resultado en la consola
            print(form.cleaned_data)
            return redirect('cliente')
    else:
        form = ClienteForm()
    return render(request, "cliente/crear_nuevo_cliente.html", {
        "form": form
    })


'''
producto
- agregar producto
- ir al registro del producto
'''
# registro de producto
@login_required
def registro_de_producto(request):
    producto = Producto.objects.filter(user=request.user)
    return render(request, "producto/registro_de_producto.html", {
        "producto": producto
    })


@ login_required
def crear_nuevo_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto')
    else:
        form = ProductoForm()
    return render(request, "producto/crear_nuevo_producto.html", {
        "form": form
    })


# editar producto
def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('registro_de_producto')
    return render(request, 'producto/editar_producto.html', {
        'form': form,
        'id': id
    })


# eliminar producto
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'producto/eliminar_producto.html', {
            'producto': Producto,
            'id': id})
    else:
        producto.delete()
        return redirect('registro_de_producto')


'''
devolucion
'''

# registro de devolucion

@login_required
def registro_de_devolucion(request):
    dolar = Dolar.objects.all()
    devolucion = Devolucion.objects.filter(user=request.user)
    return render(request, "devolucion/registro_de_devolucion.html", {
        "devolucion": devolucion,
        "dolar": dolar
    })


# crear nueva devolucion
@login_required
def crear_nueva_devolucion(request):
    if request.method == 'POST':
        form = DevolucionForm(request.POST)
        if form.is_valid():
            form.save()
            # mostrar resultado en la consola
            print(form.cleaned_data)
            return redirect('devolucion')
    else:
        form = DevolucionForm()
    return render(request, "devolucion/crear_nueva_devolucion.html", {
        "form": form
    })


