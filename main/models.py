from django.db import models
import uuid

# Create your models here.
class Contact(models.Model):
  nombre = models.CharField(max_length=15)
  email = models.CharField(max_length=15)
  mensaje = models.CharField(max_length=155)
  
class Flan(models.Model):
  uuid= models.UUIDField(editable=False, default=uuid)
  nombre = models.CharField(max_length=64)
  descripcion = models.TextField()
  precio = models.IntegerField(default=1000)
  foto = models.URLField
  is_private = models.BooleanField(default=False)