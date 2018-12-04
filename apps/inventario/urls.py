from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url, include
from .views import *
from . import views

app_name = 'inventario'

urlpatterns =[

    url(r'^gestionInventario$', gestionInventario, name="ges_inv"),
    url(r'^EditarInventario/(?P<idMercancia>\d+)/$', EditarInventario, name="edi_inv"),
    #url(r'^DetalleInventario/(?P<idProducto>\d+)/$', DetallesInventario, name="det_inv"),
    url(r'^EliminarInventario/(?P<idMercancia>\d+)/$', EliminarMercancia, name="eli_inv")

]