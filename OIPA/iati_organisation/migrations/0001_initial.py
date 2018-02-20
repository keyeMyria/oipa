# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('iati_vocabulary', '0001_initial'),
        ('iati_codelists', '0001_initial'),
        ('geodata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentLinkRecipientCountry',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Document link categories',
            },
        ),
        migrations.CreateModel(
            name='DocumentLinkTitle',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_identifier', models.CharField(
                    db_index=True, max_length=150, unique=True)),
                ('normalized_organisation_identifier', models.CharField(db_index=True, max_length=150)),
                ('last_updated_datetime', models.DateTimeField(blank=True, null=True)),
                ('reported_in_iati', models.BooleanField(default=True)),
                ('primary_name', models.CharField(db_index=True, max_length=150)),
                ('published', models.BooleanField(db_index=True, default=False)),
                ('ready_to_publish', models.BooleanField(db_index=True, default=False)),
                ('modified', models.BooleanField(db_index=True, default=False)),
                ('default_currency',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_codelists.Currency')),
                ('default_lang',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_codelists.Language')),
                ('iati_standard_version', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='iati_codelists.Version')),
                ('type',
                 models.ForeignKey(blank=True,
                                   default=None,
                                   null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_codelists.OrganisationType')),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationDocumentLink',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(max_length=500)),
                ('iso_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationDocumentLinkCategory',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('category',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_codelists.DocumentCategory')),
                ('document_link',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_organisation.OrganisationDocumentLink')),
            ],
            options={
                'verbose_name_plural': 'Document link categories',
            },
        ),
        migrations.CreateModel(
            name='OrganisationDocumentLinkLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('document_link',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_organisation.OrganisationDocumentLink')),
                ('language', models.ForeignKey(blank=True, default=None, null=True,
                                               on_delete=django.db.models.deletion.CASCADE, to='iati_codelists.Language')),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationName',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                                      related_name='name', to='iati_organisation.Organisation')),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationNarrative',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name=b'related object')),
                ('content', models.TextField()),
                ('content_type', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('language', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='iati_codelists.Language')),
                ('organisation',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_organisation.Organisation')),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationReportingOrganisation',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('reporting_org_identifier', models.CharField(max_length=250, null=True)),
                ('secondary_reporter', models.BooleanField(default=False)),
                ('org_type',
                 models.ForeignKey(default=None,
                                   null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_codelists.OrganisationType')),
                ('organisation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                                      related_name='reporting_org', to='iati_organisation.Organisation')),
                ('reporting_org',
                 models.ForeignKey(db_constraint=False,
                                   null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   related_name='reported_by_orgs',
                                   to='iati_organisation.Organisation')),
            ],
        ),
        migrations.CreateModel(
            name='RecipientCountryBudget',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('period_start', models.DateField(null=True)),
                ('period_end', models.DateField(null=True)),
                ('value_date', models.DateField(null=True)),
                ('value', models.DecimalField(decimal_places=2, default=None, max_digits=14, null=True)),
                ('country',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='geodata.Country')),
                ('currency',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_codelists.Currency')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                   related_name='recipient_country_budgets', to='iati_organisation.Organisation')),
                ('status',
                 models.ForeignKey(default=1,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_codelists.BudgetStatus')),
            ],
        ),
        migrations.CreateModel(
            name='RecipientCountryBudgetLine',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=150)),
                ('value', models.DecimalField(decimal_places=2, default=None, max_digits=14, null=True)),
                ('value_date', models.DateField(null=True)),
                ('currency',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_codelists.Currency')),
                ('recipient_country_budget',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_organisation.RecipientCountryBudget')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RecipientOrgBudget',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_org_identifier', models.CharField(max_length=150,
                                                              null=True, verbose_name=b'recipient_org_identifier')),
                ('period_start', models.DateField(null=True)),
                ('period_end', models.DateField(null=True)),
                ('value_date', models.DateField(null=True)),
                ('value', models.DecimalField(decimal_places=2, default=None, max_digits=14, null=True)),
                ('currency',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_codelists.Currency')),
                ('organisation',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_organisation.Organisation')),
                ('recipient_org',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   related_name='recieving_org',
                                   to='iati_organisation.Organisation')),
                ('status',
                 models.ForeignKey(default=1,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_codelists.BudgetStatus')),
            ],
        ),
        migrations.CreateModel(
            name='RecipientOrgBudgetLine',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=150)),
                ('value', models.DecimalField(decimal_places=2, default=None, max_digits=14, null=True)),
                ('value_date', models.DateField(null=True)),
                ('currency',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_codelists.Currency')),
                ('recipient_org_budget',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_organisation.RecipientOrgBudget')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RecipientRegionBudget',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('vocabulary_uri', models.URLField(blank=True, null=True)),
                ('period_start', models.DateField(null=True)),
                ('period_end', models.DateField(null=True)),
                ('value_date', models.DateField(null=True)),
                ('value', models.DecimalField(decimal_places=2, default=None, max_digits=14, null=True)),
                ('currency',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_codelists.Currency')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                   related_name='recipient_region_budget', to='iati_organisation.Organisation')),
                ('region',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='geodata.Region')),
                ('status',
                 models.ForeignKey(default=1,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_codelists.BudgetStatus')),
                ('vocabulary',
                 models.ForeignKey(default=1,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_vocabulary.RegionVocabulary')),
            ],
        ),
        migrations.CreateModel(
            name='RecipientRegionBudgetLine',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=150)),
                ('value', models.DecimalField(decimal_places=2, default=None, max_digits=14, null=True)),
                ('value_date', models.DateField(null=True)),
                ('currency',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_codelists.Currency')),
                ('recipient_region_budget',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_organisation.RecipientRegionBudget')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TotalBudget',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('period_start', models.DateField(null=True)),
                ('period_end', models.DateField(null=True)),
                ('value_date', models.DateField(null=True)),
                ('value', models.DecimalField(decimal_places=2, default=None, max_digits=14, null=True)),
                ('currency',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_codelists.Currency')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                   related_name='total_budgets', to='iati_organisation.Organisation')),
                ('status',
                 models.ForeignKey(default=1,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_codelists.BudgetStatus')),
            ],
        ),
        migrations.CreateModel(
            name='TotalBudgetLine',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=150)),
                ('value', models.DecimalField(decimal_places=2, default=None, max_digits=14, null=True)),
                ('value_date', models.DateField(null=True)),
                ('currency',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_codelists.Currency')),
                ('total_budget',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_organisation.TotalBudget')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TotalExpenditure',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('period_start', models.DateField(null=True)),
                ('period_end', models.DateField(null=True)),
                ('value_date', models.DateField(null=True)),
                ('value', models.DecimalField(decimal_places=2, default=None, max_digits=14, null=True)),
                ('currency',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_codelists.Currency')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                   related_name='total_expenditure', to='iati_organisation.Organisation')),
            ],
        ),
        migrations.CreateModel(
            name='TotalExpenditureLine',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=150)),
                ('value', models.DecimalField(decimal_places=2, default=None, max_digits=14, null=True)),
                ('value_date', models.DateField(null=True)),
                ('currency',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_codelists.Currency')),
                ('total_expenditure',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='iati_organisation.TotalExpenditure')),
            ],
        ),
        migrations.AddField(
            model_name='organisationdocumentlink',
            name='categories',
            field=models.ManyToManyField(
                through='iati_organisation.OrganisationDocumentLinkCategory',
                to='iati_codelists.DocumentCategory'),
        ),
        migrations.AddField(
            model_name='organisationdocumentlink',
            name='file_format',
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='iati_codelists.FileFormat'),
        ),
        migrations.AddField(
            model_name='organisationdocumentlink',
            name='language',
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='iati_codelists.Language'),
        ),
        migrations.AddField(
            model_name='organisationdocumentlink',
            name='organisation',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='iati_organisation.Organisation'),
        ),
        migrations.AddField(
            model_name='organisationdocumentlink',
            name='recipient_countries',
            field=models.ManyToManyField(
                blank=True,
                related_name='recipient_countries',
                through='iati_organisation.DocumentLinkRecipientCountry',
                to='geodata.Country'),
        ),
        migrations.AddField(
            model_name='documentlinktitle',
            name='document_link',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to='iati_organisation.OrganisationDocumentLink'),
        ),
        migrations.AddField(
            model_name='documentlinkrecipientcountry',
            name='document_link',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='iati_organisation.OrganisationDocumentLink'),
        ),
        migrations.AddField(
            model_name='documentlinkrecipientcountry',
            name='recipient_country',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='geodata.Country'),
        ),
        migrations.AlterIndexTogether(
            name='organisationnarrative',
            index_together=set([('content_type', 'object_id')]),
        ),
    ]
