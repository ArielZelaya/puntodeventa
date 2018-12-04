from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url, include
from .views import *
from . import views

app_name = 'producto'

urlpatterns =[

    url(r'^gestionProducto$', gestionProducto, name="ges_pro"),
    url(r'^EditarProducto/(?P<idProducto>\d+)/$', EditarProducto, name="edi_pro"),
    url(r'^DetalleProducto/(?P<idProducto>\d+)/$', DetallesProducto, name="det_pro"),
    url(r'^EliminarProducto/(?P<idProducto>\d+)/$', EliminarProducto, name="eli_pro")

]