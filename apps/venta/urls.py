from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url, include
from .views import *

app_name = 'venta'

urlpatterns =[

    url(r'^facturar$', facturar, name="facturar"),
    #url(r'^nuevoCliente$', crear_cliente, name="crearCliente"),
    url(r'^producto/(?P<codigo>\w{0,50})/$', obtener_producto, name='obt_producto'),
    url(r'^guardar', guardar_factura, name="guardar"),
    url(r'^ventas', listar_ventas,name='ventas'),
]