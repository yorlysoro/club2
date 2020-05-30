# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-05-30 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CI', models.CharField(help_text='Solo colocar numeros', max_length=8, unique=True)),
                ('Apellidos', models.CharField(help_text='Solo colocar caracteres', max_length=64)),
                ('Nombres', models.CharField(help_text='Solo colocar caracteres', max_length=64)),
                ('Departamento', models.CharField(help_text='Coloque el Departamento en donde trabaja', max_length=255)),
                ('Carga_Familiar', models.IntegerField()),
                ('FechaNacimiento', models.DateField(help_text='Coloque su fecha de nacimiento en formato dia/mes/año')),
                ('Sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=2)),
                ('Correo', models.EmailField(blank=True, help_text='Coloque una direccion de correo valida', max_length=254, null=True)),
                ('Foto', models.ImageField(upload_to='fotos/')),
                ('Carnet', models.FileField(blank=True, null=True, upload_to='carnet/')),
                ('Activo', models.BooleanField(default=False)),
                ('Numero_Personal', models.CharField(max_length=256)),
            ],
        ),
    ]
