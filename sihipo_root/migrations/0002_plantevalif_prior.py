# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-16 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sihipo_root', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantevalif',
            name='prior',
            field=models.IntegerField(default=10, unique=True, verbose_name='Priority'),
        ),
    ]
