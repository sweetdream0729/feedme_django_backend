# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 07:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20170211_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('logo_url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='delivery_link',
            field=models.URLField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='delivery_provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.DeliveryProvider'),
        ),
    ]
