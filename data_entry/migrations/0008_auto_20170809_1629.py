# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-09 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0007_auto_20170802_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipedraft',
            name='keywords',
            field=models.ManyToManyField(blank=True, to='main.Keyword'),
        ),
        migrations.AlterField(
            model_name='recipedraft',
            name='tags',
            field=models.ManyToManyField(blank=True, to='main.Tag'),
        ),
    ]
