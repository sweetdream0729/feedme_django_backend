# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-25 07:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0005_auto_20170717_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientdraft',
            name='recipe_draft',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='data_entry.RecipeDraft'),
        ),
    ]
