# Generated by Django 3.0.7 on 2020-07-31 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_auto_20200731_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cel',
            field=models.BigIntegerField(verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='document',
            field=models.BigIntegerField(verbose_name='Documento'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.BigIntegerField(blank=True, default=0, null=True, verbose_name='Telefono'),
        ),
    ]
