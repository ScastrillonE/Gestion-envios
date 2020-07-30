from django.db import models

# Create your models here.
from core.models import BaseModel


class CompanySettings(BaseModel):
    name_company = models.CharField(max_length=100, verbose_name='Nombre de la empresa')
    phone_number = models.CharField(max_length=100,verbose_name='Numero contacto')
    cel = models.CharField(max_length=100,verbose_name='Numero celular')
    email = models.EmailField(verbose_name='Correo electronico')
    logo = models.ImageField(upload_to='logo/', blank=True)
    address = models.CharField(max_length=200, verbose_name='Direccion de la empresa')

    def __str__(self):
        return self.name_company

    def create_company():
        default = CompanySettings(
            name_company='Default',
            phone_number=2845698,
            cel=3002545632,
            email='Default@gmail.com',
            address='Cll 35 # 45-32',
            logo='static/img/empty.png'

        )
        default.save()
        print('Guardado exitosamente')

    def get_email(self):
        return self.email
