# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 00:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20170918_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employeePhoto',
            field=models.CharField(db_column=b'employeePhoto', max_length=200),
        ),
    ]