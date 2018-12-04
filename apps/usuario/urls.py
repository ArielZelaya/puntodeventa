from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url, include
from .views import *
from . import views

app_name = 'usuario'

urlpatterns =[

    url(r'^gestionEmpleado$', gestionEmpleado, name="ges_emp"),
    url(r'^EditarEmpleado/(?P<idEmpleado>\d+)/$', EditarEmpleado, name="edi_emp"),
    url(r'^DetallesEmpleado/(?P<idEmpleado>\d+)/$', DetallesEmpleado, name="det_emp"),
    url(r'^EliminarEmpleado/(?P<idEmpleado>\d+)/$', EliminarEmpleado, name="eli_emp"),
    url(r'^gestionCliente$', gestionCliente, name="ges_cli"),
    url(r'^EditarCliente/(?P<idCliente>\d+)/$', EditarCliente, name="edi_cli"),
    url(r'^DetallesCliente/(?P<idCliente>\d+)/$', DetallesCliente, name="det_cli"),
    url(r'^EliminarCliente/(?P<idCliente>\d+)/$', EliminarCliente, name="eli_cli"),
    url(r'^logout$', cerrarSesion, name="logout"),
    url(r'^login$', iniciarSesion, name="login")
]