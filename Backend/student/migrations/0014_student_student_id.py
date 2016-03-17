# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 12:05
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_auto_20160315_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_ID',
            field=models.CharField(default=547832563, max_length=9, unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Must be 9 unique numbers', regex='^[0-9]{9,9}$')]),
            preserve_default=False,
        ),
    ]