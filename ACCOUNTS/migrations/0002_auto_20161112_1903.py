# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-12 13:33
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ACCOUNTS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professordetail',
            name='PId',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name=django.contrib.auth.models.User),
        ),
    ]
