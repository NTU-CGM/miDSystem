# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-07 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0009_user_job_tree_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_job',
            name='parsing_status',
            field=models.CharField(default='WAITING', max_length=10),
        ),
    ]
