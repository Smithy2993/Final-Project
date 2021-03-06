# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-21 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='name',
            field=models.CharField(choices=[('Computer Processors', 'Computer Processors'), ('Computer Architecture', 'Computer Architecture'), ('Introduction to Discrete Mathematics', 'Introduction to Discrete Mathematics'), ('Procedural Programming', 'Procedural Programming'), ('Professional Computing', 'Professional Computing'), ('Databases', 'Databases'), ('Fundamental Mathematical Concepts', 'Fundamental Mathematical Concepts'), ('Object Oriented Programming', 'Object Oriented Programming'), ('Programming Project', 'Programming Project'), ('Operating Systems', 'Operating Systems'), ('Formal Language and Finite Automata', 'Formal Language and Finite Automata'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Software Engineering', 'Software Engineering'), ('Networks', 'Networks'), ('User Interfaces', 'User Interfaces'), ('Algorithms and Data Structures I', 'Algorithms and Data Structures I'), ('Research Project', 'Research Project'), ('Data Science', 'Data Science'), ('Computer Graphics', 'Computer Graphics'), ('Secure Computing', 'Secure Computing'), ('Cryptography', 'Cryptography'), ('Information Visualization', 'Information Visualization'), ('Web Services and Web Data', 'Web Services and Web Data'), ('Graph Algorithms and Complexity Theory', 'Graph Algorithms and Complexity Theory'), ('Combinatorial Optimisation', 'Combinatorial Optimisation'), ('Distributed Systems', 'Distributed Systems'), ('Mobile Application Development', 'Mobile Application Development'), ('Programming Languages and Compilation', 'Programming Languages and Compilation'), ('User Adaptive Intelligent Systems', 'User Adaptive Intelligent Systems'), ('Robotics', 'Robotics')], max_length=128),
        ),
    ]
