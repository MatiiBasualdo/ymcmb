# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ymc', '0012_auto_20170630_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuario',
            name='avatar',
            field=models.ImageField(default=None, upload_to='avatars/%Y/%m/%d/'),
        ),
    ]