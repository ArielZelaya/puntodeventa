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
# Create your views here.
@login_required(login_url='/usuario/login')
def gestionInventario(request):
    usuario = User.objects.get(id=request.user.id)
    ListaMercancias=Mercancia.objects.all()
    productos = Producto.objects.all()
    if usuario.is_superuser:
        if request.method=='POST':
            mercancia = Mercancia()
            mercancia.Producto =Producto.objects.get(id=request.POST.get('Producto'))
            id = Producto.objects.get(id= mercancia.Producto.id)
            mercancia.id =id.id
            mercancia.cantidad =request.POST.get('Cantidad')
            mercancia.save()
        return render(request, 'inventario/gest_inventario.html', {'ListaMercancias': ListaMercancias,'productos':productos})
    else:
        return render(request, 'base/base.html')
    return render(request, 'inventario/gest_inventario.html', {'ListaMercancias': ListaMercancias,'productos':productos})

def actualizar(id,cantidad):
	mercancia=Mercancia.objects.get(id=id)
	mercancia.cantidad= mercancia.cantidad - cantidad
	mercancia.save()

def EditarInventario(request,idMercancia):
    mercancia = Mercancia.objects.get(id=idMercancia)
    editar = True
    if request.method=='POST':
        mercancia = Mercancia()
        mercancia.Producto =Producto.objects.get(id=request.POST.get('Producto'))
        id = Producto.objects.get(id= mercancia.Producto.id)
        mercancia.id =id.id
        mercancia.cantidad =request.POST.get('Cantidad')
        mercancia.save()
        return redirect('inventario:ges_inv')

    	
    return render(request, 'inventario/editar_inventario.html', {'mercancia': mercancia,'editar':editar})

def EliminarMercancia(request,idMercancia):
    mercancia = Mercancia.objects.get(id=idMercancia)
    if request.method=='POST':
        mercancia.delete()
        return redirect('inventario:ges_inv')
    return render(request, 'inventario/eliminar_inventario.html', {'mercancia': mercancia})
