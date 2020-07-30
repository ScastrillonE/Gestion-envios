# Generated by Django 3.0.7 on 2020-07-17 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanySettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(max_length=100, verbose_name='Nombre de la empresa')),
                ('phone_number', models.PositiveIntegerField(verbose_name='Numero contacto')),
                ('cel', models.PositiveIntegerField(verbose_name='Numero celular')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electronico')),
                ('logo', models.ImageField(upload_to='logo/')),
                ('address', models.CharField(max_length=200, verbose_name='Direccion de la empresa')),
            ],
        ),
    ]
