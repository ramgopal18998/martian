# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-28 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0004_auto_20180828_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
