# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-21 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='course',
            field=models.CharField(choices=[('IT', 'IT'), ('CS', 'Computer Science')], max_length=30),
        ),
    ]
