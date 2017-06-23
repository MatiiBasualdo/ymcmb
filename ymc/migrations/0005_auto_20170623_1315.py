# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ymc', '0004_auto_20170623_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_asignado',
        ),
        migrations.AddField(
            model_name='video',
            name='usuario',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_video_asignado', to='ymc.Usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='video_asignado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_usuario', to='ymc.Video'),
        ),
    ]
