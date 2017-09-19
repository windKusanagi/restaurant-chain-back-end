# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-16 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170916_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employeeId',
            field=models.IntegerField(auto_created=True, db_column=b'employeeId', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipeId',
            field=models.IntegerField(auto_created=True, db_column=b'recipeId', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurantId',
            field=models.IntegerField(auto_created=True, db_column=b'restaurantId', primary_key=True, serialize=False),
        ),
    ]
