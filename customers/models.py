from django.db import models
from django.forms import model_to_dict
from core.models import BaseModel

from departamentos.models import Departamento, Municipio
import csv

# Create your models here.
TYPE_DOCUMENT = [
    ('Cedula', 'Cedula'),
    ('Cedula Extranjeria', 'Cedula Extranjeria'),
    ('Pasaporte', 'Pasaporte'),
    ('NIT', 'NIT'),
]


def buscar_dep(dep):
    try:
        return Departamento.objects.get(nombre=dep)
    except Exception as e:
        print(str(e))
        print(dep)
        print("##########################")

def buscar_mun(dep,mun):
    try:
        dep = Departamento.objects.get(nombre=dep)
        m = Municipio.objects.get(departamento=dep,nombre=mun)
        return m
    except Exception as e :
        print(str(e))
        return print(f'departamento -- {dep} -- municipio -- {mun}')

def guardar_customer():
    with open('/app/customers/clientes-stric.csv', newline='') as File:
        reader = csv.reader(File)
        for cus, doc, addr, dep, mun, tel in reader:

            try:
                customer = Customer.objects.get_or_create(
                    name=cus,
                    T_document='NIT',
                    document=doc,
                    email='email@gmail.com',
                    address=addr,
                    phone=tel,
                    cel=123456,
                    department=buscar_dep(dep),
                    municipio=buscar_mun(dep,mun),

                )
                print(customer)
            except Exception as e:
                print(str(e))


class Customer(BaseModel):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    T_document = models.CharField(choices=TYPE_DOCUMENT, max_length=18, verbose_name='Tipo documento')
    document = models.CharField(verbose_name='Documento', max_length=980)
    email = models.EmailField(max_length=100, verbose_name='Correo electronico')
    address = models.CharField(max_length=150)
    phone = models.CharField(verbose_name='Telefono', blank=True, null=True, default=0, max_length=12)
    cel = models.BigIntegerField(verbose_name='Celular')
    department = models.ForeignKey(Departamento, on_delete=models.CASCADE, default=1)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, default=1)

    def toJson(self):
        customer = model_to_dict(self)
        customer['departamento'] = self.department.toJson()
        customer['c_municipio'] = self.municipio.toJson()

        return customer

    def guardar(self):
        guardar_customer()

    def __str__(self):
        return '{} - {}'.format(self.name, self.document)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
