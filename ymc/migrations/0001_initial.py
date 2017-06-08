# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('puntaje', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Publicidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('duracion', models.DurationField()),
                ('dinero_generado', models.IntegerField()),
                ('cant_clicks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('usuario', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('comentario', models.TextField()),
                ('categoria', models.CharField(max_length=200)),
                ('duracion', models.DurationField()),
                ('puntaje', models.IntegerField()),
                ('cant_clicks', models.IntegerField()),
                ('cant_comentarios', models.IntegerField()),
                ('publicidad_asignada', models.ForeignKey(to='ymc.Publicidad')),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='video_asignado',
            field=models.ForeignKey(to='ymc.Video'),
        ),
    ]
