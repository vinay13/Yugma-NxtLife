# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-24 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=233)),
                ('body', models.TextField()),
                ('category_id', models.CharField(blank=True, max_length=122)),
                ('against_id', models.CharField(blank=True, max_length=122)),
                ('anonymous', models.BooleanField(default=True)),
                ('createdDate', models.DateTimeField(auto_now=True)),
                ('closedDate', models.DateTimeField()),
                ('user', models.CharField(blank=True, max_length=12)),
                ('assignedTo', models.CharField(blank=True, max_length=122)),
                ('priority', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SuggestionComment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('complaint_id', models.CharField(blank=True, max_length=1)),
                ('employee_id', models.CharField(blank=True, max_length=1)),
                ('parent_id', models.CharField(blank=True, max_length=2)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
