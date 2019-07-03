from django.db import models

# Create your models here.
class Service(models.Model):
    nombre = models.CharField(max_length= 200, verbose_name="Nombre")
    precio = models.FloatField(verbose_name="Precio")
    descripcion = models.TextField(verbose_name="descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name ="Plato"
        verbose_name_plural="Platos"
        ordering=['-created']

    def __str__(self):
        return self.nombre