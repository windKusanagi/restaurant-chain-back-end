# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-16 19:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170916_1857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='eemployeeTitle',
            new_name='employeeTitle',
        ),
    ]
