from django.contrib import admin
# . hace referencia a esta carpeta
from .models import Soporte, PQR
# Register your models here.

admin.site.register(Soporte)
admin.site.register(PQR)