# Generated by Django 4.1.3 on 2022-11-17 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movilAPI', '0024_alter_conductor_c_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conductor',
            name='c_car',
            field=models.ForeignKey(blank='True', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='c_car', to='movilAPI.auto'),
        ),
    ]
