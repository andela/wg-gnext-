# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-30 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_workoutlog_workout_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutlog',
            name='workout_session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='manager.WorkoutSession'),
        ),
    ]
