# Generated by Django 4.1.3 on 2022-11-16 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movilAPI', '0016_alter_pasajero_p_trip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pasajero',
            name='p_trip',
        ),
    ]
