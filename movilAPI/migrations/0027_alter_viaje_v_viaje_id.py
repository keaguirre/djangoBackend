# Generated by Django 4.1.3 on 2022-11-17 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movilAPI', '0026_auto_a_conductor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='v_viaje_id',
            field=models.IntegerField(max_length=254, primary_key=True, serialize=False, verbose_name='Identificador de viaje'),
        ),
    ]
