# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-02-07 07:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0020_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedulestep',
            name='duration',
        ),
    ]
