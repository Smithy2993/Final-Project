# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Degree_Pro',
            new_name='degree',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='First_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Middle_name',
            new_name='middle_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Student_ID',
            new_name='student_ID',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Year',
            new_name='year',
        ),
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'media/profile_pictures', blank=True),
            preserve_default=True,
        ),
    ]
