# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-29 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0005_auto_20180828_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='profile_link',
            field=models.FileField(blank=True, default='user.png', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='user_name',
            field=models.CharField(default='dummy', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.FileField(blank=True, default='user.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, default='user.png', null=True, upload_to=''),
        ),
    ]
