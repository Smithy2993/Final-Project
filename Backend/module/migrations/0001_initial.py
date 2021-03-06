# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-22 20:19
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('COMP1212', 'Computer Processors'), ('COMP1211', 'Computer Architecture'), ('COMP1511', 'Introduction to Discrete Mathematics'), ('COMP1711', 'Procedural Programming'), ('COMP1911', 'Professional Computing'), ('COMP1121', 'Databases'), ('COMP1421', 'Fundamental Mathematical Concepts'), ('COMP1721', 'Object Oriented Programming'), ('COMP1921', 'Programming Project'), ('COMP2211', 'Operating Systems'), ('COMP2321', 'Formal Language and Finite Automata'), ('COMP2611', 'Artificial Intelligence'), ('COMP2931', 'Software Engineering'), ('COMP2221', 'Networks'), ('COMP2811', 'User Interfaces'), ('COMP2711', 'Algorithms and Data Structures I'), ('COMP3860', 'Research Project'), ('COMP3111', 'Data Science'), ('COMP3811', 'Computer Graphics'), ('COMP3911', 'Secure Computing'), ('COMP3223', 'Cryptography'), ('COMP3736', 'Information Visualization'), ('COMP3011', 'Web Services and Web Data'), ('COMP3940', 'Graph Algorithms and Complexity Theory'), ('COMP3910', 'Combinatorial Optimisation'), ('COMP3211', 'Distributed Systems'), ('COMP3222', 'Mobile Application Development'), ('COMP3321', 'Programming Languages and Compilation'), ('COMP3771', 'User Adaptive Intelligent Systems'), ('COMP3631', 'Robotics')], max_length=128)),
                ('credits', models.CharField(choices=[('10', '10'), ('20', '20'), ('60', '60')], max_length=2)),
                ('results', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('student_ID', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='student.student', verbose_name='Student ID')),
            ],
        ),
    ]
