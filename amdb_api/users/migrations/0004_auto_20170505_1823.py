# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 12:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_accesstoken'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accesstoken',
            old_name='accesss_token',
            new_name='access_token',
        ),
    ]
