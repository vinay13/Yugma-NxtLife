# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 14:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]