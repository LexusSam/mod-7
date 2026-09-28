from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .models import Cliente, Cuenta, Transaccion


class ClienteListView(ListView):
    model = Cliente
    template_name = "gestion/cliente_list.html"
    context_object_name = "clientes"


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = "gestion/cliente_form.html"
    fields = ["nombre", "email", "telefono"]
    success_url = reverse_lazy("cliente-list")


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "gestion/cliente_detail.html"
    context_object_name = "cliente"


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = "gestion/cliente_form.html"
    fields = ["nombre", "email", "telefono"]
    context_object_name = "cliente"
    success_url = reverse_lazy("cliente-list")


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "gestion/cliente_confirm_delete.html"
    context_object_name = "cliente"
    success_url = reverse_lazy("cliente-list")

class CuentaListView(ListView):
    model = Cuenta
    template_name = "gestion/cuenta_list.html"
    context_object_name = "cuentas"

class CuentaCreateView(CreateView):
    model = Cuenta
    template_name = "gestion/cuenta_form.html"
    fields = ["cliente", "numero", "saldo"]
    success_url = reverse_lazy("cuenta-list")

class CuentaUpdateView(UpdateView):
    model = Cuenta
    template_name = "gestion/cuenta_form.html"
    fields = ["cliente", "numero", "saldo"]
    context_object_name = "cuenta"
    success_url = reverse_lazy("cuenta-list")

class CuentaDeleteView(DeleteView):
    model = Cuenta
    template_name = "gestion/cuenta_confirm_delete.html"
    context_object_name = "cuenta"
    success_url = reverse_lazy("cuenta-list")

class TransaccionListView(ListView):
    model = Transaccion
    template_name = "gestion/transaccion_list.html"
    context_object_name = "transacciones"

class TransaccionCreateView(CreateView):
    model = Transaccion
    template_name = "gestion/transaccion_form.html"
    fields = ["cuenta", "tipo", "monto", "descripcion"]
    success_url = reverse_lazy("transaccion-list")

class TransaccionUpdateView(UpdateView):
    model = Transaccion
    template_name = "gestion/transaccion_form.html"
    fields = ["cuenta", "tipo", "monto", "descripcion"]
    context_object_name = "transaccion"
    success_url = reverse_lazy("transaccion-list")

class TransaccionDeleteView(DeleteView):
    model = Transaccion
    template_name = "gestion/transaccion_confirm_delete.html"
    context_object_name = "transaccion"
    success_url = reverse_lazy("transaccion-list")