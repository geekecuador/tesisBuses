from django.contrib import admin
from .models import Reserva,Asiento,Bus,Cliente,Ruta
# Register your models here.
admin.site.register(Reserva)
admin.site.register(Asiento)
admin.site.register(Bus)
admin.site.register(Cliente)
admin.site.register(Ruta)