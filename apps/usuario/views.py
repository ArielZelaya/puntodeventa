from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import time, date
import datetime
from .models import *

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required


# Create your views here.
def iniciarSesion(request):
    form=AuthenticationForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try: #se trata de verificar el usuario si existe
            user = User.objects.get(username=username)
        except: #Sino existe se pasaa la escepcion
            valor = "Ingrese un usuario valido"
            context = {"form": form, 'valor': valor}
            return render(request, 'usuario/login.html', context)
        # user = authenticate(username=username, password=password)
        if user.check_password(password) :
            login(request,user)
            if request.GET.get('next') is None:
                return redirect('index')
            else:
                return HttpResponseRedirect(request.GET.get('next'))
        else:
            valor = "Contraseña incorrecta"
            print(user)
            context={"form":form,'valor':valor}
            return render(request,'usuario/login.html',context)
    if request.user.is_active:
        return redirect('/')
    valor =""
    context={"form":form,'valor':valor}
    return render(request,'usuario/login.html',context)

def cerrarSesion(request):
    logout(request)
    return redirect('usuario:login')

@login_required(login_url='/usuario/login')
def gestionEmpleado(request):
    usuario = User.objects.get(id=request.user.id)
    if usuario.is_superuser:

        ListaEmpleados = Empleado.objects.all()
        if request.method == 'POST':
            first_name = request.POST.get('Nombres')
            last_name = request.POST.get('Apellidos')
            dui = request.POST.get('Dui')
            username = request.POST.get('username')
            domicilio = request.POST.get('Domicilio')
            telefono = request.POST.get('Telefono')
            nit = request.POST.get('Nit')
            isss = request.POST.get('Isss')
            email = request.POST.get('email')
            password = request.POST.get('password')
            nup=request.POST.get('Nup')
            empleado = Empleado.objects.create_user(
                username=username,
                email=email,
                password=password,
                dui=dui,
                first_name=first_name,
                last_name=last_name,
                domicilio=domicilio,
                telefono=telefono,
                nit=nit,
                isss=isss,
                nup=nup
                )

            return redirect('usuario:ges_emp')
        return render(request, 'usuario/gest_empleado.html', {'ListaEmpleados': ListaEmpleados})
    else:
        return render(request, 'base/base.html')

def DetallesEmpleado(request,idEmpleado):
    empleado=Empleado.objects.get(id=idEmpleado)
    editar=False
    return render(request, 'usuario/editar_empleado.html', {'empleado': empleado,'editar':editar})

def EditarEmpleado(request,idEmpleado):
    empleado = Empleado.objects.get(id=idEmpleado)
    editar = True
    if request.method=='POST':
        empleado.first_name = request.POST.get('Nombres')
        empleado.last_name = request.POST.get('Apellidos')
        empleado.dui = request.POST.get('Dui')
        empleado.codigo = request.POST.get('Codigo')
        empleado.domicilio = request.POST.get('Domicilio')
        empleado.telefono = request.POST.get('Telefono')
        empleado.nit = request.POST.get('Nit')
        empleado.isss = request.POST.get('Isss')
        empleado.email = request.POST.get('email')
        empleado.nup = request.POST.get('Nup')
        empleado.save()
        return redirect('usuario:ges_emp')
    return render(request,'usuario/editar_empleado.html',{'empleado':empleado,'editar':editar})

def EliminarEmpleado(request,idEmpleado):
    empleado = Empleado.objects.get(id=idEmpleado)
    if request.method=='POST':
        empleado.delete()
        return redirect('usuario:ges_emp')
    return render(request, 'usuario/eliminar_empleado.html', {'empleado': empleado})

@login_required(login_url='/usuario/login')
def gestionProducto(request):
    usuario = User.objects.get(id=request.user.id)
    ListaClientes=Cliente.objects.all()
    if usuario.is_superuser:
        if request.method=='POST':
            first_name = request.POST.get('Nombres')
            tipo= rquest.POST.get('Tipo')
            last_name = request.POST.get('Apellidos')
            dui = request.POST.get('Dui')
            username = request.POST.get('username')
            direccion = request.POST.get('direccion')
            telefono = request.POST.get('Telefono')
            email = request.POST.get('email')
            password = request.POST.get('password')
            cliente = Cliente.objects.create_user(
                username=username,
                tipo=tipo,
                email=email,
                password=password,
                dui=dui,
                first_name=first_name,
                last_name=last_name,
                domicilio=domicilio,
                telefono=telefono,
                )
        return render(request, 'cliente/ges_cliente.html', {'ListaClientes': ListaClientes})
    else:
        return render(request, 'base/base.html')
@login_required(login_url='/usuario/login')
def gestionCliente(request):
    usuario = User.objects.get(id=request.user.id)
    if usuario.is_superuser:

        ListaClientes = Cliente.objects.all()
        if request.method == 'POST':
            first_name = request.POST.get('Nombres')
            last_name = request.POST.get('Apellidos')
            dui = request.POST.get('Dui')
            direccion = request.POST.get('Direccion')
            telefono = request.POST.get('Telefono')
            tipo= request.POST.get('Tipo')
            cliente = Cliente.objects.create_user(
                username=first_name,
                email=first_name,
                password=last_name,
                dui=dui,
                first_name=first_name,
                last_name=last_name,
                direccion=direccion,
                telefono=telefono,
                tipo=tipo
                )

            return redirect('usuario:ges_cli')
        return render(request, 'usuario/gest_cliente.html', {'ListaClientes': ListaClientes})
    else:
        return render(request, 'base/base.html')

def EditarCliente(request,idCliente):
    cliente = Cliente.objects.get(id=idCliente)
    editar = True
    if request.method=='POST':
        cliente.first_name = request.POST.get('Nombres')
        cliente.last_name = request.POST.get('Apellidos')
        cliente.dui = request.POST.get('Dui')
        cliente.domicilio = request.POST.get('Direccion')
        cliente.telefono = request.POST.get('Telefono')
        cliente.tipo = request.POST.get('Tipo')
        cliente.username = request.POST.get('Nombres')
        cliente.password = request.POST.get('Apellidos')
        cliente.email = request.POST.get('Nombres')
        cliente.save()
        return redirect('usuario:ges_cli')
    return render(request,'usuario/editar_cliente.html',{'cliente':cliente,'editar':editar})

def DetallesCliente(request,idCliente):
    cliente=Cliente.objects.get(id=idCliente)
    editar=False
    return render(request, 'usuario/editar_cliente.html', {'cliente': cliente,'editar':editar})

def EliminarCliente(request,idCliente):
    cliente = Cliente.objects.get(id=idCliente)
    if request.method=='POST':
        cliente.delete()
        return redirect('usuario:ges_cli')
    return render(request, 'usuario/eliminar_cliente.html', {'cliente': cliente})
