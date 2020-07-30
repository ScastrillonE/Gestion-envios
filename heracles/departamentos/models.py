from django.db import models
import csv
# Create your models here.
from django.forms import model_to_dict


def guardar_departamento():
    with open('/app/departamentos/colombia.csv', newline='') as File:
        reader = csv.reader(File)
        for dep, mun in reader:
            _,depa= Departamento.objects.get_or_create(nombre=dep)

def guardar_municipio():
    with open('/app/departamentos/colombia.csv', newline='') as File:
        reader = csv.reader(File)
        for dep, mun in reader:
            mun = Municipio.objects.get_or_create(
                departamento = Departamento.objects.get(nombre=dep),
                nombre = mun
            )

class Departamento(models.Model):
    nombre = models.CharField(max_length=255,verbose_name='Nombre departamento')

    def guardar(self):
        guardar_departamento()

    def toJson(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255,verbose_name='Nombre Municipio')

    def guardar(self):
        guardar_municipio()

    def toJson(self):
        item = model_to_dict(self)
        return item
    def __str__(self):
        return '{} - {}'.format(self.departamento,self.nombre)