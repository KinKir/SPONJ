# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-14 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ACCOUNTS', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='SubmissionId',
        ),
        migrations.AddField(
            model_name='submission',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]