from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    delete = models.BooleanField('Eliminado/Activo',default=False)
    class Meta:
        abstract = True