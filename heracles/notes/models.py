from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Titulo de la nota")
    content = models.TextField(verbose_name="Contenido")
    status = models.BooleanField('Hecho/pendiente')