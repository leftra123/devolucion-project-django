from django.urls import path
from . import views

urlpatterns = [
    #principal
    path('', views.home, name="home"),
    #registro
    path('crearcuenta/', views.signup, name='crearcuenta'),
    path('registro/', views.registro_creado, name='registro_creado'),
    path('cerrarsesion/', views.signout, name='cerrarsesion'),
    path("iniciarsesion/", views.signin, name="iniciarsesion"),
    #productos
    path('producto/', views.registro_de_producto, name='producto'),
    path('crearproducto/', views.crear_nuevo_producto, name='crearproducto'),
    path('editarproducto/<int:producto_id>', views.editar_producto, name='editarproducto'),
    path('eliminarproducto/<int:producto_id>', views.eliminar_producto, name='eliminarproducto'),
    #cliente
    path('cliente/', views.registro_de_cliente, name='cliente'),
    path('crearcliente/', views.crear_nuevo_cliente, name='crearcliente'),
    # devolucion
    path('devolucion/', views.registro_de_devolucion, name='devolucion'),
    path('creardevolucion/', views.crear_nueva_devolucion, name='creardevolucion'),
    #api
    path('dolar/', views.dolar, name='dolar'),
    

    #path('cliente/', views.cliente, name='cliente'),
    #path('tipo_cliente/', views.tipo_cliente, name='tipo_cliente'),
    # path('registro_de_devoluciones/', views.registro_de_devoluciones, name="registro_de_devoluciones"),
    # path('crear_nueva_devolucion/', views.crear_nueva_devolucion, name="crear_nueva_devolucion"),
    # path('editar_devolucion/<int:id>', views.editar_devolucion, name="editar_devolucion"),
    # path('eliminar_devolucion/<int:id>', views.eliminar_devolucion, name="eliminar_devolucion")
]
