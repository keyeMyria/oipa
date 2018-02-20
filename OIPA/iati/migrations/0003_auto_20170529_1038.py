# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0002_auto_20170424_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityaggregation',
            name='credit_guarantee_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='activityaggregation',
            name='credit_guarantee_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AddField(
            model_name='activityaggregation',
            name='incoming_commitment_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='activityaggregation',
            name='incoming_commitment_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AddField(
            model_name='activityaggregation',
            name='interest_payment_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='activityaggregation',
            name='interest_payment_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AddField(
            model_name='activityaggregation',
            name='loan_repayment_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='activityaggregation',
            name='loan_repayment_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AddField(
            model_name='activityaggregation',
            name='purchase_of_equity_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='activityaggregation',
            name='purchase_of_equity_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AddField(
            model_name='activityaggregation',
            name='reimbursement_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='activityaggregation',
            name='reimbursement_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AddField(
            model_name='activityaggregation',
            name='sale_of_equity_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='activityaggregation',
            name='sale_of_equity_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AddField(
            model_name='activitypluschildaggregation',
            name='credit_guarantee_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='activitypluschildaggregation',
            name='credit_guarantee_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AddField(
            model_name='activitypluschildaggregation',
            name='incoming_commitment_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='activitypluschildaggregation',
            name='incoming_commitment_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AddField(
            model_name='activitypluschildaggregation',
            name='interest_payment_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='activitypluschildaggregation',
            name='interest_payment_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AddField(
            model_name='activitypluschildaggregation',
            name='loan_repayment_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='activitypluschildaggregation',
            name='loan_repayment_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AddField(
            model_name='activitypluschildaggregation',
            name='purchase_of_equity_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='activitypluschildaggregation',
            name='purchase_of_equity_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AddField(
            model_name='activitypluschildaggregation',
            name='reimbursement_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='activitypluschildaggregation',
            name='reimbursement_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AddField(
            model_name='activitypluschildaggregation',
            name='sale_of_equity_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='activitypluschildaggregation',
            name='sale_of_equity_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AddField(
            model_name='childaggregation',
            name='credit_guarantee_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='childaggregation',
            name='credit_guarantee_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AddField(
            model_name='childaggregation',
            name='incoming_commitment_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='childaggregation',
            name='incoming_commitment_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AddField(
            model_name='childaggregation',
            name='interest_payment_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='childaggregation',
            name='interest_payment_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AddField(
            model_name='childaggregation',
            name='loan_repayment_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='childaggregation',
            name='loan_repayment_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AddField(
            model_name='childaggregation',
            name='purchase_of_equity_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='childaggregation',
            name='purchase_of_equity_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AddField(
            model_name='childaggregation',
            name='reimbursement_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='childaggregation',
            name='reimbursement_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AddField(
            model_name='childaggregation',
            name='sale_of_equity_currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='childaggregation',
            name='sale_of_equity_value',
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                max_digits=15,
                null=True),
        ),
        migrations.AlterIndexTogether(
            name='activityaggregation',
            index_together=set([('sale_of_equity_value',
                                 'activity'),
                                ('commitment_value',
                                 'activity'),
                                ('incoming_commitment_value',
                                 'activity'),
                                ('budget_value',
                                 'activity'),
                                ('disbursement_value',
                                 'activity'),
                                ('interest_payment_value',
                                 'activity'),
                                ('incoming_funds_value',
                                 'activity'),
                                ('purchase_of_equity_value',
                                 'activity'),
                                ('loan_repayment_value',
                                 'activity'),
                                ('expenditure_value',
                                 'activity'),
                                ('credit_guarantee_value',
                                 'activity'),
                                ('reimbursement_value',
                                 'activity')]),
        ),
        migrations.AlterIndexTogether(
            name='activitypluschildaggregation',
            index_together=set([('sale_of_equity_value',
                                 'activity'),
                                ('commitment_value',
                                 'activity'),
                                ('incoming_commitment_value',
                                 'activity'),
                                ('budget_value',
                                 'activity'),
                                ('disbursement_value',
                                 'activity'),
                                ('interest_payment_value',
                                 'activity'),
                                ('incoming_funds_value',
                                 'activity'),
                                ('purchase_of_equity_value',
                                 'activity'),
                                ('loan_repayment_value',
                                 'activity'),
                                ('expenditure_value',
                                 'activity'),
                                ('credit_guarantee_value',
                                 'activity'),
                                ('reimbursement_value',
                                 'activity')]),
        ),
        migrations.AlterIndexTogether(
            name='childaggregation',
            index_together=set([('sale_of_equity_value',
                                 'activity'),
                                ('commitment_value',
                                 'activity'),
                                ('incoming_commitment_value',
                                 'activity'),
                                ('budget_value',
                                 'activity'),
                                ('disbursement_value',
                                 'activity'),
                                ('interest_payment_value',
                                 'activity'),
                                ('incoming_funds_value',
                                 'activity'),
                                ('purchase_of_equity_value',
                                 'activity'),
                                ('loan_repayment_value',
                                 'activity'),
                                ('expenditure_value',
                                 'activity'),
                                ('credit_guarantee_value',
                                 'activity'),
                                ('reimbursement_value',
                                 'activity')]),
        ),
    ]
