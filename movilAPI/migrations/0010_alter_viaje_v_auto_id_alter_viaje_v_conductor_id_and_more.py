# Generated by Django 4.1.3 on 2022-11-16 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movilAPI', '0009_alter_auto_a_conductor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='v_auto_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ID_Auto', to='movilAPI.auto'),
        ),
        migrations.AlterField(
            model_name='viaje',
            name='v_conductor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ID_conductor', to='movilAPI.conductor'),
        ),
        migrations.AlterField(
            model_name='viaje',
            name='v_pasajero_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ID_Pasajero', to='movilAPI.pasajero'),
        ),
    ]
