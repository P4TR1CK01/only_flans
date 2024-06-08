from django.db import models

# Create your models here.
class Flan(models.Model):
  nombre = models.CharField(max_length=15)
  email = models.CharField(max_length=15)
  mensaje = models.IntegerField(null=False)
  