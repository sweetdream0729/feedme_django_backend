# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 09:18
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
from django.contrib.postgres.operations import CreateExtension


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        CreateExtension('postgis'),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(blank=True, default='', max_length=255)),
                ('image_url', models.URLField(blank=True, default='')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(help_text='A slug helps query cuisines via url')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image_url', models.URLField(blank=True, default='')),
                ('price', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=255)),
                ('instagram_user', models.CharField(blank=True, default='', max_length=61)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('has_positive_sentiment', models.BooleanField()),
                ('gave_rating', models.BooleanField(default=False)),
                ('content', models.TextField(blank=True, default='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(help_text='A slug helps query highlights via url', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('did_like', models.BooleanField(default=False)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='main.Dish')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OpeningTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opens', models.TimeField()),
                ('closes', models.TimeField()),
                ('day_of_week', models.CharField(choices=[('sun', 'Sunday'), ('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday')], max_length=3)),
                ('valid_from', models.DateField(blank=True, null=True)),
                ('valid_through', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_id', models.BigIntegerField(blank=True, null=True)),
                ('photo_url', models.URLField(blank=True, default='', max_length=255)),
                ('provider', models.CharField(blank=True, default='', max_length=55)),
                ('bio', models.TextField(blank=True, default='')),
                ('country', models.CharField(blank=True, default='', max_length=255)),
                ('state', models.CharField(blank=True, default='', max_length=255)),
                ('city', models.CharField(blank=True, default='', max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(default='')),
                ('type', models.CharField(max_length=55)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.URLField()),
                ('address', models.CharField(blank=True, default='', max_length=255)),
                ('information', models.TextField(blank=True, default='')),
                ('phone_number', models.CharField(blank=True, default='', max_length=20)),
                ('suburb', models.CharField(blank=True, default='', max_length=55)),
                ('instagram_user', models.CharField(blank=True, default='', max_length=61)),
                ('time_offset_minutes', models.IntegerField(default=0, help_text='Multiply hours by 60')),
                ('tripadvisor_widget', models.TextField(blank=True, default='')),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, default='POINT(0.0 0.0)', srid=4326)),
                ('cuisines', models.ManyToManyField(to='main.Cuisine')),
                ('highlights', models.ManyToManyField(to='main.Highlight')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='report',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='main.Restaurant'),
        ),
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reports', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='openingtime',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opening_times', to='main.Restaurant'),
        ),
        migrations.AddField(
            model_name='dish',
            name='keywords',
            field=models.ManyToManyField(to='main.Keyword'),
        ),
        migrations.AddField(
            model_name='dish',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='main.Restaurant'),
        ),
    ]
