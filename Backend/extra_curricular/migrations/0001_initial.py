# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-11 21:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0009_auto_20160310_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='extra_curricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_exp', models.CharField(choices=[('WE', 'Work Experience'), ('SE', 'Society Experience'), ('VE', 'Volunteering Experience')], max_length=1)),
                ('name', models.CharField(max_length=128)),
                ('role', models.CharField(max_length=128)),
                ('start_date', models.DateField(blank=True, verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, verbose_name='End date')),
                ('Location', models.CharField(max_length=128)),
                ('Description', models.TextField(validators=[django.core.validators.MaxLengthValidator(200)])),
                ('student_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]