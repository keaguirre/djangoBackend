# Generated by Django 4.1.3 on 2022-11-13 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movilAPI', '0004_alter_conductor_c_email_alter_pasajero_p_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='v_state',
            field=models.CharField(max_length=30, verbose_name='Estado'),
        ),
    ]
