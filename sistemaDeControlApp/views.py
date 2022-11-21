from django.shortcuts import redirect, render

from .forms import DevolucionesForm
from .models import Devoluciones


# base
def base(request):
    return render(request, "layouts/base.html")

#inicio
def home(request):
    return render(request, "home/home.html")


#registro de devoluciones
def registro_de_devoluciones(request):
    print("devoluciones")
    return render(request, "devoluciones/registro_de_devoluciones.html", {
        "devoluciones": Devoluciones.objects.all()
    })


#crerar nueva devolucion
def crear_nueva_devolucion(request):
    if request.method == 'POST':
        form = DevolucionesForm(request.POST)
        if form.is_valid():
            form.save()
            # mostrar resultado en la consola
            print(form.cleaned_data)
        return redirect("registro_de_devoluciones")
    else: 
        form = DevolucionesForm()
    return render(request, "devoluciones/crear_nueva_devolucion.html", {
        "form": form
    })


# editar devolucion
def editar_devolucion(request, id):
    devoluciones = Devoluciones.objects.get(id=id)
    if request.method == 'GET':
        form = DevolucionesForm(instance=devoluciones)
    else:
        form = DevolucionesForm(request.POST, instance=devoluciones)
        if form.is_valid():
            form.save()
        return redirect('registro_de_devoluciones')
    return render(request, 'devoluciones/editar_devolucion.html', {
        'form': form,
        'id': id
    })


# eliminar devolucion
def eliminar_devolucion(request, id):
    devoluciones = Devoluciones.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'devoluciones/eliminar_devolucion.html', {
            'devolucion': devoluciones,
            'id': id})
    else:
        devoluciones.delete()
        return redirect('registro_de_devoluciones')