# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-10 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20161209_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votes',
            name='code',
        ),
        migrations.AddField(
            model_name='votes',
            name='code',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='code_votes', to='main.Code'),
            preserve_default=False,
        ),
    ]
