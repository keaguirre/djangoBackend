# Generated by Django 4.1.3 on 2022-11-16 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movilAPI', '0014_alter_auto_a_conductor'),
    ]

    operations = [
        migrations.AddField(
            model_name='conductor',
            name='c_trip',
            field=models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, related_name='c_trip', to='movilAPI.viaje'),
        ),
        migrations.AddField(
            model_name='pasajero',
            name='p_trip',
            field=models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, related_name='p_trip', to='movilAPI.viaje'),
        ),
    ]
