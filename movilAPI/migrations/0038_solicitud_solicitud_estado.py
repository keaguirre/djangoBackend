# Generated by Django 4.1.3 on 2022-12-12 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movilAPI', '0037_alter_solicitud_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='solicitud_estado',
            field=models.CharField(max_length=30, null=True, verbose_name='Estado solicitud'),
        ),
    ]
