# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-08 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metag_pipeline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meta_user_job',
            name='non_annotate_status',
            field=models.CharField(default='WAITING', max_length=10),
        ),
    ]
