# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('est', '0007_auto_20160219_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zona',
            name='riesgo',
            field=models.ManyToManyField(to='est.Riesgo'),
        ),
    ]