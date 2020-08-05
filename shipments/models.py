import uuid
from django.db import models
from django.forms import model_to_dict
from customers.models import Customer
from departamentos.models import Departamento,Municipio

# Create your models here.
from core.models import BaseModel

STATUS = [
    ('Bodega', 'Bodega'),
    ('Enviado', 'Enviado'),

]
def gen():
    consecutivo = uuid.uuid4()
    consecutivo = str(consecutivo)
    consecutivo = consecutivo[0:13]
    print(consecutivo)
    codigo = consecutivo.split('-')
    codigo = codigo[0]+codigo[1]
    codigo = str(codigo)
    return codigo

class ShippingCompany(BaseModel):
    name = models.CharField(verbose_name='Nombre de la empresa',max_length=300, unique=True)

    def __str__(self):
        return self.name


class Shipping(BaseModel):
    consecutivo = models.CharField(max_length=13, default=gen())
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                 verbose_name='Cliente')
    c_Tdocument = models.CharField(max_length=18, verbose_name='Tipo Documento')
    c_document = models.CharField(verbose_name='Documento',max_length=100,)
    c_address = models.CharField(max_length=150)
    c_phone = models.CharField(verbose_name='Telefono', max_length=30, blank=True, null=True)
    c_cel = models.CharField(verbose_name='Celular',max_length=30,)
    c_email = models.EmailField(max_length=100, verbose_name='Correo electronico')
    shipping_number = models.CharField(max_length=200, verbose_name='Numero guia',
                                       blank=True, null=True)
    shipping_company = models.ForeignKey(ShippingCompany, on_delete=models.CASCADE)
    photo = models.CharField(max_length=1048576, blank=True, null=True)
    weight = models.CharField(max_length=500,blank=True,null=True,verbose_name='Peso')
    send_date = models.DateField(blank=True, null=True)
    status = models.CharField(choices=STATUS, default='Bodega',
                              max_length=7)
    c_department=models.ForeignKey(Departamento,on_delete=models.CASCADE,default=1)
    c_municipio=models.ForeignKey(Municipio,on_delete=models.CASCADE,default=1)
    observations = models.TextField(verbose_name='Observaciones',
                                    null=True,blank=True)

    @property
    def get_customer(self):
        return self.customer.name

    @property  # Obtiene el nombre de la compañia de envio para el excel
    def get_company(self):
        return self.shipping_company.name

    def __str__(self):
        return self.customer

    def toJson(self):
        item = model_to_dict(self)
        item["consecutivo"] = self.consecutivo
        item['s_company'] = self.shipping_company.name
        item['cust'] = self.customer.toJson()
        item['departamento'] = self.c_department.toJson()
        item['municip'] = self.c_municipio.toJson()
        return item
