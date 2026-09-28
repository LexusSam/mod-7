from django.contrib import admin
from .models import Cliente, Cuenta, Transaccion


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "telefono")
    search_fields = ("nombre", "email")


@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ("numero", "cliente", "saldo")
    search_fields = ("numero", "cliente__nombre")
    list_filter = ("cliente",)


@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ("cuenta", "tipo", "monto", "fecha")
    search_fields = ("cuenta__numero", "descripcion")
    list_filter = ("tipo", "fecha")