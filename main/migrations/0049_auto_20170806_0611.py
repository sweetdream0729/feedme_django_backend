# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-06 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_auto_20170802_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipequery',
            name='difficulty',
            field=models.CharField(default='', max_length=25),
        ),
    ]
