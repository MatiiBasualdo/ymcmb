# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ymc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='fecha_publicacion',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
