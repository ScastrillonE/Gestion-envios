from django.db import models
from django.forms import model_to_dict
from core.models import BaseModel

from departamentos.models import Departamento,Municipio

# Create your models here.
TYPE_DOCUMENT = [
    ('Cedula', 'Cedula'),
    ('Cedula Extranjeria', 'Cedula Extranjeria'),
    ('Pasaporte', 'Pasaporte'),
    ('NIT','NIT'),
]

class Customer(BaseModel):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    T_document = models.CharField(choices=TYPE_DOCUMENT, max_length=18, verbose_name='Tipo documento')
    document = models.IntegerField(verbose_name='Documento', unique=True)
    email=models.EmailField(max_length=100,verbose_name='Correo electronico')
    address = models.CharField(max_length=150)
    phone = models.IntegerField(verbose_name='Telefono', blank=True, null=True,default=0)
    cel = models.IntegerField(verbose_name='Celular')
    department=models.ForeignKey(Departamento,on_delete=models.CASCADE,default=1)
    municipio=models.ForeignKey(Municipio,on_delete=models.CASCADE,default=1)

    def toJson(self):
        customer = model_to_dict(self)
        customer['departamento'] = self.department.toJson()
        customer['c_municipio'] = self.municipio.toJson()

        return customer

    def __str__(self):
        return '{} - {}'.format(self.name,self.document)

    class Meta:
        verbose_name = 'Cliente'    
        verbose_name_plural = 'Clientes'