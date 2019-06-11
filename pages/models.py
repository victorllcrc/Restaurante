from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Page(models.Model):

    title = models.CharField(verbose_name="Red Social", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name = "pagina"
        verbose_name_plural = "paginas"
        ordering = ['title']
    def __str__(self):
        return self.title
