# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 15:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=140)),
                ('ciudad', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=140)),
                ('duracion', models.IntegerField()),
                ('genero', models.CharField(choices=[('terror', 'Terror'), ('SciFI', 'Ciencia Ficcion')], max_length=140)),
                ('clase', models.CharField(max_length=3)),
                ('sinopsis', models.TextField()),
                ('trailer', models.CharField(max_length=500)),
                ('horario', models.CharField(max_length=60)),
                ('cines', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='peliculas', to='main.Cine')),
            ],
        ),
    ]
