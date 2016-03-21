# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-21 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alumni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('course', models.CharField(choices=[('IT', 'Information Technology'), ('CS', 'Computer Science')], max_length=30)),
                ('faculty', models.CharField(choices=[('Art', 'Faculty of Art'), ('Bio', 'Faculty of Biological Sciences'), ('Bus', 'Faculty of Business'), ('Eds', 'Faculty of Education, Social Sciences and Law'), ('Eng', 'Faculty of Engineering'), ('Env', 'Faculty of Enviroment'), ('Mat', 'Faculty of Mathematics and Physical Sciences'), ('Med', 'Faculty of Medicine and Health'), ('Per', 'Faculty of Performance, Visual Arts and Communications')], max_length=60)),
                ('sector', models.CharField(choices=[('ACC', 'Accountancy, banking and finance'), ('BUS', 'Business, consulting and management'), ('CHA', 'Charity and voluntary work'), ('CRE', 'Creative arts and design'), ('ENE', 'Energy and utilities'), ('ENG', 'Engineering and manufacturing'), ('ENV', 'Environment and agriculture'), ('HEA', 'Healthcare'), ('HOS', 'Hospitality and events management'), ('IT', 'Information technology'), ('LAW', 'Law'), ('LES', 'Law enforcement and security'), ('LST', 'Leisure, sport and tourism'), ('MAP', 'Marketing, advertising and PR'), ('MI', 'Media and internet'), ('PC', 'Property and construction'), ('PSA', 'Public services and administration'), ('RHR', 'Recruitment and HR'), ('SR', 'Sales and Retail'), ('SP', 'Science and pharmaceuticals'), ('SC', 'Social care'), ('TE', 'Teaching and education'), ('TL', 'Transport and logistics')], max_length=60)),
                ('self_employed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
            ],
        ),
    ]
