from django.db import models

# Create your models here.
class deadpool (models.Model):
    name = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.IntegerField()
