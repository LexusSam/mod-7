from django.db import models
from django.core.exceptions import ValidationError


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Cuenta(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="cuentas"
    )
    numero = models.CharField(max_length=20, unique=True)
    saldo = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return f"Cuenta {self.numero} - {self.cliente.nombre}"


class Transaccion(models.Model):

    TIPO_CHOICES = [
        ("deposito", "Depósito"),
        ("retiro", "Retiro"),
    ]

    cuenta = models.ForeignKey(
        Cuenta,
        on_delete=models.CASCADE,
        related_name="transacciones"
    )

    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES
    )

    monto = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    descripcion = models.CharField(
        max_length=200,
        blank=True
    )

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    def clean(self):
        if self.monto <= 0:
            raise ValidationError(
                "El monto debe ser mayor que cero."
            )

        if self.tipo == "retiro" and self.monto > self.cuenta.saldo:
            raise ValidationError(
                "No puedes retirar un monto mayor al saldo disponible."
            )

    def save(self, *args, **kwargs):

        if self.pk:
            transaccion_anterior = Transaccion.objects.get(pk=self.pk)

            # Revertir el efecto de la transacción anterior
            if transaccion_anterior.tipo == "deposito":
                transaccion_anterior.cuenta.saldo -= transaccion_anterior.monto

            elif transaccion_anterior.tipo == "retiro":
                transaccion_anterior.cuenta.saldo += transaccion_anterior.monto

            transaccion_anterior.cuenta.save()

            # Recargar la cuenta actual desde la base de datos
            self.cuenta.refresh_from_db()

        self.full_clean()

        # Aplicar el efecto de la nueva transacción
        if self.tipo == "deposito":
            self.cuenta.saldo += self.monto

        elif self.tipo == "retiro":
            self.cuenta.saldo -= self.monto

        self.cuenta.save()

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):

        # Revertir el efecto de la transacción
        if self.tipo == "deposito":
            self.cuenta.saldo -= self.monto

        elif self.tipo == "retiro":
            self.cuenta.saldo += self.monto

        self.cuenta.save()

        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.tipo} - ${self.monto}"