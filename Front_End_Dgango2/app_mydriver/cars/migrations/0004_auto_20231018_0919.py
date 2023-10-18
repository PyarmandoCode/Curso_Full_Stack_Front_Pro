# Generated by Django 3.2.22 on 2023-10-18 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_driver_coments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='coments',
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coments', models.TextField(null=True)),
                ('date_feedback', models.DateField(auto_now=True)),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.driver')),
            ],
        ),
    ]
