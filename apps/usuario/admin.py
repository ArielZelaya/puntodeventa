from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Cliente)
admin.site.register(Empleado)
