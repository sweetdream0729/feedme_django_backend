# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-15 08:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0029_auto_20170515_0439'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_requests', to='main.Dish')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_request', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(choices=[('es', 'Easy'), ('md', 'Moderate'), ('dt', 'Difficult')], default='es', max_length=3),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='ingredient_type',
            field=models.CharField(blank=True, choices=[('mn', 'Main'), ('sc', 'Sauce'), ('gn', 'Garnish'), ('sd', 'Side')], default='mn', max_length=2),
        ),
    ]
