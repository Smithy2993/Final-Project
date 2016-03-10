# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Student_ID', models.PositiveIntegerField(unique=True, max_length=9)),
                ('First_name', models.CharField(max_length=128)),
                ('Middle_name', models.CharField(max_length=128)),
                ('Last_name', models.CharField(max_length=128)),
                ('Year', models.CharField(max_length=3)),
                ('Degree_Pro', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
