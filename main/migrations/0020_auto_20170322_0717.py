# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20170306_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='title',
            field=models.CharField(max_length=600),
        ),
    ]