# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20171119_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='total_price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
