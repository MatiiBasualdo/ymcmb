# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ymc', '0011_auto_20170629_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.FileField(default=None, upload_to=b'avatars/%Y/%m/%d/')),
            ],
        ),
        migrations.AlterField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='video',
            name='usuario_asignado',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
