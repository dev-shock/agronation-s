# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 17:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='cost',
            new_name='item_cost',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='image',
            new_name='item_image',
        ),
        migrations.RemoveField(
            model_name='item',
            name='name',
        ),
        migrations.AddField(
            model_name='item',
            name='date_added',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='item',
            name='item_name',
            field=models.CharField(default='a', max_length=255),
        ),
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.CharField(default='a', max_length=255),
        ),
    ]