# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-21 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=122)),
                ('options_type', models.CharField(choices=[('1', 'single'), ('2', 'multiple')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('expiredAt', models.DateField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('question', models.CharField(max_length=155)),
                ('user', models.CharField(max_length=144)),
                ('poll_type', models.CharField(choices=[('1', 'school'), ('2', 'standard')], max_length=1)),
            ],
        ),
    ]
