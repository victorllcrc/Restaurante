from django.db import models
from services.models import Service
from django.utils.timezone import now



# Create your models here.
class Pedido(models.Model):

    monto_total = models.FloatField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    def __str__(self):
        return str(self.id)

class Detalle_pedido (models.Model):

    cantida = models.CharField(max_length=50)
    subtotal = models.FloatField()
    plato = models.ForeignKey(Service, verbose_name="Plato", on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, verbose_name="Pedido", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    def __str__(self):
        return str(self.id)

class Reserva (models.Model):

    fecha = models.CharField(verbose_name="fecha de reserva", max_length=255    )
    pedido = models.ForeignKey(Pedido, verbose_name='Pedidos' ,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    def __str__(self):
        return str(self.id)