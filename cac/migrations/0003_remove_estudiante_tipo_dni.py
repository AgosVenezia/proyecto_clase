# Generated by Django 3.2.14 on 2022-11-03 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cac', '0002_estudiante_tipo_dni'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='tipo_dni',
        ),
    ]
