# Generated by Django 3.0.7 on 2020-07-31 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingcompany',
            name='name',
            field=models.CharField(max_length=300, unique=True, verbose_name='Nombre de la empresa'),
        ),
    ]
