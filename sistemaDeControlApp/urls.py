from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base, name="base"),
    path('', views.home, name="home"),
    path('registro_de_devoluciones/', views.registro_de_devoluciones, name="registro_de_devoluciones"),
    path('crear_nueva_devolucion/', views.crear_nueva_devolucion, name="crear_nueva_devolucion"),
    path('editar_devolucion/<int:id>', views.editar_devolucion, name="editar_devolucion"),
    path('eliminar_devolucion/<int:id>', views.eliminar_devolucion, name="eliminar_devolucion"),
]