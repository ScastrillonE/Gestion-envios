# Generated by Django 3.0.7 on 2020-07-23 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0003_auto_20200722_1443'),
        ('customers', '0002_auto_20200716_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='departamentos.Departamento'),
        ),
        migrations.AddField(
            model_name='customer',
            name='municipio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='departamentos.Municipio'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='T_document',
            field=models.CharField(choices=[('Cedula', 'Cedula'), ('Cedula Extranjeria', 'Cedula Extranjeria'), ('Pasaporte', 'Pasaporte'), ('NIT', 'NIT')], max_length=18, verbose_name='Tipo documento'),
        ),
    ]
