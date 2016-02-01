# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20160131_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdetails',
            name='account_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='accountdetails',
            name='account_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='accountdetails',
            name='account_type',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='accountdetails',
            name='accountee_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='accountdetails',
            name='bank_branch_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='accountdetails',
            name='bank_city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='accountdetails',
            name='bank_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='accountdetails',
            name='ifsc_code',
            field=models.CharField(max_length=15),
        ),
    ]