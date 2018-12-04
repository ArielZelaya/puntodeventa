from .models import *
from django.shortcuts import render
from django.http import HttpResponse
from apps.producto.models import Categoria
from apps.producto.models import Tipo

from django.contrib.auth.decorators import login_required
from django.core import serializers
import json
import datetime



# Create your views here.

def obtener_producto(request, codigo):
    producto = Producto.objects.filter(codigo=codigo)
    qs_json = serializers.serialize('json', producto)
    return HttpResponse(qs_json)

def guardar_factura(request):
    arreglo_json = request.POST.get('registros', '')
    total = request.POST.get('total','')
    idCliente = request.POST.get('idCliente', '')

    lineas = json.loads(arreglo_json)

    venta = Venta()
    venta.cliente = Cliente.objects.get(id=idCliente)
    venta.fecha = datetime.date.today()
    venta.total = total
    venta.save()

    for elemento in lineas:
        linea = Linea()
        linea.venta = venta
        linea.producto = Producto.objects.get(nombre=elemento['producto'])
        linea.cantidad = elemento['cantidad']
        linea.subtotal = elemento['subtotal']
        linea.save()

    return HttpResponse()




def facturar(request):
    clientes = Cliente.objects.all()
    return render(request, 'venta/facturar.html', {'clientes': clientes})


def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'venta/listado_ventas.html', {'ventas' : ventas})

@login_required
def crear_cliente(request):
    if request.method == 'POST':
        first_name = request.POST.get('Nombres')
        last_name = request.POST.get('Apellidos')
        username = request.POST.get('username')
        dui = request.POST.get('Dui')
        telefono = request.POST.get('Telefono')
        direccion = request.POST.get('Direccion')
        tipo = request.POST.get('Tipo')
        email = request.POST.get('email')

        cliente = Cliente.objects.create_user(
            username=username,
            email=email,
            dui=dui,
            first_name=first_name,
            last_name=last_name,
            direccion=direccion,
            telefono=telefono,
            tipo=tipo
        )
    return HttpResponse()

