# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-01 12:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ACCOUNTS', '0016_remove_questiondetail_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssistantDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Batch', models.CharField(max_length=20)),
                ('CourseId', models.CharField(blank='False', max_length=20)),
                ('TaId', models.CharField(blank='False', max_length=20)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
