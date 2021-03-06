# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iati_synchroniser', '0002_auto_20170529_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='iati_id',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='iati_id',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
