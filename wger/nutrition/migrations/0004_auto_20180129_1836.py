# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-29 15:36
from __future__ import unicode_literals

from django.db import migrations
import wger.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0003_mealitem_time_stamp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meal',
            options={},
        ),
        migrations.AlterModelOptions(
            name='mealitem',
            options={'ordering': ['time_stamp']},
        ),
        migrations.RemoveField(
            model_name='meal',
            name='time',
        ),
        migrations.AlterField(
            model_name='mealitem',
            name='time_stamp',
            field=wger.utils.fields.Html5TimeField(blank=True, null=True, verbose_name='Time (approx)'),
        ),
    ]
