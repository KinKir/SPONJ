# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-12 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ACCOUNTS', '0002_auto_20161112_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professordetail',
            name='PId',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='SId',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
