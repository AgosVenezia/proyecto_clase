# Generated by Django 3.2.14 on 2022-11-08 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cac', '0003_docenteabs'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonaM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_m', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido_m', models.CharField(max_length=150, verbose_name='Apellido')),
                ('email_m', models.EmailField(max_length=150, null=True)),
                ('dni_m', models.IntegerField(verbose_name='DNI')),
            ],
        ),
        migrations.CreateModel(
            name='DocenteM',
            fields=[
                ('personam_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cac.personam')),
                ('legajo_m', models.CharField(max_length=10, verbose_name='Legajo')),
            ],
            bases=('cac.personam',),
        ),
        migrations.CreateModel(
            name='EstudianteM',
            fields=[
                ('personam_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cac.personam')),
                ('matricula_m', models.CharField(max_length=10, verbose_name='Matricula')),
            ],
            bases=('cac.personam',),
        ),
    ]
