from django.shortcuts import redirect, render

# from .forms import DevolucionesForm
# from .models import Devoluciones

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def home(request):
    return render(request, "index.html")


def signup(request):
    if request.method == 'GET':
        return render(request, 'auth/signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #registrar usuario
                user = User.objects.create_user(
                    username=request.POST['username'], 
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                #este redirect hay que modificarlo
                return redirect('home')
            except IntegrityError:
                return render(request, 'auth/signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'auth/signup.html', {
            'form': UserCreationForm,
            'error': 'Contraseñas no coinciden'
        })
            

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
            password = request.POST['password'])
        if user is None:
            return render(request, 'auth/signin.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o contraseña es incorrecto'
            })
        else:
            login(request, user)
            #este redirect hay que modificarlo
            return redirect('home')


# # registro de devoluciones
# def registro_de_devoluciones(request):
#     print("devoluciones")
#     return render(request, "devoluciones/registro_de_devoluciones.html", {
#         "devoluciones": Devoluciones.objects.all()
#     })


# # crerar nueva devolucion
# def crear_nueva_devolucion(request):
#     if request.method == 'POST':
#         form = DevolucionesForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # mostrar resultado en la consola
#             print(form.cleaned_data)
#         return redirect("registro_de_devoluciones")
#     else:
#         form = DevolucionesForm()
#     return render(request, "devoluciones/crear_nueva_devolucion.html", {
#         "form": form
#     })


# # editar devolucion
# def editar_devolucion(request, id):
#     devoluciones = Devoluciones.objects.get(id=id)
#     if request.method == 'GET':
#         form = DevolucionesForm(instance=devoluciones)
#     else:
#         form = DevolucionesForm(request.POST, instance=devoluciones)
#         if form.is_valid():
#             form.save()
#         return redirect('registro_de_devoluciones')
#     return render(request, 'devoluciones/editar_devolucion.html', {
#         'form': form,
#         'id': id
#     })


# # eliminar devolucion
# def eliminar_devolucion(request, id):
#     devoluciones = Devoluciones.objects.get(id=id)
#     if request.method == 'GET':
#         return render(request, 'devoluciones/eliminar_devolucion.html', {
#             'devolucion': devoluciones,
#             'id': id})
#     else:
#         devoluciones.delete()
#         return redirect('registro_de_devoluciones')
