# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-24 11:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0009_auto_20160303_2340'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rest_user_creator', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='can_create_users',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='full_name',
            field=models.CharField(help_text='If a license has been localized, e.g. the Creative Commons licenses for the different countries, add them as separate entries here.', max_length=60, verbose_name='Full name'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='show_english_ingredients',
            field=models.BooleanField(default=True, help_text='Check to also show ingredients in English while\ncreating a nutritional plan. These ingredients are extracted from a list\nprovided by the US Department of Agriculture. It is extremely complete,\nwith around 7000 entries, but can be somewhat overwhelming and make the\nsearch difficult.', verbose_name='Also use ingredients in English'),
        ),
    ]