# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 16:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
