# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-22 16:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0005_auto_20160421_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='additional',
            field=models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(200)], verbose_name='Additional information'),
        ),
    ]
