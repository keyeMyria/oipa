# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-31 16:52
from __future__ import unicode_literals

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0004_activityparticipatingorganisation_org_activity_obj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitysearch',
            name='document_link',
        ),
        migrations.RemoveField(
            model_name='activitysearch',
            name='text',
        ),
        migrations.AddField(
            model_name='activitysearch',
            name='document_link_vector',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='activitysearch',
            name='search_vector_text',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AlterField(
            model_name='activitysearch',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='activitysearch',
            name='iati_identifier',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='activitysearch',
            name='participating_org',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='activitysearch',
            name='recipient_country',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='activitysearch',
            name='recipient_region',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='activitysearch',
            name='reporting_org',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='activitysearch',
            name='sector',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='activitysearch',
            name='title',
            field=models.TextField(null=True),
        ),
        migrations.AddIndex(
            model_name='activitysearch',
            index=django.contrib.postgres.indexes.GinIndex(
                fields=[b'search_vector_text'], name='iati_activi_search__168aa4_gin'),
        ),
    ]
