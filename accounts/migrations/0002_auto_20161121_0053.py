# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-20 18:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='created',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='updated',
        ),
    ]
