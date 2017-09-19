# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-17 13:21
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170917_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurantMenu',
            field=jsonfield.fields.JSONField(db_column=b'restaurantMenu', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurantSales',
            field=jsonfield.fields.JSONField(db_column=b'restaurantSales', max_length=1000, null=True),
        ),
    ]
