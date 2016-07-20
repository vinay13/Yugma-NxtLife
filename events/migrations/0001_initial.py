# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-20 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=123)),
                ('body', models.CharField(blank=True, max_length=255)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('event_date', models.DateField(auto_now=True)),
                ('event_time', models.CharField(blank=True, max_length=50)),
                ('event_type_id', models.IntegerField(blank=True)),
                ('event_standard', models.CharField(blank=True, max_length=128)),
            ],
        ),
    ]