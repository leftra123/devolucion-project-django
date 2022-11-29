from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('crearcuenta/', views.signup, name='crearcuenta'),
    path('cerrarsesion/', views.signout, name='cerrarsesion'),
    path("iniciarsesion/", views.signin, name="iniciarsesion"),
    # path('registro_de_devoluciones/', views.registro_de_devoluciones, name="registro_de_devoluciones"),
    # path('crear_nueva_devolucion/', views.crear_nueva_devolucion, name="crear_nueva_devolucion"),
    # path('editar_devolucion/<int:id>', views.editar_devolucion, name="editar_devolucion"),
    # path('eliminar_devolucion/<int:id>', views.eliminar_devolucion, name="eliminar_devolucion")
]