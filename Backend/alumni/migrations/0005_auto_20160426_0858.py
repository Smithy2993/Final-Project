# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-26 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0004_auto_20160421_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumni',
            name='id',
        ),
        migrations.AddField(
            model_name='alumni',
            name='identifier',
            field=models.CharField(default=None, max_length=8, primary_key=True, serialize=False, unique=True),
        ),
    ]
