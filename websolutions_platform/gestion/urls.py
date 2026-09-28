from django.urls import path

from .views import (
    ClienteListView,
    ClienteCreateView,
    ClienteDetailView,
    ClienteUpdateView,
    ClienteDeleteView,
    CuentaListView,
    CuentaCreateView,
    CuentaUpdateView,
    CuentaDeleteView,
    TransaccionListView,
    TransaccionCreateView,
    TransaccionUpdateView,
    TransaccionDeleteView,
)


urlpatterns = [

    path(
        "clientes/",
        ClienteListView.as_view(),
        name="cliente-list"
    ),

    path(
        "clientes/nuevo/",
        ClienteCreateView.as_view(),
        name="cliente-create"
    ),

    path(
        "clientes/<int:pk>/",
        ClienteDetailView.as_view(),
        name="cliente-detail"
    ),

    path(
        "clientes/<int:pk>/editar/",
        ClienteUpdateView.as_view(),
        name="cliente-update"
    ),

    path(
        "clientes/<int:pk>/eliminar/",
        ClienteDeleteView.as_view(),
        name="cliente-delete"
    ),

    path(
    "cuentas/",
    CuentaListView.as_view(),
    name="cuenta-list"),

    path(
        "cuentas/nueva/",
        CuentaCreateView.as_view(), 
        name="cuenta-create"),

    path(
        "cuentas/<int:pk>/editar/",
        CuentaUpdateView.as_view(),
        name="cuenta-update",
    ),

    path(
        "cuentas/<int:pk>/eliminar/",
        CuentaDeleteView.as_view(),
        name="cuenta-delete",
    ),

    path(
        "transacciones/",
        TransaccionListView.as_view(), 
        name="transaccion-list"),

    path(
        "transacciones/nueva/",
        TransaccionCreateView.as_view(),
        name="transaccion-create"),

    path(
        "transacciones/<int:pk>/editar/",
        TransaccionUpdateView.as_view(),
        name="transaccion-update",
    ),

    path(
        "transacciones/<int:pk>/eliminar/",
        TransaccionDeleteView.as_view(),
        name="transaccion-delete",
    ),
    ]