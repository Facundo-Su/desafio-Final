from django.http import HttpResponse
from django.shortcuts import render
from appFinal.forms import ProductosFormulario
from appFinal.models import Productos

# Create your views here.

def inicio(request):
    return render(request,"plantilla.html")

def productos(request):
    return render(request,"productos.html")

def alta_productos(request, nombre,precio):
    producto = Productos(nombre=nombre , precio=precio)
    producto.save()
    texto = f"Se guardo en la BD el Producto: {producto.nombre} Camada: {producto.camada}"
    return HttpResponse(texto)


def producto_formulario(request):
    
    if request.method == "POST":

        mi_formulario = ProductosFormulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            producto = Productos( nombre=datos['nombre'] , precio=datos['precio'])
            producto.save()
            return render( request , "productos.html")

    return render( request, "productos.html")


def buscar_productos(request):
    
    return render( request , "buscarProductos.html")


def buscar(request):
    
    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        productos = Productos.objects.filter(nombre__icontains = nombre)
        return render( request , "resultadoBusquedasProductos.html" , {"productos": productos})
    else:
        return HttpResponse("Campo vacio")
   