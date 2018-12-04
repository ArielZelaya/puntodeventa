from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import time, date
import datetime
from .models import *

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required

@login_required(login_url='/usuario/login')
def gestionProducto(request):
    usuario = User.objects.get(id=request.user.id)
    ListaProductos=Producto.objects.all()
    tipos = Tipo.objects.all()
    if usuario.is_superuser:
        if request.method=='POST':
            producto = Producto()
            producto.tipo = Tipo.objects.get(id=request.POST.get('Tipo'))
            producto.nombre = request.POST.get('Nombre')
            producto.marca = request.POST.get('Marca')
            producto.precio = request.POST.get('Precio')
            producto.codigo = request.POST.get('Codigo')
            producto.descripcion = request.POST.get('Descripcion')
            producto.save()
        return render(request, 'producto/gest_producto.html', {'ListaProductos': ListaProductos,'tipos':tipos})
    else:
        return render(request, 'base/base.html')
    return render(request, 'producto/gest_producto.html', {'ListaProductos': ListaProductos,'tipos':tipos})

def DetallesProducto(request,idProducto):
    producto=Producto.objects.get(id=idProducto)
    tipo = Tipo.objects.get(id=producto.tipo.id)
    editar=False
    return render(request, 'producto/editar_producto.html', {'producto': producto,'tipo':tipo,'editar':editar})

def EditarProducto(request,idProducto):
    producto = Producto.objects.get(id=idProducto)
    tipos = Tipo.objects.all()
    editar = True
    if request.method=='POST':
        producto.tipo = Tipo.objects.get(id=request.POST.get('Tipo'))
        producto.nombre = request.POST.get('Nombre')
        producto.marca = request.POST.get('Marca')
        producto.precio = request.POST.get('Precio')
        producto.codigo = request.POST.get('Codigo')
        producto.descripcion = request.POST.get('Descripcion')
        producto.save()
        return redirect('producto:ges_pro')
    return render(request,'producto/editar_producto.html',{'producto':producto,'tipos':tipos,'editar':editar})

def EliminarProducto(request,idProducto):
    producto = Producto.objects.get(id=idProducto)
    if request.method=='POST':
        producto.delete()
        return redirect('producto:ges_pro')
    return render(request, 'producto/eliminar_producto.html', {'producto': producto})