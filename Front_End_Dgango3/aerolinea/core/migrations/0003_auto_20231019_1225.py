# Generated by Django 3.2.22 on 2023-10-19 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_vuelo_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='pasajero',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='vuelos'),
        ),
        migrations.AddField(
            model_name='pasajero',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
    ]