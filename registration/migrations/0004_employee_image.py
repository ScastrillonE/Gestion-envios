# Generated by Django 3.0.7 on 2020-07-10 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d'),
        ),
    ]
