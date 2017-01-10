# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-05 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iati_synchroniser', '0020_auto_20161027_0115'),
        ('iati', '0061_auto_20161212_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='publisher',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='iati_synchroniser.Publisher'),
        ),
    ]
