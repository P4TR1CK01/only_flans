import uuid
from django.db import models

# Create your models here.
class Pizza(models.Model):
  uuid = models.UUIDField()
  nombre = models.CharField(max_length=64)
  descripciom = models.TextField()
  precio = models.IntegerField(default=1000)
  imagen_url = models.URLField()
  is_private = models.BooleanField(default=False)
  