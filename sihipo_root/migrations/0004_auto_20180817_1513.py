# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-17 15:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sihipo_root', '0003_auto_20180816_2313'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plantevalif',
            options={'ordering': ['prior'], 'verbose_name': 'Kondisi'},
        ),
        migrations.AlterModelOptions(
            name='plantevalthen',
            options={'verbose_name': 'Aksi'},
        ),
    ]
