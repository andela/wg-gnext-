# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-30 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_userprofile_privacy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='show_english_ingredients',
            field=models.BooleanField(default=True, help_text='Check to also show ingredients in English while\ncreating a nutritional plan. These ingredients are extracted from a list\nprovided by the US Department of Agriculture. It is extremely complete,\nwith around 7000 entries, but can be somewhat overwhelming and make the\nsearch difficult.', verbose_name='Also use ingredients in English'),
        ),
    ]
