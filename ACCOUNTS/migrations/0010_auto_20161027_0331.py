# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-26 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ACCOUNTS', '0009_auto_20161027_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='CreationDate',
            field=models.DateField(max_length=20),
        ),
    ]
