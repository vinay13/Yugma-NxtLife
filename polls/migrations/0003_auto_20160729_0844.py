# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 08:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160728_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='poll',
            name='option_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Option'),
        ),
    ]
