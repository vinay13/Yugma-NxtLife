# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 08:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0006_historicalcomplaint_historicalcomplaintcomment'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='historicalcomplaint',
            table='complaint_history',
        ),
    ]
