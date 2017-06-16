# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-11 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_price_license'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='license',
            field=models.CharField(choices=[(0, 'CC0'), (1, 'CC - BY'), (2, 'CC - BY - NC'), (3, 'CC - BY - NC'), (4, 'CC - BY - NC - ND'), (5, 'CC - BY - SA'), (6, 'CC - BY - NC - SA'), (7, 'CC0'), (8, 'PPDL'), (9, 'Standard copyright'), (10, 'Unknown')], default='', max_length=1),
        ),
    ]