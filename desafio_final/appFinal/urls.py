from django.urls import path
from . import views

urlpatterns = [
    path("",views.inicio),
    path("productos",views.productos,name="productos"),
    path("alta_productos" , views.producto_formulario),
    path("buscarProductos", views.buscar_productos),
    path("buscar",views.buscar)
]
