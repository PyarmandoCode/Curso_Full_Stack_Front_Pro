# Generated by Django 3.2.22 on 2023-10-18 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_driver_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='coments',
            field=models.TextField(null=True),
        ),
    ]
